x = int(input())
total = 0
total += x//500*1000
total += (x%500)//5*5
print(total)