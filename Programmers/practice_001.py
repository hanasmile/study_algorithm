# 제일 작은 수 제거하기

# 문제 설명
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

# 제한 조건
# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

# 입출력 예
# arr = [4,3,2,1]
# return = [4,3,2]

# arr2 = [10]
# return = [-1]

# 답안
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.sort(reverse = True)
        arr.pop()
        return arr

# 답안
# 배열은 통계자료같은 개념으로 사용할 수 있기 때문에 마음대로 내림차순 sort를 하게되면 규칙에 맞도록 정렬된 값이 변경될 수 있기 때문에
# 반드시 필요한 경우에만 sort를 사용해야 한다.
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
    return arr