from time import time
from PIL import Image
import imagehash


def timestamp_now():
    return int(time())


hash = imagehash.average_hash(Image.open('test.jpg'))
otherhash = imagehash.average_hash(Image.open('test_matchish.jpeg'))

print(hash - otherhash)