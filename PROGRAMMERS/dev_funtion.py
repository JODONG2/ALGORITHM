def solution(progresses, speeds):
    answer = []
    day = progresses[:]
    while day : 
        day = [progress+speed for progress,speed in zip (day,speeds)]
        release = 0 
        print(day)
        while day and day[0] >= 100 : 
            del day[0]
            del speeds[0]
        if not release == 0 : 
            answer.append(release)
    return answer


assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1] ) == [1,3,2]

