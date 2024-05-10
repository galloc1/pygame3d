import pygame, sys, math
import colours
import py3d

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Helvetica', 30)

########## Config ##########
windowSize = (1280, 720) # The size of the pygame window
windowCaption = 'Project Name'  # The caption for the pygame window, generally the name of the project
backgroundColour = colours.white    # The background colour of the window
frameRate = 60  # The target frame rate of the window
############################

########## Pygame Setup ##########
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption(windowCaption)
clock = pygame.time.Clock()
##################################

line = py3d.Line(screen, 100, py3d.Transform(py3d.Vector3(500, 500, 1), py3d.Vector3(math.radians(90), math.radians(90), math.radians(90))))
camera = py3d.Camera(py3d.Transform(py3d.Vector3(0, 0, 0), py3d.Vector3(0, 0, 0)))


########## Main Loop ##########
while True:
    line.draw(camera)
    relativeRotation = line.transform.rotation - camera.transform.rotation
    screen.blit(font.render(str(relativeRotation.x)+', '+str(relativeRotation.y)+', '+str(relativeRotation.z), False, colours.black), (0, 0))
    
    ##### Pygame Eventz #####
    for event in pygame.event.get():
        # Closing the window
        if event.type == pygame.QUIT:
            playing_game = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                camera.transform.rotation.y+=math.radians(15)
            if event.key == pygame.K_s:
                camera.transform.rotation.y-=math.radians(-15)
    #########################
    pygame.display.flip()   # Reloads screen
    screen.fill(backgroundColour)   # Sets screen to background colour (for next frame)
    clock.tick(frameRate)   # Maintains framerate
###############################