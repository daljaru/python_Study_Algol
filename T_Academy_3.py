#거듭제곱 연산
#문자열을 숫자로 변환하기

'''
#n진법
def stoi(s, n):
    ret = 0
    l = len(s)
    for i in range(l): ret += int(s[i]) * n**(l-i-1)
    return ret
'''
#이진수를 활용하는 것도 시간복잡도를 줄일 수 있는 방법이다.
def stoi(s, n):
    ret = 0
    for i in s : ret = ret * n +int(i)
    return ret

#거듭제곱은 거듭제곱 간의 곱으로 표현이 가능
'''
def pow_custon(a, b):
    ret = 1
    while b:
        if b % 2 == 1 : ret *= a
        a = a*a
        b //= 2
    return ret
'''

#모듈러는 그때그때 하는 것이 좋다.
#왜냐하면 큰수를 계산하는 것이 더 비효율적이다.

def pow_custom(a, b, mod):
    ret = 1
    while b:
        if b % 2 == 1 : ret = ret * a % mod
        a = a * a % mod
        b //= 2
    return ret


#최대공약수 유클리드 호제법
def gcd(a, b):
    return b if a%b == 0 else gcd(b, a%b)


#소인수 분해
def isPrime(N):
    i = 2
    while i*i <= N:
        if N % i == 0: return False
        i += 1
    return True

#에라토스테네스의 체
def era(N):
    ck, p = [False for _ in range(N+1)], []
    for i in range(2, N+1):
        if ck[i] == True : continue
        p.append(i)
        for j in range(i*i, N+1, i):
            ck[j] = True
    return ck, p

#분할정복
#하노이의 탑
def hanoi(st, ed, sz):
    if sz == 1: return print(st, ed)
    hanoi(st, 6-st-ed, z-1)
    print(st, ed)
    hanoi(6-st-ed, ed, sz-1)

n = int(input())
print(2**n-1)
hanoi(1, 3, n)


