import pygame,sys,random

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos):
		super().__init__()
		self.uncharged = pygame.image.load(path)#default one.passive_ship_surface
		self.charged = pygame.image.load('images/spaceship_charged.png')#active_ship_surface

		self.image = self.uncharged
		self.rect = self.image.get_rect(center = (x_pos,y_pos))
		self.shield_surface = pygame.image.load('images/shield.png')
		self.health = 5

	def update(self):
		self.rect.center = pygame.mouse.get_pos()
		self.screen_constrain()
		self.display_health()

	def screen_constrain(self):
		if self.rect.right >= 1280:
			self.rect.right = 1280
		if self.rect.left <= 0:
			self.rect.left = 0

	def display_health(self):
		for index,shield in enumerate(range(self.health)):
			screen.blit(self.shield_surface,(10 + index * 40 ,10))

	def get_damage(self,damage_amount):
		self.health -= damage_amount

	def charge(self):
		self.image = self.charged

	def discharge(self):
		self.image = self.uncharged



class Meteor(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos,x_speed,y_speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (x_pos,y_pos))
		self.x_speed = x_speed
		self.y_speed = y_speed

	def update(self):
		self.rect.centerx += self.x_speed
		self.rect.centery += self.y_speed

		if self.rect.centery >= 800:
			self.kill()

class Laser(pygame.sprite.Sprite):
	def __init__(self,path,pos,speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed

	def update(self):
		self.rect.y -= self.speed
		if self.rect.centery <= -100:
			self.kill()

#the main_game is a local scope 
def main_game():
	global laser_active
	laser_group.draw(screen)
	spaceship_group.draw(screen)
	meteor_group.draw(screen)

	laser_group.update()
	spaceship_group.update()
	meteor_group.update()

	# Collision 
	if pygame.sprite.spritecollide(spaceship_group.sprite,meteor_group,True):
		spaceship_group.sprite.get_damage(1)

	for laser in laser_group:
		pygame.sprite.spritecollide(laser,meteor_group,True)

	#Laser timer
	if pygame.time.get_ticks() - laser_timer >= 1000:
		laser_active = True # after 1 sec it becomes true
		spaceship_group.sprite.charge()

	return 1
	

def end_game():
	text_surface = game_font.render('Game Over',True,(255,255,255))
	text_rect = text_surface.get_rect(center = (640,340))
	screen.blit(text_surface,text_rect)

	score_surface = game_font.render(f'Score: {score}',True,(255,255,255))
	score_rect = score_surface.get_rect(center = (640,380))
	screen.blit(score_surface,score_rect)

	

pygame.init() # initiate pygame
screen = pygame.display.set_mode((1280,720)) # Create display surface
clock = pygame.time.Clock() # Create clock object
game_font = pygame.font.Font('images/LazenbyCompSmooth.ttf',40)
score = 0  #this score is in the global scope
laser_timer = 0
laser_active = False

spaceship = SpaceShip('images/spaceship.png',640,500)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

laser_group = pygame.sprite.Group()

meteor_group = pygame.sprite.Group()
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT,150)

while True: # Game loop
	for event in pygame.event.get(): # Check for events / Player input
		if event.type == pygame.QUIT: # Close the game
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and laser_active: #shooting when the mouse works with laser
			new_laser = Laser('images/Laser.png',event.pos,15)
			laser_group.add(new_laser)
			laser_active = False #cannot shoot no more
			laser_timer = pygame.time.get_ticks()
			spaceship_group.sprite.discharge() #calling a function



#this checks the mouse button when the game is over
		if event.type == pygame.MOUSEBUTTONDOWN and spaceship_group.sprite.health <= 0:
			spaceship_group.sprite.health = 5
			meteor_group.empty()
			score = 0
			

		if event.type == METEOR_EVENT:
			random_meteor_image = random.choice(('images/Meteor1.png','images/Meteor2.png','images/Meteor3.png'))
			random_x_pos = random.randrange(0,1280)
			random_y_pos = random.randrange(-600,-40)
			random_speed_y = random.randint(3,10)
			random_speed_x = random.randint(-1,1)
			meteor = Meteor(random_meteor_image,random_x_pos,random_y_pos,random_speed_x,random_speed_y,)
			meteor_group.add(meteor)

	screen.fill((42,45,51))
	if spaceship_group.sprite.health > 0:
		score += main_game()#when the game keeps on running it changes the score by 1
	else:
		end_game()

	pygame.display.update() # Draw frame
	clock.tick(120) # Control the framerate