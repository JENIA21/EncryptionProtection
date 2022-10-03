import random
import string

from scripts.decode import DecodeClass
from scripts.encode import EncodeClass
from scripts.prepare import PrepareClass
from scripts.translate import TranslateClass


class Main:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for _ in range(length))
        return rand_string

    prepare = PrepareClass(name='test.jpg')
    prepare.prepare()
    encode = EncodeClass(name='test.jpg', key=generate_random_string(8))
    encode.encode()
    translate = TranslateClass(name='test.jpg')
    translate.translate()
    decode = DecodeClass(name='test.jpg')
    decode.decode()
