#!/bin/bash

mainfile=main.py

echo '[TESTING] Using raw key value'

key=fdsaf

echo '[TESTING] Group testing with text '

echo '[TESTING] make Caesar'
python3 $mainfile encode caesar tests/testsources/source.txt tests/testresults/1.encrypt --key_raw $key
python3 $mainfile decode caesar tests/testresults/1.encrypt tests/testresults/result1.txt --key_raw $key

echo '[TESTING] make Vernam'
python3 $mainfile encode vernam tests/testsources/source.txt tests/testresults/2.encrypt --key_raw $key
python3 $mainfile decode vernam tests/testresults/2.encrypt tests/testresults/result2.txt --key_raw $key

echo '[TESTING] make Vigenere'
python3 $mainfile encode vigenere tests/testsources/source.txt tests/testresults/3.encrypt --key_raw $key
python3 $mainfile decode vigenere tests/testresults/3.encrypt tests/testresults/result3.txt --key_raw $key



echo '[TESTING] Group testing with BMP'

echo '[TESTING] make Caesar'
python3 $mainfile encode caesar tests/testsources/source.txt tests/testresults/pict4.bmp --key_raw $key --useimg --img tests/testsources/pict.bmp
python3 $mainfile decode caesar tests/testresults/pict4.bmp tests/testresults/result4.txt --key_raw $key --useimg

echo '[TESTING] make Vernam'
python3 $mainfile encode vernam tests/testsources/source.txt tests/testresults/pict5.bmp --key_raw $key --useimg --img tests/testsources/pict.bmp
python3 $mainfile decode vernam tests/testresults/pict5.bmp tests/testresults/result5.txt --key_raw $key --useimg

echo '[TESTING] make Vigenere'
python3 $mainfile encode vigenere tests/testsources/source.txt tests/testresults/pict6.bmp --key_raw $key --useimg --img tests/testsources/pict.bmp
python3 $mainfile decode vigenere tests/testresults/pict6.bmp tests/testresults/result6.txt --key_raw $key --useimg



echo '[TESTING] Group testing with PNG'

echo '[TESTING] make Caesar'
python3 $mainfile encode caesar tests/testsources/source.txt tests/testresults/pict7.png --key_raw $key --useimg --img tests/testsources/pict.png
python3 $mainfile decode caesar tests/testresults/pict7.png tests/testresults/result7.txt --key_raw $key --useimg

echo '[TESTING] make Vernam'
python3 $mainfile encode vernam tests/testsources/source.txt tests/testresults/pict8.png --key_raw $key --useimg --img tests/testsources/pict.png
python3 $mainfile decode vernam tests/testresults/pict8.png tests/testresults/result8.txt --key_raw $key --useimg

echo '[TESTING] make Vigenere'
python3 $mainfile encode vigenere tests/testsources/source.txt tests/testresults/pict9.png --key_raw $key --useimg --img tests/testsources/pict.png
python3 $mainfile decode vigenere tests/testresults/pict9.png tests/testresults/result9.txt --key_raw $key --useimg







echo '[TESTING] Using file key value'

key=tests/testsources/key.txt

echo '[TESTING] Group testing with text '

echo '[TESTING] make Caesar'
python3 $mainfile encode caesar tests/testsources/source.txt tests/testresults/10.encrypt --key $key
python3 $mainfile decode caesar tests/testresults/10.encrypt tests/testresults/result10.txt --key $key

echo '[TESTING] make Vernam'
python3 $mainfile encode vernam tests/testsources/source.txt tests/testresults/11.encrypt --key $key
python3 $mainfile decode vernam tests/testresults/11.encrypt tests/testresults/result11.txt --key $key

echo '[TESTING] make Vigenere'
python3 $mainfile encode vigenere tests/testsources/source.txt tests/testresults/12.encrypt --key $key
python3 $mainfile decode vigenere tests/testresults/12.encrypt tests/testresults/result12.txt --key $key



echo '[TESTING] Group testing with BMP'

echo '[TESTING] make Caesar'
python3 $mainfile encode caesar tests/testsources/source.txt tests/testresults/pict13.bmp --key $key --useimg --img tests/testsources/pict.bmp
python3 $mainfile decode caesar tests/testresults/pict13.bmp tests/testresults/result13.txt --key $key --useimg

echo '[TESTING] make Vernam'
python3 $mainfile encode vernam tests/testsources/source.txt tests/testresults/pict14.bmp --key $key --useimg --img tests/testsources/pict.bmp
python3 $mainfile decode vernam tests/testresults/pict14.bmp tests/testresults/result14.txt --key $key --useimg

echo '[TESTING] make Vigenere'
python3 $mainfile encode vigenere tests/testsources/source.txt tests/testresults/pict15.bmp --key $key --useimg --img tests/testsources/pict.bmp
python3 $mainfile decode vigenere tests/testresults/pict15.bmp tests/testresults/result15.txt --key $key --useimg



echo '[TESTING] Group testing with PNG'

echo '[TESTING] make Caesar'
python3 $mainfile encode caesar tests/testsources/source.txt tests/testresults/pict16.png --key $key --useimg --img tests/testsources/pict.png
python3 $mainfile decode caesar tests/testresults/pict16.png tests/testresults/result16.txt --key $key --useimg

echo '[TESTING] make Vernam'
python3 $mainfile encode vernam tests/testsources/source.txt tests/testresults/pict17.png --key $key --useimg --img tests/testsources/pict.png
python3 $mainfile decode vernam tests/testresults/pict17.png tests/testresults/result17.txt --key $key --useimg

echo '[TESTING] make Vigenere'
python3 $mainfile encode vigenere tests/testsources/source.txt tests/testresults/pict18.png --key $key --useimg --img tests/testsources/pict.png
python3 $mainfile decode vigenere tests/testresults/pict18.png tests/testresults/result18.txt --key $key --useimg

echo '[TESTING] hack caesar'
python3 $mainfile hack caesar tests/testresults/10.encrypt tests/testresults/result19.txt --hack_tries 7
