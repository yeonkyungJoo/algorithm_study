# https://programmers.co.kr/learn/courses/30/lessons/12949
# 행렬의 곱셉
'''
arr1 * arr2

# solution
## 1. numpy
## 2. zip?
'''
import numpy as np
def solution(arr1, arr2):
    return (np.matrix(arr1) * np.matrix(arr2)).tolist()
