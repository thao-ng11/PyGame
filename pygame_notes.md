# What is a videogame?
    A game is a movie. A movie is a bunch of images playing very quickly, called frames. A movie generally has 24 frames per second
    3 Ways to make a movie:
        1) Record with a camera
        2) Draw images
        3) Use digital tools

    Differences between movies and video games:
    Movies take no input other than ff rewind or pause

    Video games constantly check for player input to update what frame is being drawn

# How a video game works
    1) Check player input(event loop)
    2) Use the inputs to place elements on the screen
        This creates one frame
        We delete the image to create the next using these parameters
        Done 30-60 times per second
        Applies to 2-d and 3-d games

# what does pygame do?
    1) pygame helps to display images
        Displays a window and helps draw images
    2) Plays sounds
    3) Looks for player inputs
    4) Has gamedev tools like collision detection, timers, text creation
# Why learn pygame over a proper game engine?
    Good for learning programming in general
# How pygame draws
    Pygame draws in similar fashion to css
    elements called later in the code take superiority
        This means two surfaces drawn at the same location are layered on top of one another with the surface appearing later in the code on top



------
Getting Started
------
# Create a window in pygame
    1) import pygame
    2) first code to call: pygame.init()
    3) # create display surface
        screen = pygame.display.set_mode((width,height))
    if code is run in this state it lasts for one frame then completes and stops running
    ______
    next: infinite loop our code
    ------
    Create an infinite loop
     Ex:
        while True:
            <loop body>

    Inside the while loop we will draw all our elements and update everything
    *****Must close the loop from the inside*****

    _______
    next update our display(screen)
    -------
    while True:
        pygame.display.update()
        <loop body>

    _______
    Check for player inputs
    -------
    while True:
        #create event loop to check for player input
        for event in pygame.event.get():
            <loop body>
        # draw all our elements
        # update everything
        pygame.display.update()

    Add condition close to end the loop
        if event.type == pygame.QUIT

    At this point if we run out code we get an error:
        "video system not initialized"
        pygame.init() initializes all of pygame
        pygame.quit() uninitialized all of pygame

        When we quit() in this situation we are quitting init() call, but the while loop is still running then encountering the update call and having no screen to update

        To solve this we import exit from the python sys module, which exits all running code. This will end our while loop

# Controling frame rate
    How fast the game is going to run
    On slow computers the frame rate will be slow and on fast computers it will be fast

    This means if we do not control the frame rate the game will play through too quickly or too slowly depending on the hardware used

    Setting the max frame rate is easy because we can instruct the game to run slower, however, we cannot instruct the hardware to run faster
        We solve this by reducing the amount of content displayed at one time
    ______
    creating the frame rate ceiling (clock object)
    ------
    clock = pygame.time.Clock()

    in our while loop we set the clock to 60 fps using:
    clock.tick(<fps>)
    which instructs the while loop to not run faster than 60 times per second
        One while loop for roughly every 17 seconds

    *****Minimum frame rate cannot be set*****
    *****We have to make sure our game is not too complex*****

# Displaying images
    Need a surface

    Two types of surfaces:
    ------
    The main game window (can only have one display surface)
    ------

    ------
    Regular surface (can have infinite)
    ------
    A single image(something imported, rendered text or a plain color)
        needs to be put on the display surface to be visible
    Created using pygame.Surface(<tuple of wdith, height>)

    to place the regular surface on the display surface we use the blit command, which stands for block image transfer(places a surface on top of another)
        screen.blit(<surface>, <position(tuple)>)

# place a blit on the display
    #plain surface
    test_plain_surface = pygame.Surface((100, 200))
    #add color to plain_surface
    test_plain_surface.fill('Red')

    In while loop:
        screen.blit(test_plain_surface, (200,100))

# Screen display coordinates system for most game engines
    origin piont 0,0 is the top left
    move right is increase x
    move down is increase y

# to place images on the display
    set the image:
        variable = pygame.image.load('<path to the image.file ending>')

# Creating text
    Breakdown:
    Create an image of the text
    Place the image on the display surface

    Steps:
    1) Create a font(text size and style)
        <font_var> = pygame.font.Font(<font_type, font_size>)
        font_type - linked font file
    2) Write text on surface
        <surface_variable> = <font_var.render(<text_info>, AA, color)>
        text - a string of text to display
        AA(Anti-Alias) - smooth the edges of the text
            used with non-pixel art
        color - color of text
    3) Blit the text surface

# Animating videogame
    Every time we update a surface it does not remove the previousframe

    By redrawing our background sufaces we overwrite the after image of any overlap afterimages

# Animating sprites
    By toggling between one image and another quickly we can give the illusion our sprite is moving
    Ex:
    # player animation
        #walking surfaces
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()

        #walking list
        player_walk = [player_walk_1,player_walk_2]
        player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

        #index to toggle images in list
        player_idx = 0
        player_surf = player_walk[player_idx]
        player_rect = player_surf.get_rect(midbottom = (80,300))
# Converting surfaces
    convert images from .png or any other format using the .convert method after our image
    We convert our file format to something pygame can work with more easily to speed up our game
    Ex:
        <varable> = pygame.image.load(<file.png>).convert(0)
    To convert with respect to the alpha channels use .convert_alpha()

# Rectangles
    Used for precise positioning of surfaces
    Help to detect basic collisions
    Drawing (pygame.draw)

    *---*---* topleft, midtop, topright
    |       |
    *   *   * midleft, center, midright
    |       |
    *---*---* bottomleft, midbottom, bottomright

    When placing a surface we are only able to place images with respect to their origin value
        By using rectangles we are able to place images with respect to other positions of the image

        This is done by combining the surface image information with placement via the rectangle. This creates what is referred to as a sprite class

