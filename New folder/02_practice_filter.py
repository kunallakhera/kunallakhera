l = [2,55,45,20,12,117,87]
def finddivisible(num):
    return num%5 == 0
print(list(filter(finddivisible,l)))
