# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자

i = 1
total = 0
while i <= 1000:
    if i % 3 == 0:
        total = total + i
    i = i + 1

print ("1부터 1000까지의 자연수 중 3의 배수의 합 = %d" % total)
