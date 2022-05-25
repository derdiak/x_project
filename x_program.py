from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from random import randint
 
app = QApplication([])
 
# главное окно:
window = QWidget()
window.setWindowTitle('Тест')
window.move(0, 100)
window.resize(1000, 500)

main_layout = QHBoxLayout()

left_layout   = QVBoxLayout()
center_layout = QVBoxLayout()
right_layout = QVBoxLayout()

left_button = QPushButton('Левая кнопка')       # кнопки не умеют растягиваться в высоту,
left_label = QLabel('Левый текст')              # поэтому label захватил всё свободное пространство
left_layout.addWidget(left_button)
left_layout.addWidget(left_label)

center_label = QLabel('Центр текст')            # поскольку конкурентов у center_label нет,
center_layout.addWidget(center_label)           # то он захватил всё пространство своего родителя - лэйаута center_layout

right_button = QPushButton('Правая кнопка')

right_layout.addWidget(right_button)           # то он захватил всё пространство своего родителя - лэйаута center_layout

# # в главный горизонтальный лэйаут вставляем 3 вертикальных
main_layout.addLayout(left_layout)
main_layout.addLayout(center_layout)
main_layout.addLayout(right_layout)

window.setLayout(main_layout)


window.show()
app.exec_()