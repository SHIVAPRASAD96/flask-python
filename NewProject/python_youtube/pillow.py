from PIL import Image

img = Image.open("IMG_0169.JPG");
#print(img.size)
#print(img.format)
area= (100,100,300,375)

croped_img = img.crop(area);

img.show()