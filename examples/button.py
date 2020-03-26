from easygame import *

# V tomto priklade mame tlacidlo, ktoreho stlacenim sa odpali zvuk pistole.

## Nacitanie zvuku pistole.
gunshot = load_audio('gunshot.wav')

## Premenne o tlacidle.
button_x1 = 230 # X-ova suradnica laveho dolneho rohu.
button_y1 = 250 # Y-ova suradnica laveho dolneho rohu.
button_x2 = 570 # X-ova suradnica praveho horneho rohu.
button_y2 = 350 # Y-ova suradnica praveho horneho rohu.

open_window('Button Example', 800, 600)

should_quit = False
while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True

        # Ked uzivatel klikne, musime skontrolovat, ci neklikol na tlacidlo.
        if type(event) is MouseDownEvent:
            # Skontrolujeme vertikalnu os.
            if button_x1 <= event.x <= button_x2:
                # Skontrolujeme horizontalnu os.
                if button_y1 <= event.y <= button_y2:
                    # Uzivatel klikol na tlacidlo. Vypalime pistol.
                    play_audio(gunshot)

    # Pekne modre pozadie.
    fill(0.7, 0.6, 0.9)

    # Nakreslime tlacidlo, je to len obdlznik a text.
    draw_polygon(
        (button_x1, button_y1),   # Lavy dolny roh.
        (button_x2, button_y1),   # Pravy dolny roh.
        (button_x2, button_y2),   # Pravy horny roh.
        (button_x1, button_y2),   # Lavy horny roh.
        color=(0.8, 0.3, 0.2, 1), # Farba tlacidla.
    )
    draw_text(
        'Shoot!', 'Arial', 80,                 # Text, font a jeho velkost.
        position=(button_x1+10, button_y1+10), # Text umiestnime do tlacidla.
        color=(1, 1, 1, 1),                    # Biela farba.
    )

    next_frame()

close_window()
