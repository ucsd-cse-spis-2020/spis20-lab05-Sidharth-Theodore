#import lab05Warmup_Theodore
#import lab05Warmup_Sidharth
from PIL import Image
import random
import numpy as np
import os

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


def scale(image):
    width,height = image.size
        
    im = Image.new('RGB', (width//2,height//2))
    
    for x in range(width//2):
        for y in range(height//2):
            im.putpixel((x,y),image.getpixel((2*x,2*y)))
    return im

def blur(image):
    width,height = image.size

    for x in range(width-3):
        for y in range(height-3):
            (r,g,b) = image.getpixel((x,y))
            (r1,g1,b1) = image.getpixel((x+1,y+1))
            (r2,g2,b2) = image.getpixel((x+2,y+2))
            (r3,g3,b3) = image.getpixel((x+3,y+3))

            (rn,gn,bn) = ((r+r1+r2+r3)//4,(g+g1+g2+g3)//4,(b+b1+b2+b3)//4)
            image.putpixel((x,y),(rn,gn,bn))

def randomGrid(image,numBlocks):
    width,height = image.size
    blocks = []
    i = 0
    jumpW = width//numBlocks
    jumpH = height//numBlocks
    im = Image.new('RGB', (width,height))
    for x in range(0,width,jumpW):
        for y in range(0,height,jumpH):
            #print(x,y)
            block = Image.new('RGB', (jumpW,jumpH))
            block = image.crop((x,y,x+jumpW,y+jumpH))

            
            blocks.append(block)
            #block.save("temp"+str(i)+".png")
            
            
            '''for subx in range(x,x+jumpW):
                for suby in range(y,y+jumpH):
                    block.putpixel((subx-x,suby-y),image.getpixel((subx,suby)))
            '''
            i += 1
    
    #print(blocks)
    random.shuffle(blocks)
    #print(blocks)

    #blockArray = np.asarray(blocks)


    #im = Image.fromarray(blockArray)
    for x in range(numBlocks):
        for y in range(numBlocks):
            im.paste(blocks[0],(x*jumpW,y*jumpH))
            del blocks[0]

    im.save("randomGrid.png")

def delTemp():
    for i in range (1500):
        if os.path.exists("temp"+str(i)+".png"):
            os.remove("temp"+str(i)+".png")
        else:
            break

randomGrid(bear,16)
bear.save("tmp_Name.png")

