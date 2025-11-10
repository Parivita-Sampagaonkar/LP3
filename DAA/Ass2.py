# -------------------------------------------------------------
# 🧩 Job Sequencing with Deadlines using Greedy Method
# -------------------------------------------------------------

# Step 1: Input number of jobs
n = int(input("Enter number of jobs: "))

jobs = []
for i in range(n):
    job_id = input(f"Enter Job ID for job {i+1}: ")
    profit = int(input(f"Enter Profit for job {i+1}: "))
    deadline = int(input(f"Enter Deadline for job {i+1}: "))
    jobs.append((job_id, profit, deadline))

# Step 2: Sort jobs by profit in descending order
jobs.sort(key=lambda x: x[1], reverse=True)

# Step 3: Find the maximum deadline to define time slots
max_deadline = max(job[2] for job in jobs)
slots = [None] * max_deadline
total_profit = 0

# Step 4: Assign jobs to the latest available slot before deadline
for job in jobs:
    job_id, profit, deadline = job
    for d in range(deadline - 1, -1, -1):  # check backward
        if slots[d] is None:
            slots[d] = job_id
            total_profit += profit
            break

# Step 5: Display results
print("\nScheduled Jobs in order of time slots:")
print(slots)
print("Total Profit:", total_profit)
