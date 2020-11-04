# This is a simple fishing game.

init:
    image bg fishing_v1_bg = "images/fishing_v1/background.jpg"

    python:
        import random
        import pygame

        # CONSTANTS
        SCREEN_HEIGHT = 720
        SCREEN_WIDTH = 1280

        class Fish():
            """A fish that can be caught by the player.

            ===Public Attributes===

            Representation Invariants:

            """
            # === Private Attributes ===
            # dimensions: [width, length]
            # position: [x, y]
            # speed: [min_speed, max_speed]

            def __init__(self):
                """Initialize.
                """
                self.image = Image("images/fishing_v1/fish.png")
                self.active = False
                self.dimensions = [100, 150]
                self.position = [0, 0]
                self.speed = [0, 10]
                self.maxY = 275

            def createNew(self):
                """Create a new Fish.
                """
                self.position[0] = random.randrange(0, 12) * 100
                self.position[1] = 0 - self.dimensions[1]                  # Start off-screen
                self.speed[1] = random.randrange(2, 10)
                self.active = True

            def update( self, deltaTime ):
                if ( self.active ):
                    self.position[1] += self.speed[1]

                if ( self.position[1] > self.maxY ):
                    self.active = False
            # update

            def isCaught(self, dogPosition, dogDimensions):
                """Check if Fish is "caught".
                """
                if ( dogPosition[0] < self.position[0] + self.dimensions[0] and
                        dogPosition[0] + dogDimensions[0] > self.position[0] and
                        dogPosition[1] < self.position[1] + self.dimensions[1] and
                        dogPosition[1] + dogDimensions[1] > self.position[1] ):
                    self.active = False
                    return True

                return False
            # isCaught

            def render(self, renderer, shownTimebase, animationTimebase):
                if (self.active):
                    r = renpy.render(self.image, 800, 600, shownTimebase, animationTimebase)
                    renderer.blit(r, (self.position[0], self.position[1]))
            # render

        class Dog():
            """The player is a dog.

            ===Public Attributes===

            Representation Invariants:
                <self.action> == "None" or "LEFT" or "RIGHT" or "GRAB"
            """
            # === Private Attributes ===
            # position: [x, y]
            # speed: [left/right, grab]
            # action: action to perform

            def __init__( self ):
                """Initialize.
                """

                self.image = Image( "images/fishing_v1/dog.png" )
                self.dimensions = [150, 200]
                self.position = [0, 520]
                self.speed = [160, 10]
                self.grabCounter = 0
                self.grabCounterMax = 20
                self.action = "NONE"
                self.score = 0

            def handleInput(self, action):
                """Handle user input (e.g. controls).
                """
                if (self.grabCounter <= 0):
                    self.action = action

            def update(self, deltaTime):
                if (self.grabCounter > 0):
                    if (self.grabCounter > self.grabCounterMax/2):
                        self.position[1] -= self.speed[1] * deltaTime
                    else:
                        self.position[1] += self.speed[1] * deltaTime

                    self.grabCounter -= 1
                    if (self.grabCounter == 0):
                        self.position[1] = 450

                else:
                    if (self.action == "LEFT" and self.grabCounter <= 0):
                        self.position[0] -= self.speed[0] * deltaTime

                    elif (self.action == "RIGHT" and self.grabCounter <= 0):
                        self.position[0] += self.speed[0] * deltaTime

                    elif (self.action == "GRAB" and self.grabCounter <= 0):
                        self.grabCounter = self.grabCounterMax

                    # check for boundary (player cannot move off screen)
                    if (self.position[0] < 0):
                        self.position[0] = 0
                    elif (self.position[0] > SCREEN_WIDTH - self.dimensions[0]):
                        self.position[0] = SCREEN_WIDTH - self.dimensions[0]

                self.action = "NONE"

            def render( self, renderer, shownTimebase, animationTimebase ):
                r = renpy.render( self.image, 800, 600, shownTimebase, animationTimebase )
                renderer.blit( r, ( self.position[0], self.position[1] ) )
            # render

        class FishingGame(renpy.Displayable):
            """A fishing game :)
            """

            def __init__( self ):
                renpy.Displayable.__init__(self)

                # Maybe I'll write a sub-class for this stuff
                self.Dog = Dog()

                self.debug = []
                self.counter = 0

                self.fish = []
                self.fishCaught = 0

                self.lastStart = None
                self.frameRate = 60

                self.clock = pygame.time.Clock()
                self.countdown = 30
                self.milliseconds = 0

                self.gameover = False
            # __init__

            def event( self, event, x, y, shownTimebase ):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.Dog.handleInput( "GRAB" )
                    # Up Key

                    if event.key == pygame.K_LEFT:
                        self.Dog.handleInput( "LEFT" )
                    # Left Key

                    if event.key == pygame.K_RIGHT:
                        self.Dog.handleInput( "RIGHT" )
                    # Right Key
                # KEYDOWN

            # event

            def update( self, shownTimebase, animationTimebase ):
                delta = self.getDelta( shownTimebase )
                rate = 1000 / self.frameRate
                speedAdjust = delta * rate

                if ( self.gameover == False ):

                    chance = random.randrange( 0, 20 )
                    if ( chance == 0 and len( self.fish ) < 5 ):
                        fish = Fish()
                        fish.createNew()
                        self.fish.append( fish )

                    removalList = []
                    # TODO: There is probably a more Python-idiomatic way to do this
                    for fish in self.fish:
                        fish.update( 1 )

                        if ( fish.isCaught( self.Dog.position, self.Dog.dimensions ) ):
                            self.Dog.score += 1

                        if ( fish.active == False ):
                            removalList.append( fish )

                    for fish in removalList:
                        self.fish.remove( fish )

                    self.Dog.update( 1 )

                    if ( self.milliseconds > 1000 ):
                        self.countdown -= 1
                        self.milliseconds = 0

                    self.milliseconds += self.clock.tick_busy_loop( 60 )
                    if ( self.countdown <= 0 ):
                        self.gameover = True

                    # TODO: Remove
                    del self.debug[:]
                    self.debug.append( "Debugging..." )
                    self.debug.append( "Random: " + str( chance ) )
                    self.debug.append( "Dog Position: " + str( self.Dog.position[0] ) + ", " + str( self.Dog.position[1] ) )
                    for fish in self.fish:
                        self.debug.append( "Fish Position: " + str( fish.position[0] ) + ", " + str( fish.position[1] ) + ", Active: " + str( fish.active ) )
                    self.debug.append( "Delta: " + str( delta ) )

                # Run while game is not over
            # update

            def render( self, width, height, shownTimebase, animationTimebase ):
                self.update( shownTimebase, animationTimebase )
                renderer = renpy.Render( width, height )

                if ( self.gameover == False ):
                    for fish in self.fish:
                        fish.render( renderer, shownTimebase, animationTimebase )

                    self.Dog.render( renderer, shownTimebase, animationTimebase )

                    counter = 0
                    for debug in self.debug:
                        txt = Text( _( debug ), size=10 )
                        textRender = renpy.render( txt, 800, 600, shownTimebase, animationTimebase )
                        renderer.blit( textRender, ( 0, 10 * counter ) )
                        counter += 1

                else: #Gameover
                    # Temporary
                    txt = Text( _( "Game Over" ), size=40 )
                    renderer.blit( renpy.render( txt, 800, 600, shownTimebase, animationTimebase ), ( 300, 250 ) )


                txtScore = Text( _( "Time: " + str( self.countdown ) ), size=20 )
                renderer.blit( renpy.render( txtScore, 800, 600, shownTimebase, animationTimebase ), ( 700, 0 ) )

                txtScore = Text( _( "Fish Caught: " + str( self.Dog.score ) ), size=20 )
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
        # FishingGame

label fishing_v1:
    window hide None

    scene bg fishing_v1_bg
    with fade

    python:
        ui.add(FishingGame())
        ui.interact(suppress_overlay = True, suppress_underlay = True)
