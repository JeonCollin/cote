T = int(input())

for test_case in range(1, T + 1):
	
    N = input()
    
    myList = []
    i = 1
    
    while True:  
        
        N = N * i
        
        myList.append(N)
        myList.sort()
        myList = list(set(myList))
        
        i = i + 1
        
        if(myList == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
            break
            
    print("#%d %d" % (test_case, i))