import threading
primes=[]
def primeNumbers():
    for i in range(2,500+1):
        if i>1:
            for j in range(2,i):
                if (i%j)==0:
                    break
                else:
                    primes.append(i)
                    break
    print("prime numbers between 2 and 500 are:\n",primes)
palindrome=[]
def palindromeNumber():
    for num in range(10,500+1):
        temp=num
        reverse=0
        while(temp>0):
            Reminder=temp%10
            reverse=(reverse*10)+Reminder
            temp=temp//10
        if(num==reverse):
            palindrome.append(num)
    print("palindrome numbers between 2 and 500 are:\n",palindrome)

t1=threading.Thread(target=primeNumbers)  
t2=threading.Thread(target=palindromeNumber)  
t1.start()
t2.start()
t1.join()
t2.join()

