def func_a(s):
    ret = 0
    for i in s:
        if i > ret:
            ret = i
    return ret

def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s):
    ret = 101
    for i in s:
        if i < ret:
            ret = i
    return ret


def solution(scores):
    sum = func_b(scores)
    max_score = func_c(scores)
    min_score = func_a(scores)
    return sum - max_score - min_score
scores = list(map(int, input().split()))
ret = solution(scores)
print(ret)
