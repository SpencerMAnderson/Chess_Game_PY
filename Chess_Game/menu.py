import pygame, sys
from inputs import songs

pygame.init()
pygame.mixer.init()

# Initialize menu screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")

# Colors
light_blue = (228, 233, 235) # Light 
dark_blue = (153 , 191, 209) # Dark
darkest_blue = (124, 158, 175)
text_color = (255, 255, 255) # Color of text
black = (0, 0, 0, 0)

# Music Button properties
button_color = dark_blue
font = pygame.font.Font(None, 35) # Font

button_rect1 = pygame.Rect(220, 100, 200, 50)
button_rect2 = pygame.Rect(220, 180, 200, 50)
button_rect3 = pygame.Rect(220, 260, 200, 50)
button_rect4 = pygame.Rect(220, 340, 200, 50) # Mute button

text1 = font.render('Song 1', True, text_color)
text2 = font.render('Song 2', True, text_color)
text3 = font.render('Song 3', True, text_color)
text4 = font.render('Mute', True, text_color) # Mute Button

buttons =  [button_rect1, button_rect2, button_rect3, button_rect4]
texts = [text1, text2, text3, text4]

# Music Button properties
vol_color = light_blue

vol_rect1 = pygame.Rect(600, 100, 35, 35)
vol_rect2 = pygame.Rect(600, 180, 35, 35)

vol_up_text = font.render('+', True, black)
vol_down_text = font.render('-', True, black)

vol_buttons = [vol_rect1, vol_rect2]
vol_texts= [vol_up_text, vol_down_text]

def draw_menu():
    screen.fill(darkest_blue)

    # Song buttons
    for button_rect, text in zip(buttons, texts):
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(text, (button_rect.x + 20, button_rect.y + 10))

    # Volume buttons
    for vol_rect, vol_text in zip(vol_buttons, vol_texts):
        pygame.draw.rect(screen, vol_color, vol_rect)
        screen.blit(vol_text, (vol_rect.x + 10, vol_rect.y + 5))
    
    pygame.display.flip()

channels = [pygame.mixer.Channel(i) for i in range(len(songs))]
vol = 1

# Function to play the song
def play_song(current_song, new_song):
    if channels[current_song].get_busy():  # Check if the channel is currently playing something
        channels[current_song].stop()      # Stop current sound if any
    channels[new_song].play(songs[new_song], loops=-1)  # Play the new song
    set_volume(vol, new_song)

# Function to set the volume of the current song
def set_volume(vol, song_index):
    channels[song_index].set_volume(vol)

# Main loop
def main_menu():
    global vol
    current_song = 0
    play_music = True
    song_buttons = [button_rect1, button_rect2, button_rect3]

    play_song(0, 0)
    draw_menu()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Song buttons
                for index, button in enumerate(song_buttons):
                    if button.collidepoint(event.pos):
                        play_song(current_song, index)
                        current_song = index
                        play_music = True
                        print(f"Song {current_song + 1} clicked!")
                        break 
                # Mute button
                if button_rect4.collidepoint(event.pos):
                    set_volume(vol, current_song) if not play_music else set_volume(0, current_song)
                    print("Muted") if play_music else print("Unmuted")
                    play_music = not play_music
                # Volume buttons
                for vol_button, inc in [(vol_rect1, 0.1), (vol_rect2, -0.1)]:
                    if vol_button.collidepoint(event.pos):
                        vol = max(0, min(1, round(vol + inc, 2)))  # Clamp vol between 0 and 1
                        set_volume(vol, current_song)
                        print("Volume:", vol)

main_menu()
