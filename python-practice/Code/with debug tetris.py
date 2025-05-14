import pygame
import random

# --- Game Constants ---
GRID_SHAPES = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[4, 5, 9, 10], [2, 6, 5, 9]],
    [[6, 7, 9, 10], [1, 5, 6, 10]],
    [[2, 1, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    [[1, 2, 5, 6]],
]
BLOCK_COLORS = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

# --- Screen Dimensions ---
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
GAME_GRID_WIDTH = 10  # Number of blocks horizontally
GAME_GRID_HEIGHT = 20  # Number of blocks vertically
BLOCK_SIZE = 20

GRID_TOP_LEFT_X = (SCREEN_WIDTH - GAME_GRID_WIDTH * BLOCK_SIZE) // 2
GRID_TOP_LEFT_Y = SCREEN_HEIGHT - GAME_GRID_HEIGHT * BLOCK_SIZE - 50


# --- Block Class ---
class TetrisBlock:
    def __init__(self, x_grid, y_grid, shape_index):
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.shape_index = shape_index
        self.color_index = shape_index
        self.rotation_state = 0

    def get_block_image(self):
        return GRID_SHAPES[self.shape_index][self.rotation_state]

    def rotate_block(self):
        self.rotation_state = (self.rotation_state + 1) % len(GRID_SHAPES[self.shape_index])


# --- Tetris Game Class ---
class TetrisGame:
    def __init__(self, grid_height, grid_width):
        self.level = 2
        self.score = 0
        self.game_state = "start"
        self.game_field = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.block_size = BLOCK_SIZE
        self.grid_x_offset = GRID_TOP_LEFT_X
        self.grid_y_offset = GRID_TOP_LEFT_Y
        self.current_block = None
        self.next_block = None

    def create_new_block(self):
        self.current_block = TetrisBlock(3, 0, random.randint(0, len(GRID_SHAPES) - 1))

    def create_next_block(self):
        self.next_block = TetrisBlock(3, 0, random.randint(0, len(GRID_SHAPES) - 1))

    def check_intersection(self):
        intersecting = False
        if self.current_block:
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.current_block.get_block_image():
                        y_pos = i + self.current_block.y_grid
                        x_pos = j + self.current_block.x_grid
                        if (y_pos > self.grid_height - 1 or
                                x_pos > self.grid_width - 1 or
                                x_pos < 0 or
                                (y_pos >= 0 and self.game_field[y_pos][x_pos] > 0)):
                            intersecting = True
                            break
                if intersecting:
                    break
        return intersecting

    def clear_full_lines(self):
        lines_cleared = 0
        row_index = self.grid_height - 1
        while row_index >= 0:
            if all(self.game_field[row_index][col] > 0 for col in range(self.grid_width)):
                lines_cleared += 1
                for y in range(row_index, 0, -1):
                    self.game_field[y] = self.game_field[y - 1][:]
                self.game_field[0] = [0] * self.grid_width
            else:
                row_index -= 1
        self.score += lines_cleared ** 2

    def draw_upcoming_block(self, surface):
        font = pygame.font.SysFont("Calibri", 30)
        label = font.render("Next Shape", 1, (128, 128, 128))
        surface.blit(label,
                     (self.grid_x_offset + self.grid_width * self.block_size + 50,
                      self.grid_y_offset + self.grid_height / 2 - 100))

        if self.next_block:
            next_shape = self.next_block.get_block_image()
            start_x = self.grid_x_offset + self.grid_width * self.block_size + 50
            start_y = self.grid_y_offset + self.grid_height / 2 - 70
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in next_shape:
                        pygame.draw.rect(surface, BLOCK_COLORS[self.next_block.color_index],
                                         (start_x + j * 30, start_y + i * 30, 30, 30), 0)

    def move_block_down(self):
        if self.current_block:
            self.current_block.y_grid += 1
            if self.check_intersection():
                self.current_block.y_grid -= 1
                self.freeze_block()

    def drop_block(self):
        if self.current_block:
            while not self.check_intersection():
                self.current_block.y_grid += 1
            self.current_block.y_grid -= 1
            self.freeze_block()

    def freeze_block(self):
        if self.current_block:
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.current_block.get_block_image():
                        y_pos = i + self.current_block.y_grid
                        x_pos = j + self.current_block.x_grid
                        if 0 <= y_pos < self.grid_height and 0 <= x_pos < self.grid_width:
                            self.game_field[y_pos][x_pos] = self.current_block.color_index
            self.clear_full_lines()
            self.current_block = self.next_block
            self.create_next_block()
            if self.check_intersection():
                self.game_state = "gameover"

    def move_block_horizontal(self, delta_x):
        if self.current_block:
            old_x = self.current_block.x_grid
            self.current_block.x_grid += delta_x
            if self.check_intersection():
                self.current_block.x_grid = old_x

    def rotate_current_block(self):
        if self.current_block:
            old_rotation = self.current_block.rotation_state
            self.current_block.rotate_block()
            if self.check_intersection():
                self.current_block.rotation_state = old_rotation


def main_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Tetris Game")
    clock = pygame.time.Clock()
    fps = 25
    game = TetrisGame(GAME_GRID_HEIGHT, GAME_GRID_WIDTH)
    game_tick_counter = 0
    is_pressing_down = False
    game.create_new_block()
    game.create_next_block()
    game_running = True

    while game_running:
        if game.current_block is None:
            game.create_new_block()
        if game.next_block is None:
            game.create_next_block()

        game_tick_counter += 1
        if game_tick_counter > 100000:
            game_tick_counter = 0

        if game.game_state == "start" and (
                game_tick_counter % (fps // game.level // 2) == 0 or is_pressing_down):
            game.move_block_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate_current_block()
                if event.key == pygame.K_DOWN:
                    game.move_block_down()
                    is_pressing_down = True
                if event.key == pygame.K_LEFT:
                    game.move_block_horizontal(-1)
                if event.key == pygame.K_RIGHT:
                    game.move_block_horizontal(1)
                if event.key == pygame.K_SPACE:
                    game.drop_block()
                if event.key == pygame.K_ESCAPE:
                    game = TetrisGame(GAME_GRID_HEIGHT, GAME_GRID_WIDTH)
                    game.create_new_block()
                    game.create_next_block()
                    game.game_state = "start"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    is_pressing_down = False

        screen.fill('#FFFFFF')

        # Draw the game grid
        for i in range(game.grid_height):
            for j in range(game.grid_width):
                pygame.draw.rect(screen, '#B2BEB5',
                                 [game.grid_x_offset + game.block_size * j,
                                  game.grid_y_offset + game.block_size * i,
                                  game.block_size, game.block_size], 1)
                if game.game_field[i][j] > 0:
                    pygame.draw.rect(screen, BLOCK_COLORS[game.game_field[i][j]],
                                     [game.grid_x_offset + game.block_size * j + 1,
                                      game.grid_y_offset + game.block_size * i + 1,
                                      game.block_size - 2, game.block_size - 2])

        # Draw the current moving block
        if game.current_block:
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in game.current_block.get_block_image():
                        pygame.draw.rect(screen, BLOCK_COLORS[game.current_block.color_index],
                                         [game.grid_x_offset + game.block_size * (
                                                 j + game.current_block.x_grid) + 1,
                                          game.grid_y_offset + game.block_size * (
                                                  i + game.current_block.y_grid) + 1,
                                          game.block_size - 2, game.block_size - 2])

        # Display the score
        font = pygame.font.SysFont('Calibri', 40, True, False)
        game_score_text = font.render(f"Score: {game.score}", True, '#000000')
        screen.blit(game_score_text, [300, 0])

        # Display game over message
        if game.game_state == "gameover":
            game_over_text = font.render("Game Over", True, '#000000')
            restart_text = font.render("Press ESC", True, '#000000')
            screen.blit(game_over_text, [300, 200])
            screen.blit(restart_text, [300, 265])

        game.draw_upcoming_block(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()  # <--- Moved pygame.quit() here


if __name__ == '__main__':
    pygame.init()
    start_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris by YourName")
    start_running = True
    start_font = pygame.font.SysFont("Calibri", 70, bold=True)
    start_label = start_font.render("Press any key to begin!", True, '#FFFFFF')
    start_color = (20, 60, 40)

    while start_running:
        start_screen.fill(start_color)
        start_screen.blit(start_label, (10, SCREEN_HEIGHT // 2 - 35))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_running = False
            if event.type == pygame.KEYDOWN:
                start_running = False
                main_game()  # Call the main game function

def check_intersection(self):
        print("check_intersection() CALLED")  # General call check
        if self.current_block:
            print(f"  Checking shape index: {self.current_block.shape_index}")  # <--- Check shape index in check_intersection
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.current_block.get_block_image():
                        y_pos = i + self.current_block.y_grid
                        x_pos = j + self.current_block.x_grid

                        if self.current_block.shape_index == 0:  # Debug for I-shape
                            print(f"    Checking I-Shape segment: x={x_pos}, y={y_pos}, rotation={self.current_block.rotation_state}")
                            if y_pos > self.grid_height - 1:
                                print("      - Below bottom!")
                            if x_pos > self.grid_width - 1:
                                print("      - Beyond right!")
                            if x_pos < 0:
                                print("      - Beyond left!")
                            if y_pos >= 0 and x_pos >= 0 and x_pos < self.grid_width and y_pos < self.grid_height and self.game_field[y_pos][x_pos] > 0:
                                print("      - Colliding with existing block!")

                        if (y_pos > self.grid_height - 1 or
                            x_pos > self.grid_width - 1 or
                            x_pos < 0 or
                            (y_pos >= 0 and x_pos >= 0 and x_pos < self.grid_width and y_pos < self.grid_height and self.game_field[y_pos][x_pos] > 0)):
                            intersecting = True
                            break
                if intersecting:
                    break
        return intersecting
    # pygame.quit() <--- Removed from here