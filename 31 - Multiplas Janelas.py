from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty


#Define our different screens
class FirstWindow(Screen):
	pass

class SecondWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass

# Designate Our .kv design file
kv = Builder.load_file('kvs/new_windows.kv')

class AwesomeApp(App):
	r = 'right'

	def build(self):
		return kv

if __name__ == '__main__':
	AwesomeApp().run()