# Face-Recognising-App-Lock

A test of mine, using [face_recognition](https://github.com/ageitgey/face_recognition), no gurantees it runs on anyone else's system and this is a slightly outdated version. 

It works by taking an image using the primary webcam when one of the listed applications is opened, if the face of the user is not recognised as being on the authorised list it will shut down the program and store the image taken of the person who tried to access it.
Detects opened programs every 0.5s, might not work this way in which case you'll have to remove the time.sleep() and cope with the performance loss

There are a million improvements to do and some I have done but not uploaded, if you want to use it or update it feel free.

TODO//
- config.json to store paths/apps etc
- Multiple apps not just one  (implemented but not on this version)
- Certain authorised users can access only certain apps (rn lets you access all of them if on authorised list)

Uploading it just as a backup.
