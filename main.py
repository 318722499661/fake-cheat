import pygame
import os
import time
from sys import exit
import math

overbar = False
pygame.init()
timeoverbar = 0
barwidth = 50
timeoffofbar = 0
textalpha = 0
def is_over(rect, pos):
    return True if rect.collidepoint(pos[0], pos[1]) else False


def easeInOutQuint(t, b, c, d):
    t /= d / 2
    if t < 1:
        return c / 2 * t * t * t * t * t + b
    t -= 2
    return c / 2 * (t * t * t * t * t + 2) + b


class Slider:
    def __init__(self):
        self.width = 255
        self.posx = 50
        self.posy = 75
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
        screen.blit(slidernametext, (60, self.posy))
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
accent = (0, 215, 135)
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
redslider = screen.fill((49, 50, 68), (100, 75, 256, 25))
greenslider = screen.fill((49, 50, 68), (100, 125, 256, 25))
blueslider = screen.fill((49, 50, 68), (100, 175, 256, 25))
# Declare sliders for autoclicker
mincps = Slider()
mincps.posx = 150

maxcps = Slider()
maxcps.posx = 150
maxcps.posy = 125
maxcps.slidername = "MaxCPS:"

clickerjitter = Slider()
clickerjitter.posx = 150
clickerjitter.posy = 175
clickerjitter.slidername = "Jitter:"
clickerjitter.steps = 3
clickerjitter.roundplaces = 1

# Declare sliders for reach
minreach = Slider()
minreach.posx = 240
minreach.steps = 7
minreach.roundplaces = 1
minreach.slidername = "Minimum Reach:"

maxreach = Slider()
maxreach.posx = 240
maxreach.posy = 125
maxreach.steps = 7
maxreach.roundplaces = 1
maxreach.slidername = "Maximum Reach:"

# Declare sliders for velocity
velhorizontal = Slider()
velhorizontal.posx = 175
velhorizontal.slidername = "Horizontal:"
velhorizontal.steps = 100
velhorizontal.roundplaces = 0
velhorizontal.suffix = "%"
velhorizontal.value = 100

velvertical = Slider()
velvertical.posx = 175
velvertical.posy = 125
velvertical.slidername = "Vertical:"
velvertical.steps = 100
velvertical.roundplaces = 0
velvertical.suffix = "%"
velvertical.value = 100

velchance = Slider()
velchance.posx = 175
velchance.posy = 175
velchance.slidername = "Chance:"
velchance.steps = 100
velchance.roundplaces = 0
velchance.suffix = "%"
velchance.value = 100
def rederRedSlider():
    pygame.draw.rect(screen, (49, 50, 68), pygame.Rect(100, 75, 255, 25), border_radius=3)
    # screen.fill((accent), (50, 175, accent[0], 25))
    pygame.draw.rect(screen, accent, pygame.Rect(100, 75, accent[0], 25), border_radius=3)
    screen.blit(redtext, (60, 75))
    rednumtext = font.render(str(accent[0]), True, (255, 255, 255))
    screen.blit(rednumtext, (375, 75))


def renderGreenSlider():
    pygame.draw.rect(screen, (49, 50, 68), pygame.Rect(100, 125, 255, 25), border_radius=3)
    # screen.fill((accent), (50, 225, accent[1], 25))
    pygame.draw.rect(screen, accent, pygame.Rect(100, 125, accent[1], 25), border_radius=3)
    screen.blit(greentext, (60, 125))
    greennumtext = font.render(str(accent[1]), True, (255, 255, 255))
    screen.blit(greennumtext, (375, 125))


def renderBlueSlider():
    pygame.draw.rect(screen, (49, 50, 68), pygame.Rect(100, 175, 255, 25), border_radius=3)
    # screen.fill((accent), (50, 275, accent[2], 25))
    pygame.draw.rect(screen, accent, pygame.Rect(100, 175, accent[2], 25), border_radius=3)
    screen.blit(bluetext, (60, 175))
    bluenumtext = font.render(str(accent[2]), True, (255, 255, 255))
    screen.blit(bluenumtext, (375, 175))


