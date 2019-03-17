# Encryptor

Command structure

`python3 <path to main> <encode/decode> <cryptor type> <source file path> <destination file path> [--key_raw || -key] <key path or value> `

If you want to encrypt with image add to the end:

`--useimg --img <path to image>`

Decrypt with image:

`--useimg`

Example:
```bash
# common text encrypting
python3 main.py encode caesar source.txt file.encrypt --key_raw asdf
python3 main.py decode caesar file.encryp  result.txt --key_raw asdf

#using image
python3 main.py encode caesar source.txt encrypted.png --key_raw asdf --useimg --img pict.png
python3 main.py decode caesar encrypted.png result.txt --key_raw asdf --useimg
```

***

Using caesar hack:

`python3 <path to main> hack caesar <source file path> <destination file pathdestination file path> --hack_tries <hack trying number>`

Example:

`python3 main.py hack caesar source.txt result.txt --hack_tries 10`

***

Tests:
`sh tests/testing.sh`

Clear test folder:
`sh tests/resettests.sh`

***

Cryptor variants:
```text
1) Caesar
2) Vernam
3) Vinegere
```

Hack works only with caesar with text in English.

***

Arguments description:
```text
1) crypt type (encode/decode/hack)
2) crypt algorithm (Caesar/Vernam/Vinegere)
3) source file
4) destination file
--key - key file
--key_raw - raw key value
--useimg - set using image option to true
--img - path to img file (only for ecnryption with image)
--hack_tries - number of hack tries
```

***

Install require packeges:

`pip install -r requirements.txt`
