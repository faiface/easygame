import sys
sys.path.append("../")

from easygame import *

figure = load_image('figure.png')
open_window('Easy Game!', 800, 600)

should_quit = False
while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True

    fill(1, 1, 0)
    draw_image(figure, position=(400, 300))

    next_frame()

close_window()
