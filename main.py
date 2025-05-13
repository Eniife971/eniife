import pygame
import time 
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

#to set up the lobby background image
lobby_bg=pygame.image.load('lobby_room.webp')
#resizing the image to fit the screen
lobby_bg=pygame.transform.scale(lobby_bg, (800,600))
#to set up the plaque background for the lobby
plaque_color=(150,150,150)
plaque_width= 200 
plaque_height=60
plaque_x=300
plaque_y=60
# to create rectangle for the plaque
plaque_rect=pygame.Rect(plaque_x, plaque_y, plaque_width, plaque_height)
#to create the text for the lobby
lobby_text=small_font.render("Lobby", True, (0,0,0))
lobby_text_rect=lobby_text.get_rect(center=plaque_rect.center)
# small font for door labels
door_font=pygame.font.SysFont(None, 17)
# Door names and their positions
door_labels=[
    {"name": "Math Room", "pos": (140,200)},
    {"name": "English Room", "pos": (275,200)},
    {"name": "Science Lab", "pos": (406,200)},
    {"name": "History Hall", "pos": (540,200)},
    {"name": "GradChamber", "pos": (670,200)}
]
#player setup
player_x=400
player_y=500
player_speed=0.5
keys_pressed={"up": False, "down": False, "left": False, "right": False}

#to draw the movement instructions
def draw_movement_instructions(surface):
    #to set the box dimension and position
    box_x, box_y=20, screen.get_height() - 120
    box_width, box_height=260, 100
    box_color=(255,255,255)
    border_color=(0,0,0)
    text_color=(0,0,0)
#to draw the white box with black border
    pygame.draw.rect(surface, box_color, (box_x, box_y, box_width, box_height))
    pygame.draw.rect(surface, border_color, (box_x, box_y, box_width, box_height), 2)
    # to load the font
    font=pygame.font.SysFont(None, 15)
    # movement instruction lines
    lines=[
        "Go North: Press up Arrow key",
        "Go South: Press Down Arrow key",
        "Go West: Press Left Arrow key",
        "Go East: Press Right Arrow key"
    ]
    # to render and draw text lines
    for i, line in enumerate(lines):
        text=font.render(line, True, text_color)
        surface.blit(text, (box_x + 10, box_y + 5 + i * 22))
# to keep track of whether the player is in the Math room
in_math_room=False

# to set up the background image for the math room
math_room_bg=pygame.transform.scale(pygame.image.load("math_room.webp"), (800,600))

# to set the math puzzle
show_math_puzzle=False
current_question_index=0
math_question=[
    {"Question": "What is the square root of 196, divided by 7, multiplied by 5?", "Answer":10},
    {"Question": "What is the cube root of 27, multiplied by 12?", "Answer":36},
    {"Question": "What is 10+11+12+13+14+15+16?", "Answer":91},
]
user_input=""
feedback_message="" 
puzzle_completed=False
font=pygame.font.SysFont(None, 30)
# to declare variables for puzzle completion and key collection
puzzle_completed=False
key_collected=False
show_congratulations=False
show_collect_key_button=True
show_success_message=False
show_instruction_message=False

#font for the congratulations message
big_font=pygame.font.SysFont(None, 30)
#inventory
inventory=[]

#font sizes for the game over message and time left text
font_large=pygame.font.SysFont("Arial", 60)
font_medium= pygame.font.SysFont("Arial", 40)

# to define restart button rect
restart_button_width = 200
restart_button_height = 50
restart_button = pygame.Surface((restart_button_width, restart_button_height))
restart_button.fill((0, 128, 0))  # Dark green color
restart_button_rect = restart_button.get_rect()
restart_button_rect.center = (400, 300)






