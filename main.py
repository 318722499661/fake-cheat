import pygame
import os
from sys import exit

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
        self.roundplaces = 1
        self.suffix = ""
        self.sliderrect = screen.fill((30, 30, 46), (self.posx, self.posy, self.width + 1, 25))

    def renderSlider(self):
        self.sliderrect = screen.fill((30, 30, 46), (self.posx, self.posy, self.width + 1, 25))
        # self.sliderrectrender = screen.fill((49, 50, 68), (self.posx, self.posy, self.width, 25))
        pygame.draw.rect(screen, (49, 50, 68), pygame.Rect(self.posx, self.posy, self.width, 25), border_radius=3)
        # screen.fill(accent, (self.posx, self.posy, self.value / (self.steps / self.width), 25))
        pygame.draw.rect(screen, accent, pygame.Rect(self.posx, self.posy, self.value / (self.steps / self.width), 25),
                         border_radius=3)
        slidernametext = font.render(self.slidername, True, (255, 255, 255))
        screen.blit(slidernametext, (10, self.posy))
        numtext = font.render(str(self.value) + self.suffix, True, (255, 255, 255))
        screen.blit(numtext, ((self.posx + self.width) + 25, self.posy))

    def setValue(self):
        self.value = round((pygame.mouse.get_pos()[0] - self.posx) * (self.steps / self.width), self.roundplaces)


if os.name == "nt":
    minecraft_running = os.popen('tasklist | FIND "javaw"')
else:
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

# Declare sliders for autoclicker
mincps = Slider()
mincps.posx = 100

maxcps = Slider()
maxcps.posx = 100
maxcps.posy = 225
maxcps.slidername = "MaxCPS:"

clickerjitter = Slider()
clickerjitter.posx = 100
clickerjitter.posy = 275
clickerjitter.slidername = "Jitter:"
clickerjitter.steps = 3
clickerjitter.roundplaces = 1

# Declare sliders for reach
minreach = Slider()
minreach.posx = 185
minreach.steps = 7
minreach.roundplaces = 1
minreach.slidername = "Minimum Reach:"

maxreach = Slider()
maxreach.posx = 190
maxreach.posy = 225
maxreach.steps = 7
maxreach.roundplaces = 1
maxreach.slidername = "Maximum Reach:"

# Declare sliders for velocity
velhorizontal = Slider()
velhorizontal.posx = 125
velhorizontal.slidername = "Horizontal:"
velhorizontal.steps = 100
velhorizontal.roundplaces = 0
velhorizontal.suffix = "%"
velhorizontal.value = 100

velvertical = Slider()
velvertical.posx = 125
velvertical.posy = 225
velvertical.slidername = "Vertical:"
velvertical.steps = 100
velvertical.roundplaces = 0
velvertical.suffix = "%"
velvertical.value = 100

velchance = Slider()
velchance.posx = 125
velchance.posy = 275
velchance.slidername = "Chance:"
velchance.steps = 100
velchance.roundplaces = 0
velchance.suffix = "%"
velchance.value = 100


def rederRedSlider():
    redslider = screen.fill((30, 30, 46), (50, 175, 255, 25))
    pygame.draw.rect(screen, (49, 50, 68), pygame.Rect(50, 175, 255, 25), border_radius=3)
    # screen.fill((accent), (50, 175, accent[0], 25))
    pygame.draw.rect(screen, accent, pygame.Rect(50, 175, accent[0], 25), border_radius=3)
    screen.blit(redtext, (10, 175))
    rednumtext = font.render(str(accent[0]), True, (255, 255, 255))
    screen.blit(rednumtext, (325, 175))


def renderGreenSlider():
    greenslider = screen.fill((30, 30, 46), (50, 225, 255, 25))
    pygame.draw.rect(screen, (49, 50, 68), pygame.Rect(50, 225, 255, 25), border_radius=3)
    # screen.fill((accent), (50, 225, accent[1], 25))
    pygame.draw.rect(screen, accent, pygame.Rect(50, 225, accent[1], 25), border_radius=3)
    screen.blit(greentext, (10, 225))
    greennumtext = font.render(str(accent[1]), True, (255, 255, 255))
    screen.blit(greennumtext, (325, 225))


def renderBlueSlider():
    blueslider = screen.fill((30, 30, 46), (50, 275, 255, 25))
    pygame.draw.rect(screen, (49, 50, 68), pygame.Rect(50, 275, 255, 25), border_radius=3)
    # screen.fill((accent), (50, 275, accent[2], 25))
    pygame.draw.rect(screen, accent, pygame.Rect(50, 275, accent[2], 25), border_radius=3)
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
        clickerjitter.renderSlider()

    elif tab == 2:
        minreach.renderSlider()
        maxreach.renderSlider()

    elif tab == 3:
        velhorizontal.renderSlider()
        velvertical.renderSlider()
        velchance.renderSlider()

    elif tab == 4:
        screen.blit(guicolortext, (10, 125))
        rederRedSlider()
        renderGreenSlider()
        renderBlueSlider()

    if pygame.mouse.get_pressed()[0]:
        # Autoclicker sliders
        if is_over(mincps.sliderrect, pygame.mouse.get_pos()) and tab == 1:
            mincps.setValue()

        elif is_over(maxcps.sliderrect, pygame.mouse.get_pos()) and tab == 1:
            maxcps.setValue()

        elif is_over(clickerjitter.sliderrect, pygame.mouse.get_pos()) and tab == 1:
            clickerjitter.setValue()

        # Reach sliders

        if is_over(minreach.sliderrect, pygame.mouse.get_pos()) and tab == 2:
            minreach.setValue()

        if is_over(maxreach.sliderrect, pygame.mouse.get_pos()) and tab == 2:
            maxreach.setValue()

        # Velocity sliders

        elif is_over(velhorizontal.sliderrect, pygame.mouse.get_pos()) and tab == 3:
            velhorizontal.setValue()

        elif is_over(velvertical.sliderrect, pygame.mouse.get_pos()) and tab == 3:
            velvertical.setValue()

        elif is_over(velchance.sliderrect, pygame.mouse.get_pos()) and tab == 3:
            velchance.setValue()

        # Color sliders

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
