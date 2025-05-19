import pygame
import random
import os


class SoundManager:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        pygame.mixer.set_num_channels(8)  # Більше каналів для ефектів
        self.music_volume = 0.5
        self.sfx_volume = 0.7
        self.base_path = os.path.join(os.path.dirname(__file__), '..', 'sound')
        self.game_tracks = [
            os.path.join(self.base_path, "game_tracks", "track1.mp3"),
            os.path.join(self.base_path, "game_tracks", "track2.mp3"),
            os.path.join(self.base_path, "game_tracks", "track3.mp3"),
        ]
        self.menu_track = os.path.join(self.base_path, "menu_track.mp3")
        self.game_over_track = os.path.join(self.base_path, "game_over.mp3")
        self.drop_sound = pygame.mixer.Sound(os.path.join(self.base_path, "drop.wav"))
        self.clear_sound = pygame.mixer.Sound(os.path.join(self.base_path, "clear.wav"))

        self.drop_sound.set_volume(self.sfx_volume)
        self.clear_sound.set_volume(self.sfx_volume)
        pygame.mixer.music.set_volume(self.music_volume)
        self.current_track = None

    def play_menu_music(self):
        """Відтворює музику головного меню в циклі."""
        pygame.mixer.music.load(self.menu_track)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        """Зупиняє поточну музику."""
        pygame.mixer.music.stop()

    def play_game_music(self):
        """Відтворює випадковий трек із плейлисту гри."""
        self.current_track = random.choice(self.game_tracks)
        pygame.mixer.music.load(self.current_track)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 2)

    def play_next_track(self, event):
        """Обробляє завершення треку та відтворює наступний."""
        if event.type == pygame.USEREVENT + 2:
            self.play_game_music()

    def play_drop_sound(self):
        """Відтворює звук падіння фігури."""
        channel = pygame.mixer.Channel(0)  # Виділений канал для ефектів
        channel.play(self.drop_sound)

    def play_clear_sound(self):
        """Відтворює звук видалення рядка."""
        channel = pygame.mixer.Channel(1)  # Окремий канал для clear
        if not channel.get_busy():  # Відтворювати, якщо канал вільний
            channel.play(self.clear_sound)

    def play_game_over_music(self):
        """Відтворює музику для екрану Game Over."""
        pygame.mixer.music.load(self.game_over_track)
        pygame.mixer.music.play(-1)

    def pause_music(self):
        """Призупиняє поточну музику."""
        pygame.mixer.music.pause()

    def unpause_music(self):
        """Відновлює відтворення музики."""
        pygame.mixer.music.unpause()