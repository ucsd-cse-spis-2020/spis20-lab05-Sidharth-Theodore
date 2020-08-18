from PIL import Image

bear = Image.open( "bear.png" )

def invert(im):

    (width, height) = im.size
    for x in range(width):
        for y in range(height):
            (red, green, blue) = im.getpixel((x, y))
            (redN,greenN,blueN) = (255-red,255-green,255-blue)
            im.putpixel((x,y),(redN,greenN,blueN))
           
def invert_block( im ):
    (width, height) = im.size

    for x in range(int(width/2),width):
        for y in range(0,int(height/2)):
            (red, green, blue) = im.getpixel((x, y))
            (redN, greenN, blueN) = (255 - red, 255 - green, 255 - blue)
            im.putpixel((x, y), (redN, greenN, blueN))
           
invert_block(bear)


#bear.show()
bear.save("tmp_Sid.png")