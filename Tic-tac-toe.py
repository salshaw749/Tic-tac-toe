print("Hey Dear.. you're playing a tic tac toe")
print("Please choose your desierd shape to play with X or O")


arr = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

arrTemp = [
    ["*","*","*"],
    ["*","*","*"],
    ["*","*","*"]
]

i=0

def checkVertical(arr):
    if (arr[0][0]=="x" and arr[1][0]=="x" and arr[2][0]=="x" ) or (arr[0][0]=="o" and arr[1][0]=="o" and arr[2][0]=="o" ):
        return True
    elif (arr[0][1]=="x" and arr[1][1]=="x" and arr[2][1]=="x" ) or (arr[0][1]=="o" and arr[1][1]=="o" and arr[2][1]=="o" ):
        return True
    elif (arr[0][2]=="x" and arr[1][2]=="x" and arr[2][2]=="x" ) or (arr[0][2]=="o" and arr[1][2]=="o" and arr[2][2]=="o" ):
        return True 
    return False

def checkHorizantal(arr):
    if (arr[0][0]=="x" and arr[0][1]=="x" and arr[0][2]=="x" ) or (arr[0][0]=="o" and arr[0][1]=="o" and arr[0][2]=="o" ):
        return True
    elif (arr[1][0]=="x" and arr[1][1]=="x" and arr[1][2]=="x" ) or (arr[1][0]=="o" and arr[1][1]=="o" and arr[1][2]=="o" ):
        return True
    elif (arr[2][0]=="x" and arr[2][1]=="x" and arr[2][2]=="x" ) or (arr[2][0]=="o" and arr[2][1]=="o" and arr[2][2]=="o" ):
        return True 
    return False

def checkDaigonal(arr):
    if (arr[0][0]=="x" and arr[1][1]=="x" and arr[2][2]=="x" ) or (arr[0][0]=="o" and arr[1][1]=="o" and arr[2][2]=="o" ):
        return True
    elif (arr[0][2]=="x" and arr[1][1]=="x" and arr[2][0]=="x" ) or (arr[0][2]=="o" and arr[1][1]=="o" and arr[2][0]=="o" ):
        return True
   
    return False

while(i<9):
    player=input("Hey Player .. please choose your shape: ")
    val1=int(input("Choose your postion: "))
    
    
    if val1 in range(0,9):
        if val1 == 0:
            arrTemp[0][0] = player
        elif val1 == 1:
            arrTemp[0][1] = player
        elif val1 == 2:
            arrTemp[0][2] = player
        elif val1 == 3:
            arrTemp[1][0] = player
        elif val1 == 4:
            arrTemp[1][1] = player
        elif val1 == 5:
            arrTemp[1][2] = player       
        elif val1 == 6:
            arrTemp[2][0] = player
        elif val1 == 7:
            arrTemp[2][1] = player
        elif val1 == 8:
            arrTemp[2][2] = player  
    
    
    checkV = checkVertical(arrTemp)
    checkH = checkHorizantal(arrTemp)
    checkD = checkDaigonal(arrTemp)
    if checkV or checkH or checkD:
        print(player + " WON!!!")
        for j in arrTemp:
            print(j)
        
        break
    

    else:
        for j in arrTemp:
            print(j)
            
    if i == 8:
        print("HEHEHE IT'S A TIE ! You Both Are Smarts!!!")
        
    i+=1



