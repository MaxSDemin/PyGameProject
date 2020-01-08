import pygame

class Ground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 50

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):  # 0 пусто, 1 белый
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, color, (
                    x * self.cell_size + self.left,
                    y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(cell)
        self.on_click(cell)

    def on_click(self, cell):
        if cell != None:
            for i in range(self.height):
                if self.board[i][cell[1]] == 0:
                    self.board[i][cell[1]] = 1
                else:
                    self.board[i][cell[1]] = 0
            for j in range(self.width):
                if self.board[cell[0]][j] == 0:
                    self.board[cell[0]][j] = 1
                else:
                    self.board[cell[0]][j] = 0
            if self.board[cell[0]][cell[1]] == 0:
                self.board[cell[0]][cell[1]] = 1
            else:
                self.board[cell[0]][cell[1]] = 0

    def get_cell(self, mouse_pos):
        if self.left < mouse_pos[
            0] < self.width * self.cell_size + self.left and self.top < \
                mouse_pos[1] < self.height * self.cell_size + self.top:
            x = (mouse_pos[0] - self.left) // self.cell_size
            y = (mouse_pos[1] - self.top) // self.cell_size
            return y, x
        else:
            return None


pygame.init()
size = width, height = 600, 800
screen = pygame.display.set_mode(size)
color = (255, 255, 0)

ground = Ground(10, 10)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ground.get_click(event.pos)
    screen.fill((0, 0, 0))
    ground.render()
    pygame.display.flip()

pygame.quit()
