import args
import kwargs

'''
def LogCall(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print(f"[LOG] {func.__name__} called with args={args}, kwargs={kwargs} → returned {result}")
        return result
    return wrapper


def add(a,b):
    return a+b

print(add(1,2))

add1 = LogCall(add)
print(add1)

@LogCall
def subtract(a, b):
    return a - b

subtract(3, 3)
'''
'''

def cache(func):
    cache_storage = {}

    def wrapper(*args):
        if args in cache_storage:
            print(f"[CACHE] Returning cached result for {args}")
            return cache_storage[args]
        result = func(*args)
        cache_storage[args] = result
        return result

    return wrapper


@cache
def slow_square(n):
    print(f"Computing square of {n}...")
    return n * n


slow_square(25)
slow_square(25)'''



'''
class logger:
    _instance = None

    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self,message):
        print("[LOG] " + message)


class JSONProcessor:
    def process(self,data):
        return f"Processing JSON: {data}"

class XMLProcessor:
    def process(self, data):
        return f"Processing XML: {data}"

class ProcesorFactory:
    def __init__(self,type):
        if type == "json":
            return JSONProcessor()
        elif type == "xml":
            return XMLProcessor()
        else:
            raise NotImplementedError
'''



    #MediaPlayer类,type,filename
class MediaPlayer:
    def play(self,audio_type,file_name):
        pass


class VlcPlayer:
    def play_vlc(self,file_name):
        print("Playing vlc file: " + file_name)

class Mp4Player:
    def play_mp4(self,file_name):
        print("Playing mp4 file: " + file_name)
    #Vlc类，filename,打印 Playing vlc file：filename
    #MP4类，同上



class MediaAdapter(MediaPlayer):
    def __init__(self,audio_type):
        if audio_type == "vlc":
            self.player = VlcPlayer()
        elif audio_type == "mp4":
            self.player = Mp4Player()
        else:
            self.player = None

    def play(self,audio_type, file_name):
        if audio_type == "vlc":
            self.player.play_vlc(file_name)
        elif audio_type == "mp4":
            self.player.play_mp4(file_name)


    #MediaAdapter类，
    # __init__如果type==VLC，调用Vlc类，同MP4，否则None
    # play方法,调用play_vlc,play_Mp4

class AudioPlayer(MediaPlayer):
        def play(self, audio_type, file_name):
                if audio_type == "mp3":
                    print("Playing mp3 file: " + file_name)
                elif audio_type in ("vlc", "mp4"):
                    adapt = MediaAdapter(audio_type)
                    adapt.play(audio_type, file_name)
                else:
                    print("Invalid media type:", audio_type)


player = AudioPlayer()

player.play("mp3", "song.mp3")
player.play("mp4", "video.mp4")
player.play("vlc", "movie.vlc")
player.play("avi", "clip.avi")

    #AudioPlayer(统一播放器),audio_type,filename
    #如果是Mp3，直接打印Playing Mp3 file: filename
    #如果 audio_type == "Vls"or"Mp4",通过adapter来创建对象，再调用play方法
    #否则打印不存在的type







