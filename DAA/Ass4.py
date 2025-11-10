# -------------------------------------------------------------
# 🔺 Binomial Coefficients (Pascal's Triangle) using Dynamic Programming
# -------------------------------------------------------------

# Input n and k
n = int(input("Enter n (row number): "))
k = int(input("Enter k (column number): "))

# Step 1: Create a 2D DP table initialized with zeros
C = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# Step 2: Build Pascal's Triangle using bottom-up DP
for i in range(n + 1):
    for j in range(i + 1):
        if j == 0 or j == i:
            C[i][j] = 1
        else:
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

# Step 3: Print Pascal’s Triangle
print("\nPascal's Triangle:")
for i in range(n + 1):
    print(C[i][:i + 1])

# Step 4: Print desired binomial coefficient
print(f"\nBinomial Coefficient C({n},{k}) = {C[n][k]}")
