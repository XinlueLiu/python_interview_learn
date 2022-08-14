

def find_bin_with_al(n):
    return ("00" not in bin(n)) and ("11" not in bin(n))

if __name__ == "__main__":
    n = 7
    sol = find_bin_with_al(n)
    print(sol)