print("####### $$ welcome to time and space $$ #######")
def calc(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total
print("")
num = int(input("enter your number"))
ans = calc(num)
print(ans)