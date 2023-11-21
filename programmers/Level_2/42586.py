"""

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""


def solution(progresses, speeds):
    answer = []
    dates = []
    count = 0
    
    for p, s in zip(progresses, speeds):
        date = -((p-100) // s)
        dates.append(date)
    
    dates.append(float("inf"))
    cnt_date = dates[0]
    for date in dates:
        if date <= cnt_date:
            count += 1
        else:
            answer.append(count)
            cnt_date = date
            count = 1
    
    return answer