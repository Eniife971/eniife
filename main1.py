import pygame
import lobby
# initialise pygame
pygame.init()

# setting up the game window
screen = pygame.display.set_mode((800, 600))
#setting the icon for the window
icon=pygame.image.load('game_icon.webp')
pygame.display.set_icon(icon)
#set title of the game
pygame.display.set_caption("Quest for knowledge")

#set up the main menu background image
menu_bg=pygame.image.load('game_menubackground.jpg')
#resizing to fit the window
menu_bg=pygame.transform.scale(menu_bg, (800, 600))

#setting up font
font=pygame.font.SysFont(None, 60)
button_color=(200, 200, 200)
button_hover_color=(170, 170, 170)
small_font=pygame.font.SysFont(None, 40)
#Text
title_text=font.render("Quest for knowledge", True, (0, 0, 0))
title_text_shadow=font.render("Quest for knowledge", True, (50,50,50))
start_text=small_font.render("Start Game", True, (0, 0, 0))
quit_text=small_font.render("Quit", True, (0, 0, 0))

#get rectangles for positioning
title_rect=title_text.get_rect(center=(400,100))
start_button_rect=pygame.Rect(300,250,200,60)
quit_button_rect=pygame.Rect(300,350,200,60)

#to Define the border for the title
border_color=(200,200,200)
border_thickness=4
#to create a rectangle for the border around the title
border_rect=pygame.Rect(title_rect.x-10, title_rect.y-10, title_rect.width + 20, title_rect.height + 20)

#to load the character image
character_img=pygame.image.load('student_character4.webp')
#to resize
character_img=pygame.transform.scale(character_img, (250,400))
# to set the position for the character
character_rect=character_img.get_rect(topleft=(50,150))

#start game button pulsing effect variables
pulse_size=1
pulse_direction=1
pulse_speed=0.005
clock=pygame.time.Clock()




#game loop(Main menu)
running=True
while running:
  # to check for events like closing the window
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running=False
      elif event.type==pygame.MOUSEBUTTONDOWN:
         mouse_x, mouse_y=pygame.mouse.get_pos()
         #start game button area
         if 330 <= mouse_x <= 470 and 250 <= mouse_y <= 290:
            print("Start Game clicked")
            running=False
            lobby.run_lobby() #----------------->calling the lobby function
        #Quit button area
         if 360 <= mouse_x <=440 and 320 <= mouse_y <= 360:
              pygame.quit()

	#to update the pulse size of the start button
  if pulse_direction==1:       # Growing
        pulse_size +=pulse_speed  
        if pulse_size >=1.2:     # the maximum size limit
            pulse_direction= -1  #to reverse the direction
  elif pulse_direction== -1:  #shrinking
      pulse_size -= pulse_speed
      if pulse_size <=1:      #the minimum size limit
          pulse_direction=1   #Reverse the direction
          

  #to show the background image
  screen.blit(menu_bg, (0,0))
  #to draw  character image
  screen.blit(character_img, character_rect)
  #to Draw shadow for the title
  screen.blit(title_text_shadow, (title_rect.x + 2, title_rect.y + 2))
  #to Draw the title text with the white font
  screen.blit(title_text, title_rect)
  #to draw border around the title
  pygame.draw.rect(screen, border_color, border_rect, border_thickness)
  #to draw the start Game button with pulsing size
  start_button_rect.width=int(200 * pulse_size)
  start_button_rect.height=int(60 * pulse_size)
  #to check for mouse hover to change button color
  mouse_pos=pygame.mouse.get_pos()
  #Draw buttons
  mouse_pos=pygame.mouse.get_pos()
  pygame.draw.rect(screen, button_hover_color if start_button_rect.collidepoint(mouse_pos) else button_color, start_button_rect)
  pygame.draw.rect(screen,button_hover_color if quit_button_rect.collidepoint(mouse_pos) else button_color, quit_button_rect)
  #draw text on buttons
  screen.blit(start_text, start_text.get_rect(center=start_button_rect.center))
  screen.blit(quit_text, quit_text.get_rect(center=quit_button_rect.center))
  pygame.display.update()
  clock.tick(60)
pygame.quit()