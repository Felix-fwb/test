#coding = 'utf-8'

from UI import Example
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    # 增加了备注，在该文件

    app.exit(app.exec_())