while True:
    screen.fill((30, 30, 46))
    screen.fill((49, 50, 68), (0, 0, 50, 500))
    cheatnametext = font.render(cheatname, True, (255, 255, 255))
    screen.blit(cheatnametext, (60, 10))
    if tab < 4:
        cheatsenabledtext = font.render("Enabled: " + str(cheatsenabled[cheatname.lower()]).lower(), True,
                                        (255, 255, 255))
        cheatsenabledrect = screen.blit(cheatsenabledtext, (60, 40))

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
        screen.blit(guicolortext, (60, 40))
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
            accent = ((pygame.mouse.get_pos()[0] - 100), accent[1], accent[2])

        elif pygame.mouse.get_pressed()[0] and is_over(greenslider, pygame.mouse.get_pos()) and tab == 4:
            accent = (accent[0], (pygame.mouse.get_pos()[0] - 100), accent[2])

        elif pygame.mouse.get_pressed()[0] and is_over(blueslider, pygame.mouse.get_pos()) and tab == 4:
            accent = (accent[0], accent[1], (pygame.mouse.get_pos()[0] - 100))
    darkenedscreen = pygame.Surface((1000, 500))
    darkenedscreen.set_alpha(textalpha / 2)
    screen.blit(darkenedscreen, (0, 0))
    leftbar = screen.fill((49, 50, 68), (0, 0, barwidth, 500))
    if is_over(leftbar, pygame.mouse.get_pos()):
        if overbar == False:
            timeoverbar = time.time()
            overbar = True
        if time.time() - timeoverbar > 1 and barwidth <= 200:
            # barwidth+=1
            barwidth = math.floor(easeInOutQuint((time.time() - timeoverbar - 1), 50, 150, 0.5))
        if textalpha < 255 and time.time() - timeoverbar > 1:
            textalpha+=0.75
    else:
        if overbar:
            timeoffofbar = time.time()
            overbar = False
        if barwidth > 50:
            #barwidth -= 1
            barwidth = math.floor(easeInOutQuint((time.time() - timeoffofbar), 200, -150, 0.5))
        if textalpha > 0:
            textalpha-=0.75
    if tab == 4:
        screen.fill(accent, (0, 410, barwidth, 43))
    screen.blit(pygame.transform.scale(Icon, (33, 35)), (7, 457))
    if tab < 4:
        screen.fill(accent, (0, (tab - 1) * 43, barwidth, 43))
    settingsblit = screen.blit(pygame.transform.scale(settings, (35, 35)), (7, 414))
    mouseblit = screen.blit(pygame.transform.scale(mouse, (35, 35)), (7, 4))
    targetblit = screen.blit(pygame.transform.scale(target, (35, 35)), (7, 47))
    movementblit = screen.blit(pygame.transform.scale(movement, (35, 35)), (7, 90))
    SettingsText = font.render("Settings", True, (255, 255, 255))
    SettingsText.set_alpha(textalpha)
    screen.blit(SettingsText, (50, 418))
    LogoText = font.render("Clever", True, (255, 255, 255))
    LogoText.set_alpha(textalpha)
    screen.blit(LogoText, (50, 461))
    AutoClickerText = font.render("Autoclicker", True, (255, 255, 255))
    AutoClickerText.set_alpha(textalpha)
    screen.blit(AutoClickerText, (50, 9))
    ReachText = font.render("Reach", True, (255, 255, 255))
    ReachText.set_alpha(textalpha)
    screen.blit(ReachText, (50, 51))
    VelocityText = font.render("Velocity", True, (255, 255, 255))
    VelocityText.set_alpha(textalpha)
    screen.blit(VelocityText, (50, 93))
    autoclickerselection = pygame.Rect(0, 0, barwidth, 43)
    reachselection = pygame.Rect(0, 43, barwidth, 43)
    velocityselection = pygame.Rect(0, 86, barwidth, 43)
    settingsselection = pygame.Rect(0, 410, barwidth, 43)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_over(autoclickerselection, pygame.mouse.get_pos()):
                tab = 1
                cheatname = "Autoclicker"
            elif is_over(reachselection, pygame.mouse.get_pos()):
                tab = 2
                cheatname = "Reach"
            elif is_over(velocityselection, pygame.mouse.get_pos()):
                tab = 3
                cheatname = "Velocity"
            elif is_over(settingsselection, pygame.mouse.get_pos()):
                tab = 4
                cheatname = "Settings"
            elif is_over(cheatsenabledrect, pygame.mouse.get_pos()):
                if cheatsenabled[cheatname.lower()]:
                    cheatsenabled[cheatname.lower()] = False
                else:
                    cheatsenabled[cheatname.lower()] = True
