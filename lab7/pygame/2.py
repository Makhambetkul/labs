import pygame
import os


pygame.init()


WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("La La Land OSTs")


music_directory = "lab7/pygame"  
music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]


current_track = 0


playing = False


def play_music():
    global playing
    if not playing:
        pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
        pygame.mixer.music.play()
        playing = True


def stop_music():
    global playing
    if playing:
        pygame.mixer.music.stop()
        playing = False


def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    if playing:
        pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
        pygame.mixer.music.play()


def previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    if playing:
        pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
        pygame.mixer.music.play()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()

pygame.quit()
