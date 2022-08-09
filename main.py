import pygame
import os
pygame.init()
minecraft_running = os.popen('pgrep -a java | grep "minecraft"')
# comment out the lines that say "pygame.quit()" and "exit()" if you want it to run even if minecraft is open
if minecraft_running.read() == "":
    print("minecraft not running")
    minecraft_running.close()
    pygame.quit()
    exit()
else:
    print("minecraft is running")


def is_over(rect, pos):
    return True if rect.collidepoint(pos[0], pos[1]) else False


minecraft_running.close()
tab = 1
cheatname = "Autoclicker"
cheatsenabled = {
    "autoclicker": False,
    "reach": False,
    "velocity": False
}
print(list(cheatsenabled)[1])
accent = (255, 0, 77)
pygame.display.set_caption('Clever Client')
Icon = pygame.image.load('logo.png')
pygame.display.set_icon(Icon)
(width, height) = (1000, 500)
screen = pygame.display.set_mode((width, height), 0, 0, 0)
font = pygame.font.Font('fonts/Poppins-Regular.ttf', 20)
mouse = pygame.image.load('mouse-new.png')
target = pygame.image.load('target.png')
movement = pygame.image.load('running.png')
settings = pygame.image.load('gear.png')
pygame.display.flip()
while True:
    screen.fill((30, 30, 46))
    screen.fill(accent, (((tab - 1) * 75), 0, ((tab - (tab - 1)) * 75), 85))
    screen.fill((49, 50, 68), (0, 450, 1000, 50))
    mouseblit = screen.blit(pygame.transform.scale(mouse, (75, 75)), (0, 5))
    targetblit = screen.blit(pygame.transform.scale(target, (75, 75)), (75, 5))
    movementblit = screen.blit(pygame.transform.scale(movement, (75, 75)), (150, 5))
    screen.blit(pygame.transform.scale(Icon, (33, 35)), (5, 457))
    settingsblit = screen.blit(pygame.transform.scale(settings, (35, 35)), (50, 457))
    cheatnametext = font.render(cheatname, True, (255, 255, 255))
    screen.blit(cheatnametext, (10, 100))
    cheatsenabledtext = font.render("Enabled: " + str(cheatsenabled[cheatname.lower()]).lower(), True, (255, 255, 255))
    cheatsenabledrect = screen.blit(cheatsenabledtext, (10, 125))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_over(mouseblit, pygame.mouse.get_pos()):
                tab = 1
                cheatname = "Autoclicker"
            elif is_over(targetblit, pygame.mouse.get_pos()):
                tab = 2
                cheatname = "Reach"
            elif is_over(movementblit, pygame.mouse.get_pos()):
                tab = 3
                cheatname = "Velocity"
            elif is_over(cheatsenabledrect, pygame.mouse.get_pos()):
                if cheatsenabled[cheatname.lower()]:
                    cheatsenabled[cheatname.lower()] = False
                else:
                    cheatsenabled[cheatname.lower()] = True
