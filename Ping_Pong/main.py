import pygame as pg
import ball as Ball
import players

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Speed of the game
SPEED = 20

# Size of the ball
BALL_SIZE = 20

# Player size
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 80

# Player speed
PLAYER_SPEED = 10

# Score
SCORE = 10


def resetGame(ball, player1, player2):
    ball.x = SCREEN_WIDTH // 2
    ball.y = SCREEN_HEIGHT // 2
    player1.x = PLAYER_WIDTH
    player1.y = SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
    player2.x = SCREEN_WIDTH - PLAYER_WIDTH * 2
    player2.y = SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
    player1.score = 0
    player2.score = 0


def main():
    pg.init()
    pg.display.set_caption("Ping Pong")
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()

    ball = Ball.Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 5, 5)
    player1 = players.Player1(
        PLAYER_WIDTH,
        SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2,
        PLAYER_SPEED,
        True,
        True,
        0,
    )
    player2 = players.Player2(
        SCREEN_WIDTH - PLAYER_WIDTH * 2,
        SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2,
        PLAYER_SPEED,
        True,
        True,
        0,
    )

    # Render text
    font = pg.font.Font(None, 36)
    player1Won = font.render("Player 1 Won", True, (255, 255, 255))
    player2Won = font.render("Player 2 Won", True, (255, 255, 255))

    player1TextSurface = player1Won.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    )
    player2TextSurface = player2Won.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    )

    font2 = pg.font.Font(None, 24)
    player1Score = font2.render("P1 Score: 0", True, (255, 255, 255))
    player2Score = font2.render("P2 Score: 0", True, (255, 255, 255))

    player1ScoreSurface = player1Score.get_rect(center=(50, 20))
    player2ScoreSurface = player2Score.get_rect(center=(SCREEN_WIDTH - 60, 20))

    running = True
    while running:
        clock.tick(SPEED)
        screen.fill((0, 0, 0))

        # Register holding keys
        pressed_keys = pg.key.get_pressed()

        if pressed_keys[pg.K_w]:
            if player1.canMoveUp:
                player1.moveUp()
        if pressed_keys[pg.K_s]:
            if player1.canMoveDown:
                player1.moveDown()
        if pressed_keys[pg.K_UP]:
            if player2.canMoveUp:
                player2.moveUp()
        if pressed_keys[pg.K_DOWN]:
            if player2.canMoveDown:
                player2.moveDown()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Draw players
        pg.draw.rect(
            screen, (255, 255, 255), (player1.x, player1.y, PLAYER_WIDTH, PLAYER_HEIGHT)
        )
        pg.draw.rect(
            screen, (255, 255, 255), (player2.x, player2.y, PLAYER_WIDTH, PLAYER_HEIGHT)
        )

        # Draw ball
        pg.draw.rect(screen, (255, 255, 255), (ball.x, ball.y, BALL_SIZE, BALL_SIZE))

        # Check if the player has reached the top or bottom of the board and stop moving
        if player1.y != 0 or player1.y != SCREEN_HEIGHT - PLAYER_HEIGHT:
            player1.canMoveUp = True
            player1.canMoveDown = True
        if player1.y <= 0:
            player1.canMoveUp = False
        if player1.y >= SCREEN_HEIGHT - PLAYER_HEIGHT:
            player1.canMoveDown = False

        if player2.y != 0 or player2.y != SCREEN_HEIGHT - PLAYER_HEIGHT:
            player2.canMoveUp = True
            player2.canMoveDown = True
        if player2.y <= 0:
            player2.canMoveUp = False
        if player2.y >= SCREEN_HEIGHT - PLAYER_HEIGHT:
            player2.canMoveDown = False

        # Check if the ball reached the top or bottom of the screen and reverse the direction
        if ball.y >= SCREEN_HEIGHT - BALL_SIZE or ball.y <= 0:
            ball.changeDirection(ball.dx, -ball.dy)

        # Add initial score to the display
        screen.blit(player1Score, player1ScoreSurface)
        screen.blit(player2Score, player2ScoreSurface)

        # Check if the ball has hit a players board and reverse the direction and add score
        if (
            ball.x <= player1.x + PLAYER_WIDTH
            and player1.y <= ball.y
            and ball.y <= player1.y + PLAYER_HEIGHT
        ):
            ball.changeDirection(-ball.dx, ball.dy)
            player1.score += SCORE
            player1Score = font2.render(
                f"P1 Score: {player1.score}", True, (255, 255, 255)
            )
        if (
            ball.x + BALL_SIZE >= player2.x
            and player2.y <= ball.y
            and ball.y <= player2.y + PLAYER_HEIGHT
        ):
            ball.changeDirection(-ball.dx, ball.dy)
            player2.score += SCORE
            player2Score = font2.render(
                f"P2 Score: {player2.score}", True, (255, 255, 255)
            )

        # Check if the ball has reached the left or right side of the screen
        # If so, reset the game
        # And update the score
        if ball.x <= 0:
            screen.blit(player2Won, player2TextSurface)
            pg.display.update()
            pg.time.wait(2000)
            resetGame(ball, player1, player2)
            player1Score = font2.render(
                f"P1 Score: {player1.score}", True, (255, 255, 255)
            )
            player2Score = font2.render(
                f"P1 Score: {player2.score}", True, (255, 255, 255)
            )
        if ball.x >= SCREEN_WIDTH - BALL_SIZE:
            screen.blit(player1Won, player1TextSurface)
            pg.display.update()
            pg.time.wait(2000)
            resetGame(ball, player1, player2)
            player1Score = font2.render(
                f"P1 Score: {player1.score}", True, (255, 255, 255)
            )
            player2Score = font2.render(
                f"P2 Score: {player2.score}", True, (255, 255, 255)
            )

        ball.move()

        pg.display.flip()
        pg.display.update()

    # If loop ends, quit the game
    pg.quit()


if __name__ == "__main__":
    main()
