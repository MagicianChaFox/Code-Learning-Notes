# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtWidgets
import sys

import def_csv
import def_wave


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Automatic reading of dynamic test results")
        #MainWindow.resize(645, 790)
        MainWindow.resize(645, 580)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # 这部分为文字标签的初始化
        self.label_001_HIGH_Side = QLabel(self.centralwidget)
        self.label_001_HIGH_Side.setObjectName(u"label_001_HIGH_Side")
        self.label_001_HIGH_Side.setGeometry(QRect(20, 20, 91, 21))
        font = QFont()  # 设置不同字体大小
        font.setPointSize(13)
        font1 = QFont()
        font1.setPointSize(10)
        self.label_001_HIGH_Side.setFont(font)
        self.label_004_LOW_Side = QLabel(self.centralwidget)
        self.label_004_LOW_Side.setObjectName(u"label_004_LOW_Side")
        self.label_004_LOW_Side.setGeometry(QRect(330, 20, 91, 21))
        self.label_004_LOW_Side.setFont(font)
        self.label_002_Channel_HIGH = QLabel(self.centralwidget)
        self.label_002_Channel_HIGH.setObjectName(u"label_002_Channel_HIGH")
        self.label_002_Channel_HIGH.setGeometry(QRect(134, 20, 70, 21))
        self.label_002_Channel_HIGH.setFont(font)
        self.label_003_Reverse_HIGH = QLabel(self.centralwidget)
        self.label_003_Reverse_HIGH.setObjectName(u"label_003_Reverse_HIGH")
        self.label_003_Reverse_HIGH.setGeometry(QRect(220, 20, 70, 21))
        self.label_003_Reverse_HIGH.setFont(font)
        self.label_005_Channel_LOW = QLabel(self.centralwidget)
        self.label_005_Channel_LOW.setObjectName(u"label_005_Channel_LOW")
        self.label_005_Channel_LOW.setGeometry(QRect(444, 20, 70, 21))
        self.label_005_Channel_LOW.setFont(font)
        self.label_006_Reverse_LOW = QLabel(self.centralwidget)
        self.label_006_Reverse_LOW.setObjectName(u"label_006_Reverse_LOW")
        self.label_006_Reverse_LOW.setGeometry(QRect(530, 20, 70, 21))
        self.label_006_Reverse_LOW.setFont(font)
        self.label_007_VgsHS_HIGH = QLabel(self.centralwidget)
        self.label_007_VgsHS_HIGH.setObjectName(u"label_007_VgsHS_HIGH")
        self.label_007_VgsHS_HIGH.setGeometry(QRect(20, 60, 91, 21))
        self.label_007_VgsHS_HIGH.setFont(font1)
        self.label_008_VdsHS_HIGH = QLabel(self.centralwidget)
        self.label_008_VdsHS_HIGH.setObjectName(u"label_008_VdsHS_HIGH")
        self.label_008_VdsHS_HIGH.setGeometry(QRect(20, 90, 91, 21))
        self.label_008_VdsHS_HIGH.setFont(font1)
        self.label_009_IdsHS_HIGH = QLabel(self.centralwidget)
        self.label_009_IdsHS_HIGH.setObjectName(u"label_009_IdsHS_HIGH")
        self.label_009_IdsHS_HIGH.setGeometry(QRect(20, 120, 91, 21))
        self.label_009_IdsHS_HIGH.setFont(font1)
        self.label_010_If_HIGH = QLabel(self.centralwidget)
        self.label_010_If_HIGH.setObjectName(u"label_010_If_HIGH")
        self.label_010_If_HIGH.setGeometry(QRect(20, 150, 91, 21))
        self.label_010_If_HIGH.setFont(font1)
        self.label_011_CrossTalk_HIGH = QLabel(self.centralwidget)
        self.label_011_CrossTalk_HIGH.setObjectName(u"label_011_CrossTalk_HIGH")
        self.label_011_CrossTalk_HIGH.setGeometry(QRect(20, 180, 91, 21))
        self.label_011_CrossTalk_HIGH.setFont(font1)
        self.label_012_VdsLS_HIGH = QLabel(self.centralwidget)
        self.label_012_VdsLS_HIGH.setObjectName(u"label_012_VdsLS_HIGH")
        self.label_012_VdsLS_HIGH.setGeometry(QRect(20, 210, 91, 21))
        self.label_012_VdsLS_HIGH.setFont(font1)
        self.label_013_IL_HIGH = QLabel(self.centralwidget)
        self.label_013_IL_HIGH.setObjectName(u"label_013_IL_HIGH")
        self.label_013_IL_HIGH.setGeometry(QRect(20, 240, 91, 21))
        self.label_013_IL_HIGH.setFont(font1)
        self.label_014_VgsLS_LOW = QLabel(self.centralwidget)
        self.label_014_VgsLS_LOW.setObjectName(u"label_014_VgsLS_LOW")
        self.label_014_VgsLS_LOW.setGeometry(QRect(330, 60, 91, 21))
        self.label_014_VgsLS_LOW.setFont(font1)
        self.label_015_VdsLS_LOW = QLabel(self.centralwidget)
        self.label_015_VdsLS_LOW.setObjectName(u"label_015_VdsLS_LOW")
        self.label_015_VdsLS_LOW.setGeometry(QRect(330, 90, 91, 21))
        self.label_015_VdsLS_LOW.setFont(font1)
        self.label_016_IdsLS_LOW = QLabel(self.centralwidget)
        self.label_016_IdsLS_LOW.setObjectName(u"label_016_IdsLS_LOW")
        self.label_016_IdsLS_LOW.setGeometry(QRect(330, 120, 91, 21))
        self.label_016_IdsLS_LOW.setFont(font1)
        self.label_017_If_LOW = QLabel(self.centralwidget)
        self.label_017_If_LOW.setObjectName(u"label_017_If_LOW")
        self.label_017_If_LOW.setGeometry(QRect(330, 150, 91, 21))
        self.label_017_If_LOW.setFont(font1)
        self.label_018_CrossTalk_LOW = QLabel(self.centralwidget)
        self.label_018_CrossTalk_LOW.setObjectName(u"label_018_CrossTalk_LOW")
        self.label_018_CrossTalk_LOW.setGeometry(QRect(330, 180, 91, 21))
        self.label_018_CrossTalk_LOW.setFont(font1)
        self.label_019_VdsHS_LOW = QLabel(self.centralwidget)
        self.label_019_VdsHS_LOW.setObjectName(u"label_019_VdsHS_LOW")
        self.label_019_VdsHS_LOW.setGeometry(QRect(330, 210, 91, 21))
        self.label_019_VdsHS_LOW.setFont(font1)
        self.label_020_IL_LOW = QLabel(self.centralwidget)
        self.label_020_IL_LOW.setObjectName(u"label_020_IL_LOW")
        self.label_020_IL_LOW.setGeometry(QRect(330, 240, 91, 21))
        self.label_020_IL_LOW.setFont(font1)
        self.label_021_HS_Vgs_positive = QLabel(self.centralwidget)
        self.label_021_HS_Vgs_positive.setObjectName(u"label_021_HS_Vgs_positive")
        self.label_021_HS_Vgs_positive.setGeometry(QRect(20, 300, 141, 21))
        self.label_021_HS_Vgs_positive.setFont(font)
        self.label_022_HS_Vgs_positive_V = QLabel(self.centralwidget)
        self.label_022_HS_Vgs_positive_V.setObjectName(u"label_022_HS_Vgs_positive_V")
        self.label_022_HS_Vgs_positive_V.setGeometry(QRect(220, 300, 21, 21))
        self.label_022_HS_Vgs_positive_V.setFont(font)
        self.label_023_HS_Vgs_negative = QLabel(self.centralwidget)
        self.label_023_HS_Vgs_negative.setObjectName(u"label_023_HS_Vgs_negative")
        self.label_023_HS_Vgs_negative.setGeometry(QRect(20, 340, 141, 21))
        self.label_023_HS_Vgs_negative.setFont(font)
        self.label_024_HS_Vgs_negative_V = QLabel(self.centralwidget)
        self.label_024_HS_Vgs_negative_V.setObjectName(u"label_024_HS_Vgs_negative_V")
        self.label_024_HS_Vgs_negative_V.setGeometry(QRect(220, 340, 21, 21))
        self.label_024_HS_Vgs_negative_V.setFont(font)
        self.label_025_LS_Vgs_positive = QLabel(self.centralwidget)
        self.label_025_LS_Vgs_positive.setObjectName(u"label_025_LS_Vgs_positive")
        self.label_025_LS_Vgs_positive.setGeometry(QRect(330, 300, 141, 21))
        self.label_025_LS_Vgs_positive.setFont(font)
        self.label_026_LS_Vgs_positive_V = QLabel(self.centralwidget)
        self.label_026_LS_Vgs_positive_V.setObjectName(u"label_026_LS_Vgs_positive_V")
        self.label_026_LS_Vgs_positive_V.setGeometry(QRect(530, 300, 21, 21))
        self.label_026_LS_Vgs_positive_V.setFont(font)
        self.label_027_LS_Vgs_negative = QLabel(self.centralwidget)
        self.label_027_LS_Vgs_negative.setObjectName(u"label_027_LS_Vgs_negative")
        self.label_027_LS_Vgs_negative.setGeometry(QRect(330, 340, 141, 21))
        self.label_027_LS_Vgs_negative.setFont(font)
        self.label_028_LS_Vgs_negative_V = QLabel(self.centralwidget)
        self.label_028_LS_Vgs_negative_V.setObjectName(u"label_028_LS_Vgs_negative_V")
        self.label_028_LS_Vgs_negative_V.setGeometry(QRect(530, 340, 21, 21))
        self.label_028_LS_Vgs_negative_V.setFont(font)
        self.label_029_low_pass_filter = QLabel(self.centralwidget)
        self.label_029_low_pass_filter.setObjectName(u"label_029_low_pass_filter")
        self.label_029_low_pass_filter.setGeometry(QRect(20, 380, 141, 21))
        self.label_029_low_pass_filter.setFont(font1)
        self.label_030_sampling_rate = QLabel(self.centralwidget)
        self.label_030_sampling_rate.setObjectName(u"label_030_sampling_rate")
        self.label_030_sampling_rate.setGeometry(QRect(170, 380, 100, 21))
        self.label_030_sampling_rate.setFont(font1)
        self.label_031_sampling_rate_unit = QLabel(self.centralwidget)
        self.label_031_sampling_rate_unit.setObjectName(u"label_031_sampling_rate_unit")
        self.label_031_sampling_rate_unit.setGeometry(QRect(315, 380, 41, 21))
        self.label_031_sampling_rate_unit.setFont(font1)
        self.label_032_cutoff_frequency = QLabel(self.centralwidget)
        self.label_032_cutoff_frequency.setObjectName(u"label_032_cutoff_frequency")
        self.label_032_cutoff_frequency.setGeometry(QRect(370, 380, 120, 21))
        self.label_032_cutoff_frequency.setFont(font1)
        self.label_033_cutoff_frequency_unit = QLabel(self.centralwidget)
        self.label_033_cutoff_frequency_unit.setObjectName(u"label_033_cutoff_frequency_unit")
        self.label_033_cutoff_frequency_unit.setGeometry(QRect(540, 380, 41, 21))
        self.label_033_cutoff_frequency_unit.setFont(font1)
        self.label_034_input_folder_path = QLabel(self.centralwidget)
        self.label_034_input_folder_path.setObjectName(u"label_034_input_folder_path")
        self.label_034_input_folder_path.setGeometry(QRect(20, 410, 141, 21))
        self.label_034_input_folder_path.setFont(font1)
        self.label_035_output_file_path = QLabel(self.centralwidget)
        self.label_035_output_file_path.setObjectName(u"label_035_output_file_path")
        self.label_035_output_file_path.setGeometry(QRect(20, 440, 161, 21))
        self.label_035_output_file_path.setFont(font1)

        # 这部分为下拉框的初始化
        self.comboBox_001_VgsHS_HIGH = QComboBox(self.centralwidget)
        self.comboBox_001_VgsHS_HIGH.addItem("")
        self.comboBox_001_VgsHS_HIGH.addItem("")
        self.comboBox_001_VgsHS_HIGH.addItem("")
        self.comboBox_001_VgsHS_HIGH.addItem("")
        self.comboBox_001_VgsHS_HIGH.addItem("")
        self.comboBox_001_VgsHS_HIGH.addItem("")
        self.comboBox_001_VgsHS_HIGH.addItem("")
        self.comboBox_001_VgsHS_HIGH.setObjectName(u"comboBox_001_VgsHS_HIGH")
        self.comboBox_001_VgsHS_HIGH.setGeometry(QRect(130, 60, 67, 22))
        self.comboBox_002_VdsHS_HIGH = QComboBox(self.centralwidget)
        self.comboBox_002_VdsHS_HIGH.addItem("")
        self.comboBox_002_VdsHS_HIGH.addItem("")
        self.comboBox_002_VdsHS_HIGH.addItem("")
        self.comboBox_002_VdsHS_HIGH.addItem("")
        self.comboBox_002_VdsHS_HIGH.addItem("")
        self.comboBox_002_VdsHS_HIGH.addItem("")
        self.comboBox_002_VdsHS_HIGH.addItem("")
        self.comboBox_002_VdsHS_HIGH.setObjectName(u"comboBox_002_VdsHS_HIGH")
        self.comboBox_002_VdsHS_HIGH.setGeometry(QRect(130, 90, 67, 22))
        self.comboBox_003_IdsHS_HIGH = QComboBox(self.centralwidget)
        self.comboBox_003_IdsHS_HIGH.addItem("")
        self.comboBox_003_IdsHS_HIGH.addItem("")
        self.comboBox_003_IdsHS_HIGH.addItem("")
        self.comboBox_003_IdsHS_HIGH.addItem("")
        self.comboBox_003_IdsHS_HIGH.addItem("")
        self.comboBox_003_IdsHS_HIGH.addItem("")
        self.comboBox_003_IdsHS_HIGH.addItem("")
        self.comboBox_003_IdsHS_HIGH.setObjectName(u"comboBox_003_IdsHS_HIGH")
        self.comboBox_003_IdsHS_HIGH.setGeometry(QRect(130, 120, 67, 22))
        self.comboBox_004_If_HIGH = QComboBox(self.centralwidget)
        self.comboBox_004_If_HIGH.addItem("")
        self.comboBox_004_If_HIGH.addItem("")
        self.comboBox_004_If_HIGH.addItem("")
        self.comboBox_004_If_HIGH.addItem("")
        self.comboBox_004_If_HIGH.addItem("")
        self.comboBox_004_If_HIGH.addItem("")
        self.comboBox_004_If_HIGH.addItem("")
        self.comboBox_004_If_HIGH.setObjectName(u"comboBox_004_If_HIGH")
        self.comboBox_004_If_HIGH.setGeometry(QRect(130, 150, 67, 22))
        self.comboBox_005_CrossTalk_HIGH = QComboBox(self.centralwidget)
        self.comboBox_005_CrossTalk_HIGH.addItem("")
        self.comboBox_005_CrossTalk_HIGH.addItem("")
        self.comboBox_005_CrossTalk_HIGH.addItem("")
        self.comboBox_005_CrossTalk_HIGH.addItem("")
        self.comboBox_005_CrossTalk_HIGH.addItem("")
        self.comboBox_005_CrossTalk_HIGH.addItem("")
        self.comboBox_005_CrossTalk_HIGH.addItem("")
        self.comboBox_005_CrossTalk_HIGH.setObjectName(u"comboBox_005_CrossTalk_HIGH")
        self.comboBox_005_CrossTalk_HIGH.setGeometry(QRect(130, 180, 67, 22))
        self.comboBox_006_VdsLS_HIGH = QComboBox(self.centralwidget)
        self.comboBox_006_VdsLS_HIGH.addItem("")
        self.comboBox_006_VdsLS_HIGH.addItem("")
        self.comboBox_006_VdsLS_HIGH.addItem("")
        self.comboBox_006_VdsLS_HIGH.addItem("")
        self.comboBox_006_VdsLS_HIGH.addItem("")
        self.comboBox_006_VdsLS_HIGH.addItem("")
        self.comboBox_006_VdsLS_HIGH.addItem("")
        self.comboBox_006_VdsLS_HIGH.setObjectName(u"comboBox_006_VdsLS_HIGH")
        self.comboBox_006_VdsLS_HIGH.setGeometry(QRect(130, 210, 67, 22))
        self.comboBox_007_IL_HIGH = QComboBox(self.centralwidget)
        self.comboBox_007_IL_HIGH.addItem("")
        self.comboBox_007_IL_HIGH.addItem("")
        self.comboBox_007_IL_HIGH.addItem("")
        self.comboBox_007_IL_HIGH.addItem("")
        self.comboBox_007_IL_HIGH.addItem("")
        self.comboBox_007_IL_HIGH.addItem("")
        self.comboBox_007_IL_HIGH.addItem("")
        self.comboBox_007_IL_HIGH.setObjectName(u"comboBox_007_IL_HIGH")
        self.comboBox_007_IL_HIGH.setGeometry(QRect(130, 240, 67, 22))
        self.comboBox_008_VgsLS_LOW = QComboBox(self.centralwidget)
        self.comboBox_008_VgsLS_LOW.addItem("")
        self.comboBox_008_VgsLS_LOW.addItem("")
        self.comboBox_008_VgsLS_LOW.addItem("")
        self.comboBox_008_VgsLS_LOW.addItem("")
        self.comboBox_008_VgsLS_LOW.addItem("")
        self.comboBox_008_VgsLS_LOW.addItem("")
        self.comboBox_008_VgsLS_LOW.addItem("")
        self.comboBox_008_VgsLS_LOW.setObjectName(u"comboBox_008_VgsLS_LOW")
        self.comboBox_008_VgsLS_LOW.setGeometry(QRect(440, 60, 67, 22))
        self.comboBox_009_VdsLS_LOW = QComboBox(self.centralwidget)
        self.comboBox_009_VdsLS_LOW.addItem("")
        self.comboBox_009_VdsLS_LOW.addItem("")
        self.comboBox_009_VdsLS_LOW.addItem("")
        self.comboBox_009_VdsLS_LOW.addItem("")
        self.comboBox_009_VdsLS_LOW.addItem("")
        self.comboBox_009_VdsLS_LOW.addItem("")
        self.comboBox_009_VdsLS_LOW.addItem("")
        self.comboBox_009_VdsLS_LOW.setObjectName(u"comboBox_009_VdsLS_LOW")
        self.comboBox_009_VdsLS_LOW.setGeometry(QRect(440, 90, 67, 22))
        self.comboBox_010_IdsLS_LOW = QComboBox(self.centralwidget)
        self.comboBox_010_IdsLS_LOW.addItem("")
        self.comboBox_010_IdsLS_LOW.addItem("")
        self.comboBox_010_IdsLS_LOW.addItem("")
        self.comboBox_010_IdsLS_LOW.addItem("")
        self.comboBox_010_IdsLS_LOW.addItem("")
        self.comboBox_010_IdsLS_LOW.addItem("")
        self.comboBox_010_IdsLS_LOW.addItem("")
        self.comboBox_010_IdsLS_LOW.setObjectName(u"comboBox_010_IdsLS_LOW")
        self.comboBox_010_IdsLS_LOW.setGeometry(QRect(440, 120, 67, 22))
        self.comboBox_011_If_LOW = QComboBox(self.centralwidget)
        self.comboBox_011_If_LOW.addItem("")
        self.comboBox_011_If_LOW.addItem("")
        self.comboBox_011_If_LOW.addItem("")
        self.comboBox_011_If_LOW.addItem("")
        self.comboBox_011_If_LOW.addItem("")
        self.comboBox_011_If_LOW.addItem("")
        self.comboBox_011_If_LOW.addItem("")
        self.comboBox_011_If_LOW.setObjectName(u"comboBox_011_If_LOW")
        self.comboBox_011_If_LOW.setGeometry(QRect(440, 150, 67, 22))
        self.comboBox_012_CrossTalk_LOW = QComboBox(self.centralwidget)
        self.comboBox_012_CrossTalk_LOW.addItem("")
        self.comboBox_012_CrossTalk_LOW.addItem("")
        self.comboBox_012_CrossTalk_LOW.addItem("")
        self.comboBox_012_CrossTalk_LOW.addItem("")
        self.comboBox_012_CrossTalk_LOW.addItem("")
        self.comboBox_012_CrossTalk_LOW.addItem("")
        self.comboBox_012_CrossTalk_LOW.addItem("")
        self.comboBox_012_CrossTalk_LOW.setObjectName(u"comboBox_012_CrossTalk_LOW")
        self.comboBox_012_CrossTalk_LOW.setGeometry(QRect(440, 180, 67, 22))
        self.comboBox_013_VdsHS_LOW = QComboBox(self.centralwidget)
        self.comboBox_013_VdsHS_LOW.addItem("")
        self.comboBox_013_VdsHS_LOW.addItem("")
        self.comboBox_013_VdsHS_LOW.addItem("")
        self.comboBox_013_VdsHS_LOW.addItem("")
        self.comboBox_013_VdsHS_LOW.addItem("")
        self.comboBox_013_VdsHS_LOW.addItem("")
        self.comboBox_013_VdsHS_LOW.addItem("")
        self.comboBox_013_VdsHS_LOW.setObjectName(u"comboBox_013_VdsHS_LOW")
        self.comboBox_013_VdsHS_LOW.setGeometry(QRect(440, 210, 67, 22))
        self.comboBox_014_IL_LOW = QComboBox(self.centralwidget)
        self.comboBox_014_IL_LOW.addItem("")
        self.comboBox_014_IL_LOW.addItem("")
        self.comboBox_014_IL_LOW.addItem("")
        self.comboBox_014_IL_LOW.addItem("")
        self.comboBox_014_IL_LOW.addItem("")
        self.comboBox_014_IL_LOW.addItem("")
        self.comboBox_014_IL_LOW.addItem("")
        self.comboBox_014_IL_LOW.setObjectName(u"comboBox_014_IL_LOW")
        self.comboBox_014_IL_LOW.setGeometry(QRect(440, 240, 67, 22))


        # 以下为勾选框的初始化
        self.checkBox_001_VgsHS_HIGH = QCheckBox(self.centralwidget)
        self.checkBox_001_VgsHS_HIGH.setObjectName(u"checkBox_001_VgsHS_HIGH")
        self.checkBox_001_VgsHS_HIGH.setGeometry(QRect(240, 62, 21, 16))
        self.checkBox_001_VgsHS_HIGH.stateChanged.connect(lambda:self.checkBox_001_VgsHS_HIGH_State(self.checkBox_001_VgsHS_HIGH))
        self.checkBox_002_VdsHS_HIGH = QCheckBox(self.centralwidget)
        self.checkBox_002_VdsHS_HIGH.setObjectName(u"checkBox_002_VdsHS_HIGH")
        self.checkBox_002_VdsHS_HIGH.setGeometry(QRect(240, 93, 21, 16))
        self.checkBox_002_VdsHS_HIGH.stateChanged.connect(lambda:self.checkBox_002_VdsHS_HIGH_State(self.checkBox_002_VdsHS_HIGH))
        self.checkBox_003_IdsHS_HIGH = QCheckBox(self.centralwidget)
        self.checkBox_003_IdsHS_HIGH.setObjectName(u"checkBox_003_IdsHS_HIGH")
        self.checkBox_003_IdsHS_HIGH.setGeometry(QRect(240, 123, 21, 16))
        self.checkBox_003_IdsHS_HIGH.stateChanged.connect(lambda:self.checkBox_003_IdsHS_HIGH_State(self.checkBox_003_IdsHS_HIGH))
        self.checkBox_004_CrossTalk_HIGH = QCheckBox(self.centralwidget)
        self.checkBox_004_CrossTalk_HIGH.setObjectName(u"checkBox_004_CrossTalk_HIGH")
        self.checkBox_004_CrossTalk_HIGH.setGeometry(QRect(240, 184, 21, 16))
        self.checkBox_004_CrossTalk_HIGH.stateChanged.connect(lambda:self.checkBox_004_CrossTalk_HIGH_State(self.checkBox_004_CrossTalk_HIGH))
        self.checkBox_005_VdsLS_HIGH = QCheckBox(self.centralwidget)
        self.checkBox_005_VdsLS_HIGH.setObjectName(u"checkBox_005_VdsLS_HIGH")
        self.checkBox_005_VdsLS_HIGH.setGeometry(QRect(240, 212, 21, 16))
        self.checkBox_005_VdsLS_HIGH.stateChanged.connect(lambda:self.checkBox_005_VdsLS_HIGH_State(self.checkBox_005_VdsLS_HIGH))
        self.checkBox_006_If_HIGH = QCheckBox(self.centralwidget)
        self.checkBox_006_If_HIGH.setObjectName(u"checkBox_006_If_HIGH")
        self.checkBox_006_If_HIGH.setGeometry(QRect(240, 153, 21, 16))
        self.checkBox_006_If_HIGH.stateChanged.connect(lambda:self.checkBox_006_If_HIGH_State(self.checkBox_006_If_HIGH))
        self.checkBox_007_VgsLS_LOW = QCheckBox(self.centralwidget)
        self.checkBox_007_VgsLS_LOW.setObjectName(u"checkBox_007_VgsLS_LOW")
        self.checkBox_007_VgsLS_LOW.setGeometry(QRect(550, 62, 21, 16))
        self.checkBox_007_VgsLS_LOW.stateChanged.connect(lambda:self.checkBox_007_VgsLS_LOW_State(self.checkBox_007_VgsLS_LOW))
        self.checkBox_008_VdsLS_LOW = QCheckBox(self.centralwidget)
        self.checkBox_008_VdsLS_LOW.setObjectName(u"checkBox_008_VdsLS_LOW")
        self.checkBox_008_VdsLS_LOW.setGeometry(QRect(550, 93, 21, 16))
        self.checkBox_008_VdsLS_LOW.stateChanged.connect(lambda:self.checkBox_008_VdsLS_LOW_State(self.checkBox_008_VdsLS_LOW))
        self.checkBox_009_IdsLS_LOW = QCheckBox(self.centralwidget)
        self.checkBox_009_IdsLS_LOW.setObjectName(u"checkBox_009_IdsLS_LOW")
        self.checkBox_009_IdsLS_LOW.setGeometry(QRect(550, 123, 21, 16))
        self.checkBox_009_IdsLS_LOW.stateChanged.connect(lambda:self.checkBox_009_IdsLS_LOW_State(self.checkBox_009_IdsLS_LOW))
        self.checkBox_010_CrossTalk_LOW = QCheckBox(self.centralwidget)
        self.checkBox_010_CrossTalk_LOW.setObjectName(u"checkBox_010_CrossTalk_LOW")
        self.checkBox_010_CrossTalk_LOW.setGeometry(QRect(550, 184, 21, 16))
        self.checkBox_010_CrossTalk_LOW.stateChanged.connect(lambda:self.checkBox_010_CrossTalk_LOW_State(self.checkBox_010_CrossTalk_LOW))
        self.checkBox_011_VdsHS_LOW = QCheckBox(self.centralwidget)
        self.checkBox_011_VdsHS_LOW.setObjectName(u"checkBox_011_VdsHS_LOW")
        self.checkBox_011_VdsHS_LOW.setGeometry(QRect(550, 212, 21, 16))
        self.checkBox_011_VdsHS_LOW.stateChanged.connect(lambda:self.checkBox_011_VdsHS_LOW_State(self.checkBox_011_VdsHS_LOW))
        self.checkBox_012_If_LOW = QCheckBox(self.centralwidget)
        self.checkBox_012_If_LOW.setObjectName(u"checkBox_012_If_LOW")
        self.checkBox_012_If_LOW.setGeometry(QRect(550, 153, 21, 16))
        self.checkBox_012_If_LOW.stateChanged.connect(lambda:self.checkBox_012_If_LOW_State(self.checkBox_012_If_LOW))
        self.checkBox_013_IL_HIGH = QCheckBox(self.centralwidget)
        self.checkBox_013_IL_HIGH.setObjectName(u"checkBox_013_IL_HIGH")
        self.checkBox_013_IL_HIGH.setGeometry(QRect(240, 243, 21, 16))
        self.checkBox_013_IL_HIGH.stateChanged.connect(lambda:self.checkBox_013_IL_HIGH_State(self.checkBox_013_IL_HIGH))
        self.checkBox_014_IL_LOW = QCheckBox(self.centralwidget)
        self.checkBox_014_IL_LOW.setObjectName(u"checkBox_014_IL_LOW")
        self.checkBox_014_IL_LOW.setGeometry(QRect(550, 243, 21, 16))
        self.checkBox_014_IL_LOW.stateChanged.connect(lambda:self.checkBox_014_IL_LOW_State(self.checkBox_014_IL_LOW))
        self.checkBox_015_low_pass_filter = QCheckBox(self.centralwidget)
        self.checkBox_015_low_pass_filter.setObjectName(u"checkBox_015_low_pass_filter")
        self.checkBox_015_low_pass_filter.setGeometry(QRect(135, 383, 21, 16))
        self.checkBox_015_low_pass_filter.stateChanged.connect(lambda:self.checkBox_015_low_pass_filter_State(self.checkBox_015_low_pass_filter))

        #以下为文字输入框的初始化
        self.lineEdit_001_HS_Vgs_positive = QLineEdit(self.centralwidget)
        self.lineEdit_001_HS_Vgs_positive.setObjectName(u"lineEdit_001_HS_Vgs_positive")
        self.lineEdit_001_HS_Vgs_positive.setGeometry(QRect(160, 300, 51, 20))
        #doubleValidator = QDoubleValidator(self)
        #doubleValidator.setRange(-30,30)
        #doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        #self.lineEdit_001_HS_Vgs_positive.setRange(-30,30)
        #self.lineEdit_001_HS_Vgs_positive.setNotation(QDoubleValidator.StandardNotation)
        #self.lineEdit_001_HS_Vgs_positive.setDecimals(2)
        self.lineEdit_002_HS_Vgs_negative = QLineEdit(self.centralwidget)
        self.lineEdit_002_HS_Vgs_negative.setObjectName(u"lineEdit_002_HS_Vgs_negative")
        self.lineEdit_002_HS_Vgs_negative.setGeometry(QRect(160, 340, 51, 20))
        self.lineEdit_003_LS_Vgs_positive = QLineEdit(self.centralwidget)
        self.lineEdit_003_LS_Vgs_positive.setObjectName(u"lineEdit_003_LS_Vgs_positive")
        self.lineEdit_003_LS_Vgs_positive.setGeometry(QRect(470, 300, 51, 20))
        self.lineEdit_004_LS_Vgs_negative = QLineEdit(self.centralwidget)
        self.lineEdit_004_LS_Vgs_negative.setObjectName(u"lineEdit_004_LS_Vgs_negative")
        self.lineEdit_004_LS_Vgs_negative.setGeometry(QRect(470, 340, 51, 20))
        self.lineEdit_005_sampling_rate = QLineEdit(self.centralwidget)
        self.lineEdit_005_sampling_rate.setObjectName(u"lineEdit_005_sampling_rate")
        self.lineEdit_005_sampling_rate.setGeometry(QRect(260, 380, 51, 20))
        self.lineEdit_006_cutoff_frequency = QLineEdit(self.centralwidget)
        self.lineEdit_006_cutoff_frequency.setObjectName(u"lineEdit_006_cutoff_frequency")
        self.lineEdit_006_cutoff_frequency.setGeometry(QRect(485, 380, 51, 20))

        # 以下为文件路径选择按钮的初始化
        self.ToolButton_001_input_folder_path = QToolButton(self.centralwidget)
        self.ToolButton_001_input_folder_path.setObjectName(u"ToolButton_001_input_folder_path")
        self.ToolButton_001_input_folder_path.setGeometry(QRect(550, 410, 30, 20))
        self.ToolButton_002_output_file_path = QToolButton(self.centralwidget)
        self.ToolButton_002_output_file_path.setObjectName(u"ToolButton_002_output_file_path")
        self.ToolButton_002_output_file_path.setGeometry(QRect(550, 440, 30, 20))

        # 以下为开始与停止按钮的初始化
        self.PushButton_001_Start = QPushButton(self.centralwidget)
        self.PushButton_001_Start.setObjectName(u"PushButton_001_Start")
        self.PushButton_001_Start.setGeometry(QRect(50, 470, 200, 80))
        self.PushButton_001_Start.setFont(font)
        self.PushButton_002_Stop = QPushButton(self.centralwidget)
        self.PushButton_002_Stop.setObjectName(u"PushButton_002_Stop")
        self.PushButton_002_Stop.setGeometry(QRect(400, 470, 200, 80))
        self.PushButton_002_Stop.setFont(font)

        # 以下为处理过程显示框的初始化
        self.textBrowser_001_input_folder_path_printf = QTextBrowser(self.centralwidget)
        self.textBrowser_001_input_folder_path_printf.setObjectName(u"textBrowser_001_input_folder_path_printf")
        self.textBrowser_001_input_folder_path_printf.setGeometry(QRect(150, 410, 380, 20))
        self.textBrowser_002_output_file_path_printf = QTextBrowser(self.centralwidget)
        self.textBrowser_002_output_file_path_printf.setObjectName(u"textBrowser_002_output_file_path_printf")
        self.textBrowser_002_output_file_path_printf.setGeometry(QRect(150, 440, 380, 20))
        self.textBrowser_003_main_printf = QTextBrowser(self.centralwidget)
        self.textBrowser_003_main_printf.setObjectName(u"textBrowser_003_main_printf")
        #self.textBrowser_003_main_printf.setGeometry(QRect(20, 570, 600, 200))
        self.textBrowser_003_main_printf.setGeometry(QRect(20, 570, 0, 0))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # 设置初始默认值
        self.comboBox_001_VgsHS_HIGH.setCurrentIndex(1)
        self.comboBox_002_VdsHS_HIGH.setCurrentIndex(2)
        self.comboBox_004_If_HIGH.setCurrentIndex(3)
        self.comboBox_005_CrossTalk_HIGH.setCurrentIndex(4)
        self.comboBox_006_VdsLS_HIGH.setCurrentIndex(5)
        self.comboBox_007_IL_HIGH.setCurrentIndex(6)
        self.comboBox_008_VgsLS_LOW.setCurrentIndex(1)
        self.comboBox_009_VdsLS_LOW.setCurrentIndex(2)
        self.comboBox_010_IdsLS_LOW.setCurrentIndex(3)
        self.comboBox_012_CrossTalk_LOW.setCurrentIndex(4)
        self.comboBox_013_VdsHS_LOW.setCurrentIndex(5)
        self.comboBox_014_IL_LOW.setCurrentIndex(6)

        # 下拉框，选择变更后将结果输出
        self.comboBox_001_VgsHS_HIGH.currentTextChanged.connect(self.GetComboBox001_VgsHS_HIGH)
        self.comboBox_002_VdsHS_HIGH.currentTextChanged.connect(self.GetComboBox002_VdsHS_HIGH)
        self.comboBox_003_IdsHS_HIGH.currentTextChanged.connect(self.GetComboBox003_IdsHS_HIGH)
        self.comboBox_004_If_HIGH.currentTextChanged.connect(self.GetComboBox004_If_HIGH)
        self.comboBox_005_CrossTalk_HIGH.currentTextChanged.connect(self.GetComboBox005_CrossTalk_HIGH)
        self.comboBox_006_VdsLS_HIGH.currentTextChanged.connect(self.GetComboBox006_VdsLS_HIGH)
        self.comboBox_007_IL_HIGH.currentTextChanged.connect(self.GetComboBox007_IL_HIGH)
        self.comboBox_008_VgsLS_LOW.currentTextChanged.connect(self.GetComboBox008_VgsLS_LOW)
        self.comboBox_009_VdsLS_LOW.currentTextChanged.connect(self.GetComboBox009_VdsLS_LOW)
        self.comboBox_010_IdsLS_LOW.currentTextChanged.connect(self.GetComboBox010_IdsLS_LOW)
        self.comboBox_011_If_LOW.currentTextChanged.connect(self.GetComboBox011_If_LOW)
        self.comboBox_012_CrossTalk_LOW.currentTextChanged.connect(self.GetComboBox012_CrossTalk_LOW)
        self.comboBox_013_VdsHS_LOW.currentTextChanged.connect(self.GetComboBox013_VdsHS_LOW)
        self.comboBox_014_IL_LOW.currentTextChanged.connect(self.GetComboBox014_IL_LOW)

        # 文字输入框，数值变更后将结果输出
        self.lineEdit_001_HS_Vgs_positive.textChanged.connect(self.lineEdit_001_HS_Vgs_positive_Info)
        self.lineEdit_002_HS_Vgs_negative.textChanged.connect(self.lineEdit_002_HS_Vgs_negative_Info)
        self.lineEdit_003_LS_Vgs_positive.textChanged.connect(self.lineEdit_003_LS_Vgs_positive_Info)
        self.lineEdit_004_LS_Vgs_negative.textChanged.connect(self.lineEdit_004_LS_Vgs_negative_Info)
        self.lineEdit_005_sampling_rate.textChanged.connect(self.lineEdit_005_sampling_rate_Info)
        self.lineEdit_006_cutoff_frequency.textChanged.connect(self.lineEdit_006_cutoff_frequency_Info)

        # 文字输出框，选择文件夹路径后，将选择的内容显示在输出框中
        self.ToolButton_001_input_folder_path.clicked.connect(self.GetToolButton_001_input_folder_path)
        self.ToolButton_002_output_file_path.clicked.connect(self.GetToolButton_002_output_file_path)

        # 按钮，被点击后输出点击结果
        self.PushButton_001_Start.clicked.connect(self.start_program)
        self.PushButton_002_Stop.clicked.connect(self.stop_program)
        QMetaObject.connectSlotsByName(MainWindow)

        # 初始化按钮状态
        self.PushButton_001_Start.setEnabled(True)
        self.PushButton_002_Stop.setEnabled(False)
        

    def retranslateUi(self, MainWindow):
        # 将各类文字与数字信息，填入已经初始化完成的位置。
        MainWindow.setWindowTitle(QCoreApplication.translate("Automatic reading of dynamic test results", u"Automatic reading of dynamic test results", None))
        self.label_001_HIGH_Side.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"HIGH Side", None))
        self.label_004_LOW_Side.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"LOW Side", None))
        self.label_002_Channel_HIGH.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Channel", None))
        self.label_003_Reverse_HIGH.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Reverse", None))
        self.label_005_Channel_LOW.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Channel", None))
        self.label_006_Reverse_LOW.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Reverse", None))
        self.label_007_VgsHS_HIGH.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Vgs_active", None))
        self.label_008_VdsHS_HIGH.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Vds_active", None))
        self.label_009_IdsHS_HIGH.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Ids_active", None))
        self.label_010_If_HIGH.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Idiode_passive", None))
        self.label_011_CrossTalk_HIGH.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Vgs_passive", None))
        self.label_012_VdsLS_HIGH.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Vds_passive", None))
        self.label_016_IdsLS_LOW.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Ids_active", None))
        self.label_014_VgsLS_LOW.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Vgs_active", None))
        self.label_015_VdsLS_LOW.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Vds_active", None))
        self.label_017_If_LOW.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Idiode_passive", None))
        self.label_018_CrossTalk_LOW.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Vgs_passive", None))
        self.label_019_VdsHS_LOW.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Vds_passive", None))
        self.comboBox_001_VgsHS_HIGH.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_001_VgsHS_HIGH.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_001_VgsHS_HIGH.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_001_VgsHS_HIGH.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_001_VgsHS_HIGH.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_001_VgsHS_HIGH.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_001_VgsHS_HIGH.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_002_VdsHS_HIGH.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_002_VdsHS_HIGH.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_002_VdsHS_HIGH.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_002_VdsHS_HIGH.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_002_VdsHS_HIGH.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_002_VdsHS_HIGH.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_002_VdsHS_HIGH.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_003_IdsHS_HIGH.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_003_IdsHS_HIGH.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_003_IdsHS_HIGH.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_003_IdsHS_HIGH.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_003_IdsHS_HIGH.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_003_IdsHS_HIGH.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_003_IdsHS_HIGH.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_004_If_HIGH.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_004_If_HIGH.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_004_If_HIGH.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_004_If_HIGH.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_004_If_HIGH.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_004_If_HIGH.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_004_If_HIGH.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_005_CrossTalk_HIGH.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_005_CrossTalk_HIGH.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_005_CrossTalk_HIGH.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_005_CrossTalk_HIGH.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_005_CrossTalk_HIGH.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_005_CrossTalk_HIGH.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_005_CrossTalk_HIGH.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_006_VdsLS_HIGH.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_006_VdsLS_HIGH.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_006_VdsLS_HIGH.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_006_VdsLS_HIGH.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_006_VdsLS_HIGH.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_006_VdsLS_HIGH.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_006_VdsLS_HIGH.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_007_IL_HIGH.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_007_IL_HIGH.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_007_IL_HIGH.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_007_IL_HIGH.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_007_IL_HIGH.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_007_IL_HIGH.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_007_IL_HIGH.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_008_VgsLS_LOW.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_008_VgsLS_LOW.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_008_VgsLS_LOW.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_008_VgsLS_LOW.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_008_VgsLS_LOW.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_008_VgsLS_LOW.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_008_VgsLS_LOW.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_009_VdsLS_LOW.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_009_VdsLS_LOW.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_009_VdsLS_LOW.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_009_VdsLS_LOW.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_009_VdsLS_LOW.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_009_VdsLS_LOW.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_009_VdsLS_LOW.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_010_IdsLS_LOW.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_010_IdsLS_LOW.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_010_IdsLS_LOW.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_010_IdsLS_LOW.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_010_IdsLS_LOW.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_010_IdsLS_LOW.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_010_IdsLS_LOW.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_011_If_LOW.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_011_If_LOW.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_011_If_LOW.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_011_If_LOW.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_011_If_LOW.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_011_If_LOW.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_011_If_LOW.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_012_CrossTalk_LOW.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_012_CrossTalk_LOW.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_012_CrossTalk_LOW.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_012_CrossTalk_LOW.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_012_CrossTalk_LOW.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_012_CrossTalk_LOW.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_012_CrossTalk_LOW.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_013_VdsHS_LOW.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_013_VdsHS_LOW.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_013_VdsHS_LOW.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_013_VdsHS_LOW.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_013_VdsHS_LOW.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_013_VdsHS_LOW.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_013_VdsHS_LOW.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.comboBox_014_IL_LOW.setItemText(0, QCoreApplication.translate("Automatic reading of dynamic test results", u"0", None))
        self.comboBox_014_IL_LOW.setItemText(1, QCoreApplication.translate("Automatic reading of dynamic test results", u"1", None))
        self.comboBox_014_IL_LOW.setItemText(2, QCoreApplication.translate("Automatic reading of dynamic test results", u"2", None))
        self.comboBox_014_IL_LOW.setItemText(3, QCoreApplication.translate("Automatic reading of dynamic test results", u"3", None))
        self.comboBox_014_IL_LOW.setItemText(4, QCoreApplication.translate("Automatic reading of dynamic test results", u"4", None))
        self.comboBox_014_IL_LOW.setItemText(5, QCoreApplication.translate("Automatic reading of dynamic test results", u"5", None))
        self.comboBox_014_IL_LOW.setItemText(6, QCoreApplication.translate("Automatic reading of dynamic test results", u"6", None))

        self.checkBox_001_VgsHS_HIGH.setText("")
        self.checkBox_002_VdsHS_HIGH.setText("")
        self.checkBox_003_IdsHS_HIGH.setText("")
        self.checkBox_004_CrossTalk_HIGH.setText("")
        self.checkBox_005_VdsLS_HIGH.setText("")
        self.checkBox_006_If_HIGH.setText("")
        self.checkBox_007_VgsLS_LOW.setText("")
        self.checkBox_008_VdsLS_LOW.setText("")
        self.checkBox_009_IdsLS_LOW.setText("")
        self.checkBox_010_CrossTalk_LOW.setText("")
        self.checkBox_011_VdsHS_LOW.setText("")
        self.checkBox_012_If_LOW.setText("")
        self.label_021_HS_Vgs_positive.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"HIGH Side Vgs+", None))
        self.label_023_HS_Vgs_negative.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"HIGH Side Vgs-", None))
        self.label_027_LS_Vgs_negative.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"LOW Side Vgs-", None))
        self.label_025_LS_Vgs_positive.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"LOW Side Vgs+", None))
        self.lineEdit_001_HS_Vgs_positive.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"18", None))
        self.lineEdit_002_HS_Vgs_negative.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"-1", None))
        self.lineEdit_003_LS_Vgs_positive.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"18", None))
        self.lineEdit_004_LS_Vgs_negative.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"-1", None))
        self.label_022_HS_Vgs_positive_V.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"V", None))
        self.label_024_HS_Vgs_negative_V.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"V", None))
        self.label_026_LS_Vgs_positive_V.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"V", None))
        self.label_028_LS_Vgs_negative_V.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"V", None))
        self.label_029_low_pass_filter.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Low Pass Filter", None))
        self.checkBox_015_low_pass_filter.setText("")
        self.lineEdit_005_sampling_rate.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"6.25", None))
        self.label_031_sampling_rate_unit.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"GS/s", None))
        self.label_030_sampling_rate.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Sampling Rate", None))
        self.label_032_cutoff_frequency.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Cut-off Frequency", None))
        self.label_033_cutoff_frequency_unit.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"MHz", None))
        self.lineEdit_006_cutoff_frequency.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"400", None))
        self.ToolButton_001_input_folder_path.setToolTip(QCoreApplication.translate("Automatic reading of dynamic test results", u"<html><head/><body><p><br/></p></body></html>", None))
        self.ToolButton_001_input_folder_path.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"...", None))
        self.label_034_input_folder_path.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Input Folder Path", None))
        self.label_035_output_file_path.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Output File Path", None))
        self.ToolButton_002_output_file_path.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"...", None))
        self.PushButton_001_Start.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Start", None))
        #self.PushButton_002_Stop.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Stop", None))
        self.PushButton_002_Stop.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"Reset", None))

        self.checkBox_013_IL_HIGH.setText("")
        self.checkBox_014_IL_LOW.setText("")

        self.label_013_IL_HIGH.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"IL", None))
        self.label_020_IL_LOW.setText(QCoreApplication.translate("Automatic reading of dynamic test results", u"IL", None))


    # 以下为下拉框变更的获取函数
    def GetComboBox001_VgsHS_HIGH(self, text):
        UIInfoDict['HS_Vgs_act_Channel'] = text
        #print(f"下拉框Vgs_HS更新为: {text}")
    def GetComboBox002_VdsHS_HIGH(self, text):
        UIInfoDict['HS_Vds_act_Channel'] = text
        #print(f"下拉框Vds_HS更新为: {text}")
    def GetComboBox003_IdsHS_HIGH(self, text):
        UIInfoDict['HS_Ids_act_Channel'] = text
        #print(f"下拉框Ids_HS更新为: {text}")
    def GetComboBox004_If_HIGH(self, text):
        UIInfoDict['HS_Idiode_pas_Channel'] = text
        #print(f"下拉框If_HIGH更新为: {text}")
    def GetComboBox005_CrossTalk_HIGH(self, text):
        UIInfoDict['HS_Vgs_pas_Channel'] = text
        #print(f"下拉框CrossTalk_HIGH更新为: {text}")
    def GetComboBox006_VdsLS_HIGH(self, text):
        UIInfoDict['HS_Vds_pas_Channel'] = text
        #print(f"下拉框Vds_LS更新为: {text}")
    def GetComboBox007_IL_HIGH(self, text):
        UIInfoDict['HS_IL_Channel'] = text
        #print(f"下拉框IL_HIGH更新为: {text}")

    def GetComboBox008_VgsLS_LOW(self, text):
        UIInfoDict['LS_Vgs_act_Channel'] = text
        #print(f"下拉框Vgs_LS更新为: {text}")
    def GetComboBox009_VdsLS_LOW(self, text):
        UIInfoDict['LS_Vds_act_Channel'] = text
        #print(f"下拉框Vds_LS更新为: {text}")
    def GetComboBox010_IdsLS_LOW(self, text):
        UIInfoDict['LS_Ids_act_Channel'] = text
        #print(f"下拉框Ids_LS更新为: {text}")
    def GetComboBox011_If_LOW(self, text):
        UIInfoDict['LS_Idiode_pas_Channel'] = text
        #print(f"下拉框If_LOW更新为: {text}")
    def GetComboBox012_CrossTalk_LOW(self, text):
        UIInfoDict['LS_Vgs_pas_Channel'] = text
        #print(f"下拉框CrossTalk_LOW更新为: {text}")
    def GetComboBox013_VdsHS_LOW(self, text):
        UIInfoDict['LS_Vds_pas_Channel'] = text
        #print(f"下拉框Vds_HS更新为: {text}")
    def GetComboBox014_IL_LOW(self, text):
        UIInfoDict['LS_IL_Channel'] = text
        #print(f"下拉框IL_LOW更新为: {text}")

    # 以下为勾选框的获取函数
    def checkBox_001_VgsHS_HIGH_State(self,cb):
        flag = self.checkBox_001_VgsHS_HIGH.isChecked()
        UIInfoDict['HS_Vgs_act_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_001_VgsHS_HIGH=' + str(flag)
        #print(check1Status)
        #print(UIInfoDict)
    def checkBox_002_VdsHS_HIGH_State(self,cb):
        flag = self.checkBox_002_VdsHS_HIGH.isChecked()
        UIInfoDict['HS_Vds_act_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_002_VdsHS_HIGH=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_003_IdsHS_HIGH_State(self,cb):
        flag = self.checkBox_003_IdsHS_HIGH.isChecked()
        UIInfoDict['HS_Ids_act_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_003_IdsHS_HIGH=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_004_CrossTalk_HIGH_State(self,cb):
        flag = self.checkBox_004_CrossTalk_HIGH.isChecked()
        UIInfoDict['HS_Vgs_pas_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_004_CrossTalk_HIGH=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_005_VdsLS_HIGH_State(self,cb):
        flag = self.checkBox_005_VdsLS_HIGH.isChecked()
        UIInfoDict['HS_Vds_pas_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_005_VdsLS_HIGH=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_006_If_HIGH_State(self,cb):
        flag = self.checkBox_006_If_HIGH.isChecked()
        UIInfoDict['HS_Idiode_pas_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_006_If_HIGH=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_007_VgsLS_LOW_State(self,cb):
        flag = self.checkBox_007_VgsLS_LOW.isChecked()
        UIInfoDict['LS_Vgs_act_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_007_VgsLS_LOW=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_008_VdsLS_LOW_State(self,cb):
        flag = self.checkBox_008_VdsLS_LOW.isChecked()
        UIInfoDict['LS_Vds_act_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_008_VdsLS_LOW=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_009_IdsLS_LOW_State(self,cb):
        flag = self.checkBox_009_IdsLS_LOW.isChecked()
        UIInfoDict['LS_Ids_act_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_009_IdsLS_LOW=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_010_CrossTalk_LOW_State(self,cb):
        flag = self.checkBox_010_CrossTalk_LOW.isChecked()
        UIInfoDict['LS_Vgs_pas_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_010_CrossTalk_LOW=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_011_VdsHS_LOW_State(self,cb):
        flag = self.checkBox_011_VdsHS_LOW.isChecked()
        UIInfoDict['LS_Vds_pas_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_011_VdsHS_LOW=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_012_If_LOW_State(self,cb):
        flag = self.checkBox_012_If_LOW.isChecked()
        UIInfoDict['LS_Idiode_pas_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_012_If_LOW=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_013_IL_HIGH_State(self,cb):
        flag = self.checkBox_013_IL_HIGH.isChecked()
        UIInfoDict['HS_IL_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_013_IL_HIGH=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_014_IL_LOW_State(self,cb):
        flag = self.checkBox_014_IL_LOW.isChecked()
        UIInfoDict['LS_IL_Reverse'] = -1 if flag else 1
        check1Status = 'checkBox_014_IL_LOW=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)
    def checkBox_015_low_pass_filter_State(self,cb):
        flag = self.checkBox_015_low_pass_filter.isChecked()
        UIInfoDict['Is_low_pass_filter'] = 1 if flag else 0
        check1Status = 'checkBox_015_low_pass_filter=' + str(flag)
        #print(UIInfoDict)
        #print(check1Status)

    # 以下为文字输入框的获取函数
    def lineEdit_001_HS_Vgs_positive_Info(self,info):
        UIInfoDict['HS_Vgs_positive_voltage'] = info
        #print(f"lineEdit_001_HS_Vgs_positive更新为: {info}")
        #print(UIInfoDict)
    def lineEdit_002_HS_Vgs_negative_Info(self,info):
        UIInfoDict['HS_Vgs_negative_voltage'] = info
        #print(f"lineEdit_002_HS_Vgs_negative更新为: {info}")
        #print(UIInfoDict)
    def lineEdit_003_LS_Vgs_positive_Info(self,info):
        UIInfoDict['LS_Vgs_positive_voltage'] = info
        #print(f"lineEdit_003_LS_Vgs_positive更新为: {info}")
        #print(UIInfoDict)
    def lineEdit_004_LS_Vgs_negative_Info(self,info):
        UIInfoDict['LS_Vgs_negative_voltage'] = info
        #print(f"lineEdit_004_LS_Vgs_negative更新为: {info}")
        #print(UIInfoDict)
    def lineEdit_005_sampling_rate_Info(self,info):
        UIInfoDict['sampling_rate'] = info
        #print(f"lineEdit_005_sampling_rate更新为: {info}")
        #print(UIInfoDict)
    def lineEdit_006_cutoff_frequency_Info(self,info):
        UIInfoDict['cutoff_frequency'] = info
        #print(f"lineEdit_006_cutoff_frequency更新为: {info}")
        #print(UIInfoDict)

    # 以下为输出框的现实更新函数
    def GetToolButton_001_input_folder_path(self):
        new_input_folder_path = QtWidgets.QFileDialog.getExistingDirectory(None,"选取文件夹","C:/")  # 起始路径
        #new_input_folder_path = QtWidgets.QFileDialog.getExistingDirectory(None,"选取文件夹",r"C:\Users\23000222\Desktop\代码改动专用\测试专用数据 新E1")  # 测试专用起始路径
        UIInfoDict['input_folder_path'] = new_input_folder_path
        self.textBrowser_001_input_folder_path_printf.setText(new_input_folder_path)
        #print(f"ToolButton_001_input_folder_path更新为: {new_input_folder_path}")
        #print(UIInfoDict)
    def GetToolButton_002_output_file_path(self):
        new_output_file_path = QtWidgets.QFileDialog.getExistingDirectory(None,"选取文件夹","C:/")  # 起始路径
        #new_output_file_path = QtWidgets.QFileDialog.getExistingDirectory(None,"选取文件夹",r"C:\Users\23000222\Desktop\代码改动专用\结果暂存")  # 测试专用起始路径
        UIInfoDict['output_file_path'] = new_output_file_path
        self.textBrowser_002_output_file_path_printf.setText(new_output_file_path)
        #print(f"ToolButton_002_output_file_path更新为: {new_output_file_path}")
        #print(UIInfoDict)

    def start_program(self):
        #print('PushButton_001_Start:被点击')
        # 设置程序正在运行的标志
        self.is_program_running = True
        # 更改按钮状态
        self.PushButton_001_Start.setEnabled(False)
        self.PushButton_002_Stop.setEnabled(True)
        try:
            self.UI_run_program()
        except FileNotFoundError:
            self.textBrowser_003_main_printf.append('File path selection error')
            print('File path selection error')
        '''except Exception as e:
            self.textBrowser_003_main_printf.append(f"Other error: {e}")'''
        



    def stop_program(self):
        #print('PushButton_002_Stop:被点击')

        # 重置程序运行标志
        self.is_program_running = False
        # 更改按钮状态
        self.PushButton_001_Start.setEnabled(True)
        self.PushButton_002_Stop.setEnabled(False)
        self.textBrowser_003_main_printf.append('Please reselect the option')

    def UI_run_program(self):
        ModuleType = ['MOSFET', 'IGBT'][1]
        self.textBrowser_003_main_printf.append('Running...')

        FolderPath = UIInfoDict['input_folder_path']
        FileOut = UIInfoDict['output_file_path']
        FileOut = def_csv.CreateCSVFile(FileOut)
        #FileOut = r"D:\File\0.公司相关\1.1.黄山MOSFET\8并1200V\12.RohmCD+鼎声IGBR\20241216 C档\4.分析报告\数据处理专用\测试专用\动态参数自动读取结果.csv"
        IsFilterFlag = [False, True][UIInfoDict['Is_low_pass_filter']]

        #self.textBrowser_003_main_printf.append('FolderPath:' + FolderPath)
        #self.textBrowser_003_main_printf.append('\n')
        #self.textBrowser_003_main_printf.append('FileOut:' + FileOut)
        #self.textBrowser_003_main_printf.append('IsFilterFlag:' + str(IsFilterFlag))

        AllCsvInfoDict = []
        G_T, G_Vge, G_Vce, G_Ic, G_Vf, G_If = [], [], [], [], [], []
        ToBeWriteList = []

        folder_list = def_csv.GetFolderList(FolderPath)
        for file_name in folder_list:
            def_csv.check_file_type(AllCsvInfoDict, FolderPath, file_name, UIInfoDict)
        #到此已经获取了需要读取的全部csv文件夹，以及对应文件夹是上桥还是下桥
        csv_num = 0  # 获取总共需要处理的文件数
        for tmp in AllCsvInfoDict:
            CSVFolderList = def_csv.GetFolderList(tmp['CsvFilePath'])
            csv_num += len(CSVFolderList)
        flag = 1
        for tmp in AllCsvInfoDict:
            CSVFolderList = def_csv.GetFolderList(tmp['CsvFilePath'])
            for csv_tmp in CSVFolderList:  # 使用csv_tmp循环读取列表中内容。
                print('Processing:', tmp['FolderInfo'], csv_tmp)
                Data = def_csv.ReadCsvFile(tmp['CsvFilePath'] + '\\' + csv_tmp)
                VgsR = -50.0  # 经过上下桥判断后，确认当前的栅极负压，默认为-50.0
                Vgs = 0.0  # 经过上下桥判断后，确认当前的栅极正压，默认为0.0
                VgsR = tmp['VgsLow']  #  该参数在驱动板通电后，使用万用表测量上桥gs电压，用于校准光隔离探头整体测量值偏移的问题。
                Vgs = tmp['VgsHigh'] #  正向驱动电压
                G_T, G_Vge, G_Vce, G_Ic, G_Vf, G_If, is_accurate = def_wave.ExtractWaveData(Data, tmp, UIInfoDict)
                G_Vge, G_Vce, G_Ic, G_Vf, G_If = def_wave.IsFilter(IsFilterFlag, G_Vge, G_Vce, G_Ic, G_Vf, G_If, UIInfoDict)
                sampling_rate = UIInfoDict['sampling_rate']
                DynamicData =def_wave.GetDynamicData(ModuleType, VgsR, Vgs, sampling_rate)
                ToBeWrite = [tmp['FolderInfo']] + DynamicData + [tmp['CsvFilePath']+ '/' + csv_tmp]
                ToBeWriteList.append(ToBeWrite)
                def_csv.FileWrite(FileOut, DynamicData, tmp, csv_tmp)
                #print('Completed：', tmp['FolderInfo'], csv_tmp)
                #self.textBrowser_003_main_printf.append('Progress:' + str(flag) + '/' + str(csv_num))
                print('Completed!  Progress:' + str(flag) + '/' + str(csv_num))
                flag += 1
                print()
        def_csv.TransposedDataListWrite(ToBeWriteList, FileOut)

        #print("全部文件处理完成")
        #self.stop_program()
        #print('程序运行结束')
        self.is_program_running = False
        # 更改按钮状态
        self.PushButton_001_Start.setEnabled(True)
        self.PushButton_002_Stop.setEnabled(False)
        #self.textBrowser_003_main_printf.append('All file processing completed')
        print('All file processing completed')

if __name__ == "__main__":
    UIInfoDict = {'HS_Vgs_act_Channel':1, 'HS_Vds_act_Channel':2, 'HS_Ids_act_Channel':0, 'HS_Idiode_pas_Channel':3, 
                  'HS_Vgs_pas_Channel':4, 'HS_Vds_pas_Channel':5, 'HS_IL_Channel':6, 
                  'LS_Vgs_act_Channel':1, 'LS_Vds_act_Channel':2, 'LS_Ids_act_Channel':3, 'LS_Idiode_pas_Channel':0, 
                  'LS_Vgs_pas_Channel':4, 'LS_Vds_pas_Channel':5, 'LS_IL_Channel':6, 
                  'HS_Vgs_act_Reverse':1, 'HS_Vds_act_Reverse':1, 'HS_Ids_act_Reverse':1, 'HS_Idiode_pas_Reverse':1, 
                  'HS_Vgs_pas_Reverse':1, 'HS_Vds_pas_Reverse':1, 'HS_IL_Reverse':1, # 未翻转使用1表示，翻转用-1表示，后期直接乘，避免if判断
                  'LS_Vgs_act_Reverse':1, 'LS_Vds_act_Reverse':1, 'LS_Ids_act_Reverse':1, 'LS_Idiode_pas_Reverse':1, 
                  'LS_Vgs_pas_Reverse':1, 'LS_Vds_pas_Reverse':1, 'LS_IL_Reverse':1, 
                  'HS_Vgs_positive_voltage':18, 'HS_Vgs_negative_voltage':-1, 
                  'LS_Vgs_positive_voltage':18, 'LS_Vgs_negative_voltage':-1, 
                  'Is_low_pass_filter':0, 'sampling_rate':6.25e9, 'cutoff_frequency':400e6,
                  'input_folder_path':'NoPath', 'output_file_path':'NoPath'} # 初始化UI界面获取的信息
    
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    # 打包命令 pyinstaller -D main.py
    # 如果有问题，使用pip install --upgrade pyinstaller 升级封装工具