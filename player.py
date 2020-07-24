from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer
from PyQt5.QtCore import Qt, QUrl


class CPlayer:

    def __init__(self, parent):
        # 윈도우 객체
        self.parent = parent

        self.player = QMediaPlayer()
        self.player.currentMediaChanged.connect(self.mediaChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.positionChanged.connect(self.positionChanged)

        self.playlist = QMediaPlaylist()

    def play(self, playlists, startRow=0, option=QMediaPlaylist.CurrentItemOnce):
        if self.player.state() == QMediaPlayer.PausedState: #멈춰있으면 재생
            self.player.play()
        else:  #재생중이면 새로 재생
            self.createPlaylist(playlists, startRow, option)
            self.player.setPlaylist(self.playlist)
            self.playlist.setCurrentIndex(startRow)
            self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def prev(self):
        self.playlist.previous()

    def next(self):
        self.playlist.next()

    def createPlaylist(self, playlists, startRow, option=QMediaPlaylist.CurrentItemOnce):
        self.playlist.clear()

        for path in playlists:
            url = QUrl.fromLocalFile(path)
            self.playlist.addMedia(QMediaContent(url))

        self.playlist.setPlaybackMode(option)

    def updatePlayMode(self, option):
        self.playlist.setPlaybackMode(option)

    def upateVolume(self, vol):
        self.player.setVolume(vol)

    def mediaChanged(self, e):
        self.parent.updateMediaChanged(self.playlist.currentIndex())

    def durationChanged(self, msec):
        if msec > 0:
            self.parent.updateDurationChanged(self.playlist.currentIndex(), msec)

    def positionChanged(self, msec): #processbar
        print('currentIndex1 = ',self.playlist.currentIndex(),'msec = ',msec)
        if msec > 0:
            print('currentIndex2 = ', self.playlist.currentIndex(),'msec = ',msec)
            self.parent.updatePositionChanged(self.playlist.currentIndex(), msec)