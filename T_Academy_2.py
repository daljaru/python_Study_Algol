
#useful code on T_Academy_2

#1부터 10까지의 합
def sum_N(N):
    return N*(N+1) // 2

#길이 N수열에서 수 K찾기
def search(lst, K):
    for i in range(len(lst)):
        if lst[i] == K: return True
    return False

'''
def solution(n):
    ret = 0
    for i in range(1, n+1):
        ret += len(str(i))
    return ret
'''
#을 Pythonic하게 고치면
def solution(n):
    return sum(map(lambda x : len(str(x)), range(1, n+1)))

'''
#수의 길이를 구하는 방법
def num_len(n):
    ret = 0
    while n :
        n /= 10
        ret ++
    return ret:
'''

#튜플로 기본 선언 시, 표현이 간결해진다.
#본인에게 익숙한 표현으로 변수를 선언하고 코드 작성을 완료한다.
def solution(n):
    l, ret = len(str(n)), 0
    for i in range(1, l): ret += i * (10**i - 10**(i-1))
    ret += l * (n - 10 ** (l-1) + 1)
    return ret


#입력 팁
num = int(input())
string = input()
char_lst = list(input())
list = list(map(int, input().split()))



#list 초기화ㅡ comprehension으로
lst_1d = [0 for _ in range(N)]
lst_2d = [[0 for _ in range(N)] for j in range(N)]


