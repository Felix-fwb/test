#coding = 'utf-8'

from UI import Example
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exit(app.exec_())