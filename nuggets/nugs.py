import time

def nugs(N, S1, S2):
    dp = []

    for i in range(N):
        T1 = (0, 0)
        T2 = (0, 0)
        if i - S1 >= 0:
            T1 = dp[i - S1]
        if i - S2 >= 0:
            T2 = dp[i - S2]

        total1 = ((T1[0] + 1) * S1) + (T1[1] * S2)
        total2 = (T2[0] * S1) + ((T2[1] + 1) * S2)
        if total1 < total2:
            dp.append((T1[0] + 1, T1[1]))
        else:
            dp.append((T2[0], T2[1] + 1))

    small,large = dp[N - 1]
    total = small * S1 + large * S2
    print('when buying %d nuggets, get %d small(%d) and %d large(%d) for total of %d nuggets' %(N, small, S1, large, S2, total) )

start_time = time.time()
nugs(20, 7, 11)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
nugs(100, 7, 11)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
nugs(101, 7, 11)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
nugs(10000000, 7, 11)
print("--- %s seconds ---" % (time.time() - start_time))
