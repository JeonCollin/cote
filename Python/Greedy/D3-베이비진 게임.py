def triplet(cards):
    # 같은 숫자가 3개 이상
    
    # 일단 정렬
    cards.sort()
    #print(cards)
    
    # 카드를 순회하며 연속인 카운트를 센다
    # 다르다면 카운트 초기화
    cnt = 0
    
    for i in range(5):
        
        # -1은 넘긴다
        if(cards[i] == -1):
            continue
        
        # 다음 카드와 같다면 카운트 증가
        if(cards[i] == cards[i+1]):
            cnt += 1
            
            # 그게 3개 이상이면 triplet
            if(cnt >= 3):
                return True
        
        # 다르다면 초기화
        else:
            cnt = 0
    
    return False

def rum(cards):
    # 연속인 숫자가 3개 이상
    
    # 일단 정렬
    cards.sort()
    
    # 카드를 순회하며 연속인 카운트를 센다
    # 다르다면 카운트 초기화
    cnt = 1
    
    for i in range(5):
        
        # -1은 넘긴다
        if(cards[i] == -1):
            continue
        
        # 다음 카드가 연속이라면 카운트 증가
        if(cards[i]+1 == cards[i+1]):
            cnt += 1
            
            # 그게 3개 이상이면 rum
            if(cnt >= 3):
                return True
        
        # 다르다면 초기화
        else:
            cnt = 1
            
    return False
    
    

def babygin(mylist):
    
    # 교대로 카드를 가져간다
    A = [-1]*6
    B = [-1]*6
    
    # 결과
    
    for i in range(0, 6):
        
        # A, B 카드에 추가
        A[i] = mylist[2*i]
        B[i] = mylist[2*i+1]
        
        #print(A, B)
        
        # rum과 triplet 판단
        rumA = rum(A[:])
        tripletA = triplet(A[:])
        rumB = rum(B[:])
        tripletB = triplet(B[:])
        
        # A B 순서
        # F F
        if(rumA == False and tripletA == False and rumB == False and tripletB == False):
            continue
        
        # F T
        elif(rumA == False and tripletA == False and (rumB == True or tripletB == True)):
            return 2
        
        # T F
        elif((rumA == True or tripletA == True) and rumB == False and tripletB == False):
            return 1
        
        # T T
        elif((rumA == True or tripletA == True) and (rumB == True or tripletB == True)):
            return 0
        
    # 둘 다 성과가 없다면 무승부
    return 0

T = int(input())

for t in range(1, T+1):
    
    mylist = list(map(int, input().split()))
    
    # 결과 출력
    print(f'#{t} {babygin(mylist)}')