# given a positive integer, check whether it has alternating bits

def find_alternating_bits(n):
    # alternating bits means it cannot have 00 or 11
    # just gonna check if 00 or 11 is in BINARY FORM of n
    return ("00" not in str(bin(n))) and ("11" not in str(bin(n)))

n = 7
sol = find_alternating_bits(n)
print(sol)