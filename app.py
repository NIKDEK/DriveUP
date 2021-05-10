import eel
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

def start ():
    eel.init('www')
    eel.start('index.html', mode='msedge')


if __name__ == "__main__":
    start()