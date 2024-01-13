from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(900,700)

zambtn = QPushButton("Створити замітку")
delitbtn = QPushButton("Видалити замітку")
savebtp = QPushButton("Зберегти замітку")
vikrbtn = QPushButton("Відкріпити від замітки")
dodatubtn = QPushButton("Додати до замітки")
searchbtn = QPushButton("Шукати замітки по тегу")

text = QTextEdit()
list1 = QListWidget()
list2 = QListWidget()
lll = QLabel("Список заміток")
kkk = QLabel("Список тегів")







mainline = QHBoxLayout()
k1line = QVBoxLayout()
k2line = QVBoxLayout()

window.show()
app.exec()