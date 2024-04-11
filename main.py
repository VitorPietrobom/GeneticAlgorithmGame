import pygame
import random

# Initialize Pygame
pygame.init()

# GAME SETTINGS
MIN_VELOCITY = 4
MAX_VELOCITY = 6
PLAYER_SPEED = 7
POINTS_SPAWN_RATE = 2
ENEMIES_SPAWN_RATE = 2

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Points Collector")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Player square class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED
        # Keep player within screen boundaries
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))




# Dot circle class
class Dot(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.radius = 10  # Define the radius of the circle
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Create a surface with per-pixel alpha
        pygame.draw.circle(self.image, color, (10, 10), 10)  # Draw a circle
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, screen_width), 0)
        self.chance = random.randint(1, 4)
        if self.chance == 1:
            self.rect.center = (0, random.randint(0, screen_height))
        elif self.chance == 2:
            self.rect.center = (screen_width, random.randint(0, screen_height))
        elif self.chance == 3:
            self.rect.center = (random.randint(0, screen_width), 0)
        else:
            self.rect.center = (random.randint(0, screen_width), screen_height)
        self.speed = random.randint(MIN_VELOCITY, MAX_VELOCITY)

    def update(self):
        if self.chance == 1:
            self.rect.x += self.speed
        elif self.chance == 2:
            self.rect.x -= self.speed
        elif self.chance == 3:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed
        if not pygame.Rect(0, 0, screen_width, screen_height).colliderect(self.rect):
            # If the enemy sprite is not colliding with the screen boundaries, delete it
            self.kill()


# Main function
def main():
    # Create player
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    points_sprites = pygame.sprite.Group()    

    enemies_sprites = pygame.sprite.Group()

    # Game loop
    running = True
    score = 0
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        # Create points circles
        
        if random.randint(1, 100) <= POINTS_SPAWN_RATE:
            points = Dot(GREEN)
            points_sprites.add(points)
            all_sprites.add(points)

        if random.randint(1, 100) <= ENEMIES_SPAWN_RATE:
            enemies = Dot(RED)
            enemies_sprites.add(enemies)
            all_sprites.add(enemies)


        all_sprites.update()
        points_sprites.update()
        enemies_sprites.update()

        # Check for collisions
        collisions = pygame.sprite.spritecollide(player, points_sprites, True)
        for _ in collisions:
            score += 1
        
        collisions = pygame.sprite.spritecollide(player, enemies_sprites, True)
        for _ in collisions:
            score -= 1

        if score < 0:
            running = False

        # Draw
        screen.fill(WHITE)
        all_sprites.draw(screen)
        points_sprites.draw(screen)

        # Display score
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
