# JadenCase 문자열 만들기

# 문제 설명
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.
# 첫 문자가 영문이 아닐 때에는 이어지는 영문은 소문자로 씁니다.(첫번째 입출력 예 참고)

# 입출력 예
# s = "3people unFollowed me"
# return = "3people Unfollowed Me"

# 입출력 예
# s = "for the last week"
# return = "For The Last Week"

# 답안
def solution(s):
    return ' '.join([word.capitalize() for word in s.split(' ')])

# capitalize()
# : 문장의 첫 글자를 대문자로 변환
# ex)
# "python is easy!" → "Python is easy!"
# "3people unFollowed me" → "3people unfollowed me"


# title()
# 단어의 첫 글자를 대문자로 변환
# ex)
# "python is easy!" → "Python Is Easy!"
# "3people unFollowed me" → "3People Unfollowed Me"