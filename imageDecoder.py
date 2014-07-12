def decode():

    from PIL import Image
    
    img1 = Image.open('test_orig.png')
    img2 = Image.open('test_encoded.png')

    img_orig = img1.convert('RGB')
    img_encoded = img2.convert('RGB')

    data_orig = img_orig.getdata()
    data_encoded = img_encoded.getdata()
    
    i = 0

    charMap = mapAlphaNum()
    message = alphaNum = ''
    while (i < len(data_orig)):
        dO = data_orig[i]
        dE = data_encoded[i]
        
        if (dO[0] != dE[0]):
            
            diff = abs(dE[0] - dO[0])
            alphaNum = getChar(charMap, diff)

            message += str(alphaNum)

        i += 1

    print message
    return message


def mapAlphaNum():

    charString = 'abcdefghijklmnopqrstuvwxyz0123456789'
    charMap = {}
    i = 1
    
    for char in charString:
        charMap[i]=char
        i += 1

    return charMap

def getChar(charMap, num):
    
    if num in charMap:
        return charMap[num]
    else:
        return ''       

if __name__ == '__main__':
    decode()
    