# Game loop function to start the game
def game_loop():
    game_timer=30   
    start_time=time.time() 
    game_over=False  
    global player_x, player_y, in_math_room, show_math_puzzle, current_question_index, user_input, feedback_message
    global show_congratulations, show_collect_key_button, show_success_message, show_instruction_message
    global inventory
    global restart_button_rect
    running=True
    while running:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            # restart button click handler
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #  to Check if the restart button was clicked
                if restart_button_rect.collidepoint(mouse_x, mouse_y):
                    # to  Reset the game variables when the restart button is clicked
                    game_timer = 30
                    start_time = time.time()  # Restart the timer
                    game_over = False
                    in_math_room=False
                    # Reset player position and other variables
                    player_x, player_y = 100, 100
                    inventory.clear()  # Clear any collected items
                    feedback_message= ""
                    current_question_index = 0
                    user_input = ""
                    show_math_puzzle = False
                    show_congratulations = False
                    show_collect_key_button = False
                    show_success_message = False
                    show_instruction_message = False

            # to handle input if the puzzle is being shown
            if show_math_puzzle:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        #to submit the answer
                        try:
                            if int(user_input)==math_question[current_question_index]["Answer"]:
                                feedback_message="Correct!"
                                current_question_index +=1
                                if current_question_index>= len(math_question):
                                    show_math_puzzle=False
                                    current_question_index=0
                                    user_input=""
                                    show_congratulations=True
                                else:
                                    user_input=""
                            else:
                                feedback_message="Wrong, try again!"
                                user_input=""
                        except ValueError:
                            feedback_message="Please enter a number"
                            user_input=""
                    elif event.key==pygame.K_BACKSPACE:
                        user_input=user_input[:-1]
                    else:
                        if event.unicode.isdigit():
                            user_input +=event.unicode
            else:
                # to check for key presses
                if event.type== pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        keys_pressed["up"]= True
                    elif event.key==pygame.K_DOWN:
                        keys_pressed["down"]= True
                    elif event.key== pygame.K_LEFT:
                        keys_pressed["left"]= True
                    elif event.key== pygame.K_RIGHT:
                        keys_pressed["right"]= True
                elif event.type==pygame.KEYUP:
                    if event.key== pygame.K_UP:
                        keys_pressed["up"]= False
                    elif event.key==pygame.K_DOWN:
                        keys_pressed["down"]= False
                    elif event.key==pygame.K_LEFT:
                        keys_pressed["left"]= False
                    elif event.key==pygame.K_RIGHT:
                        keys_pressed["right"]= False
                    
        if keys_pressed["up"]:
            player_y -= player_speed
        if keys_pressed["down"]:
            player_y += player_speed
        if keys_pressed["left"]:
            player_x -= player_speed
        if keys_pressed["right"]:
            player_x += player_speed
        # to restrict player movement inside the screen boundaries
        if in_math_room:
        # Stay inside the math room screen size 
            player_x = max(0, min(player_x, 800 - 25))  
            player_y = max(0, min(player_y, 600 - 20))  
        else:
            # restricting the movement in the lobby
            player_x = max(0, min(player_x, 800 - 25))
            player_y = max(0, min(player_y, 600 - 20))
                
            

        player_rect=pygame.Rect(player_x, player_y, 25, 20)
        # to update the timer
        if not game_over:
            time_left=game_timer-int(time.time() - start_time)
            if time_left<=0:
                game_over=True

        #to check if the player has reached the math room door
        math_room_door_rect= pygame.Rect(150,150,50,100)
        if player_rect.colliderect(math_room_door_rect) and not in_math_room:
            in_math_room= True
            show_math_puzzle=True
            current_question_index=0
            user_input=""
            feedback_message=""
        #to display background and to only draw the lobby elements if the player is in the lobby
        if in_math_room:
            screen.blit(math_room_bg, (0,0))
        else:
            screen.blit(lobby_bg, (0,0))
            #to show the lobby background for the game screen
            screen.blit(lobby_bg, (0,0))
            # to draw the plaque
            pygame.draw.rect(screen, plaque_color, plaque_rect)
            #to draw the lobby text on the plaque
            screen.blit(lobby_text, lobby_text_rect)
            #to draw door labels
            for label in door_labels:
                label_text=door_font.render(label["name"], True, (0,0,0))
                label_rect=label_text.get_rect(center=label["pos"])
                screen.blit(label_text, label_rect)
            
            #to Draw the invisible player as a black rectangle
            pygame.draw.rect(screen, (0,0,0), player_rect)

            instruction_text=[
                "you are now in the Lobby.",
                "All other Rooms are locked except the Math Room.",
                "The Math Room is your starting point.",
                "use your arrow keys to move the black box",
                "to enter the Math Room and begin your task."
            ]
            #to draw the instruction box
            instruction_box_rect=pygame.Rect(480,20,260,140)
            pygame.draw.rect(screen, (255,255,255), instruction_box_rect)
            pygame.draw.rect(screen, (0,0,0), instruction_box_rect, 2)
            #to draw the lines of instruction
            font=pygame.font.SysFont(None, 15)
            for i, line in enumerate(instruction_text):
                text_surface=font.render(line, True, (0,0,0))
                screen.blit(text_surface, (instruction_box_rect.x + 10, instruction_box_rect.y + 10 + i * 20))
            # calling the function of the movement instruction 
            draw_movement_instructions(screen)

            # to draw the puzzle interface
        if show_math_puzzle:
             # to draw a backkground box for the puzzle
            pygame.draw.rect(screen,(255,255,255), (150,250,500,200))
            pygame.draw.rect(screen, (0,0,0), (150,250,500,200),4)
            #to display the current question
            question_surface=font.render("Question: "+ math_question[current_question_index]["Question"], True, (0,0,0))
            screen.blit(question_surface, (170,280))
            #to display the user's current input
            input_surface=font.render("Your Answer: " + user_input, True, (0,0,0))
            screen.blit(input_surface, (170,340))
            #to display feedback
            feedback_surface=font.render(feedback_message, True, (0,128,0) if feedback_message=="Correct!" else (255,0,0))
            screen.blit(feedback_surface, (170,400))
            # to draw an hint button
            hint_button_color=(0,100,0)
            hint_button_rect = pygame.Rect(550, 202, 100, 40)  # Adjust x=530 (150+500-120), y=260 (just below top edge)
            pygame.draw.rect(screen, hint_button_color, hint_button_rect)
            hint_text = font.render("Hint", True, (255, 255, 255))
            screen.blit(hint_text, (hint_button_rect.x + 20, hint_button_rect.y + 5))
        # to display conversation message and button after all questions are completed
        if show_congratulations:
            #to display the congratulations message
            message_text="Congratulations! You just earned a key to unlock the next Room."
            message_surface=big_font.render(message_text, True, (0,128,0))
            message_rect=message_surface.get_rect(center=(screen.get_width() // 2, 300))
            screen.blit(message_surface, message_rect)
            #to draw the button to collect the new key
            button_rect = pygame.Rect(screen.get_width() // 2 - 100, 360, 200, 50)
            pygame.draw.rect(screen, (0, 128, 0), button_rect)
            button_text = font.render("Click to collect Key", True, (255, 255, 255))
            screen.blit(button_text, (button_rect.x + 15, button_rect.y + 15))
 
            mouse_x, mouse_y=0, 0
            if show_congratulations and  event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y=pygame.mouse.get_pos()
                if screen.get_width() // 2 - 100 <=mouse_x <=screen.get_width() // 2 + 100 and 360 <= mouse_y <=410:
                    show_collect_key_button=False
                    show_congratulations=False
                    if "Key" not in inventory:
                        inventory.append("Key")
                    key_collected=True
                    show_success_message=True
                    show_instruction_message=True
                    print("Key collected")

            # inventory box
        if inventory:
            inventory_rect=pygame.Rect(10,10,120,60)
            pygame.draw.rect(screen, (255,255,255), inventory_rect)
            pygame.draw.rect(screen, (0,0,0), inventory_rect, 2)
            inventory_text=font.render("Inventory:", True, (0,0,0))
            screen.blit(inventory_text, (inventory_rect.x +5, inventory_rect.y+5))
            for i, item in enumerate(inventory):
                item_text=font.render(item, True, (0,0,0))
                screen.blit(item_text,(inventory_rect.x + 10, inventory_rect.y + 25 + i * 20))
        
        #to show success and instruction messages
        if show_success_message:
            success_text="Key collected successfully and added to your inventory"
            success_surface=big_font.render(success_text, True, (0,0,0))
            success_rect=success_surface.get_rect(center=(screen.get_width() // 2, 280))
            screen.blit(success_surface, success_rect)
        if show_instruction_message:
            instruction_maths_text="Return to the lobby and use the key to unlock the door"
            instruction_surface=big_font.render(instruction_maths_text, True, (0,0,0))
            instruction_rect=instruction_surface.get_rect(center=(screen.get_width() // 2,330))
            screen.blit(instruction_surface, instruction_rect)

        #to draw the timer
        if not game_over:
            timer_text=font.render(f"Time Left: {time_left} seconds", True, (255,0,0))
            text_rect=timer_text.get_rect()
            text_rect.centerx=(screen.get_width() // 2)
            text_rect.top=20
            screen.blit(timer_text, text_rect)
        # to display game over message
        if game_over:
            game_over_text=font_large.render("Time's Up! Game Over", True, (255,0,0))
            game_over_rect=game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(game_over_text, game_over_rect)
            # to display the restart button
            restart_button_text=font_medium.render("Restart", True, (255,255,255))
            restart_button_rect=pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 50,200,60)
            pygame.draw.rect(screen, (0,100,0), restart_button_rect)
            screen.blit(restart_button_text, restart_button_text.get_rect(center=restart_button_rect.center))
        

       


           


        # to draw the player in both rooms
        pygame.draw.rect(screen, (0,0,0), player_rect)
           
            
            
       
       
        pygame.display.update()




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
            game_loop()
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




