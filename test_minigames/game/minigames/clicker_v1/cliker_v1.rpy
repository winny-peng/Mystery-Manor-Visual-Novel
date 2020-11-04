# This is a simple clicker game. Click the enemies to destroy them.

init:
    image bg clicker_v1_bg = "images/clicker_v1/background.jpg"

    python:
        import random
        import pygame

        # CONSTANTS
        SCREEN_HEIGHT = 720
        SCREEN_WIDTH = 1280

        class Alien(Sprite):
            """An Alien that can be destroyed by the player.

            ===Public Attributes===

            Representation Invariants:

            """
            # === Private Attributes ===
            # dimensions: [width, length]
            # position: [x, y]

            def __init__(self):
                """Initialize.
                """
                self.image = Image("images/clicker_v1/alien.png")
                self.active = False
                self.dimensions = [75, 75]
                self.position = [0, 0]
                self.maxY = 1005

            def createNew(self):
                """Create a new Alien.
                """
                self.position[0] = random.randrange(0, SCREEN_WIDTH - self.dimensions[0])
                self.position[1] = random.randrange(0, SCREEN_HEIGHT - self.dimensions[1])
                self.active = True

            def update(self, deltaTime):
                if (self.active):
                    self.dimensions[0] += 10
                    self.dimensions[1] += 10

                if (self.dimensions[0] > self.maxY):
                    self.active = False

            def isClicked(self, mouseX, mouseY):
                """Check if Alien is clicked by player.
                """
                # first check if Alien is "alive"
                if self.active == False:
                    return False
                # get boundaries of Alien
                boundaryX = [self.position[0] - self.dimensions[0]/2,
                             self.position[0] + self.dimensions[0]/2]
                boundaryY = [self.position[1] - self.dimensions[1]/2,
                             self.position[1] + self.dimensions[1]/2]

                # check if mouse is within Alien boundaries
                if (boundaryX[0] <= mouseX <= boundaryX[1] and boundaryY[0] <=
                     mouseY <= boundaryY[1]):
                    self.active = False
                    return True
                return False

            def handleInput(self, mouseX, mouseY):
                """Handle user input (e.g. mouse click).
                """
                if (self.grabCounter <= 0):
                    self.action = action

            def render(self, renderer, shownTimebase, animationTimebase):
                if (self.active):
                    r = renpy.render(self.image, 800, 600, shownTimebase, animationTimebase)
                    renderer.blit(r, (self.position[0], self.position[1]))
            # render

        class ClickerGame(renpy.Displayable):
            """A clicker game :)
            """

            def __init__( self ):
                renpy.Displayable.__init__(self)

                self.debug = []
                self.counter = 0

                self.aliens = []
                self.aliensCaught = 0

                self.lastStart = None
                self.frameRate = 60

                self.clock = pygame.time.Clock()
                self.countdown = 30
                self.milliseconds = 0

                self.gameover = False
                self.score = 0

            def event(self, event, x, y, shownTimebase):
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    # go through "alive" Aliens to check if it's clicked
                    for alien in self.aliens:
                        if alien.isClicked(x, y):
                            self.score += 1
                            break

            def update( self, shownTimebase, animationTimebase ):
                delta = self.getDelta( shownTimebase )
                rate = 1000 / self.frameRate
                speedAdjust = delta * rate

                if (self.gameover == False):

                    chance = random.randrange( 0, 20 )
                    if ( chance == 0 and len( self.aliens ) < 5 ):
                        alien = Alien()
                        alien.createNew()
                        self.aliens.append( alien )

                    removalList = []
                    # TODO: There is probably a more Python-idiomatic way to do this
                    for alien in self.aliens:
                        alien.update(1)

                        if (alien.active == False):
                            removalList.append(alien)

                    for alien in removalList:
                        self.aliens.remove(alien)

                    if (self.milliseconds > 1000):
                        self.countdown -= 1
                        self.milliseconds = 0

                    self.milliseconds += self.clock.tick_busy_loop( 60 )
                    if ( self.countdown <= 0 ):
                        self.gameover = True

                    # TODO: Remove
                    del self.debug[:]
                    self.debug.append( "Debugging..." )
                    self.debug.append( "Random: " + str( chance ) )
                    for alien in self.aliens:
                        self.debug.append( "alien Position: " + str( alien.position[0] ) + ", " + str( alien.position[1] ) + ", Active: " + str( alien.active ) )
                    self.debug.append( "Delta: " + str( delta ) )

                # Run while game is not over
            # update

            def render( self, width, height, shownTimebase, animationTimebase ):
                self.update( shownTimebase, animationTimebase )
                renderer = renpy.Render( width, height )

                if (self.gameover == False):
                    for alien in self.aliens:
                        alien.render(renderer, shownTimebase, animationTimebase)

                    counter = 0
                    for debug in self.debug:
                        txt = Text( _( debug ), size=10 )
                        textRender = renpy.render(txt, 800, 600, shownTimebase, animationTimebase)
                        renderer.blit( textRender, (0, 10 * counter ))
                        counter += 1

                else: #Gameover
                    # Temporary
                    txt = Text( _( "Game Over" ), size=40 )
                    renderer.blit( renpy.render( txt, 800, 600, shownTimebase, animationTimebase ), ( 300, 250 ) )


                txtScore = Text(_( "Time: " + str(self.countdown)), size=20)
                renderer.blit(renpy.render(txtScore, 800, 600, shownTimebase, animationTimebase), (700, 0 ))

                txtScore = Text( _( "Aliens Destroyed: " + str(self.score)), size=20 )
                renderer.blit( renpy.render( txtScore, 800, 600, shownTimebase, animationTimebase ), ( 700, 20 ) )


                renpy.redraw( self, 0 )

                return renderer
            # render

            def per_interact( self ):
                renpy.timeout( 0 )
                renpy.redraw( self, 0 )
            # per_interact

            def getDelta( self, shownTimebase ):
                if self.lastStart is None:
                    self.lastStart = shownTimebase

                delta = shownTimebase - self.lastStart
                self.lastStart = shownTimebase

                return delta
            # updateRate

label clicker_v1:
    window hide None

    scene bg clicker_v1_bg
    with fade

    python:
        ui.add(ClickerGame())
        ui.interact(suppress_overlay = True, suppress_underlay = True)
