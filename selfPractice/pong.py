import pygame
import random

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)

    # Game variables
    paddle_width, paddle_height = 15, 90
    ball_radius = 7
    ball_speed_x, ball_speed_y = 7 * random.choice((1, -1)), 7 * random.choice((1, -1))
    player_speed = 0
    opponent_speed = 0
    player_score = 0
    opponent_score = 0
    game_font = pygame.font.Font(None, 36)

    # Timer
    start_time = pygame.time.get_ticks()

    # Positions
    ball = pygame.Rect(width // 8 - ball_radius, height // 8 - ball_radius, ball_radius * 8, ball_radius * 8)
    player = pygame.Rect(width - 20 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
    opponent = pygame.Rect(20, height // 2 - paddle_height // 2, paddle_width, paddle_height)

    # Game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_speed -= 7
                if event.key == pygame.K_s:
                    opponent_speed += 7
                if event.key == pygame.K_w:
                    opponent_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7
                if event.key == pygame.K_s:
                    opponent_speed -= 7
                if event.key == pygame.K_w:
                    opponent_speed += 7

        # Game logic
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        player.y += player_speed
        opponent.y += opponent_speed

        if ball.top <= 0 or ball.bottom >= height:
            ball_speed_y *= -1

        if ball.left <= 0:
            player_score += 1
            ball_speed_x *= -1
        if ball.right >= width:
            opponent_score += 1
            ball_speed_x *= -1

        if ball.colliderect(player) or ball.colliderect(opponent):
            ball_speed_x *= -1

        if player.top <= 0:
            player.top = 0
        if player.bottom >= height:
            player.bottom = height
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= height:
            opponent.bottom = height

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, WHITE, opponent)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (width // 2, 0), (width // 2, height))

        # Display Scores
        player_text = game_font.render(f"{player_score}", False, WHITE)
        screen.blit(player_text, (660, 10))
        opponent_text = game_font.render(f"{opponent_score}", False, WHITE)
        screen.blit(opponent_text, (120, 10))

        # Display Timer
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert milliseconds to seconds
        timer_text = game_font.render(f"{elapsed_time}", False, WHITE)
        screen.blit(timer_text, (width // 2 - 20, 10))

        # Updating the window
        pygame.display.flip()
        clock.tick(60)

    # End Game Screen
    end_game = True
    restart_button = pygame.Rect(width // 2 - 100, height // 2 - 60, 200, 50)
    quit_button = pygame.Rect(width // 2 - 100, height // 2 + 10, 200, 50)

    while end_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if restart_button.collidepoint(mouse_pos):
                    main()
                if quit_button.collidepoint(mouse_pos):
                    end_game = False

        screen.fill(BLACK)
        pygame.draw.rect(screen, GREY, restart_button)
        pygame.draw.rect(screen, GREY, quit_button)

        restart_text = game_font.render("Restart", True, BLACK)
        quit_text = game_font.render("Quit", True, BLACK)

        screen.blit(restart_text, (restart_button.x + 50, restart_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 65, quit_button.y + 10))

        pygame.display.flip()
        clock.tick(60)

    # Quit Pygame
    pygame.quit()

# Run the game
main()

