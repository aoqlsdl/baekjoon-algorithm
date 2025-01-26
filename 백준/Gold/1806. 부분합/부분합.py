n, s = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

left, right = 0,0
sum = 0
length = 1000001

while True:
    if sum >= s:
        length = min(length, right-left) # 현재 최소 길이와 right - left 한 값 중 더 작은 값을 저장
        sum -= nums[left]
        left +=1 # 왼쪽 점을 옮긴다 == 길이를 줄인다
    elif right == n:
        break
    else:
        sum += nums[right] # 오른쪽 점을 옮긴다 == 길이를 늘린다
        right += 1

if length == 1000001:
    print(0)
else:
    print(length)