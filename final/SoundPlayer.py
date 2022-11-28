import threading
from playsound import playsound


class SoundPlayer:

    def play(self, sound_path):
        threading.Thread(target=playsound, args=(sound_path,), daemon=True).start()
        return self
