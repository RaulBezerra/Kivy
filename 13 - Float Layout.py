from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button

# Designate Our .kv design file
Builder.load_file('kvs/float_layout.kv')

class MyLayout(Widget):

	pass

class AwesomeApp(App):

	def build(self):

		Window.clearcolor = (1,1,1,1)
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()