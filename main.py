import pygame
import math
height = 600
width = 800
screen = pygame.display.set_mode((width,height))

running = True

red = (255,0,0)
white = (255, 255, 255)

clock = pygame.time.Clock()

class User():
	def __init__(self , surface , colour , x_rect,y_rect,rect_width,rect_height):
		self.surface = surface
		self.colour = colour
		self.x_rect = x_rect
		self.y_rect = y_rect
		self.rect_width = rect_width
		self.rect_height = rect_height
	def moveup(self):
		self.y_rect -= 5
	def movedown(self):
		self.y_rect += 5
	def draw_rect(self):
		pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.x_rect, self.y_rect, self.rect_width,self.rect_height))
		
	def getxy(self):
		return self.x_rect,self.y_rect
		
class Ball():
	def __init__(self , surface , colour , x_circle,y_circle,radius,speed,velocityX,velocityY ):
		self.surface = surface
		self.colour = colour
		self.x_circle = x_circle
		self.y_circle = y_circle
		self.radius = radius
		self.speed = speed
		self.velocityX = velocityX
		self.velocityY = velocityY
		
		
		
		
	def moment(self):
		self.x_circle += self.velocityX
		self.y_circle += self.velocityY
		self.ball = pygame.draw.circle(self.surface, self.colour, (self.x_circle,self.y_circle), self.radius)
		
	def getballxy(self):
		return self.x_circle,self.y_circle
		
	def collision(self ,x_rect,y_rect,xcomp,ycomp):
		if(self.y_circle + self.radius > height or  self.y_circle-self.radius  < 0 ):
			self.velocityY = -self.velocityY

			
		if (self.y_circle + self.radius  > y_rect and self.x_circle - self.radius < x_rect + 50 and self.y_circle - self.radius < y_rect + 160 and self.x_circle + self.radius > x_rect):
			
			if self.x_circle < width/2:
				direction = 1
			else:
				direction = -1
			collide_point = (self.y_circle - (y_rect + 80))/80
			radian = collide_point * math.pi/4
			self.velocityX = direction *(self.speed * math.cos(radian))
			self.velocityY = direction * (self.speed * math.sin(radian))
			self.speed +=0.1
			
		if (self.y_circle + self.radius  > ycomp and self.x_circle - self.radius < xcomp + 50 and self.y_circle - self.radius < ycomp + 160 and self.x_circle + self.radius > xcomp):
			
			if self.x_circle > width/2:
				direction = -1
			else:
				direction = 1
			collide_point = (self.y_circle - (ycomp + 80))/80
			radian = collide_point * math.pi/4
			self.velocityX = direction *(self.speed * math.cos(radian))
			self.velocityY = direction * (self.speed * math.sin(radian))
			self.speed +=0.1			
	def scoring(self):

			if (self.x_circle + self.radius > width or self.x_circle - self.radius < 0):
				self.x_circle = width/2
				self.y_circle = height/2

			
			
ball = Ball(screen,red,width/2,height/2,25,5,5,5) 
user = User(screen,white,0,height/2-100,50,160)
computer = User(screen,white,width-50,height/2-100,50,160)
moveup = False
movedown  = False

moveup1 = False
movedown1  = False
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				moveup = True
			if event.key == pygame.K_s:
				movedown = True
			if event.key == pygame.K_UP:
				moveup1 = True
			if event.key == pygame.K_DOWN:
				movedown1 = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				moveup = False
			if event.key == pygame.K_s:
				movedown = False
			if event.key == pygame.K_UP:
				moveup1 = False
			if event.key == pygame.K_DOWN:
				movedown1 = False
				
			
	screen.fill((0,0,0))
	
			
	ball.moment()
	xrect,yrect = user.getxy()	
	xcomp,ycomp = computer.getxy()
	ball.collision(xrect,yrect,xcomp,ycomp)
	xcomp,ycomp = computer.getxy()
	#ball.collision(xcomp,ycomp)
	
	
	if moveup == True:
		user.moveup()
	if movedown == True:
		user.movedown()
	if moveup1 == True:
		computer.moveup()
	if movedown1 == True:
		computer.movedown()
	user.draw_rect()
	computer.draw_rect()
	ball.scoring()
	pygame.display.flip()
	clock.tick(60)

	


