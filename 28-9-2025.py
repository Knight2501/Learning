#Bai 6 tim don vi so trong 1 so
num = 75869
count = 0
while num != 0:
        num = num // 10
        count = count + 1
        print("So don vi la: ",count)


#Bai 7 dem nguoc so tu 5 den 1
i = 5
k = 5
for i in range(5, i + 1):
        for k in range(k - i, k - i + 1):
                print(k, end =' ')
                print(' ')


#Bai 8 sap xep list nguoc lai tu tren xuong
list1 = [10, 20, 30, 40, 50]
list1.reverse()
print(list1)

#Bai 9 cho tu -10 den -1 sap xep nguoc lai 
for num in range(-10, 0, 1):
        print(num)


list2 =[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
list2.reverse()
print(list2)

#Bai 10 In ra tu 0 den 4 va done
for i in range(5):
        print(i)
else:
        print("Done")

#Bai 11 In ra cac so nguyen to tu 25 den 50
start = 25
end = 50
for num in range(start,end + 1):
        if num > 1:
                for i in range(2, num):
                        if (num % i) == 0:
                                break
                        else:
                                print(num)

#Bai 12 In ra cac so Fibonacci 10 lan
num1 = 0
num2 = 1
result = num1 + num2
count = 10
for i in range(count):
        print(num1)
        num1 = num2
        num2 = result
        result = num1 + num2

#Bai 13 In ra cac so giai thua
factorial = 1
Number = 5
if Number < 0:
        print("The factorial number doesn't exist")
elif Number == 0:
                print("The factorial of 0 is 1")
else:
        for i in range(1, Number + 1):
                factorial = factorial * i
                print(factorial)



