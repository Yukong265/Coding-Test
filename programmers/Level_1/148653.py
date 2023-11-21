"""
마법의 돌을 아끼기 위해 민수는 항상 최소한의 버튼을 눌러서 이동하려고 합니다. 민수가 어떤 층에서 엘리베이터를 타고 0층으로 내려가는데 필요한 마법의 돌의 최소 개수를 알고 싶습니다. 민수와 마법의 엘리베이터가 있는 층을 나타내는 정수 storey 가 주어졌을 때, 0층으로 가기 위해 필요한 마법의 돌의 최소값을 return 하도록 solution 함수를 완성하세요.

https://school.programmers.co.kr/learn/courses/30/lessons/148653
"""

def solution(storey):
    if storey < 10 :
        return min(storey, 11 - storey)
    left = storey % 10
    return min(left + solution(storey // 10), 10 - left + solution(storey // 10 + 1))