import os

from Qt import QtCore, QtGui, QtWidgets
from PyQt5 import QtMultimediaWidgets, QtMultimedia

from gazupublisher.utils.connection import get_data_from_url, get_host
from gazupublisher.views.task_panel.PreviewWidget import PreviewWidget


class FrameCounterWidget(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(FrameCounterWidget, self).__init__(parent)
        self.frame_cnt = 0
        self.setText("0")

    def process_frame(self, frame):
        self.frame_cnt = self.frame_cnt + 1
        self.setText(str(self.frame_cnt))

    def set_frame(self, frame):
        self.frame_cnt = frame
        self.setText(self.frame_cnt)


class PreviewVideoWidget(PreviewWidget):
    def __init__(self, parent, preview_file):
        PreviewWidget.__init__(self, parent, preview_file)

    def complete_ui(self):
        """
        Complete the interface with the widgets needed for a video.
        """
        self.frame_counter = FrameCounterWidget()
        self.timer_label = QtWidgets.QLabel()

        self.toolbar_widget.layout().insertWidget(0, self.frame_counter)
        self.toolbar_widget.layout().insertWidget(0, self.timer_label)

        self.duration = None
        self.fps = None

        self.play_button = QtWidgets.QPushButton()
        self.play_button.setEnabled(False)
        self.play_button.setIcon(
            self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay)
        )
        self.play_button.clicked.connect(self.play)
        self.toolbar_widget.layout().insertWidget(0, self.play_button)

        self.position_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.setSingleStep(10)
        self.position_slider.sliderMoved.connect(self.set_position)
        self.preview_vertical_layout.insertWidget(0, self.position_slider)

        self.error_label = QtWidgets.QLabel()
        self.error_label.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        self.preview_vertical_layout.insertWidget(0, self.error_label)
        self.error_label.hide()

        self.setup_video_player()

        self.probe = QtMultimedia.QVideoProbe(self)
        self.probe.videoFrameProbed.connect(self.frame_counter.process_frame)
        self.probe.setSource(self.media_player)

    def setup_video_player(self):
        self.url = os.path.join(
            get_host(),
            "movies",
            "originals",
            "preview-files",
            self.preview_file["id"] + "." + self.preview_file["extension"],
        )

        self.media_player = QtMultimedia.QMediaPlayer(
            None, QtMultimedia.QMediaPlayer.VideoSurface
        )

        video_widget = QtMultimediaWidgets.QVideoWidget()
        self.preview_vertical_layout.insertWidget(0, video_widget)

        self.media_player.setVideoOutput(video_widget)
        self.media_player.stateChanged.connect(self.media_state_changed)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.media_player.mediaStatusChanged.connect(self.status_changed)
        self.media_player.error.connect(self.handle_error)

        self.buffer = QtCore.QBuffer()
        self.open_file(self.url)

    def open_file(self, url):
        """
        Open the video file from the url, and link it to the media player
        widget.
        """
        with get_data_from_url(url) as data:
            self.data = data.read()
            self.buffer.setData(self.data)
            self.buffer.open(QtCore.QIODevice.ReadOnly)
            self.media_player.setMedia(
                QtMultimedia.QMediaContent(), self.buffer
            )

        self.play_button.setEnabled(True)

    def play(self):
        """
        Play/pause the player
        """
        if self.media_player.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def media_state_changed(self, state):
        if self.media_player.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.play_button.setIcon(
                self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause)
            )
        else:
            self.play_button.setIcon(
                self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay)
            )

    def position_changed(self, position):
        position /= 1000

        if not self.position_slider.isSliderDown():
            self.position_slider.setValue(position)

        self.update_duration_info(position)

    def update_duration_info(self, current_info):
        if current_info or self.duration:
            currentTime = QtCore.QTime(
                (current_info / 3600) % 60,
                (current_info / 60) % 60,
                current_info % 60,
                (current_info * 1000) % 1000,
            )
            totalTime = QtCore.QTime(
                (self.duration / 3600) % 60,
                (self.duration / 60) % 60,
                self.duration % 60,
                (self.duration * 1000) % 1000,
            )

            format = "hh:mm:ss" if self.duration > 3600 else "mm:ss"
            tStr = (
                currentTime.toString(format)
                + " / "
                + totalTime.toString(format)
            )
        else:
            tStr = ""

        self.timer_label.setText(tStr)

    def duration_changed(self, duration):
        self.duration = duration / 1000
        self.position_slider.setRange(0, self.duration)

    def status_changed(self, status):
        if status == QtMultimedia.QMediaPlayer.EndOfMedia:
            self.set_position(0)
            self.play()

    def set_position(self, position):
        self.media_player.setPosition(position * 1000)

    def handle_error(self):
        self.play_button.setEnabled(False)
        self.error_label.setText("Error: " + self.media_player.errorString())
        self.error_label.show()

    def clear_setup_media_widget(self):
        for i in reversed(range(self.preview_vertical_layout.count())):
            widget = self.preview_vertical_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
