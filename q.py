
import json
from kivy.app import App
import webbrowser 
from kivy.network.urlrequest import UrlRequest
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import subprocess
import requests
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics import Color
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton

count=7	
dcount=7
scount=7
class MainAppScreen(Screen):
	pass


class Mood(Screen):
	pass
class one(Screen):
	def onn_state1(self):
		global count
		count=count-1
	pass
class two(Screen):
	def onn_state2(self):
		global count
		count=count-1
	pass
class three(Screen):
	def onn_state3(self):
		global count
		count=count-1
	pass	
class four(Screen):
	def onn_state4(self):
		global count
		count=count-1
	pass	
class five(Screen):
	def onn_state5(self):
		global count
		count=count-1
	pass	
class six(Screen):
	def onn_state6(self):
		global count
		count=count-1
	pass	
class seven(Screen):
	def onn_state7(self):
		global count
		count=count-1
	pass	

class dresult(Screen):
	def resultt(self):
		global dcount
		if(dcount<3):
			result=Popup(title="RESULT",content=Label(text="Your score is " + str(dcount) + "/7."+"\nYou are not at all dperessed \nand are living a pleasant life"),size_hint =(0.8,0.8))
            		
            	elif(dcount>3 and dcount<5):
			result=Popup(title="RESULT",content=Label(text="Your score is " + str(dcount)+"/7."+"\nYou have an average level of \ndepression but can take efforts to come out of it "),size_hint =(0.8,0.8))
            		
            	else:
			result=Popup(title="RESULT",content=Label(text="Your score is " + str(dcount)+"/7."+"\nYou are extremely depressed and\n need to consult a doctor"),size_hint =(0.8,0.8))
            	result.open()

class mresult(Screen):
	def resultt(self):
		global count
		if(count<=3):
			result=Popup(title="RESULT",content=Label(text="Your score is " + str(count)+"/7."+"\nYou have a very good mood \nand happy life"),size_hint =(0.8,0.8),font_size='20sp')
            		
            	elif(count>3 and count<=5):
			result=Popup(title="RESULT",content=Label(text="Your score is " + str(count)+"/7."+"\nYou are at an average mood but also \ncan improve it by involving yourself in hobbies "),size_hint =(0.8,0.8))
            		
            	else:
            		result=Popup(title="RESULT",content=Label(text="Your score is " + str(count)+"/7."+"\nYou seem to be very upset\n and need to spend time with your \nbeloved ones to be in a good state of mind"),size_hint =(0.8,0.8),font_size='50sp')
            	result.open()

class sresult(Screen):
	def resultt(self):
		global scount
		if(scount<=3):
			result=Popup(title="RESULT",content=Label(text="Your score is " + str(scount)+"/7."+"\nYou have a good sleep and \n are not insomniac"),size_hint =(0.8,0.8))
            		
            	elif(scount>3 and scount<=5):
			result=Popup(title="RESULT",content=Label(text="Your score is " + str(scount)+"/7."+"\nYou have an average level of sleep\n but you can improve it by reducing \n the level of stress in your life "),size_hint =(0.8,0.8))
            		
            	else:
			result=Popup(title="RESULT",content=Label(text="Your score is " + str(scount)+"/7."+"\nYou are highly insomniac and you \nneed to take actions to improve your sleep"),size_hint =(0.8,0.8))
            	result.open()

class Depression(Screen):

	pass
class done(Screen):
	def onn_state8(self):
		global dcount
		dcount=dcount-1
	pass
class dtwo(Screen):
	def onn_state9(self):
		global dcount
		dcount=dcount-1
	pass
class dthree(Screen):
	def onn_state10(self):
		global dcount
		dcount=dcount-1
	pass	
class dfour(Screen):
	def onn_state11(self):
		global dcount
		dcount=dcount-1
	pass	
class dfive(Screen):
	def onn_state12(self):
		global dcount
		dcount=dcount-1
	pass	
class dsix(Screen):
	def onn_state13(self):
		global dcount
		dcount=dcount-1
	pass	
class dseven(Screen):
	def onn_state14(self):
		global dcount
		dcount=dcount-1
	pass	

class Sleep(Screen):
	pass

class sone(Screen):
	def onn_state15(self):
		global scount
		scount=scount-1
	pass
class stwo(Screen):
	def onn_state16(self):
		global scount
		scount=scount-1
	pass
class sthree(Screen):
	def onn_state17(self):
		global scount
		scount=scount-1
	pass	
class sfour(Screen):
	def onn_state18(self):
		global scount
		scount=scount-1
	pass	
class sfive(Screen):
	def onn_state19(self):
		global scount
		scount=scount-1
	pass	
class ssix(Screen):
	def onn_state20(self):
		global scount
		scount=scount-1
	pass	
class sseven(Screen):
	def onn_state21(self):
		global scount
		scount=scount-1
	pass	

class MentalApp(App):
	pass	

if __name__=='__main__':
	MentalApp().run()



