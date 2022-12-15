def sumofSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum +=pow(i,3)

    return sum
n = 5
print(sumofSeries(n))