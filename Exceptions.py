import Locales


class NoVernamHackException(Exception):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['No hack methods for Vernam are available']


class NoVigenereHackException(Exception):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['No hack methods for Vigenere are available']


class HackIsNotCaesarException(Exception):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['Not Caesar is set for hacking']


class BadInputFileException(FileNotFoundError):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['Bad input file']


class BadOutputFileException(FileNotFoundError):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['Bad output file']


class BadKeyFileException(FileNotFoundError):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['Bad key file']


class BadImageFileException(FileNotFoundError):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['Bad image file']


class BadPictureFormatException(FileNotFoundError):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['Picture file should be .bpm or .png']


class BadInputPictFormatException(FileNotFoundError):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['Input file should be .png or .bpm if you are using steganography']


class BadOutputPictFormatException(FileNotFoundError):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['Output file should be .png or .bpm if you are using steganography']


class BadCryptMethodException(Exception):
    def __init__(self, method):
        self.method = method

    def __str__(self):
        return Locales.locales['No such crypt type: ' + self.method]


class NoKeyException(Exception):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['No key file']


class HackTriesNumberException(Exception):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['No hack tries number']


class SmallImageException(Exception):
    def __init__(self):
        return

    def __str__(self):
        return Locales.locales['The image is too small to put text into it']
