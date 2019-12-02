import random
import math
import statistics as st
from PIL import Image,ImageDraw,ImageFilter


print("""\nExercises 1\n """)
"""****************************************************************************************"""
x=[3,1.5,4.5,6.75,2.25,5.75,2.25]
print (st.mean(x))
print (st.harmonic_mean(x))
print (st.median(x))
print (st.median_low(x))
print (st.median_high(x))
print (st.median_grouped(x))
print (st.mode(x))
print (st.pstdev(x))
print (st.pvariance(x))
print (st.stdev(x))
print (st.variance(x))
print()


print("""\nExercises 2\n """)
"""****************************************************************************************"""
print( random.random() )
print ( random.randrange(10) )
print ( random.choice(['Ali', 'Khalid', 'Hussam']) )
print ( random.sample(range(1000), 10) )
print ( random.choice('OrangeAcademy') )
items = [1,5,8,9,2,4]
random.shuffle(items)
print( items )
print ( random.randint(20, 30) )
print ( random.randrange(1000, 2111, 5) )
print ( random.uniform(10000, 11000))
print()


print("""\nExercises 3\n """)
"""****************************************************************************************"""
print(math.pi)
print(math.cos(math.radians(200)),math.sin(math.radians(30)),math.tan(math.radians(180)))
print(math.floor(10.8))
print(math.ceil(10.8))


print()
print("""\nExercises 4\n """)
"""****************************************************************************************"""

img1=Image.open("d9_img1.jpg")
print(img1.format,img1.size,img1.mode)
#img1.show()

img1_flip=img1.transpose(Image.FLIP_TOP_BOTTOM)
#img1_flip.show()

img1_gray=img1.convert('L')
#img1_gray.show()

img1_crop=img1.crop((0,0,50,50))
#img1_crop.show()

# =============================================================================
# d = ImageDraw.Draw(img1)
# d.line((0,0)+img1.size,fill=(255,255,255))
# d.line((0,img1.size[1],img1.size[0],0),fill=(255,255,255))
# d.text((img1.size[0]/2-img1.size[1]/2,img1.size[1]/2),"naaman",fill=(255,255,0))
# img1.show()
# # =============================================================================

# =============================================================================
# ​img1_draw = ImageDraw.Draw(img1)
# img1_draw.line((0,0)+img1.size,fill=(255,255,255))
# img1_draw.line((0,img1.size[1],img1.size[0],0),fill=(255,255,255))
# img1_draw.text((img1.size[0]/2-img1.size[0]/2,img1.size[1]/2+20),"naaman",fill=(255,255,0))
# img1.show()
# =============================================================================

img1_f1 = img1.filter(ImageFilter.EDGE_ENHANCE)
#img1_f1.show()

img1_f2 = img1.filter(ImageFilter.FIND_EDGES)
#img1_f2.show()

img1_f3 = img1.filter(ImageFilter.SMOOTH)
#img1_f3.show()

img1_f4 = img1.filter(ImageFilter.SHARPEN)
#img1_f4.show()

alpha=0.6
img2=Image.open("d9_img2.jpg").resize(img1.size)
Image.blend(img1,img2,alpha).save("img4.JPG".format(alpha))
img3=Image.open("img4.JPG")
#img3.show()

blur=img2.filter(ImageFilter.BLUR)
#blur.show()
size=(128,128)
img3.thumbnail(size)
#img3.show()

img1_rot=img1.rotate(90)
#img1_rot.show()

mask=Image.open("mask.jpg")
mask=mask.resize(img1.size)

Image.composite(img1,img2,mask).save("mask_new.jpg")
mask_new=Image.open("mask_new.jpg")
#mask_new.show()

