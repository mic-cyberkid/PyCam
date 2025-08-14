[app]

# (str) Title of your application
title = PyCam

# (str) Package name
package.name = pycam

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test.pycam

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,spec

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 0.1

# (list) Requirements (usually 'python3,kivy' with addition of your custom modules)
# This includes `pillow` which we needed for the gallery.
requirements = python3,kivy,pillow

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
# A recent stable version is recommended.
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android build tools version to use (fixes the Aidl error)
android.build_tools_version = 30.0.3

# (list) Android architectures to build for
android.archs = arm64-v8a,armeabi-v7a

# (bool) If True, then automatically accept SDK license agreements.
android.accept_sdk_license = True

# (bool) If True, an ABIsplit file will be created.
android.abisplit = False

# (str) The name of the Java entry point class.
android.entrypoint = org.kivy.android.PythonActivity

# (list) Permissions
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) The path to a custom AndroidManifest.xml
#android.manifest.tmpl = %(source.dir)s/AndroidManifest.tmpl.xml

# (bool) To compile a release version of the app.
# The user needs to manually sign this APK with a keystore.
android.release = False

# (str) A path to your keystore file
#android.keystore = %(source.dir)s/debug.keystore

# (str) The alias of the keystore key
#android.keystore.alias = androiddebugkey

# (str) A path to a custom icon
#icon.filename = %(source.dir)s/data/icon.png

# (str) A path to a custom presplash
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) A path to a custom presplash background color
#presplash.color = #FFFFFF

[buildozer]
# (str) The directory where the Buildozer environment will be stored.
buildozer.dir = ./.buildozer
