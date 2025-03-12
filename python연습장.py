T = int(input())
 
 
def swap(idx):
    global nums, length
    if idx == N:
        return
 
    tmp = set()
    for num in nums:
        for i in range(length-1):
            for j in range(i+1, length):
                t = [n for n in num]
                t[i], t[j] = t[j], t[i]
                tmp.add(''.join(t))
    nums = tmp
    print(nums)
    swap(idx+1)
 
 
 
for tc in range(1, T+1):
    num, N = input().split()
    N = int(N)
    length = len(num)
    nums = set()
    nums.add(num)
 
    swap(0)
 
    print(f"#{tc} {max([int(n) for n in nums])}")