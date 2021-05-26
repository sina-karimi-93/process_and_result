
from .widgets import PURPLE, YELLOW, ORANGE
from .widgets import QVBoxLayout, QHBoxLayout
from .widgets import QFrame
from .widgets import QLabel, Label, Button, Entry, Combobox
from .widgets import pyqtSlot, QImage, QPixmap
# from ... import Thread


# ===================================== LEFT FRAME ====================================


class TopFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style
        self.setStyleSheet(f"""
            border:none;
        """)
        # Set Main Layout
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        # File Address (Entry)
        self.file_address = Entry(placeholder='Address Bar')
        self.file_address.setMinimumWidth(700)
        self.main_layout.addWidget(self.file_address)
        # Browse (Button)
        self.browse_button = Button(
            label='Browse', callback_func=self.browse_file)
        self.main_layout.addWidget(self.browse_button)

    def browse_file(self) -> None:
        pass


class MiddleFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style
        self.setStyleSheet(f"""
            border:none;
        """)
        # Video Label
        self.video_label = QLabel()
        self.main_layout.addWidget(self.video_label)
        self.main_layout.addStretch()

        # self.th = Thread(self)
        # self.th.changePixmap.connect(self.setImage)
        # self.th.start()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.video_label.setPixmap(QPixmap.fromImage(image))


class BottomFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style
        self.setStyleSheet(f"""
            border:none;
        """)
        # Set Main Layout
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        # Start Button
        self.start_button = Button(
            label='Start', callback_func=self.start_video)
        self.start_button.setMinimumWidth(750)
        self.main_layout.addWidget(self.start_button)
        # 2X Speed
        self.speed_2x = Button(
            label='2x', callback_func=lambda: self.speed(speed=2))
        self.main_layout.addWidget(self.speed_2x)
        # 4X Speed
        self.speed_4x = Button(
            label='4x', callback_func=lambda: self.speed(speed=4))
        self.main_layout.addWidget(self.speed_4x)
        # 6X Speed
        self.speed_6x = Button(
            label='6x', callback_func=lambda: self.speed(speed=6))
        self.main_layout.addWidget(self.speed_6x)

    def start_video(self) -> None:
        pass

    def speed(self, speed: int):
        pass


class LeftFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style
        self.setStyleSheet(f"""
            border:2px solid {YELLOW};
            border-radius:10;
            margin:10px 5px;
        """)
        self.setMinimumWidth(980)
        # Set Main Layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        # Top Frame
        self.top_frame = TopFrame()
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addStretch()
        # Bottom Frame
        self.bottom_frame = BottomFrame()
        self.main_layout.addWidget(self.bottom_frame)

# ===================================== RIGHT FRAME ====================================


class TimeFrame(QFrame):
    def __init__(self, label: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style
        self.setStyleSheet(f"""
            padding:0;
            margin:0;
        """)
        # Set Main Layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        # Label
        self.shift_change_label = Label(label=label)
        self.main_layout.addWidget(self.shift_change_label)
        # Horizontal Layout
        self.hr_layout = QHBoxLayout()
        self.main_layout.addLayout(self.hr_layout)
        # Hour
        self.hour = Entry(placeholder='Hour')
        self.hr_layout.addWidget(self.hour)
        # Splitter
        self.splitter = Label(label=':')
        self.hr_layout.addWidget(self.splitter)
        # Minute
        self.minute = Entry(placeholder='Minute')
        self.hr_layout.addWidget(self.minute)


class RightFrameContent(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style
        self.setStyleSheet(f"""
            border:none;   
        """)
        # Set Main Layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Change Shift
        self.shift_change_entries = TimeFrame(label="Change Shift Time")
        self.main_layout.addWidget(self.shift_change_entries)
        # Number of Parts
        self.nubmer_of_parts_label = Label('Number of Parts')
        self.main_layout.addWidget(self.nubmer_of_parts_label)
        self.nubmer_of_parts_entry = Entry(placeholder='Number of Parts')
        self.main_layout.addWidget(self.nubmer_of_parts_entry)
        # Begin Work
        self.begin_work = TimeFrame(label='Begin Work Time')
        self.main_layout.addWidget(self.begin_work)
        # End Work
        self.end_work = TimeFrame(label='End Work Time')
        self.main_layout.addWidget(self.end_work)
        # Free Time
        self.free_time = TimeFrame(label="Free Time")
        self.main_layout.addWidget(self.free_time)
        # STRETCHHHHHHH
        self.main_layout.addStretch()


class RightFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style
        self.setStyleSheet(f"""
            border: 2px solid {YELLOW};
            border-radius:10;
            margin:10px 5px;
        """)
        # Set Main Layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        # Content
        self.content = RightFrameContent()
        self.main_layout.addWidget(self.content)

# ===================================== MAIN FRAME ====================================


class MainFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(f"""
            background-color: {PURPLE};
        """)
        # SET MAIN FRAME
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        # LEFT FRAME
        self.left_frame = LeftFrame()
        self.main_layout.addWidget(self.left_frame)
        self.main_layout.addStretch()
        # RIGHT FRAME
        self.right_frame = RightFrame()
        self.main_layout.addWidget(self.right_frame)
