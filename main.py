import pygame
import random
import threading

# Import the game modules
from game_objects.character import CircleCharacter
from game_objects.nlp_module import LLMHandler

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move the Circle")

# Declare parameters
# Colors
BACKGROUND_COLOR = (135, 206, 235)  # Sky blue
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR = (0, 255, 0)

# Some screen object
font = pygame.font.SysFont(None, 48) # Font of the text
title_text = font.render("Welcome to the Game!", True, TEXT_COLOR)
button_text = font.render("Start Game", True, TEXT_COLOR)
padding_size = 30
button_rect = pygame.Rect((width // 2 - button_text.get_width()//2 - padding_size//2, height // 2 - button_text.get_height()//2- padding_size//2),
                          (button_text.get_width()+padding_size, button_text.get_height()+padding_size))

def draw_start_screen():
    # Fill the background
    screen.fill(BACKGROUND_COLOR)
    # Add title
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - 100))
    # Draw the start button
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)  
    # Add text on the button
    screen.blit(button_text, (button_rect.x + button_rect.width // 2 - button_text.get_width() // 2,
                               button_rect.y + button_rect.height // 2 - button_text.get_height() // 2))   

def implement_llm_instruction(llm_handler, character):    
    # Control the character following LLM result
    if llm_handler.llm_instruction:
        if llm_handler.llm_instruction.stop:
            pass
        elif llm_handler.llm_instruction.move_left:
            character.move_left()
        elif llm_handler.llm_instruction.move_right:
            character.move_right()
        elif llm_handler.llm_instruction.move_up:
            character.move_up()
        elif llm_handler.llm_instruction.move_down:
            character.move_down()
        if llm_handler.llm_instruction.change_color:
            character.change_color((llm_handler.llm_instruction.red_in_rgb,
                                    llm_handler.llm_instruction.green_in_rgb,
                                    llm_handler.llm_instruction.blue_in_rgb))

# Main loop
running = True
in_start_screen = True

# Init the character
character = CircleCharacter(screen=screen, x=width // 2, y=height // 2, radius=30, color=(255, 0, 0))
# Init the AI
llm_handler = LLMHandler()
recording_thread = None
       
while running:
    for event in pygame.event.get():
        # End if user exit
        if event.type == pygame.QUIT:
            running = False
        # Start the game if user click on start screen
        if event.type == pygame.MOUSEBUTTONDOWN and in_start_screen:
            if button_rect.collidepoint(event.pos):  # Check if the button is clicked
                in_start_screen = False  # Transition to the main game loop
                
        # Start recording when space is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not llm_handler.recording:
                recording_thread = threading.Thread(target=llm_handler.start_recording)
                recording_thread.start()

        # Stop recording when space is release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and llm_handler.recording:
                llm_handler.stop_recording()
                recording_thread.join()  # Wait for the recording thread to finish

    if in_start_screen:
        draw_start_screen()
    else:
        # Get the keys pressed and move the character
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  # Change color on space press
            character.move_left()
        if keys[pygame.K_RIGHT]:  # Change color on space press
            character.move_right()
        if keys[pygame.K_UP]:  # Change color on space press
            character.move_up()
        if keys[pygame.K_DOWN]:  # Change color on space press
            character.move_down()
        # if keys[pygame.K_SPACE]:  # Change color on space press
        #     character.change_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            
        # Control the character through llm result
        implement_llm_instruction(llm_handler=llm_handler, character=character)

        # Fill the background
        screen.fill(BACKGROUND_COLOR)
        # Draw the circle
        character.render()

    # Update the display
    pygame.display.flip()
    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()