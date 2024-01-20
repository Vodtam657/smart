from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(900,700)

zambtn = QPushButton("Створити замітку")
delete = QPushButton("Видалити замітку")
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
mainline.addLayout(k1line)
mainline.addLayout(k2line)

k1line.addWidget(text)
k2line.addWidget(dodatubtn)
k2line.addWidget(list1)
k2line.addWidget(list2)
k2line.addWidget(zambtn)
k2line.addWidget(delete)
k2line.addWidget(savebtp)

mainline.addWidget(lll)




window.setLayout(mainline)
window.show()
app.exec()