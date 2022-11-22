inString = input("")

def letToNum(letter):
    if letter == 'B' or letter == 'I' or letter == 'N' or letter == 'G' or letter == 'O': 
        return {
                'B':1,
                'I':2,
                'N':3,
                'G':4,
                'O':5    
        }[letter]
    else:
        return letter
    
qa = [int(letToNum(i))-1 for i in inString]


with open("mod12activity.txt") as file:
    bigString = file.read()
    
    bigList = bigString.split("\n")
    
    key = [bigList[0:5],bigList[5:10],bigList[10:15],bigList[15:20],bigList[20:25]]
    
    n = 0
    fString = []

    letts = qa[1::2]
    nums = qa[::2]
    for i in range(len(letts)):
        
        fString.append(key[letts[i]][nums[i]])
        
    for i in fString:
        print(i, end='')
       
    
    
    

    
        
        
        
        
        
        
        
        
        
        
        
    
