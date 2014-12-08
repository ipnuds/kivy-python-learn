import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.uix.scatter import ScatterPlane
from kivy.uix.image import Image 
from PIL import Image
import os
from os.path import join
# open text file if exist or make a new file if not exist
fo=open("imgList.txt","w")
# list files inside directory
imdir="Project\\Latihan\\Desain\\menu utama"
for filename in os.listdir(imdir):
    # write filename in textfile separated by \n
    fo.write(filename+"\n")
# close the text file
fo.close()

with open("imgList.txt") as f:
	# read text file line by line
	content=f.readlines()
	# print the filename by index
	print content


class TutorialApp (App):
	def build(self):
		ikon=content[3]
		s = ScatterPlane(scale=.5)
		filename=join(imdir, 'background.png')
		print filename[:-1]
		filename2=join(imdir,content[1][:-1])	
		print filename2
		im=Image(source=filename2,size=(1920,1090))
		img=Image.open(filename2)
		exif_data=img._getexif();
		s.add_widget(im)
		return s


if __name__=="__main__":
	TutorialApp().run()