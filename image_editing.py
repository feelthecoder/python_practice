# Image Editing using Pillow Library Python

from PIL import Image,ImageEnhance,ImageFilter
import os

#changing extension tp jpeg,pdf,gif,etc

img1= Image.open(r'text1.jpg')
img1.save('text1.jpeg')
img1.save('text1.pdf')
img1.save('text1.jpg')
img1.save('text1.gif')
img1.show() #Show Image

#RESIZE IMAGE

MAX_SIZE = (100,100)
img1.thumbnail(MAX_SIZE)
img1.save('smalltext.jpg')

#WORKING WITH MULTIPLE IMAGES

for item in  os.listdir(r'IBM Hack Text Extraction'):
   if item.endswith('.png'):
        img1=Image.open(r'IBM Hack Text Extraction\\'+item)
        img1.thumbnail(MAX_SIZE)
        img1.save(f"x.jpeg")

#IMAGE ENHANCEMENT


#SHARPNESS

enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(0).save('en0.png') #blur
enhancer.enhance(1).save('en1.png') #Normal Image
enhancer.enhance(2).save('en2.png')
enhancer.enhance(4).save('en4.png')
enhancer.enhance(6).save('en6.png')


#COLOR

enhancer = ImageEnhance.Color(img1)
enhancer.enhance(0).save('color0.png') #black & white
enhancer.enhance(1).save('color1.png') #Normal Image
enhancer.enhance(2).save('color2.png')
enhancer.enhance(3).save('color3.png')
enhancer.enhance(4).save('color4.png')

#BRIGHTNESS

enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(0).save('br0.png') #black 
enhancer.enhance(1).save('br1.png') #Normal Image
enhancer.enhance(2).save('br2.png')  
enhancer.enhance(3).save('br3.png')
enhancer.enhance(4).save('br4.png')


#CONTRAST

enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(0).save('cr0.png') 
enhancer.enhance(1).save('cr1.png') 
enhancer.enhance(2).save('cr2.png')  
enhancer.enhance(3).save('cr3.png')
enhancer.enhance(4).save('cr4.png')



#IMAGE BLUR


img1.filter(ImageFilter.GaussianBlur(radius=2)).save('gauss.png')


