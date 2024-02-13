import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QScrollBar
from qfluentwidgets import LineEdit, InfoBar, InfoBarIcon, InfoBarPosition, TabBar


class Layout(QWidget):
    def __init__(self, parent=None, config=None):
        super().__init__(parent=parent)
        self.config = config
        self.hBoxLayout = QVBoxLayout(self)

        self.lay1 = QHBoxLayout(self)
        self.lay2 = QHBoxLayout(self)
        self.lay3 = QHBoxLayout(self)

        self.label = QLabel('用">"分割物品，排在前面的会优先选择', self)
        self.input1 = LineEdit(self)
        self.input2 = LineEdit(self)
        self.accept = QPushButton('确定', self)

        priority = self.config.get('createPriority')  # type: str
        time = self.config.get('createTime')

        # self.setFixedHeight(120)
        self.input1.setText(priority)
        self.input1.setFixedWidth(600)
        self.input2.setText(time)

        self.tabBar = TabBar(self)
        self.tabBar.setMovable(True)
        self.tabBar.setTabsClosable(False)
        self.tabBar.setScrollable(True)
        self.tabBar.setTabMaximumWidth(50)
        self.tabBar.setAddButtonVisible(False)
        self.tabBar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tabBar.setFixedHeight(60)

        self.tabBar.setFixedWidth(750)
        for item in priority.split('>'):
            self.tabBar.addTab(f'{random.Random().randint(0, 1000)}_{item}', item)

        self.lay1.setContentsMargins(10, 0, 0, 10)
        self.lay2.setContentsMargins(10, 0, 0, 10)
        self.lay3.setContentsMargins(10, 0, 0, 10)

        self.accept.clicked.connect(self.__accept_main)

        self.lay1.addWidget(self.label, 0, Qt.AlignLeft)
        self.lay2.addWidget(self.input1, 1, Qt.AlignLeft)
        self.lay2.addWidget(self.input2, 1, Qt.AlignLeft)
        self.lay2.addWidget(self.accept, 0, Qt.AlignLeft)

        self.lay3.addWidget(self.tabBar, 1, Qt.AlignLeft)

        self.lay1.addStretch(1)
        self.lay1.setAlignment(Qt.AlignCenter)
        self.lay2.setAlignment(Qt.AlignCenter)

        self.hBoxLayout.addSpacing(16)
        self.hBoxLayout.setAlignment(Qt.AlignCenter)

        self.hBoxLayout.addLayout(self.lay1)
        self.hBoxLayout.addLayout(self.lay2)
        self.hBoxLayout.addLayout(self.lay3)

    def __accept_main(self):
        # input1_content = self.input1.text()
        # input2_content = self.input2.text()
        #
        # self.config.set('createPriority', input1_content)
        # self.config.set('createTime', input2_content)
        #
        # w = InfoBar(
        #     icon=InfoBarIcon.SUCCESS,
        #     title='设置成功',
        #     content=f'制造次数：{input2_content}',
        #     orient=Qt.Vertical,
        #     position=InfoBarPosition.TOP_RIGHT,
        #     duration=800,
        #     parent=self.parent().parent().parent().parent()
        # )
        # w.show()
        print('test')
        print('>'.join(list(map(lambda x: x.text(), self.tabBar.items))))
