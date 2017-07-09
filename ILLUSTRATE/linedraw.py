# -*- coding: utf-8 -*- 
 
# ------------------------------------
# python modules
# ------------------------------------
from PIL import Image
import cv2
import numpy as np
#Visualization for jupyter
#from IPython.display import display, Image
import os
# ------------------------------------
# own python modules
# ------------------------------------
 
 
# ------------------------------------
# Main function
# ------------------------------------
def main(args):
    #read arguments
    print(args)
    src_dir = args.input_dir
    out_dir = args.out_dir
    # make thumbnail dir, 
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    linedraw_all(src_dir, out_dir)

# difine neiborhood8
neiborhood8 = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]],
                        np.uint8)

#Visualization for
#def display_cv_image(image, format='.jpg'):
#    decoded_bytes = cv2.imencode(format, image)[1].tobytes()
#    display(Image(data=decoded_bytes))    
def linedraw_all(src_dir, out_dir):
    files = []
    jpgs = []
    for x in os.listdir(src_dir):
        if os.path.isfile(src_dir + x):
            files.append(x)
    for y in files:
        # to get only jpg files
        if(y[-4:] == '.jpg'):
            # add list
            jpgs.append(y)
    for index, file_name in enumerate(jpgs):
        file_path = src_dir + '/' + file_name
        print(file_path)
        #number = index
        #number_padded = '{0:08d}'.format(number)
        #print(number_padded)
        #linedraw(file_path, out_dir, number_padded)
        linedraw(file_path, out_dir)

def linedraw(file_path, out_dir):
    img = cv2.imread(file_path, 0)
    gray_img = img
    #output for gray image
    #out_path = out_dir + str(number_padded) + "_" + os.path.splitext(os.path.basename(file_path))[0] + "_gray.jpg"
    out_path = out_dir + os.path.splitext(os.path.basename(file_path))[0] + "_gray.jpg"
    #save for gray image
    cv2.imwrite(out_path, gray_img)
    print("Gray!:{}".format(out_path))
    # dilate
    img_dilate = cv2.dilate(img, neiborhood8, iterations=1)
    # diff between original and dilatation
    img_diff = cv2.absdiff(img, img_dilate)
    # inverted
    img_diff_not = cv2.bitwise_not(img_diff)
    #output for line image
    #out_path = out_dir + str(number_padded) + "_" + os.path.splitext(os.path.basename(file_path))[0] + "_line.jpg"
    out_path = out_dir + os.path.splitext(os.path.basename(file_path))[0] + "_line.jpg"
    #save for line image
    cv2.imwrite(out_path, img_diff_not)
    print("Line!:{}".format(out_path))
