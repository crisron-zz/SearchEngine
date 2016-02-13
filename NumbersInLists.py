string = raw_input()

answer = []
tempList = []
for i in range( len( string ) ):
    num = int( string[ i ] )
    if not i:
        answer.append( num )
        maxNum = num
    elif num > maxNum:
        maxNum = num
        if tempList:
           answer.append( tempList )
           tempList = []
        answer.append( num )
    else:
        tempList.append( num )

if tempList:
    answer.append( tempList )
print answer
