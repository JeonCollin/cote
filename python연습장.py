def hex_to_bin(item):

    if(item == '0'):
        return '0000'
    elif(item == '1'):
        return '0001'
    elif(item == '2'):
        return '0010'
    elif(item == '3'):
        return '0011'
    elif(item == '4'):
        return '0100'
    elif(item == '5'):
        return '0101'
    elif(item == '6'):
        return '0110'
    elif(item == '7'):
        return '0111'
    elif(item == '8'):
        return '1000'
    elif(item == '9'):
        return '1001'
    elif(item == 'A'):
        return '1010'
    elif(item == 'B'):
        return '1011'
    elif(item == 'C'):
        return '1100'
    elif(item == 'D'):
        return '1101'
    elif(item == 'E'):
        return '1110'
    elif(item == 'F'):
        return '1111'
    
mystr = '1DB176C588D26EC'
result = ''

for i in range(len(mystr)):
    result += hex_to_bin(mystr[i])
print(result)