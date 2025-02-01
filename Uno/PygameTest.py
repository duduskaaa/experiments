import pygame as pg
import sys

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Уно")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 30
clock = pg.time.Clock()

x, y = 400, 300
button = pg.Rect(x, y, 40, 40)
button_clicked = False

running = True
while running:
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
	
	if event.type == pg.MOUSEBUTTONDOWN:
		if button.collidepoint(event.pos):
			button_color = GREEN if button_clicked else RED
			 

	screen.fill((BLACK))

	
	pg.draw.rect(screen, button_color, button)
	
	clock.tick(FPS)
	pg.display.flip()
	

pg.quit()
sys.exit()