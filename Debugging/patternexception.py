def printbox(symbol,width,height) :
    if len(symbol) != 1 :
        raise Exception('"symbol" needs to be a string of length 1')
    if (width<2) or (height<2) :
        raise Exception('"Width" and "height" must be greater than or equal to 2.')
    print(symbol * width)
    
    for i in range(height-2) : 
        print(symbol + (' ' * (width-2))+symbol)
    print(symbol * width)


print(printbox('5',5,6))
print(printbox('*',1,1))
print(printbox('**',5,3))