import random
import time
import pygame

# инициализация
pygame.init()
pygame.font.init()
pygame.mixer.init()

# music

pygame.mixer.music.load('music/kazino.mp3')
pygame.mixer.music.play(loops=99)
pygame.mixer.music.set_volume(0.1)

# main menu


# Настройки экрана
screen = pygame.display.set_mode((950, 500))

clock = pygame.time.Clock()

background_image = pygame.image.load('pics/table.jpg')




# cards
tuz = 5
king = 4
dama = 3
valet = 2
ten = 10
nine = 9
eight = 8
seven = 7
six = 6
cards = [six, six, six, six, seven, seven, seven, seven, eight, eight, eight, eight, nine, nine, nine, nine, ten, ten,
         ten, ten, valet, valet, valet, valet, dama, dama, dama, dama, king, king, king, king, tuz, tuz, tuz, tuz]

ran = random.choice(cards)




max = 22
# colors
white = ((255, 255, 255))
blue = ((0, 0, 255))
green = ((0, 255, 0))
red = ((255, 0, 0))
black = ((0, 0, 0))

# очки
o4ko_player = '0'
o4ko_bot = '0'
o4ko_bot_final = 0

card_b1 = random.choice(cards)
card_b2 = random.choice(cards)
o4ko_bot_final = card_b1 + card_b2


max = 22

stop_word = 1
# font
font = pygame.font.Font('font/bruh.ttf', 20)
text_player = font.render("Сумма: ", True, white)
text_bot = font.render("Сумма: ", True, white)
text_win = font.render("", True, white)
text_lose = font.render("", True, white)
text_restart = font.render("",True,white)
text_o4ki_player = font.render(o4ko_player, True, white)
text_o4ki_bot = font.render(o4ko_bot, True, white)
text_uprav = font.render("Управление:", True, white)
e = font.render("У = Добавить карту", True, white)
r = font.render("К = Раскрыть карты", True, white)
q = font.render("Й = Рестарт", True, white)
text_draw = font.render("", True, white)


true = True


# _____________________game stuff
o4ko_player = int(o4ko_player)
if o4ko_player > 21:
    print("lose")
    screen.blit(text_lose, (400, 250))
    screen.blit(background_image, (0, 0))
    o4ko_player = str(o4ko_player)
    print("lose text")

