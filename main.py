import pygame
import os

pygame.init()


def is_over(rect, pos):
    return True if rect.collidepoint(pos[0], pos[1]) else False


class Slider:
    def __init__(self):
        self.width = 255
        self.posx = 50
        self.posy = 175
        self.value = 0
        self.steps = 20
        self.slidername = "MinCPS:"
        self.value = 0.0

    def renderSlider(self):
        self.sliderrect = screen.fill((49, 50, 68), (self.posx, self.posy, self.width, 25))
        screen.fill(accent, (self.posx, self.posy, self.value / (self.steps / self.width), 25))
        slidernametext = font.render(self.slidername, True, (255, 255, 255))
        screen.blit(slidernametext, (10, self.posy))
        numtext = font.render(str(self.value), True, (255, 255, 255))
        screen.blit(numtext, ((self.posx + self.width) + 25, self.posy))


minecraft_running = os.popen('pgrep -a java | grep "minecraft"')
# comment out the lines that say "pygame.quit()" and "exit()" if you want it to run even if minecraft is not open
if minecraft_running.read() == "":
    print("minecraft not running")
    minecraft_running.close()
    pygame.quit()
    exit()
else:
    print("minecraft is running")


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
Icon = pygame.image.load('images/logo.png')
pygame.display.set_icon(Icon)
(width, height) = (1000, 500)
screen = pygame.display.set_mode((width, height), 0, 0, 0)
font = pygame.font.Font('fonts/Poppins-Regular.ttf', 20)
guicolortext = font.render("Accent color:", True, (255, 255, 255))
redtext = font.render("R:", True, (255, 255, 255))
greentext = font.render("G:", True, (255, 255, 255))
bluetext = font.render("B:", True, (255, 255, 255))
mouse = pygame.image.load('images/mouse-new.png')
target = pygame.image.load('images/target.png')
movement = pygame.image.load('images/running.png')
settings = pygame.image.load('images/gear.png')
pygame.display.flip()
redslider = screen.fill((49, 50, 68), (50, 175, 256, 25))
greenslider = screen.fill((49, 50, 68), (50, 225, 256, 25))
blueslider = screen.fill((49, 50, 68), (50, 275, 256, 25))

mincps = Slider()
mincps.posx = 100
maxcps = Slider()
maxcps.posx = 100
maxcps.posy = 225
maxcps.slidername = "MaxCPS:"
def rederRedSlider():
    redslider = screen.fill((49, 50, 68), (50, 175, 255, 25))
    screen.fill((accent), (50, 175, accent[0], 25))
    screen.blit(redtext, (10, 175))
    rednumtext = font.render(str(accent[0]), True, (255, 255, 255))
    screen.blit(rednumtext, (325, 175))


def renderGreenSlider():
    greenslider = screen.fill((49, 50, 68), (50, 225, 255, 25))
    screen.fill((accent), (50, 225, accent[1], 25))
    screen.blit(greentext, (10, 225))
    greennumtext = font.render(str(accent[1]), True, (255, 255, 255))
    screen.blit(greennumtext, (325, 225))


def renderBlueSlider():
    blueslider = screen.fill((49, 50, 68), (50, 275, 255, 25))
    screen.fill((accent), (50, 275, accent[2], 25))
    screen.blit(bluetext, (10, 275))
    bluenumtext = font.render(str(accent[2]), True, (255, 255, 255))
    screen.blit(bluenumtext, (325, 275))


while True:
    screen.fill((30, 30, 46))
    screen.fill((49, 50, 68), (0, 450, 1000, 50))
    if tab < 4:
        screen.fill(accent, (((tab - 1) * 75), 0, ((tab - (tab - 1)) * 75), 85))
    else:
        screen.fill(accent, (46, 450, 45, 50))
    mouseblit = screen.blit(pygame.transform.scale(mouse, (75, 75)), (0, 5))
    targetblit = screen.blit(pygame.transform.scale(target, (75, 75)), (75, 5))
    movementblit = screen.blit(pygame.transform.scale(movement, (75, 75)), (150, 5))
    screen.blit(pygame.transform.scale(Icon, (33, 35)), (5, 457))
    settingsblit = screen.blit(pygame.transform.scale(settings, (35, 35)), (50, 457))
    cheatnametext = font.render(cheatname, True, (255, 255, 255))
    screen.blit(cheatnametext, (10, 100))
    if tab < 4:
        cheatsenabledtext = font.render("Enabled: " + str(cheatsenabled[cheatname.lower()]).lower(), True,
                                        (255, 255, 255))
        cheatsenabledrect = screen.blit(cheatsenabledtext, (10, 125))

    if tab == 1:
        mincps.renderSlider()
        maxcps.renderSlider()
    elif tab == 4:
        screen.blit(guicolortext, (10, 125))
        rederRedSlider()
        renderGreenSlider()
        renderBlueSlider()
    if pygame.mouse.get_pressed()[0]:
        if is_over(mincps.sliderrect, pygame.mouse.get_pos()) and tab == 1:
            mincps.value = round((pygame.mouse.get_pos()[0] - mincps.posx) * (mincps.steps / mincps.width), 2)

        if is_over(maxcps.sliderrect, pygame.mouse.get_pos()) and tab == 1:
            maxcps.value = round((pygame.mouse.get_pos()[0] - maxcps.posx) * (maxcps.steps / maxcps.width), 2)
        elif is_over(redslider, pygame.mouse.get_pos()) and tab == 4:
            accent = ((pygame.mouse.get_pos()[0] - 50), accent[1], accent[2])
        elif pygame.mouse.get_pressed()[0] and is_over(greenslider, pygame.mouse.get_pos()) and tab == 4:
            accent = (accent[0], (pygame.mouse.get_pos()[0] - 50), accent[2])
        elif pygame.mouse.get_pressed()[0] and is_over(blueslider, pygame.mouse.get_pos()) and tab == 4:
            accent = (accent[0], accent[1], (pygame.mouse.get_pos()[0] - 50))
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
            elif is_over(settingsblit, pygame.mouse.get_pos()):
                tab = 4
                cheatname = "Settings"
            elif is_over(cheatsenabledrect, pygame.mouse.get_pos()):
                if cheatsenabled[cheatname.lower()]:
                    cheatsenabled[cheatname.lower()] = False
                else:
                    cheatsenabled[cheatname.lower()] = True
