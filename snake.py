import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLOCK_SIZE = 20

INITIAL_SPEED = 10


class SnakeGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 36)

        self.reset()

    def reset(self):
        self.snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = "right"

        self.food = self.generate_food()

        self.score = 0
        self.speed = INITIAL_SPEED

        self.game_over = False

    def generate_food(self):
        while True:
            x = random.randint(
                0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randint(
                0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            food_pos = (x, y)

            if food_pos not in self.snake:
                return food_pos

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != "down":
                    self.direction = "up"
                elif event.key == pygame.K_DOWN and self.direction != "up":
                    self.direction = "down"
                elif event.key == pygame.K_LEFT and self.direction != "right":
                    self.direction = "left"
                elif event.key == pygame.K_RIGHT and self.direction != "left":
                    self.direction = "right"

    def update(self):
        head = self.snake[0]
        x, y = head

        if self.direction == "up":
            y -= BLOCK_SIZE
        elif self.direction == "down":
            y += BLOCK_SIZE
        elif self.direction == "left":
            x -= BLOCK_SIZE
        elif self.direction == "right":
            x += BLOCK_SIZE

        new_head = (x, y)
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.speed += 1
            self.food = self.generate_food()
        else:
            self.snake.pop()

        if (
            x < 0 or x >= SCREEN_WIDTH or
            y < 0 or y >= SCREEN_HEIGHT or
            new_head in self.snake[1:]
        ):
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)

        for block in self.snake:
            pygame.draw.rect(self.screen, GREEN,
                             (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

        pygame.draw.rect(self.screen, RED,
                         (self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE))

        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def run(self):
        while not self.game_over:
            self.handle_events()

            self.update()

            self.draw()

            pygame.display.flip()

            self.clock.tick(self.speed)

        pygame.quit()


game = SnakeGame()
game.run()

