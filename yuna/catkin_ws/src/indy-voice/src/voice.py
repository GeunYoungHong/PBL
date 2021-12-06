#!/usr/bin/env python3
 
import rospy
from std_msgs.msg import String

import speech_recognition as sr

r = sr.Recognizer()

def indy_voice():

	with sr.Microphone() as source:
		print("Start Speech Recognition")
		audio = r.listen(source)

		try :
			transcript = r.recognize_google(audio, language="ko-KR")
			print("Google Speech Recognition <<Command>> : " + transcript)

		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")

		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
			
		pub = rospy.Publisher('Voice',String,queue_size=10)
		rospy.init_node('indy_voice', anonymous = True)
		rate = rospy.Rate(10)	

		while not rospy.is_shutdown():
			rospy.loginfo(transcript)
			pub.publish(transcript)
			rate.sleep()

if __name__=='__main__':

	try:
		indy_voice()
	except rospy.ROSInterruptException:
		pass

