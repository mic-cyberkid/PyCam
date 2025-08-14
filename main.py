import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.camera_screen import CameraScreen
# Import the gallery screen later
from screens.gallery_screen import GalleryScreen

class PyCamApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CameraScreen(name='camera_screen'))
        # sm.add_widget(GalleryScreen(name='gallery_screen'))
        return sm

if __name__ == '__main__':
    PyCamApp().run()
