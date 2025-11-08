'''
#Question 1: Write a Python program to print the square of all numbers from 0 to 19.
for i in range (20):
    print(i,'→', i*i)
#Question 2: Write a Python program to print all numbers from 0 to 9 and then print 'blast off' after the loop.
for i in range(10):
   # print(i)
print('blast off')
#3. Write a Python function that checks whether a number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for num in range(1,51):
    if is_prime(num):
        print(num)
'''
#4. Write a Python program to print all prime numbers between 1 and 50.
def btc_savings(start, weekly_invest, weeks):
    BTC = 65000
    total_usd = start+(weekly_invest * weeks)
    btc_bought = total_usd / BTC
    return btc_bought, total_usd
    
print(btc_savings(1000, 100, 10))  #(0.03076923076923077, 2000)