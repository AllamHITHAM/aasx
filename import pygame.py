import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up display
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chasing the Dot Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
yellow = (255, 255, 0)

# Set up clock
clock = pygame.time.Clock()
dot_size = 10
player_size = 15
game_duration = 30  # seconds
player_speed = 5

# Set up fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score
def display_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    screen.blit(value, [0, 0])

# Function to draw the player (the dot you control)
def draw_player(x, y):
    pygame.draw.circle(screen, green, (x, y), player_size)

# Function to draw the target (the dot you chase)
def draw_target(x, y):
    pygame.draw.circle(screen, yellow, (x, y), dot_size)

# Function to display a message when the game ends
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Main game loop
def gameLoop():
    game_over = False
    score = 0

    # Player's initial position
    player_x = width / 2
    player_y = height / 2

    # Player's movement
    x_change = 0
    y_change = 0

    # Create the target (dot to chase)
    target_x = random.randint(50, width - 50)
    target_y = random.randint(50, height - 50)

    # Obstacles list
    obstacles = []
    for _ in range(3):  # Create 3 obstacles
        obs_x = random.randint(50, width - 50)
        obs_y = random.randint(50, height - 50)
        obstacles.append((obs_x, obs_y))

    start_time = time.time()

    while not game_over:
        # Check time limit
        elapsed_time = time.time() - start_time
        if elapsed_time > game_duration:
            game_over = True
            display_message("Time's up! Final Score: " + str(score), red)
            pygame.display.update()
            pygame.time.wait(2000)  # Wait for 2 seconds before closing
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -player_speed
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = player_speed
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -player_speed
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = player_speed
                    x_change = 0

        # Update player's position
        player_x += x_change
        player_y += y_change

        # Check for boundary collisions
        if player_x > width:
            player_x = 0
        elif player_x < 0:
            player_x = width
        if player_y > height:
            player_y = 0
        elif player_y < 0:
            player_y = height

        # Fill the screen with a background color
        screen.fill(blue)

        # Draw the player
        draw_player(player_x, player_y)

        # Draw the target (dot to chase)
        draw_target(target_x, target_y)

        # Draw obstacles
        for obs in obstacles:
            pygame.draw.rect(screen, red, [obs[0], obs[1], 20, 20])

        # Display the score
        display_score(score)

        # Check if player catches the target
        if (player_x - target_x)**2 + (player_y - target_y)**2 < (player_size + dot_size)**2:
            score += 1
            target_x = random.randint(50, width - 50)
            target_y = random.randint(50, height - 50)

        # Check if player hits any obstacle
        for obs in obstacles:
            if (player_x - obs[0])**2 + (player_y - obs[1])**2 < (player_size + 10)**2:
                score -= 1
                obstacles.remove(obs)
                break

        # Update the screen
        pygame.display.update()

        # Set the frame rate
        clock.tick(30)

    pygame.quit()
    quit()

# Run the game
gameLoop()
