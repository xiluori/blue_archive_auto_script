from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from qfluentwidgets import FlowLayout, CheckBox, LineEdit


class Layout(QWidget):
    def __init__(self, parent=None, config=None):
        super().__init__(parent=parent)
        self.config = config
        self.__check_server()
        self.goods = self.config.get(key='TacticalChallengeShopList')
        goods_count = len(self.goods)
        layout = FlowLayout(self, needAni=True)
        layout.setContentsMargins(30, 0, 0, 30)
        layout.setVerticalSpacing(0)
        # layout.setHorizontalSpacing(0)

        self.setFixedHeight(250)
        self.setStyleSheet('Demo{background: white} QPushButton{padding: 5px 10px; font:15px "Microsoft YaHei"}')
        self.label = QLabel('刷新次数', self)
        self.input = LineEdit(self)
        self.input.setValidator(QIntValidator(0, 3))
        self.input.setText(self.config.get('TacticalChallengeShopRefreshTime'))

        self.accept = QPushButton('确定', self)
        self.boxes = []
        for i in range(0, goods_count):
            t_cbx = CheckBox(self)
            t_cbx.setChecked(self.goods[i] == 1)
            ccs = QLabel(f"商品{i + 1}", self)
            ccs.setFixedWidth(60)
            wrapper_widget = QWidget()
            wrapper = QHBoxLayout()
            wrapper.addWidget(ccs)
            wrapper.addWidget(t_cbx)
            wrapper_widget.setLayout(wrapper)
            layout.addWidget(wrapper_widget)
            t_cbx.stateChanged.connect(lambda x, index=i: self.alter_status(index, goods_count))
            self.boxes.append(t_cbx)
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.accept)
        self.accept.clicked.connect(self.__accept)

    def alter_status(self, index, goods_count):
        self.boxes[index].setChecked(self.boxes[index].isChecked())
        self.config.set(key='TacticalChallengeShopList',
                        value=[1 if self.boxes[i].isChecked() else 0 for i in range(0, goods_count)])

    def __accept(self):
        self.config.set('TacticalChallengeShopRefreshTime', self.input.text())

    def __check_server(self):
        if self.config.server_mode in ['Global', 'JP'] and len(self.config.get('TacticalChallengeShopList')) != 15:
            self.config.set('TacticalChallengeShopList', [0] * 15)
        elif self.config.server_mode == 'CN' and len(self.config.get('TacticalChallengeShopList')) != 14:
            self.config.set('TacticalChallengeShopList', [0] * 14)
