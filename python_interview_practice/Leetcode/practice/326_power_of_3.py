# return true if it is a power of 3, else return false
# keep dividing until value is not greater than 1
# then if it is power of 3, the remaining value must be 1

def po3(n):
    while(n > 1):
        n /= 3
    return n == 1

n = 27
sol = po3(n)
print(sol)