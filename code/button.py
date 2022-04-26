import pygame



class Button:
	def __init__(self, screen, text, position, size, color, command,):
		self.screen = screen
		self.text = text
		self.position = self.x, self.y = position
		self.size = size
		self.command = command
		self.color = color
		self.create_button()

	def create_button(self):
		''' creates button on first istance with text and colors '''
		self.font = pygame.font.SysFont("Arial", self.size)
		self.tx = self.font.render(self.text, 1, (0,0,0))
		tw, th = self.tx.get_size()
		self.rect = pygame.Rect(self.x, self.y, tw, th)
		self.image = pygame.Surface((tw,th))
		self.image.fill(self.color)
		self.image.blit(self.tx, (0,0))

	def blit(self):
		''' shows button '''
		self.hover_effect()
		self.image.blit(self.tx, (0,0))
		self.screen.blit(self.image, self.position)

	def hover_effect(self):
		''' creates hover and click color effect for button '''
		if self.rect.collidepoint(pygame.mouse.get_pos()): # checks if mouse is on button
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.command()
					self.image.fill((0,255,0)) # color when click
				else:
					self.image.fill((244,0,0)) # color when hover
		else:
			self.image.fill((255,255,0)) # color when not hover / default

