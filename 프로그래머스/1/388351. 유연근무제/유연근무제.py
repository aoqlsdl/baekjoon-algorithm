def solution(schedules, timelogs, startday):
    answer = 0
    
    n = len(schedules)

    for i in range(n):
        for j in range(7):
            day = startday + j # 오늘 요일 구하기
            
            if day > 7:
                day -= 7
                
            if day > 5: # 주말이라면 고려하지 않음
                continue
            
            arrive = schedules[i] + 10
            
            h = arrive // 100
            m = arrive % 100
            
            if m >= 60:
                arrive = (h + 1) * 100 + (m - 60)
                
            if timelogs[i][j] > arrive:
                timelogs[i][j] = 0 # 실패 --> 0으로 표시
                break # 이후는 고려할 필요 없음
        
        
        if 0 not in timelogs[i]: # 실패한 날이 없을 경우 성공
            answer += 1
            
    return answer