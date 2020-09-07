import imagehash
from time import time
from PIL import Image
from typing import List


def timestamp_now():
    return int(time())


# def compare_images(original_imag_hash: Image, comparison: Image):
#     """ Compare original image against many images to find similar images"""

#     og_image_hash = imagehash.average_hash(Image.open(original_image))
#     for 
#     other_hash = imagehash.average_hash(Image.open('test_matchish.jpeg'))
#     print(hash - otherhash)