while True:






    # вывод фона
    screen.blit(background_image, (0, 0))

    # вывод текста
    screen.blit(text_player, (250, 400))
    screen.blit(text_o4ki_player, (350, 400))
    screen.blit(text_lose, (400, 200))
    screen.blit(text_win, (400, 200))
    screen.blit(text_restart,(400,250))
    screen.blit(text_uprav,(0,0))
    screen.blit(e,(0,20))
    screen.blit(r,(0,40))
    screen.blit(q,(0,60))
    o4ko_player = int(o4ko_player)
    screen.blit(text_draw, (450,200))



    screen.blit(text_bot, (250, 100))
    screen.blit(text_o4ki_bot, (350, 100))

    player_card1 = pygame.draw.rect(screen, (255, 255, 255), (400, 350, 70, 100))
    player_card2 = pygame.draw.rect(screen, (255, 255, 255), (500, 350, 70, 100))

    bot_card1 = pygame.draw.rect(screen, (255, 255, 255), (400, 50, 70, 100))
    bot_card2 = pygame.draw.rect(screen, (255, 255, 255), (500, 50, 70, 100))
    pygame.display.update()
    clock.tick(60)
    pygame.display.flip()

    # font

    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit()

        o4ko_player = int(o4ko_player)
        o4ko_bot = int(o4ko_bot)
        if o4ko_player < 22:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e and stop_word == 1:

                o4ko_player = int(o4ko_player)
                ran = random.choice(cards)
                ran = int(ran)
                text_o4ki_player = '0'
                ran = random.choice(cards)
                cards.pop(ran)
                o4ko_player = int(o4ko_player)
                o4ko_player += ran
                o4ko_player = str(o4ko_player)
                o4ko_bot = str(o4ko_bot)
                text_o4ki_player = 0
                text_o4ki_player = font.render(o4ko_player, True, white)
                text_o4ki_bot = font.render(o4ko_bot, True, white)

                o4ko_player = int(o4ko_player)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    print("fgafa")
                    o4ko_player = '0'
                    o4ko_bot = '0'
                    text_win = font.render("", True, white)
                    text_lose = font.render("", True, white)
                    text_restart = font.render("", True, white)
                    true = False
                    cards = [six, six, six, six, seven, seven, seven, seven, eight, eight, eight, eight, nine, nine,
                             nine,
                             nine, ten, ten,
                             ten, ten, valet, valet, valet, valet, dama, dama, dama, dama, king, king, king, king, tuz,
                             tuz,
                             tuz, tuz]
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        o4ko_player = int(o4ko_player)
                        ran = random.choice(cards)

                        text_o4ki_player = '0'
                        ran = random.choice(cards)
                        cards.pop(ran)
                        o4ko_player = int(o4ko_player)
                        o4ko_player += ran
                        o4ko_player = str(o4ko_player)
                        text_o4ki_player = 0
                        text_o4ki_player = font.render(o4ko_player, True, white)
                        text_o4ki_bot = font.render(o4ko_bot, True, white)

                        text_win = font.render("", True, white)
                        text_lose = font.render("", True, white)
                        text_restart = font.render("", True, white)

                o4ko_player = int(o4ko_player)
                o4ko_bot = int(o4ko_bot)
                if o4ko_player > 21:
                    text_lose = font.render("Вы Проиграли", True, white)
                    text_restart = font.render("press q to restart", True, white)
                    screen.blit(text_lose, (400, 250))
                    screen.blit(text_restart, (500, 250))
                    cards = [six, six, six, six, seven, seven, seven, seven, eight, eight, eight, eight, nine, nine,
                             nine, nine, ten, ten,
                             ten, ten, valet, valet, valet, valet, dama, dama, dama, dama, king, king, king, king, tuz,
                             tuz, tuz, tuz]

        if max > o4ko_player :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                o4ko_bot = o4ko_bot_final
                o4ko_player = int(o4ko_player)
                o4ko_bot = str(o4ko_bot_final)


                text_o4ki_bot = font.render(o4ko_bot, True, white)

                o4ko_bot = int(o4ko_bot)
                if o4ko_player > o4ko_bot or o4ko_bot > 21:
                    text_win = font.render("Вы Выиграли", True, white)
                    text_restart = font.render("press q  to restart", True, white)

                elif o4ko_bot == o4ko_player:
                    text_draw = font.render("Ничья", True, white)
                    text_restart = font.render("press q to restart", True, white)
                    stop_word = 0
                else:
                    text_lose = font.render("Вы Проиграли", True, white)
                    text_restart = font.render("press q to restart", True, white)
                    o4ko_bot = str(o4ko_bot_final)
                    text_o4ki_bot = font.render(o4ko_bot, True, white)
                    o4ko_bot = int(o4ko_bot_final)
                    print("fa")

                stop_word = 0






        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            print("fgafa")

            o4ko_player = '0'
            o4ko_bot = '0'

            card_b1 = random.choice(cards)
            card_b2 = random.choice(cards)
            o4ko_bot_final = card_b1 + card_b2



            text_win = font.render("", True, white)
            text_lose = font.render("", True, white)
            text_restart = font.render("", True, white)
            text_draw = font.render("", True, white)
            text_o4ki_player = font.render(o4ko_player, True, white)
            text_o4ki_bot = font.render(o4ko_bot, True, white)
            true = False
            cards = [six, six, six, six, seven, seven, seven, seven, eight, eight, eight, eight, nine, nine, nine,
                         nine, ten, ten,
                         ten, ten, valet, valet, valet, valet, dama, dama, dama, dama, king, king, king, king, tuz, tuz,
                         tuz, tuz]

            stop_word = 1


        o4ko_bot = str(o4ko_bot)
        o4ko_player = str(o4ko_player)





