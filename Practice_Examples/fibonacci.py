
def fib_itter(n):
    if n > 1:
        print("0\n1")
    else:
        print("0")

    n_2 = 0
    n_1 = 1
    for i in range(2, n):
        n = n_1 + n_2
        n_2 = n_1
        n_1 = n
        print(n)



def fib_recursive(count, cur_count=0, n_2=0, n_1=1):
    if cur_count == 0 and count > 1:
        cur_count += 2
        print("0\n1")
        fib_recursive(count, cur_count=2, n_2=0, n_1=1)    
    elif count == 1:
        print("0")
    elif cur_count < count:
        n = n_2 + n_1
        print(n)
        fib_recursive(count, cur_count+1, n_2=n_1, n_1=n) 
    
    return



if __name__ == "__main__":
    n=3

    print("Iterative Fibonacci:\n")
    fib_itter(n)
    print("Recursive Fibonacci:\n")
    fib_recursive(n)
