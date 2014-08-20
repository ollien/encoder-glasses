from sys import argv
from PIL import Image
from os.path import expanduser
image = None
#Check if the user has specified a file
try:
	image = Image.open(argv[1])
except IndexError:
	image = Image.open(expanduser("~")+"/Desktop/out.bmp")
pixels = image.load()
for i in range(image.size[0]):
	for j in range(image.size[1]):
		pixel = pixels[i,j]
		#If the pixel is red set it to black
		if pixel == (255,0,0):
			pixels[i,j] = (0,0,0)
		#If the pixel is white set it to black
		elif pixel == (255,255,255):
			pixels[i,j] = (0,0,0)
path = expanduser("~")+"/Desktop/decoded.bmp"
image.save(path,format="BMP")
print "Saved to",path

