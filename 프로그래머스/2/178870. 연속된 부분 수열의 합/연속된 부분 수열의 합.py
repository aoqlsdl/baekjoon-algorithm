# def isMin(s, e, ans): # 최소 길이인지 판별하는 함수
#     if len(ans) == 0:
#         return True
    
#     if ans[1] - ans[0] > e - s:
#         return True
    
#     return False

def solution(sequence, k):
    start = 0
    end = 0
    
    answer = [0, len(sequence)]
    sum = sequence[0]
    
    while True:
        if sum < k:
            end += 1
             
            if end == len(sequence): break
            
            sum += sequence[end]
        else:
            if sum == k:
                if end - start < answer[1] - answer[0]:
                    answer = [start, end]

            sum -= sequence[start]
            start += 1   
    return answer