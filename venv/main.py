from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello, Akhona!')

if __name__ == '__main__':
    MyApp().run()

class Stock:
    def __init__(self):
        self.items = {}

   