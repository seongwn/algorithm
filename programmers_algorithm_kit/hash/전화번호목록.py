"""
Level 2

문제 설명

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

    구조대 : 119
    박준영 : 97 674 223
    지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
제한 사항

    phone_book의 길이는 1 이상 1,000,000 이하입니다.
        각 전화번호의 길이는 1 이상 20 이하입니다.
        같은 전화번호가 중복해서 들어있지 않습니다.

"""


def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number[:-1]:
            temp += number
            if temp in hash_map:
                return False

    return True
# def solution(phone_book):
#     phone_book.sort()
#     p_nbr = phone_book[0]

#     for nbr in phone_book[1:]:
#         if p_nbr == nbr[:len(p_nbr)]:
#             return False
#         p_nbr = nbr

#     return True