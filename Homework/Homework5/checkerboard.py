def checkerboard(size, symbol_1, symbol_2):
    
    s = symbol_1 + symbol_2
    for i in range(1,size):
        if(len(s) < size):
            if(s[i] != symbol_1):
                s+= symbol_1
            elif(s[i] != symbol_2):
                s+= symbol_2
        
        if(len(s) == size):
            break
   
    
    return s

n =int(input("What size do you want? "))
v = input("What symbols do you want? ")
n1 = v[0]
n2 = v[2]

word = checkerboard( n, n1 , n2)
 
print(word)

s = []
for x in word:
    s.append(x)
    
for i in range(len(s)):
    s[i],s[i-1,-1] = s[i-1,-1],s[i]
    print(s)