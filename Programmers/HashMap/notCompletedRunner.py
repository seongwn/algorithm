'''아이디어 1
    participant와 completion을 정렬 후 (sort() 사용)
    앞에서부터 차례로 비교
'''
def solution(participant, completion):

    answer = ''

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            answer = participant[i]
            break
    if answer == '':
        answer = participant[-1]
    return answer
