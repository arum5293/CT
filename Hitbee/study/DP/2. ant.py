'''
개미 전사

개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 한다.
메뚜기 마을에는 여러개의 식량창고가 있는데, 식량창고는 일직선으로 이루어져 있다.

각 식량칭고에는 정해진 수의 식량을 저장하고 있으며, 개미 전사는 식량창고를 선택적으로
약탈하여 식량을 뺏을 예정이다.
이때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다.

따라서, 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.

예를 들어 식량창고 4개가 다음과 같이 존재한다고 가정해보자.
[1, 3, 1, 5]
이때 개미 전사는 두 번째 식량 창고와 네 번째 식량 창고를 선택했을 때 최댓값인 총 8개의 식량을 약탈할 수 있다.
개미 전사는 식량창고가 이렇게 일직선 상일때 최대한 많은 식량을 얻기를 원한다.

개미전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.
'''

'''
최소 한 칸 이상 떨어진 곳을 약탈해야 하는데, 두칸이 될 수도 있고, 세칸이 될 수도 있다.
DP를 적용해서 풀어보자.
'''

# 식량을 얻을 수 있는 경우의 수는 총 8가지이다. (완전 탐색)
# a_i = i번째 식량창고까지의 최적의 해라고 정의하면 DP를 적용할 수 있다.

'''
왼쪽부터 차례대로 식량창고를 턴다고 했을 때, 특정한 i번째 식량창고에 대해서 털지 안털지의 여부를 결정하면,
아래 2가지의 경우 중에서 더 많은 식량을 털 수 있는 경우를 선택하면 된다.
i-1, i-2

a_i = i번째 식량창고까지의 최적의 해(얻을 수 있는 식량의 최댓값)
k_i = i번째 식량 창고에 있는 식량의 양

a_i = max(a_{i-1}, a_{i-2}+k_i)
한 칸 이상 떨어진 식량창고는 고려하지 않아도 됨.
'''

N = 4
K = [1, 3, 1, 5]

dp = [0] * (N)
dp[0] = K[0]
dp[1] = max(K[0], K[1])
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+K[i])

print(dp[N-1]) # 인덱스로 계산을 하기 떄문에 마지막에 -1
print(dp)