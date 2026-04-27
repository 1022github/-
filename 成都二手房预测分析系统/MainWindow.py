# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 390)                 # 窗口出现时的大小703
        MainWindow.setMinimumSize(QtCore.QSize(695, 390))               # 最小大小
        MainWindow.setMaximumSize(QtCore.QSize(710, 695))               # 最大大小710
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)            # 上下文菜单策略
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)        # 工具按钮类型

        self.centralwidget = QtWidgets.QWidget(MainWindow)          # 主窗口 中心窗口部件
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)           # QLabel标签 居中
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 321))        # 设置窗口的几何形状，QRect(0, 0, 711, 321)左边界,上边界,宽度,高度

        self.label.setText("")                                  # 改变标签的内容

        self.label.setPixmap(QtGui.QPixmap("../img/背景图.png"))
        self.label.setScaledContents(True)                      # 将图片自动缩放以适应label大小，同时不影响窗口大小
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)           # QToolBar控件是由文本按钮，图标或其他小控件按钮组成的可移动面板，通常位于菜单栏下方
        self.toolBar.setAcceptDrops(True)                       # 控件的拖拽-setAcceptDrops()
        self.toolBar.setIconSize(QtCore.QSize(48, 48))           # setIconSize改变单元格中图片的尺寸
        self.toolBar.setObjectName("toolBar")

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)       # 将 self.toolBar 这个工具栏对象添加到 MainWindow 主窗口中
        self.btn_1 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/图标-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_1.setIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")

        self.btn_2 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/图标-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_2.setIcon(icon1)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")

        self.btn_3 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../img/图标-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_3.setIcon(icon2)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")

        self.btn_4 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../img/图标-4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_4.setIcon(icon3)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")

        self.btn_5 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../img/图标-5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_5.setIcon(icon4)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")

        # # 新增功能
        # self.btn_6 = QtWidgets.QAction(MainWindow)
        # icon4 = QtGui.QIcon()
        # icon4.addPixmap(QtGui.QPixmap("../img/图标-6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.btn_6.setIcon(icon4)
        # font = QtGui.QFont()
        # font.setPointSize(1)
        # self.btn_6.setFont(font)
        # self.btn_6.setObjectName("btn_6")

        # # 新增功能
        # self.btn_7 = QtWidgets.QAction(MainWindow)
        # icon4 = QtGui.QIcon()
        # icon4.addPixmap(QtGui.QPixmap("../img/图标-7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.btn_7.setIcon(icon4)
        # font = QtGui.QFont()
        # font.setPointSize(1)
        # self.btn_7.setFont(font)
        # self.btn_7.setObjectName("btn_7")


        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_4)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_5)
        self.toolBar.addSeparator()

        # # 新增功能
        # self.toolBar.addSeparator()
        # self.toolBar.addAction(self.btn_6)
        # self.toolBar.addSeparator()

        # # 新增功能
        # self.toolBar.addSeparator()
        # self.toolBar.addAction(self.btn_7)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.btn_1.setText(_translate("MainWindow", "各区二手房均价分析"))
        self.btn_1.setToolTip(_translate("MainWindow", "各区二手房均价分析"))
        self.btn_2.setText(_translate("MainWindow", "各区二手房数量所占比例"))
        self.btn_2.setToolTip(_translate("MainWindow", "各区二手房数量所占比例"))
        self.btn_3.setText(_translate("MainWindow", "全市二手房装修程度分析"))
        self.btn_3.setToolTip(_translate("MainWindow", "全市二手房装修程度分析"))
        self.btn_4.setText(_translate("MainWindow", "热门户型均价分析"))
        self.btn_4.setToolTip(_translate("MainWindow", "热门户型均价分析"))
        self.btn_5.setText(_translate("MainWindow", "二手房售价预测"))
        self.btn_5.setToolTip(_translate("MainWindow", "二手房售价预测"))


        # # 新增功能
        # self.btn_6.setText(_translate("MainWindow", "全市楼房结构分析"))
        # self.btn_6.setToolTip(_translate("MainWindow", "全市楼房结构分析"))

        # # 新增功能
        # self.btn_7.setText(_translate("MainWindow", "全市房源发布时间分析"))
        # self.btn_7.setToolTip(_translate("MainWindow", "全市房源发布时间分析"))