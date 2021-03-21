# def bank(a, years):
#     result = 0
#     for i in range(0, years):
#         print(a)
#         a =a * 1.1
#         result=a
#     return result
#
# print(bank(1000,3))

def isprime(a):
    for b in range (0, a):
        if b == 1 or b == a or b == 0:
            continue
        if a % b == 0:
            return False
    return True
print(isprime(37))