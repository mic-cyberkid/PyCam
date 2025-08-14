import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class PyCamApp(App):
    def build(self):
        sm = ScreenManager()
        # Add your screens here
        return sm

if __name__ == '__main__':
    PyCamApp().run()
