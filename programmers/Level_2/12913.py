"""
땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다. 
1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다.
단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

https://school.programmers.co.kr/learn/courses/30/lessons/12913
"""

def solution(land):
    for i in range(1,len(land)):
        for j in range(4):
            land[i][j] = max(land[i-1][:j] + land[i-1][j+1:]) + land[i][j]
    return max(land[-1])