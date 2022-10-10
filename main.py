
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
# Make your Code
# ******************************
if len(num1) < len(num2) or len(num1) == len(num2):
    print(num1 + num2)
else:
    print(num2 + num1)


