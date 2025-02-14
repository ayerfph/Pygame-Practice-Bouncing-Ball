import pygame

pygame.init()

#Display Resolution
display = pygame.display.set_mode((1000, 600))

#Real-time clock / fps
clock = pygame.time.Clock()
FPS = 50

#Set ng Acceleration para sa bounce ng ball
ACCELERATION = 0.5

class Ball():
    #initialize yung ball
    def __init__(self):
        self.y = 200
        self.velocity = 10
    
    #define mo yung circle (ball)
    def draw(self):
        pygame.draw.circle(display, (0, 0, 0), (500, int(self.y)), 17)
        pygame.draw.circle(display, (255, 215, 0), (500, int(self.y)), 15)

    #define mo yung movement ng ball
    def move(self):
        self.velocity += ACCELERATION
        self.y += self.velocity
        if self.y >= 375:
            self.velocity = -self.velocity

#Game loop
def game():
    ball = Ball()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #loop
        ball.move()

        # Eto yung background color
        display.fill((255,255,255))

        # Dito yung gagawa ng lines (display, (color), (x1, y1), (x2, y2), thickness)
        pygame.draw.line(display, (0, 0, 0), (0, 400), (1000, 400), 10)

        #i call mo yung ball
        ball.draw()

        # Dito yung gagawa ng circle (bounce) : For demo muna tas i comment mo nalang mamaya
        #pygame.draw.circle(display, (255, 0, 0), (500, 200), 15)

        #Update the display
        pygame.display.update()
        clock.tick(FPS)
game()
pygame.quit()