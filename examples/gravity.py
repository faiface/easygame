from easygame import *

# V tomto priklade mame jednoducheho stvorcoveho hraca, ktoreho vieme ovladat
# sipkami a posobi na neho gravitacia. Zaroven sa v priestore nachadza plosina,
# na ktoru moze hraca vyskocit. Principy z tohoto prikladu sa daju pouzit na
# naprogramovanie plosinovky.

## Konstanty.
gravity      = 0.3 # O kolko sa zvacsi rychlost hraca smerom dole za 1 frame.
player_size  = 50  # Sirka a vyska stvorca, ktory reprezentuje hraca.
player_speed = 3   # Rychlost horizontalneho pohybu hraca.
jump_speed   = 10  # Vertikalna rychlost pri skoku.

## Stavove premenne hraca.
player_pos = (400, 300) # Aktualna pozicia stredu spodku hraca. Povodne stred obrazovky.
player_vel = (0, 0)     # Aktualna rychlost pohybu hraca. Povodne stoji.

## Plosina.
platform_y     = 100 # Vyska, v ktorej sa nachadza plosina.
platform_left  = 500 # X-ova suradnica laveho okraja plosiny.
platform_right = 700 # X-ova suradnica praveho okraja plosiny.

open_window('Gravity Example', 800, 600)

should_quit = False
while not should_quit:
    # Nacitame vsetky eventy od posledneho framu.
    for event in poll_events():
        # Ked uzivatel klikne na X, ukoncime hru.
        if type(event) is CloseEvent:
            should_quit = True

        # Klavesy ovladaju rychlost hraca, preto si ju najprv rozlozime na zlozky.
        (vx, vy) = player_vel

        if type(event) is KeyDownEvent:
            # Pri stlaceni lavej sipky chceme zvacsit rychlost smerom dolava.
            if event.key == 'LEFT':
                vx -= player_speed
            # Pri pravej sipke to iste do druhej strany. Toto zabezpeci, ze
            # ked su stlacene obe sipky, hrac sa nehybe.
            if event.key == 'RIGHT':
                vx += player_speed
            # Sipka hore je na skok. Vtedy chceme len vertikalnu rychlost hraca
            # nastavit smerom hore.
            if event.key == 'UP':
                vy = jump_speed

        if type(event) is KeyUpEvent:
            # Pri pusteni sipiek zase chceme vratit horizontalnu rychlost
            # do povodneho stavu.
            if event.key == 'LEFT':
                vx += player_speed
            if event.key == 'RIGHT':
                vx -= player_speed

        # A zbalime zlozky do premennych.
        player_vel = (vx, vy)

    ## Pohyb objektov.

    # Najprv si rozlozime poziciu a rychlost hraca na zlozky.
    (px, py) = player_pos
    (vx, vy) = player_vel

    # Aplikujeme gravitaciu. To znamena jednoducho zvacsit rychlost smerom dole.
    vy -= gravity

    # Zmenime poziciu podla rychlosti.
    px += vx
    py += vy

    # Skontrolujeme, ci hrac nespadol na zem. Ak ano, opravime jeho poziciu a rychlost
    # zresetujeme na nulu.
    if py <= 0:
        py = 0
        vy = 0

    # Skontrolujeme, ci hrac nespadol na plosinu. Pozor, aby sa na plosinu dalo vyskocit
    # zo spodku, toto chceme kontrolovat len v pripade, ze rychlost hraca je smerom dole,
    # cize pada. Ak skace, chceme aby cez plosinu bez problemov presiel.
    if vy < 0:
        # Tu skontrolujeme, ci sa hrac nachadza v X-ovom rozmedzi plosiny.
        if platform_left < px+player_size/2 and px-player_size/2 < platform_right:
            # Tato posledna kontrola je trosku tricky. V podstate kontrolujeme, ci sa hrac
            # v predchadzajucom frame nachadzal nad plosinou, ale v tomto sa nachadza pod nou.
            if py - vy >= platform_y and py <= platform_y:
                # Kolizia nastala! Napravime poziciu hraca, aby bol presne na plosine
                # a vynulujeme jeho rychlost.
                py = platform_y
                vy = 0

    # Nakoniec upravene zlozky zbalime spat do premennych.
    player_pos = (px, py)
    player_vel = (vx, vy)

    ## Kreslenie.

    # Vyplnime krasnym zltym pozadim.
    fill(1, 0.9, 0.1)

    # Nakreslime plosinu. To je len jednoducha ciara.
    draw_line(
        (platform_left, platform_y),  # Lavy bod plosiny.
        (platform_right, platform_y), # Pravy bod plosiny.
        thickness=4,                  # Hrubka ciary, nech to vidiet.
        color=(0.2, 0.2, 0.4, 1),     # Farba plosiny.
    )

    # Nakreslime hraca. Premenna player_pos urcuje poziciu stredu spodku stvorca.
    # Jednotlive rohy stvorca teda vypocitame s tymto na mysli.
    (px, py) = player_pos
    draw_polygon(
        (px - player_size/2, py),               # Lavy dolny roh.
        (px - player_size/2, py + player_size), # Lavy horny roh.
        (px + player_size/2, py + player_size), # Pravy horny roh.
        (px + player_size/2, py),               # Pravy dolny roh.
        color=(0.4, 0, 0.8, 1),                 # Farba stvorca.
    )

    next_frame()

close_window()
