def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0
    
    while progresses :
        if (progresses[0] + speeds[0] * time) >= 100 :
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else :
            if cnt > 0 :
                answer.append(cnt)
                cnt = 0
            time += 1
    answer.append(cnt)
    
    return answer