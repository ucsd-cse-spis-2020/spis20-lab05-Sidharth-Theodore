#import lab05Warmup_Theodore
#import lab05Warmup_Sidharth
from PIL import Image

bear = Image.open("bear.png")

def grayscale(im):
    ''' Invert the colors in the input image, im '''

    # Find the dimensions of the image

    (width, height) = im.size

    # Loop over the entire image

    for x in range(width):

        for y in range(height):
            (red, green, blue) = im.getpixel((x, y))
            luminance = int(red*.21) + int(green*.72) + int(blue*.07)
            im.putpixel((x, y), (luminance,luminance,luminance))

def binarize(im, thresh, startx, starty, endx, endy):
    ''' Invert the colors in the input image, im '''

    # Find the dimensions of the image
    
    (width, height) = im.size
    if startx not in range(width):
        print(f'x value of {startx}, not in {width}')
        return
    if endx not in range(width):
        print(f'x value of {endx}, not in {width}')
        return
    if starty not in range(height):
        print(f'y value of {starty}, not in,{height}')
        return
    if endy not in range(height):
        print(f'y value of {endy}, not in,{height}')
        return

    # Loop over the entire image
    #startx,starty = 0,0
    #(endx,endy) = im.size


    for x in range(startx,endx):

        for y in range(starty,endy):
            (red, green, blue) = im.getpixel((x, y))
            luminance = int(red*.21) + int(green*.72) + int(blue*.07)
            if luminance <= thresh:
                im.putpixel((x, y), (0,0,0))
                #print("pixel: black")
            else:
                im.putpixel((x, y), (255,255,255))
                #print("pixel: white")
    


def mirrorVert(im):
    (width, height) = im.size
    for x in range(width):
        for y in range(height//2):
            im.putpixel((x,y*-1), im.getpixel((x,y)))


def mirrorHoriz(im):
    width,height = im.size
    width//=2

    for x in range(width):
        for y in range(height):
            (r,g,b) = im.getpixel((x,y))
            im.putpixel(((-1*x),y),(r,g,b))


def flipVert(im):
    width,height = im.size
    #flipping top half
    for x in range(width):
        for y in range(height//2):
            #store inverse pixel
            pixel = im.getpixel((x,y*-1))
            #flip (x,y) onto inverse
            im.putpixel((x,y*-1), im.getpixel((x,y)))
            #put inverse in original (x,y)
            im.putpixel((x,y), pixel)


flipVert(bear)
bear.save("tmp_Name.png")