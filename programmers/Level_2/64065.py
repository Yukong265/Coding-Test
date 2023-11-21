"""
특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, 
s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

https://school.programmers.co.kr/learn/courses/30/lessons/64065
"""

def solution(s) :
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)

    for i in s :
        data = i.split(",")
        for value in data :
            if int(value) not in answer:
                answer.append(int(value))

    return answer