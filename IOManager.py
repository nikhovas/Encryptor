import sys
import os
import numpy
from PIL import Image
import Exceptions


def get_right_bit(num):
    return num & 1


def set_right_bit(num, bit):
    if bit == 1:
        num |= 1
    else:
        num &= 0b11111110
    return num


def to_bit_array(num, bits):
    for i in range(bits):
        yield (num >> (bits - 1 - i)) & 1


class BMPFile:

    @staticmethod
    def open(src):
        input_arr = []
        f = open(src, 'rb')
        int_size = sys.getsizeof(len([])) * 8
        arr_size = 0
        f.read(74)

        for i in range(int_size):
            arr_size <<= 1
            arr_size |= (f.read(1)[0] & 1)

        meta_char = 0

        for i in range(arr_size * 8):
            meta_char <<= 1
            meta_char |= f.read(1)[0] & 1
            if (i + 1) % 8 == 0:
                input_arr.append(meta_char)
                meta_char = 0

        return input_arr

    @staticmethod
    def write(img, dest, res_arr):
        f1 = open(img, 'rb')
        f2 = open(dest, 'wb+')

        arr_size = len(res_arr)
        int_size = sys.getsizeof(len([])) * 8
        img_size = os.path.getsize(img)

        if img_size - (74 + int_size + arr_size) < 0:
            raise Exceptions.SmallImageException()

        f2.write(f1.read(74))
        f2.write(bytearray([set_right_bit(f1.read(1)[0], j) for j in to_bit_array(arr_size, int_size)]))
        f2.write(bytearray([set_right_bit(f1.read(1)[0], j) for i in res_arr for j in to_bit_array(i, 8)]))
        f2.write(f1.read())


class ArrayProection:
    arr = []
    width = 0
    height = 0
    colours = 0
    line_size = 0
    dim_2_matrix_size = 0

    def __init__(self, array):
        self.arr = array
        self.height = len(array)
        self.width = len(array[0])
        self.colours = len(array[0][0])
        self.line_size = self.width * self.colours

    def __setitem__(self, key, value):
        self.arr[key // self.line_size][(key % self.line_size) // self.colours][key % self.colours] = value

    def __getitem__(self, item):
        return self.arr[item // self.line_size][(item % self.line_size) // self.colours][item % self.colours]

    def __len__(self):
        return self.height * self.width * self.colours


class PNGFile:

    @staticmethod
    def open(src):
        input_arr = []
        f = Image.open(src)
        aaa = ArrayProection(numpy.array(f))

        int_size = sys.getsizeof(len([])) * 8
        arr_size = 0

        y = 0

        for i in range(int_size):
            arr_size <<= 1
            arr_size = set_right_bit(arr_size, get_right_bit(aaa[y]))
            y += 1
        meta_char = 0

        for i in range(arr_size * 8):
            meta_char <<= 1
            meta_char |= (aaa[y] & 1)
            if (i + 1) % 8 == 0:
                input_arr.append(meta_char)
                meta_char = 0
            y += 1

        return input_arr

    @staticmethod
    def write(img, dest, res_arr):
        f = Image.open(img)
        aaa = ArrayProection(numpy.array(f))

        int_size = sys.getsizeof(len([])) * 8
        arr_size = len(res_arr)

        y = 0
        for i in to_bit_array(arr_size, int_size):
            aaa[y] = set_right_bit(aaa[y], i)
            y += 1

        for i in res_arr:
            for j in to_bit_array(i, 8):
                aaa[y] = set_right_bit(aaa[y], j)
                y += 1
        f = Image.fromarray(aaa.arr)

        f.save(dest)


class IOManager:
    dest = ''
    img = ''
    useImg = False
    isEncode = True
    input_arr = []
    key_arr = []

    def __init__(self, args):
        self.isEncode = args.crypt == 'encode'
        self.dest = args.dest
        self.img = args.img
        self.useImg = args.useimg

        if self.useImg and not self.isEncode:
            if args.src.endswith('bmp'):
                self.input_arr = BMPFile.open(args.src)
            elif args.src.endswith('png'):
                self.input_arr = PNGFile.open(args.src)
            else:
                raise Exceptions.BadInputPictFormatException()
        else:
            self.input_arr = bytearray(open(args.src, 'rb').read())

        if args.key is not None:
            self.key_arr = bytearray(open(args.key, 'rb').read())
        elif args.key_raw is not None:
            self.key_arr = bytearray(args.key_raw, sys.stdin.encoding)

    def push(self, res_arr):
        if self.useImg and self.isEncode:
            if self.dest.endswith('bmp'):
                BMPFile.write(self.img, self.dest, res_arr)
            elif self.dest.endswith('png'):
                PNGFile.write(self.img, self.dest, res_arr)
            else:
                raise Exceptions.BadOutputPictFormatException()
        else:
            file = open(self.dest, 'wb+')
            file.write(bytearray(res_arr))
            file.close()

    def push_pack(self, res_arr):
        j = 1
        for i in res_arr:
            file = open(self.dest + ' ' + str(j), 'wb+')
            file.write(bytearray(i))
            file.close()
            j += 1
