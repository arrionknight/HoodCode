def trap_sack(cap,n):
  if n == 0 or cap == 0:
    return 0

  elif weight[n-1] > cap:
    return trap_sack(cap,n-1)

  else:
    take = money[n-1] + trap_sack(cap - weight[n-1],n-1)
    skip = trap_sack(cap,n-1)
    return max(take,skip)

capacity = 30
money = [70, 120, 55]
n = len(money)
weight =[14,28,3.5]

result = trap_sack(capacity,n)
print(result)
