"""
Level 3

문제 설명

아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.
제한사항

    N은 1 이상 9 이하입니다.
    number는 1 이상 32,000 이하입니다.
    수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
    최솟값이 8보다 크면 -1을 return 합니다.

"""


def return_results(arr1, arr2):
    results = []
    for a1 in arr1:
        for a2 in arr2:
            results.append(a1 + a2)
            results.append(a1 * a2)
            results.append(a1 - a2)
            results.append(a2 - a1)
            try:
                results.append(a1 // a2)
            except:
                pass
            try:
                results.append(a2 // a1)
            except:
                pass

    return results


def solution(N, number):
    cases = [[] for i in range(9)]
    cases[1] = [N]
    cases[2] = [int(str(N) * 2), N + N, N / N, N * N]

    for i in range(3):
        if number in cases[i]:
            return i

    for i in range(3, 9):
        cases[i].append(int(str(N) * i))
        for j in range(1, i // 2 + 1):
            cases[i] += return_results(cases[j], cases[i - j])
        cases[i] = list(set(cases[i]))
        if number in cases[i]:
            return i

    return -1
