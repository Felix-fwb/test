#coding = 'utf-8'


from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class Example(QWidget):
    """
        none
    """
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        """
            none
        """
        self.setGeometry(800, 800, 900, 800)
        self.setWindowTitle('一起来学习')

        bt1 = QPushButton('a', self)
        # bt1.move(50, 250)

        bt2 = QPushButton('b', self)
        # bt2.move(150, 250)

        bt3 = QPushButton('c', self)
        # bt3.move(250, 250)
        h_box = QHBoxLayout()
        h_box.addStretch(20)

        h_box.addWidget(bt1)
        h_box.addStretch(1)
        h_box.addWidget(bt2)
        h_box.addStretch(1)
        h_box.addWidget(bt3)
        h_box.addStretch(1)

        v_box = QVBoxLayout()
        v_box.addStretch(1)
        v_box.addLayout(h_box)
        v_box.addStretch(1)

        self.setLayout(v_box)



