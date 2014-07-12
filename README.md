secretMessages
==============

Embedding secure messages in an image to avoid detection

Two images look identical in every way but within the RGB values of each pixel, you can encode values with slight variations which are invisible to the naked eye but can conceal a number which can map to an actual alphanumeric character.
I could have used the ASCII value of to account for each character

How to run:
1. Choose an image and name it original.png.
2. Download the 2 python files imageEncoder.py and imageDecoder.py into the same folder as the image.
3. Take any text of an format and put it in a message.txt file in the same folder. The text can have any character in it but only the letters and numbers will be dissolved in the image.
4. After steps 1-3, your folder should have the following files
- imageEncoder.py
- imageDecoder.py
- message.txt
- original.png
5. Through the command line or python IDE
- run imageEncoder.py first (this will create 2 new images - one original and another encoded one)
- run imageDecoder.py (you'll see the message being decoded from the second image)
