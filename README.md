# Fujifilm Tools

## About the Project
I'm a hobbyist photographer using the Fujifilm system, and I'm currently developing software tools to improve my photography workflow from shooting to printing. I became interested in tracking the camera and recipe settings I use for photos and in organizing my images in a more automated manner.

More specifically, these tools extract and display Fujifilm image metadata describing the image's file properties, camera capture/shooting settings, and Fujifilm recipe settings (if applicable). The image's path is entered in the ```fujifilm_metadata.py``` script (line 19), and the relevant metadata is taken and displayed in a PyQt5 window. By obtaining this data, I can check:
- the camera settings I used, such as the ISO, f-stop, and shutter speed
- what Fujifilm film recipe I used for that image
- if an image has been edited
- if an image is ready for print or web upload

These scripts work for both JPEG and RAF (Fujifilm RAWs) files.

### What is a Fujifilm Film Recipe?
A Fujifilm film recipe consists of Fuji camera settings one can tweak to simulate the look of 35mm films, such as those produced by Fujifilm and Kodak. Some of the websites I like to get recipes from are:
- [Fuji X Weekly](https://fujixweekly.com/)
- [film.recipes](https://film.recipes/)

## Software dependencies
- [ExifTool](https://exiftool.org/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [PyQt5](https://pypi.org/project/PyQt5/)

## Roadmap
- [x] Get relevant metadata from Fujifilm Images 
- [ ] Set up database with Fujifilm recipes I've used
- [ ] Write function/s to identify Fujifilm recipe used in JPEG/RAF based on recipe database
- [ ] Write scripts to check if folders are ready for printing or web upload
- [ ] Write scripts for organizing images (still thinking about how I want to approach organization)
- [ ] General GUI improvements

## Contact
Andie Buenconsejo  
Email: al.buenco@gmail.com  
[Project Link](https://github.com/abuenco/FujifilmTools)

