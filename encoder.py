from PIL import Image,ImageFont,ImageDraw
from random import getrandbits as randBits
from random import randint
from sys import argv
from os.path import expanduser
text = "The proof is in the pudding"
#Check if the user has specified text
try:
	text=argv[1]
except IndexError:
	pass
font = ImageFont.truetype("courier.ttf",24)
size = ImageDraw.Draw(Image.new("RGB",(0,0))).textsize(text,font)
img = Image.new("RGB",(size[0]+300,size[1]+300))
draw = ImageDraw.Draw(img)
#Make the whole image white
draw.rectangle([(0,0),(img.size[0],img.size[1])],fill=(255,255,255))
#Draw some text in a very light blue
draw.text(((img.size[0]-size[0])/2,(img.size[1]-size[1])/2),text,(182,255,255),font=font)
p = img.load()
for i in range(img.size[0]*img.size[1]):
	if bool(randBits(1)):
		#Make random pixels red
		p[randint(0,img.size[0]-1),randint(0,img.size[1]-1)] = (255,0,0)
path = expanduser("~")+"/Desktop/out.bmp"
img.save(path,format="BMP")
print "Saved to",path