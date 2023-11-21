"""
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

https://school.programmers.co.kr/learn/courses/30/lessons/12950
"""


def solution(arr1, arr2):
    answer = arr2
    a = len(arr1)
    b = len(arr1[0])

    for i in range(a):
        for j in range(b):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer