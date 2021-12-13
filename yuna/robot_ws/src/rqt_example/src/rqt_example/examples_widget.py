#!/usr/bin/env python3

import os
import sys

from ament_index_python.resources import get_resource
from std_msgs.msg import String
from python_qt_binding import loadUi
from python_qt_binding.QtCore import Qt
from python_qt_binding.QtCore import QTimer, QCoreApplication
from python_qt_binding.QtGui import QKeySequence, QPixmap
from python_qt_binding.QtWidgets import QShortcut, QLabel, QTextEdit
from python_qt_binding.QtWidgets import QWidget, QApplication

import numpy as np
import rclpy

from rclpy.qos import QoSProfile

import speech_recognition as sr

class ExamplesWidget(QWidget):

    def __init__(self, node):
        super(ExamplesWidget, self).__init__()
        self.setObjectName('CHoi')

        self.transcript = ''

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

        self.label.setStyleSheet('Color:white; background:rgb(150,150,150)')
        self.label.setAlignment(Qt.AlignCenter)

    def voice_recognition(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
               print("Start Speech Recognition")
               audio = r.listen(source, timeout = )

               self.transcript = r.recognize_google(audio, language="en-US")
               self.label.setText(self.transcript)

    def send_voice(self):
        msg = String()
        msg.data = '{0}'.format(self.transcript)
        self.publisher.publish(msg)
        self.node.get_logger().info('{0}'.format(msg.data))

    def shutdown_widget(self):
        self.node.destroy_publisher(self.publisher)