# surface placement
    1) Create rectangle
        creates a rectangle where we specify dimensions
        <variable> = pygame.rect(<left>,<top>,<width>,<height>)

        Idealy we want a rectangle the exact same size as the surface

        Therefore we use:
        <surface_variable>.get_rect(<position_type> = (x,y))
            pygame takes the surface and draws a rectangle around it
    2) replace coordinate position of screen blit with the rect variable

# surface movement of sprite(surface in ractangle)
    instantiate or decrement a particular point on the rectangle
    Can use print to measure position

# Transform a surface
    Scale, rotate .etc
    pygame.transform.<method>(<surface>,args)
    Scale:
        pygame.transform.scale(<surface>, (<width>, <height>))
    Scale2x:
        pygame.transform.scale2x(<surface>)
    rotozoom:
        shorthand to rotate, scale and filter a surface
        filter smooths image
        pygame.rotozoom(<surface>, <angle>, <scale>(single int))


# collisions
    Check for collision between the rectangles containing our image surfaces
    rect1.colliderect(rect2) returns 0(no col) or 1(yes col)
    returns 1(True) for every collided frame
        must account for only a single collision

    Collide point
        checks if one point collides with a rectangle
            incredible important for clicking with a mouse
        rect1.collidepoint((x,y))

# Getting mouse position
    Two options:
        Pygame.mouse
            Gives information on:
                mouse position, button clicks, visibility...
                    Ex:
                            #****check for mouse input in eventloop****
                        #pygame.MOUSEMOTION - give mouse position
                        # if event.type == pygame.MOUSEMOTION:
                        #     #event.pos holds position of mouse x,y coordinates
                        #     if player_rect.collidepoint(event.pos):
                        #         print('collision')
                        # # triggered on button press
                        # if event.type == pygame.MOUSEBUTTONDOWN:
                        #     print('mouse down')
                        # # triggered on mouse button release
                        # if event.type == pygame.MOUSEBUTTONUP:
                        #     print('mouse up')

        Check event loop
            get mousemotion, clicks, position

# pygame.draw
    draw recatangles, circles, lines, points, elipses
        pygame.draw.rect(<surface_drawn_on>, <color>, <rectangle>,<line_width,border_radius>)
    when line width is specified pygame stops drawing the rectangle center
        To create a rectangle with a border and solid background
            we need two rectangles layered on top of one another
    pygame.draw.line(<surface>, <color>, start(x,y),end(x,y), width)
    pygame.drae.rect(<surface>, colore, <left>,<top><width>,<height>)
        left - refers to pixels from the left
        top - refers to pixels from the top

# specifying colors with rgb and hexidecimal colors
    rgb - specified in color argument as touple of 3 values
    hex_color - specified in color arguments as #rrggbb

# Inputs
    Two methods for input:
    1) pygame.key
    2) event loop

    Why 2 methods to get input?
        when using classes you want the controls inside the relevant class. pygame.mouse & pygame. key is great for that which allow us to set inputs apart from the event loop

    Keyboard input
        pygame.key
            pygame.key.get_pressed()
                returns object with all buttons and their current state
                    initial unpressed state is zero
                    pressed == 1
                        Ex:
                        // creates keys list
                        keys = pygame.key.get_pressed()
                            // checks for specific button
                            if keys[pygame.K_SPACE]:
                                // Executes body if button == 1
                                <body>
        event loop
        keyboard input in event loop steps:
        1) check if any button was pressed
        2) work with specific key
            use button press or release
        Ex:
            for event in pygame.event.get():
                //pressing key
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        <body>
                //releasing key
                if event.type == pygame.KEYUP:
                    if event.key == K_SPACE:
                        <body>

# Game States
    Game & Game over
    Game -start screen
    Game -option to start again or start screen

# Time
    Milliseconds since the game started
    pygame.time.get_ticks()

# Timers
    Used to create a custom user event triggered at certain time intervals
    pygame.time.set_timer(<event>,<delay>)


# sprite class
    A class which contains a surface and a rectangle which can be dawn and updated easily
    Our sprite class will inherit from pygames sprite class
    class <class_name>(pygame.sprite.Sprite)
    Pygame does not draw sprites automatically
        screen.blit does not work with psrites
        Use Group or GroupSingle to store sprites then draw/update all sprites in that group
    Instead of calling the methods of our classes directly we create an update function within our class and call that in our game loop

# Groups
    To get our sprites on the screen we first must add them to a group
    -----
    Group
    -----
    Group for multiple sprites which do not interact with one another

    -----
    GroupSingle
    -----
    Group with a single sprite(generally our player)

    We then call the draw method on the group to draw it to the screen
        <Group>.draw(<surface to draw on>)

# Sprite collisions
    Sprites have their own collision mechanics
    Most Common collision mechanic: spritecollide(sprite,group,dokilll)
        Takes a sprite and check if it is colliding with any other sprite in another group(this is part of why we put our player in GroupSingle)
            returns a list of all collided sprites


# sound
    import a sound then play at certain parts of our game
    pygame.mixer.Sound('<path/to/audio>')
    use .play() method to play passing in the amount of times to loop(-1 for infinity)
        Ex:
            pygame.mixer.Sound('<path/to/audio>').play(loop = -1)
# *****Simple Mind Blowing idea***
#   Functions can be used to display surfaces and return a value

# Errors
    Problem: Score variable not updating
    Solution:
        Pygame creates surfaces and draws images from top to bottom.
        A surface is static and unchanging from the time it is declared even if it is not blit to the screen yet
        Therefore updating surfaces which use variables like scores must be drawn after the line they are updated

