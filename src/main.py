import sys, pygame


assetsPath = [
    "assets/black_bishop.svg",
    "assets/black_king.svg",
    "assets/black_knight.svg",
    "assets/black_pawn.svg",
    "assets/black_queen.svg",
    "assets/black_rook.svg",
    "assets/whit_rook.svg",
    "assets/white_bishop.svg",
    "assets/white_king.svg",
    "assets/white_knight.svg",
    "assets/white_pawn.svg",
    "assets/white_queen.svg"
]


def main():
    print (pygame.ver)

    pygame.init()

    size = width, height = 800, 600
    
    speed = [2, 2]
    background = 255, 255, 255

    screen = pygame.display.set_mode(size, pygame.RESIZABLE, vsync=1)

    ball = pygame.image.load("assets/intro_ball.gif")
    ballrect = ball.get_rect()

    assets = []
    for path in assetsPath:
        assets.append(pygame.image.load(path))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(background)
        screen.blit(ball, ballrect)

        for asset in assets:
            screen.blit(asset, asset.get_rect())

        pygame.display.flip()


main()