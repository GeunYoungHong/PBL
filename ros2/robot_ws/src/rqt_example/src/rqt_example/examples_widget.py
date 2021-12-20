# -*- coding: utf-8 -*-

import os
import sys

from ament_index_python.resources import get_resource
from std_msgs.msg import String
from python_qt_binding import loadUi
from python_qt_binding.QtCore import Qt
from python_qt_binding.QtCore import QTimer, QCoreApplication
from python_qt_binding.QtGui import QKeySequence
from python_qt_binding.QtWidgets import QShortcut, QLabel, QTextEdit
from python_qt_binding.QtWidgets import QWidget, QApplication, QRadioButton

import numpy as np
import rclpy

from rclpy.qos import QoSProfile

import speech_recognition as sr

class ExamplesWidget(QWidget):

    def __init__(self, node):
        super(ExamplesWidget, self).__init__()
        self.setObjectName('CHoi')

        self.transcript = ''
        self.lang = 0

        self.axis = ''
        self.num = 0
        self.mode = 0

        self.node = node

        self.REDRAW_INTERVAL = 30
        self.PUBLISH_INTERVAL = 100

        pkg_name = 'rqt_example'
        ui_filename = 'rqt_example.ui'

        topic_name = 'Voice'

        _, package_path = get_resource('packages', pkg_name)

        ui_file = os.path.join(package_path, 'share', pkg_name, 'resource', ui_filename)
        loadUi(ui_file, self)

        qos = QoSProfile(depth=10)
        self.publisher = self.node.create_publisher(String, topic_name, qos)

        self.timer = QTimer(self)
        #self.timer.timeout.connect(self.send_voice)
        self.timer.start(self.PUBLISH_INTERVAL)

        self.push_button_start.pressed.connect(self.voice_recognition)
        self.push_button_comm.pressed.connect(self.send_voice)
        self.push_button_exit.pressed.connect(QCoreApplication.instance().quit)

        self.push_button_start.setStyleSheet('Color:white; background:rgb(0,0,51)')
        self.push_button_comm.setStyleSheet('Color:white; background:rgb(0,0,51)')
        self.push_button_exit.setStyleSheet('Color:white; background:rgb(0,0,51)')

        self.radioButton_kor.clicked.connect(self.select_lang)
        self.radioButton_eng.clicked.connect(self.select_lang)

        self.label.setStyleSheet('Color:white; background:rgb(150,150,150)')
        self.label.setAlignment(Qt.AlignCenter)

    def voice_recognition(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Start Speech Recognition")
            audio = r.listen(source)

            if self.lang == 1 :
                self.transcript = r.recognize_google(audio, language="ko-KR")
                self.label.setText(self.transcript)

            if self.lang == 2 :
                self.transcript = r.recognize_google(audio, language="en-US")
                self.label.setText(self.transcript)

            if self.transcript == 'ready':
                self.mode = 0

            else:
                self.mode = 1
                self.axis = self.transcript[0:1]
                self.num = self.transcript[6:7]

    def send_voice(self):
        result = String()
        
        if self.mode == 0 :
            result.data = '{0}'.format(self.transcript)

        if self.mode == 1 :
            result.data = '{0}'.format(self.axis) + ' ' +'{0}'.format(self.num)

        self.publisher.publish(result)
        self.node.get_logger().info('{0}'.format(self.transcript))

    def select_lang(self):
        if self.radioButton_kor.isChecked() :
            self.lang = 1
        elif self.radioButton_eng.isChecked() :
            self.lang = 2

    def shutdown_widget(self):
        self.node.destroy_publisher(self.publisher)
