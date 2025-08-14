import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.image import Image

# Load the kv file
Builder.load_file('kv/gallery_screen.kv')

class GalleryScreen(Screen):
    
    def on_enter(self):
        '''
        This method is called every time the screen is displayed.
        It will load all the images from our data/photos directory.
        '''
        self.load_photos()

    def load_photos(self):
        '''
        Clears the grid and populates it with images from the directory.
        '''
        image_grid = self.ids.image_grid
        image_grid.clear_widgets() # Clear old images to avoid duplicates
        
        # Get the path to the photos directory
        photos_path = "data/photos"
        if not os.path.exists(photos_path):
            os.makedirs(photos_path)

        # Get a list of all files in the directory
        photo_files = [f for f in os.listdir(photos_path) if f.endswith('.png')]
        
        # Sort files by creation time to show newest first
        photo_files.sort(key=lambda f: os.path.getctime(os.path.join(photos_path, f)), reverse=True)

        for filename in photo_files:
            file_path = os.path.join(photos_path, filename)
            # Create an Image widget and add it to the grid
            image = Image(source=file_path, fit_mode='cover')
            image_grid.add_widget(image)
