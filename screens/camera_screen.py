import os
import time

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# Load the kv file for the screen
Builder.load_file('kv/camera_screen.kv')

class CameraScreen(Screen):

    def capture_photo(self):
        '''
        This method is called when the "Capture" button is pressed.
        It saves the current frame from the camera to a file.
        '''
        # Get the Camera widget by its ID
        camera = self.ids.camera
        
        # Check if the camera is playing before trying to capture
        if camera.play:
            # Create a unique filename based on the current timestamp
            timestr = time.strftime("%Y%m%d_%H%M%S")
            filename = f"IMG_{timestr}.png"
            
            # Use the camera's export_to_png method to save the image
            camera.export_to_png(os.path.join("data/photos", filename))
            print(f"Captured: {filename}")
