from easygame import *
import random

# V tomto priklade je ukazany jeden z moznych sposobov, ako implementovat
# prepinanie medzi roznymi obrazovkami v hre. Taketo obrazovky mozu byt
# napriklad hlavne menu, nastavenia, samotna hra, a tak dalej. Konkretne
# tu budeme mat jednoduche "hlavne menu" a "hru".

# Pomocna funkcia na vygenerovanie nahodnej farby.
def random_color():
    return (random.random(), random.random(), random.random(), 1)

# Pomocna funkcia na najdenie inverznej farby.
def inverse_color(color):
    (r, g, b, a) = color
    return (1-r, 1-g, 1-b, a)

open_window('Screens Example', 800, 600)

## Premenna urcujuca aktivnu obrazovku.
active_screen = 'MENU'

## Premenne pre obrazovku 'MENU'.
# Ziadne.

## Premenne pre obrazovku 'GAME'.
screen_color = random_color()

should_quit = False
while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True

        ## Spracovanie udalosti (okrem CloseEvent) si rozvetvime medzi
        ## jednotlive obrazovky.

        # Spracovanie udalosti pre menu.
        if active_screen == 'MENU':
            # Klavesa ENTER nas posunie z menu do hry.
            if type(event) is KeyDownEvent and event.key == 'ENTER':
                active_screen = 'GAME'
                continue

        # Spracovanie udalosti pre hru.
        if active_screen == 'GAME':
            # Klavesa ESC nas posunie spat od menu.
            if type(event) is KeyDownEvent and event.key == 'BACKSPACE':
                active_screen = 'MENU'
                continue
            # Stlacenie mysi zmeni farbu pozadia v "hre".
            if type(event) is MouseDownEvent:
                screen_color = random_color()

    ## Kreslenie si opat rozvetvime medzi jednotlive obrazovky.

    # Kreslenie menu.
    if active_screen == 'MENU':
        # Nakreslime bledoruzove pozadie a text hovoriaci, ze
        # ENTER nas posunie do hry.
        fill(0.9, 0.7, 0.8)
        draw_text(
            'Press ENTER to start the game!', 'Arial', 36,
            position=(20, 300), color=(0, 0, 0, 1), bold=True,
        )

    # Kreslenie hry.
    if active_screen == 'GAME':
        # Nakreslime pozadie podla premennej a text inverznou farbou.
        (r, g, b, a) = screen_color
        fill(r, g, b)
        draw_text(
            'Press BACKSPACE to go back.', 'Arial', 36,
            position=(20, 325), color=inverse_color(screen_color), bold=True,
        )
        draw_text(
            'Click to see some magic!', 'Arial', 36,
            position=(20, 275), color=inverse_color(screen_color), bold=True,
        )

    next_frame()

close_window()
