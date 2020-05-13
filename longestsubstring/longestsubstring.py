def longest_substring(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    sLen = 0
    x = 0
    y = 0
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > sLen:
                    sLen = dp[i][j]
                    x,y = i,j
    # print(dp)
    # print(sLen)

    result = []
    while dp[x][y] > 0:
        result.append(str1[x - 1])
        x -= 1
        y -= 1
    print("".join(result))




# case 1
s1 = "abcdtaf"
s2 = "3bcdttf"
longest_substring(s1, s2)
print('----------------------------------------------------------------------')

# case 2
s1 = "sineavnsoabcdefghibttale390825ufnnvas_(&^"
s2 = "abcdefghitt"
longest_substring(s1, s2)
print('----------------------------------------------------------------------')

# case 3
s1 = "a8dgk1ndflg0s84142kd"
s2 = "093841tgpngh044flg0s84142123rbbdja7"
longest_substring(s1, s2)
