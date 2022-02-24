# Shuffle String

# input
s = "art"
indices = [1,0,2]

def solution(s, indices):
    arr=[]
    for a, b in zip(list(s), indices):
        arr.insert(b,a)
    return ''.join(arr)