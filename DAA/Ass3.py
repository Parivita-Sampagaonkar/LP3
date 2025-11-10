# -------------------------------------------------------------
# 🎒 Fractional Knapsack Problem using Greedy Method
# -------------------------------------------------------------

# Step 1: Input number of items
n = int(input("Enter number of items: "))

items = []
for i in range(n):
    value = float(input(f"Enter value of item {i+1}: "))
    weight = float(input(f"Enter weight of item {i+1}: "))
    ratio = value / weight
    items.append((value, weight, ratio))

capacity = float(input("Enter knapsack capacity: "))

# Step 2: Sort items by value/weight ratio in descending order
items.sort(key=lambda x: x[2], reverse=True)

# Step 3: Add items to knapsack
total_value = 0.0
taken = []  # to store which items are taken and how much

for i, (value, weight, ratio) in enumerate(items, start=1):
    if capacity >= weight:
        # take the whole item
        capacity -= weight
        total_value += value
        taken.append((i, 100.0))  # 100% of item taken
    else:
        # take fractional part
        fraction = (capacity / weight) * 100
        total_value += ratio * capacity
        taken.append((i, fraction))  # partial item taken
        capacity = 0
        break  # knapsack is full

# Step 4: Display result
print("\nItems taken in the knapsack:")
for item_num, percent in taken:
    print(f"Item {item_num} -> {percent:.1f}% of it taken")

print(f"\nMaximum value that can be obtained: {total_value:.1f}")
