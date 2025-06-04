import pygame

white, black, red, blue = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 0, 255)

pygame.init()

width, height = 305, 400
screen = pygame.display.set_mode((width, height))

ball = pygame.Rect(width // 2 - 5, height // 2, 10, 10)

ballDx, ballDy = 3, -3

paddle = pygame.Rect(width // 2 - 50, height - 50, 100, 10)

brickRows, brickCols = 3, 4
brickGap = 5
brickWidth = 70
brickHeight = 30
bricks = []
for r in range(brickRows):
    for c in range(brickCols):
        brick = pygame.Rect(
            c * (brickWidth + brickGap) + brickGap,
            r * (brickHeight + brickGap) + brickGap,
            brickWidth,
            brickHeight,
        )
        bricks.append(brick)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ball.left <= 0 or ball.right >= width:
        ballDx = -ballDx

    elif ball.top <= 0:
        ballDy = -ballDy

    elif ball.bottom >= height:
        running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle = paddle.move(-3, 0)

    elif keys[pygame.K_RIGHT] and paddle.right < width:
        paddle = paddle.move(3, 0)

    ball = ball.move(ballDx, ballDy)

    if ball.colliderect(paddle) and ballDy > 0:
        ballDy = -ballDy

    for brick in bricks:
        if ball.colliderect(brick):
            ballDy = -ballDy
            bricks.remove(brick)
    if bricks == []:
        running = False

    screen.fill(white)
    pygame.draw.ellipse(screen, black, ball)
    pygame.draw.rect(screen, blue, paddle)
    for brick in bricks:
        pygame.draw.rect(screen, red, brick)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit
