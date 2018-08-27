#Asn6.py: Image processing

#If you use .jpeg images, change this to import pilimages130 as images
import images
import random
#import pilimages130 as images

def draw_lines(pic):
    '''Write code below to draw a green vertical line from top to bottom,
       1/3 of the way across a copy of edinburgh-castle.gif; also draw a
       horizontal blue line 1/3 of the way down the same image. Return
       the copy'''
    pic2 = pic.clone()  #Make a copy of pic
    y_third = int(pic2.getHeight()/3)
    x_third = int(pic2.getWidth()/3)
    #Draw your green and blue lines on pic2
    #vertical green line
    green = (0, 255, 0)
    for y in range(0, pic2.getHeight()):
        pic2.setPixel(x_third, y, green)
    #horizontal blue line
    blue = (0, 0 , 255)
    for x in range(0, pic2.getWidth()):
        pic2.setPixel(x, y_third, blue)
            
    return pic2

def border(pic):
    '''Write code below to draw a black border 10 pixels wide around
       arch.gif; this amounts to drawing 10 black lines across the
       top and bottom and 10 vertical black lines on the left and
       right sides. For full credit, draw the lines using loops and draw
       the lines pixel by pixel.'''
    pic2 = pic.clone()  #Make a copy of pic
    #Draw the border on pic2
    black = (0, 0, 0)
    
    for y in range(0, 11): #top border
        for x in range(0, pic2.getWidth()):
            pic2.setPixel(x, y, black)
    for y in range(pic2.getHeight()-10, pic2.getHeight()): #bottom border
        for x in range(0, pic2.getWidth()):
            pic2.setPixel(x, y, black)
            
    for x in range(0, 11): #left border
        for y in range(0, pic2.getHeight()):
            pic2.setPixel(x, y, black)
    for x in range(pic2.getWidth()-10, pic2.getWidth()): #right border
        for y in range(0, pic2.getHeight()):
            pic2.setPixel(x, y, black)
            
    return pic2

def blend(pic1, pic2):
    '''Write code below to blend .6 of pic1 with .4 of pic2; assume
       pic1 and pic2 are the same size'''
    #new_image = pilimages.Image(pic1.getWidth(), pic1.getHeight())
    new_image = images.Image(pic1.getWidth(), pic1.getHeight())
    for y in range(0, new_image.getHeight()):
        for x in range(0, new_image.getWidth()):
            r1, g1, b1 = pic1.getPixel(x, y)
            r2, g2, b2 = pic2.getPixel(x, y)
            r = int((.6*r1) + (.4*r2))
            g = int((.6*g1) + (.4*g2))
            b = int((.6*b1) + (.4*b2))
            #print(r, g, b)
            new_image.setPixel(x, y, (r, g, b))
    
    #for y in range of the height of new_img
    #    for x in the range of the width of new_image
    #        get a pixel from the x, y position of pic1
    #        get a pixel from the x, y position of pic2
    #        set r to 0.6 * red from pic1 pixel + 0.4 * red from pic2 pixel
    #        create g & b using the same method as for r
    #        set the pixel in the x, y position in new_img to the (r, g, b)
    
    return new_image

def fuzz(pic, region_size):
    '''OPTIONAL Extra challenge: Write code below to blur an image by
       randomly swapping pixels within a region around the x, y position.
       For example, if region size is 10, x is 50, and y is 65, you'll
       swap the pixel at (50, 65) with another pixel randomly chosen
       from (40, 60) to (55, 75). Watch out for edge conditions - if
       the x position is < 0 or > height-1, choose a different random
       x position.'''
    #Add import random after import pilimages above
    target = pic.clone()
    w = target.getWidth()
    h = target.getHeight()
    for y in range(h):
        for x in range(w):
            r, g, b = target.getPixel(x, y)
            swap_y = random.randint(y-region_size, y+region_size)
            while swap_y < 0 or swap_y > (h-1):
                swap_y = random.randint(y-region_size, y+region_size)
            swap_x = random.randint(x-region_size, x+region_size)
            while swap_x < 0 or swap_x > (w-1):
                swap_x = random.randint(x-region_size, x+region_size)
            red, green, blue = target.getPixel(swap_x, swap_y)
            target.setPixel(x, y, (red, green, blue))
            target.setPixel(swap_x, swap_y, (r, g, b))
                
    return target
    
def main():
    #img1 = images.Image('images//edinburgh-castle.gif')
    img1 = images.Image('images//edinburgh-castle.jpg')
    new_img1 = draw_lines(img1)
    new_img1.draw()
    
    #img2 = images.Image('images//arch.gif')
    img2 = images.Image('images//arch.jpg')
    new_img2 = border(img2)
    new_img2.draw()
    
    #img3 = images.Image('images//beach.gif')
    img3 = images.Image('images//beach.jpg')
    #img4 = images.Image('images//blueMotorcycle.gif')
    img4 = images.Image('images//blueMotorcycle.jpg')
    img5 = blend(img3, img4)
    img5.draw()
    
    #Uncomment the following if you do the extra challenge
    region_size = 10  #fuzz pixels in a region this big
    #img6 = images.Image('images//arch.gif')
    img6 = images.Image('images//arch.jpg')
    img7 = fuzz(img6, region_size)
    img7.draw()
    
main()
