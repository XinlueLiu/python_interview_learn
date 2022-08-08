
def find_prime(num):
    flag = True
    if num > 1:
        for i in range(2,num):
            # prime numbers are numbers that only have factor of 1 and itself
            # so we are checking if it has any other factors from 2 to num-1
            # if it does not have other factor, we know num is a prime number
            # check if num is an integer multiple of num 2 to (num-1)
            if (num % i) == 0:
                flag = False
                print(f'first factor find thats not 1 nor itself is {i}')
                break
    else:
        print(f'{num} is not a prime number')
        return
    if flag:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is NOT a prime number')

if __name__ == '__main__':
    num = input("input int\n")
    find_prime(int(num))