# ---------------------------------------------
# 🌀 Fibonacci Series (Iterative + Recursive)
# ---------------------------------------------

# ---- Iterative Fibonacci ----
n = int(input("Enter how many Fibonacci numbers to print (Iterative): "))

a, b = 0, 1
steps = 0
series = []

for i in range(n):
    series.append(a)
    temp = a + b
    a = b
    b = temp
    steps += 1

print("\nFibonacci Series (Iterative):", series)
print("Total Steps (iterations):", steps)

# ---- Recursive Fibonacci ----
steps = 0  # global counter

def fib(n):
    """Recursive Fibonacci with step counting."""
    global steps
    steps += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

num = int(input("\nEnter how many Fibonacci numbers to print (Recursive): "))
series = [fib(i) for i in range(num)]

print("\nFibonacci Series (Recursive):", series)
print("Total Steps (recursive calls):", steps)
