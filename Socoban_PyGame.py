import pygame
import sys
import os
from os import path
from random import randint

FPS = 50
level_list = [["Уровень 1", 0], ['Уровень 2', 1], ['Уровень 3', 1],
              ['Уровень 4', 1]]


def terminate():
    pygame.quit()
    sys.exit()


def game_end():
    color = [pygame.Color('white'), pygame.Color(50, 50, 50, 255)]
    fon = pygame.transform.scale(load_image('The-End-Game.png'),
                                 (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('font.ttf', 30)

    game_name_text = ('Нажмите ЛКМ...')
    text_rendered = font.render(game_name_text, 1, pygame.Color('white'))
    game_name_text_rect = text_rendered.get_rect()
    game_name_text_rect.x = WIDTH / 2 - game_name_text_rect.width / 2
    game_name_text_rect.y = HEIGHT - 58
    screen.blit(text_rendered, game_name_text_rect)

    game_result_text = ('Ваш резельтат: ' + str(player.score))
    text_rendered = font.render(game_result_text, 1, pygame.Color('white'))
    game_result_text_rect = text_rendered.get_rect()
    game_result_text_rect.x = 150
    game_result_text_rect.y = 22
    screen.blit(text_rendered, game_result_text_rect)
    print('Ваш резельтат: ', player.score)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


class StartScreen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.start_screen()

    def start_screen(self):
        pygame.mixer.music.load('sound/start.mp3')
        pygame.mixer.music.play()
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()

        welcome_text = [' ']
        fon = pygame.transform.scale(load_image('welcome_fon.jpg'),
                                     (self.width, self.height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font('font.ttf', 24)
        text_coord = 50

        game_name_text = ['Pac-Man-Don']
        for i in game_name_text:
            text_rendered = font.render(i, 1, pygame.Color('white'))
            game_name_text_rect = text_rendered.get_rect()
            game_name_text_rect.x = 200
            game_name_text_rect.y = 80
            screen.blit(text_rendered, game_name_text_rect)

        for line in welcome_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        # play button
        play_button = pygame.transform.scale(load_image('play_button.png'),
                                             (324, 141))
        cord_button = play_button.get_rect()
        cord_button.x = WIDTH / 4
        cord_button.y = 400
        screen.blit(play_button, (150, 450))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x >= 160 and y >= 465:
                        if x <= 465 and y <= 582:
                            pygame.mixer.music.pause()
                            return  # начинаем игру
            pygame.display.flip()
            clock.tick(FPS)


def win():  # победа
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    global opened_levels, level_list
    player.status = 'идет игра'
    if opened_levels < 4:
        opened_levels += 1
    else:
        player.status = 'game end'
    print(opened_levels)
    level_list[opened_levels - 1][1] = 0
    print('method win completed')
    fon = pygame.transform.scale(load_image('welcome_fon.jpg'),
                                 (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('font.ttf', 26)

    game_win_text = ['ПОДЕДА!!', '', '', '', '', '', '', '', '',
                     'Нажмите ЛКМ']

    text_coord = 20
    for line in game_win_text:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = WIDTH / 2 - intro_rect.width / 2
        intro_rect.y += 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def game_over():
    x = -610
    v = 200
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    img = pygame.transform.scale(load_image('gameover.png'), (WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        if x <= 0:
            x += v * clock.tick() / 1000
        else:
            break
        screen.fill((0, 0, 0))
        screen.blit(img, (x, 10))
        pygame.display.flip()

    font = pygame.font.Font('font.ttf', 26)

    game_win_text = ['', '', '', '', '', '', '', '', '',
                     'Нажмите ЛКМ']

    text_coord = 20
    for line in game_win_text:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = WIDTH / 2 - intro_rect.width / 2
        intro_rect.y += 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    k = True
    while k:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                k = False
        pygame.display.flip()
        clock.tick(FPS)


def try_again():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    welcome_text = ['Упс, тебя съели!!!', '',
                    ' Попробуй еще раз', '', '', '', '',
                    'Нажмите ПКМ/ЛКМ',
                    'чтобы продолжить...']
    fon = pygame.transform.scale(load_image('welcome_fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('font.ttf', 37)
    text_coord = 20
    for line in welcome_text:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = 80
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                for ghost in list_ghost:
                    ghost.start_pos()

                player.start_pos()
                player.status = 'идет игра'
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def level_choose():
    global level_list
    color = [pygame.Color('white'), pygame.Color(50, 50, 50, 255)]
    fon = pygame.transform.scale(load_image('back_ground.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('font.ttf', 30)

    game_name_text = 'Выберите уровень: '
    text_rendered = font.render(game_name_text, 1, pygame.Color('white'))
    game_name_text_rect = text_rendered.get_rect()
    game_name_text_rect.x = WIDTH / 2 - game_name_text_rect.width / 2
    game_name_text_rect.y = 65
    screen.blit(text_rendered, game_name_text_rect)

    font = pygame.font.Font('font.ttf', 25)
    n_string = 250
    level_text = []
    for level, c in level_list:
        text_rendered = font.render(level, 1, color[c])
        level_text_rect = text_rendered.get_rect()
        level_text.append(level_text_rect)
        level_text_rect.x = WIDTH / 2 - level_text_rect.width / 2
        level_text_rect.y = n_string
        n_string += 55
        screen.blit(text_rendered, level_text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for num_level, lt in enumerate(level_text):
                    if lt.x < event.pos[0] < lt.x + lt.width and lt.y < \
                            event.pos[1] < lt.y + lt.height:
                        if level_list[num_level][1] == 0:
                            return num_level + 1  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def load_image(name, colorkey=None):
    fullname = os.path.join('data/40/', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    # image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def load_level(filename):
    level_map = []
    filename = "level/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        widht = int(mapFile.readline()[6:].rstrip())
        height = int(mapFile.readline()[7:].rstrip())
        background = mapFile.readline()[11:]
        for line in mapFile:
            level_map.append(line.rstrip(',\n').split(','))
    # и подсчитываем максимальную длину
    # max_width = max(map(len, level_map))
    return level_map
    # дополняем каждую строку пустыми клетками ('.')
    # return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Life(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(life_group, all_sprites)
        self.image = load_image('91.png')
        self.rect = self.image.get_rect().move(tile_width * x, tile_height * y)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        tile_images = load_image('182.png')
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class Wall(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(wall_group, all_sprites)
        self.image = load_image(tile_type + '.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        player_image = load_image('91.png')
        self.image = player_image
        self.start_pos_x = pos_x
        self.start_pos_y = pos_y
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.eat_sound = pygame.mixer.Sound('sound/eat_point.ogg')
        self.lost_sound = pygame.mixer.Sound('sound/lost.ogg')
        self.speed = 4
        self.score = 0
        self.status = 'идет игра'

    def start_pos(self):
        self.rect.x = self.start_pos_x * tile_width
        self.rect.y = self.start_pos_y * tile_height

    def up(self):
        self.rect.y -= self.speed
        self.image = load_image('108.png')
        if pygame.sprite.spritecollideany(self, wall_group):
            self.rect.y += self.speed

    def right(self):
        self.rect.x += self.speed
        self.image = load_image('77.png')
        if pygame.sprite.spritecollideany(self, wall_group):
            self.rect.x -= self.speed

    def left(self):
        self.rect.x -= self.speed
        self.image = load_image('57.png')
        if pygame.sprite.spritecollideany(self, wall_group):
            self.rect.x += self.speed

    def down(self):
        self.rect.y += self.speed
        self.image = load_image('91.png')
        if pygame.sprite.spritecollideany(self, wall_group):
            self.rect.y -= self.speed

    def score_print(self):
        text = 'Счёт: ' + str(self.score)
        font = pygame.font.Font(None, 35)
        text_coord = 50
        string_rendered = font.render(text, 1, pygame.Color('white'))
        score_rect = string_rendered.get_rect()
        score_rect.top = text_coord
        score_rect.x = 20
        score_rect.y = 610
        text_coord += score_rect.height
        screen.blit(string_rendered, score_rect)

    def update(self):
        point = pygame.sprite.spritecollideany(self, point_group)
        coin = pygame.sprite.spritecollideany(self, coins_group)
        cherry = pygame.sprite.spritecollideany(self, cherry_group)
        ghost = pygame.sprite.spritecollideany(self, ghost_group)
        if ghost in ghost_group:
            self.status = 'монстр'
            self.lost_sound.play()
            print('monster')
            if len(list_sprites) == 0:
                self.status = 'конец игры'
                return
            for_kill = list_sprites.pop()
            for_kill.kill()

        if point in point_group:
            self.score += 10
            self.eat_sound.play()
            point.kill()
        if coin in coins_group:
            self.score += 100
            coin.kill()
        if cherry in cherry_group:
            for ghost in list_ghost:
                ghost.start_ticks = pygame.time.get_ticks()
                # print(ghost.start_ticks)
            self.score += 50
            cherry.kill()
        if not point_group:
            self.status = 'выигрыш'
            print('Game end')


class Coins(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(coins_group, all_sprites)
        self.image = load_image(tile_type + '.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class Point(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(point_group, all_sprites)
        self.image = load_image(tile_type + '.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class Cherry(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(cherry_group, all_sprites)
        self.image = load_image(tile_type + '.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class Ghost(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(ghost_group, all_sprites)
        self.start_pos_x = pos_x
        self.start_pos_y = pos_y
        self.start_picture = tile_type
        self.image = load_image(tile_type + '.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.speed = 2
        self.direction = 'down'
        self.list_dir = ['up', 'left', 'down', 'right']
        self.timer = 60
        self.start_ticks = -5000

    def update(self, *args):
        self.moving()
        self.time_scale()

    def start_pos(self):
        self.rect.move(self.start_pos_x * tile_width,
                       self.start_pos_y * tile_height)

    def moving(self):
        possible_dir = self.list_dir.copy()
        if self.direction == 'up':
            back_move = 'down'
        if self.direction == 'down':
            back_move = 'up'
        if self.direction == 'left':
            back_move = 'right'
        if self.direction == 'right':
            back_move = 'left'
        possible_dir.remove(back_move)
        not_variant = True
        while possible_dir:
            rnd_n = randint(0, len(possible_dir) - 1)
            rnd_dir = possible_dir.pop(rnd_n)
            if rnd_dir == 'up':
                self.rect.y -= self.speed
                if pygame.sprite.spritecollideany(self, wall_group):
                    self.rect.y += self.speed
                    continue
                self.direction = 'up'
                not_variant = False
                self.image = load_image(
                    str(int(self.start_picture) + 3) + '.png')
                break
            if rnd_dir == 'down':
                self.rect.y += self.speed
                if pygame.sprite.spritecollideany(self, wall_group):
                    self.rect.y -= self.speed
                    continue
                self.direction = 'down'
                not_variant = False
                self.image = load_image(self.start_picture + '.png')
                break
            if rnd_dir == 'left':
                self.rect.x -= self.speed
                if pygame.sprite.spritecollideany(self, wall_group):
                    self.rect.x += self.speed
                    continue
                self.direction = 'left'
                not_variant = False
                self.image = load_image(
                    str(int(self.start_picture) + 2) + '.png')
                break
            if rnd_dir == 'right':
                self.rect.x += self.speed
                if pygame.sprite.spritecollideany(self, wall_group):
                    self.rect.x -= self.speed
                    continue
                self.direction = 'right'
                not_variant = False
                self.image = load_image(
                    str(int(self.start_picture) + 1) + '.png')
                break
        if not_variant:
            if back_move == 'up':
                self.rect.y -= self.speed
            if back_move == 'down':
                self.rect.y += self.speed
            if back_move == 'left':
                self.rect.x -= self.speed
            if back_move == 'right':
                self.rect.x += self.speed
            self.direction = back_move

    def time_scale(self):
        seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
        if seconds < 5:
            self.speed = 1
        else:
            self.speed = 2


def generate_level(level):
    list_sprites = []
    list_ghost = []
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x, name in enumerate(level[y]):
            if int(name) >= 172 and int(name) <= 233:
                Wall(name, x, y)
            if int(name) == 1:
                Coins(name, x, y)
            if int(name) == 91:
                new_player = Player(x, y)
                list_sprites.append(Life(11, 15))
                list_sprites.append(Life(12, 15))
                list_sprites.append(Life(13, 15))
            if 27 <= int(name) <= 30 or 44 <= int(name) <= 47:
                list_ghost.append(Ghost(name, x, y))
            if int(name) == 14:
                Point(name, x, y)
            if int(name) == 48:
                Cherry(name, x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x + 1, y + 2, list_sprites, list_ghost


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 200
        self.dy = 200

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - tile_height // 2)


# НАЧАЛО ПРОГРАММЫ

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
cherry_group = pygame.sprite.Group()
point_group = pygame.sprite.Group()
life_group = pygame.sprite.Group()

pygame.init()

tile_width = tile_height = 40
clock = pygame.time.Clock()

opened_levels = 1

x = 15
y = 16

size = WIDTH, HEIGHT = x * tile_width, y * tile_height
screen = pygame.display.set_mode(size)

StartScreen(WIDTH, HEIGHT)
last_level = False

player = Player(-1, -1)
player.status = 'идет игра'
while True:
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    coins_group = pygame.sprite.Group()
    ghost_group = pygame.sprite.Group()
    cherry_group = pygame.sprite.Group()
    point_group = pygame.sprite.Group()
    life_group = pygame.sprite.Group()

    if player.status == 'конец игры':
        last_level = True

    if last_level:
        print('STOP')
        break

    n_level = str(level_choose())
    if int(n_level) == 4:
        last_level = True

    player, x, y, list_sprites, list_ghost = generate_level(
        load_level('level_' + n_level + '.txt'))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                pygame.quit()
        for key, func in [(pygame.K_d, player.right), (pygame.K_a, player.left),
                          (pygame.K_s, player.down), (pygame.K_w, player.up)]:
            if pygame.key.get_pressed()[key]:
                func()

        if player.status == 'конец игры':
            game_over()
            break

        if player.status == 'идет игра':
            all_sprites.update()
            screen.fill((0, 0, 0))
            tiles_group.draw(screen)
            wall_group.draw(screen)
            coins_group.draw(screen)
            cherry_group.draw(screen)
            point_group.draw(screen)
            player_group.draw(screen)
            ghost_group.draw(screen)
            life_group.draw(screen)

            player.score_print()
            pygame.display.flip()
            clock.tick(60)
        if player.status == 'монстр':
            try_again()
        if player.status == 'выигрыш':
            win()
            break

game_end()
