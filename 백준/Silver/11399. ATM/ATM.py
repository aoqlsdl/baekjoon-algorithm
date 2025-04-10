people = int(input())
times = list(map(int, input().split()))

# 소요 시간이 적은 순으로 정렬
times.sort()

total_times = 0
per_times = 0
result = 0

for i in range(len(times)): # 리스트 길이만큼 덧셈 반복
    # 한 사람당 기다리는 시간 계산
    per_times = 0
    for j in range(i):
        per_times += times[j]

    # 최종적으로 기다리는 시간
    total_times = per_times + times[i]
    
    # 한 사람이 최종적으로 기다리는 시간 모두 더하기
    result += total_times

print(result)