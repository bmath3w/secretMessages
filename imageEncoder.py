def encode():
    from PIL import Image
    from random import randint

    im = Image.open('original.png')

    rgb_im = im.convert('RGB')
    dimensions = rgb_im.size
    width = dimensions[0]
    height = dimensions[1]

    data = rgb_im.getdata()
    newData = []

    message = readMessage().lower()
    charMap = mapAlphaNum()
    
    count = 0

    for d in data:
        rand = randint(0, 20)

        if (rand == 1 and count < len(message)):
            value = getNum(charMap, message[count])
            if (value > 0):

                if ((d[0]+value) > 255):
                    finalvalue = d[0]-value
                else:
                    finalvalue = d[0]+value

                #print d[0], finalvalue

                newData.append((finalvalue, d[1]+1, d[2]))
                
            else:
                newData.append((d[0], d[1], d[2]))
            count += 1
        else:
            newData.append((d[0], d[1], d[2]))

    size = (width, height)
    new_im = Image.new('RGB', size)
    new_im.putdata(newData)
    data2 = new_im.getdata()
        
    #rgb_im.show()
    #new_im.show()
    rgb_im.save('test_orig.png', "PNG")
    new_im.save('test_encoded.png', "PNG")
    

def readMessage():
    f = open('message.txt', 'r')
    message = f.read()
    return message

def mapAlphaNum():

    charString = 'abcdefghijklmnopqrstuvwxyz0123456789'
    charMap = {}
    i = 1
    
    for char in charString:
        charMap[char]=i
        i += 1

    return charMap


def getNum(charMap, letter):

    if letter in charMap:
        return charMap[letter]
    else:
        return 0
        

if __name__ == '__main__':
    encode()
    
