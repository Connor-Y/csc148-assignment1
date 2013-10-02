store_i = {}
def i_solver(n):
    if n == 1:
        return 1
    for i in range(1, n):
       # print("for n = " + str(n) + " and i = " + str(i) + " moves = " + str(2 * i_solver(n-i) + (2 ** i) - 1))
        if n == 12:
            store_i[i] = (2 * i_solver(n-i) + (2 ** i) - 1)
    return(2 * i_solver(n-i) + (2 ** i) - 1)


if __name__ == '__main__':
    print(i_solver(12))
    print(store_i)
