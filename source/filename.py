class AudioFile():

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Formato inválido")

        self.filename = filename
    

class Mp3File(AudioFile):
    
    ext = "mp3"
    def play(self):
            print("tocando arquivo mp3")


class WavFile(AudioFile):

    ext = "wav"
    def play(self):
            print("tocando arquivo wav")


class OggFile(AudioFile):

    ext = "ogg"
    def play(self):
            print("tocando arquivo ogg")

mp3 = Mp3File('musica.mp3')
mp3.play()
ogg = OggFile('musica.ogg')
ogg.play()

mp3_falso = Mp3File('musica.ogg')
mp3_falso.play()
