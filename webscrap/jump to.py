'''
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

5
1 1
12 34
5 500
40 60
1000 1000
'''

import sys
number = int(input())

for i in range(number):
    a, b = map(int,sys.stdin.readline().split())
    print(a)


