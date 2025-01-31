# DO NOT EDIT THIS FILE
from PIL import Image
import numpy as np

def ListToImage(img_list):
    '''Converts a 2D list to an image.'''
    img_arr = np.uint8(np.asarray(img_list))
    img = Image.fromarray(img_arr)
    return img

def ImageToList(img):
    '''Converts an image to a 2D list.'''
    img_arr = np.uint8(np.asarray(img))
    pixels = img_arr.tolist()
    for row in range(len(pixels)):
        for col in range(len(pixels[row])):
            pixels[row][col] = (pixels[row][col][0], pixels[row][col][1], pixels[row][col][2])
    return pixels

