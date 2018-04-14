import os
import sys
import argparse
from PIL import Image # From Pillow (pip install Pillow)

def resize_photos(dir, new_x, new_y, scale):
    if(not os.path.exists(dir)):
        # if not in full path format (/usrers/user/....)
        # check if path is in local format (folder is in current working directory)
        if(not os.path.exists(os.path.join(os.getcwd(), dir))):
            print(dir + " does not exist.")
            exit()
        else:
            # path is not a full path, but folder exists in current working directory
            # convert path to full path
            dir = os.path.join(os.getcwd(), dir)
            
    i = 1 # image counter for print statements
    for f in os.listdir(dir):
        if(not f.startswith('.') and '.' in f):
            # accepted image types. add more types if you need to support them!
            accepted_types = ["jpg", "png", "bmp"]
            if(f[-3:].lower() in accepted_types):
                # checks last 3 letters of file name to check file type (png, jpg, bmp...)
                # TODO: need to handle filetypes of more than 3 letters (for example, jpeg)
                path = os.path.join(dir, f)
                img = Image.open(path)

                if(scale > 0):
                    w, h = img.size
                    newIm = img.resize((w*scale, h*scale))
                else:
                    newIm = img.resize((new_x, new_y))

                newIm.save(path)
                print("Image #" + str(i) + " finsihed resizing: " + path)
                i=i+1
            else:
                print(f + " of type: " + f[-3:].lower() + " is not an accepted file type. Skipping.")
    print("ALL DONE :) Resized: " + str(i) + " photos")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "-directory", help="(String) Specify the folder path of images to resize")
    parser.add_argument("-s", "-size", help="(Integer) New pixel value of both width and height. To specify width and height seperately, use -x and -y.")
    parser.add_argument("-x", "-width", help="(Integer) New pixel value of width")
    parser.add_argument("-y", "-height", help="(Integer) New pixel value of height")
    parser.add_argument("-t", "-scale", help="(Integer) Scales pixel sizes.")

    args = parser.parse_args()

    if(not args.d or ((not args.s) and (not args.x and not args.y) and (not args.t))):
        print("You have error(s)...\n")
        if(not args.d):
            print("+ DIRECTORY value missing Please provide a path to the folder of images using the argument '-d'\n")
        if((not args.s) and (not args.x or not args.y) and (not args.t)):
            print("+ SIZE value(s) missing! Please provide a new pixel size. Do this by specifying -s (width and height) OR -x (width) and -y (height) values OR -t (scale) value")
        exit()

    x = 0
    y = 0
    scale = 0
    if(args.s):
        x = int(args.s)
        y = int(args.s)
    elif(args.x and args.y):
        x = int(args.x)
        y = int(args.y)
    elif(args.t):
        scale = int(args.t)

    print("Resizing all photos in: " + args.d + " to size: " + str(x)+"px,"+str(y)+"px")
    resize_photos(args.d, x, y, scale)
