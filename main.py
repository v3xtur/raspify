import pygame
import os
from dotenv import load_dotenv
from io import BytesIO
import requests

from spotipy.oauth2 import SpotifyOAuth
import spotipy

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = "http://localhost:8080/"
scope = "user-read-playback-state,user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope,
                                               open_browser=True))

devices = sp.devices()
tv_id = None

pygame.init()
pygame.display.set_caption("Raspify - Made possible with Spotify")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font_title = pygame.font.Font("raspify/SansSerifBldFLF.otf", 50)
font_artist = pygame.font.Font("raspify/SansSerifBookFLF.otf", 32)
running = True

icon = pygame.image.load("raspify/icon.png")
icon = pygame.transform.scale(icon, (75, 75))

previous = pygame.image.load("raspify/previous.png")
pause = pygame.image.load("raspify/pause.png")
next = pygame.image.load("raspify/next.png")

while running:
    screen.fill((18, 18, 18))

    screen.blit(icon, (1195, 635))

    previous_button = previous.get_rect(topleft=(10, 610))
    pause_button = pause.get_rect(topleft=(120, 610))
    next_button = next.get_rect(topleft=(230, 610))

    screen.blit(previous, previous_button)
    screen.blit(pause, pause_button)
    screen.blit(next, next_button)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if previous_button.collidepoint(x, y):
                sp.previous_track(device_id=tv_id)
            
            if pause_button.collidepoint(x, y):
                if sp.current_user_playing_track()["is_playing"]:
                    sp.pause_playback(device_id=tv_id)
                else:
                    sp.start_playback(device_id=tv_id)

            if next_button.collidepoint(x, y):
                sp.next_track(device_id=tv_id)

    if sp.current_user_playing_track() != None:
        track_name = sp.current_user_playing_track()["item"]["name"]
        artist_name = sp.current_user_playing_track()["item"]["artists"][0]["name"]

        pygame.display.set_caption(f"{artist_name} - {track_name}")

        image = pygame.image.load(BytesIO(requests.get(sp.current_user_playing_track()["item"]["album"]["images"][1]["url"]).content)).convert()
        name = font_title.render(track_name, True, (224, 224, 224), (18, 18, 18))
        name_rect = name.get_rect()
        name_rect.topleft = (10, 320)
        artist = font_artist.render(artist_name, True, (126, 137, 135), (18, 18, 18))
        artist_rect = artist.get_rect()
        artist_rect.topleft = (10, 375)

        screen.blit(image, (10, 10))
        screen.blit(name, name_rect)
        screen.blit(artist, artist_rect)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
