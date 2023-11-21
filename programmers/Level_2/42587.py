"""
현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 
몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 
해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

https://school.programmers.co.kr/learn/courses/30/lessons/42587
"""


def solution(priorities, location):
    max_num = max(priorities)
    result = 0
    while True:
        for i in range(len(priorities)):
            if max_num == priorities[i]:
                result += 1
                priorities[i] = 0
                max_num = max(priorities)
                if i == location:
                    return result