"""
민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다.
이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

https://school.programmers.co.kr/learn/courses/30/lessons/77484
"""

def solution(lottos, win_nums):
    answer = []
    zero = 0
    count = 0
    rank = { 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 0:6}

    for i in lottos:
        if i == 0:
            zero += 1

    for i in range(6):
        if lottos[i] in win_nums:
            count += 1

    if count == 0:
        answer.append(6)
    else:
        answer.append(rank[count])
    answer.insert(0, rank[count+zero])

    return answer