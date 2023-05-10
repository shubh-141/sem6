n = int(input("Enter no of candidates: "))
arr = [0] * n
name = [None] * n
skill = [None] * n
skill2 = [None] * n
for i in range(n):
    s = 1
    name[i] = input("Enter the name: ")
    skill[i] = input("Enter the skill: ")
    skill2[i] = input("Enter the skill2: ")
    if skill[i] == "english":
        s += 2
    if skill2[i] == "coding":
        s += 1
    print("Skill score is", s)
    arr[i] = s

print("Skill score of all candidates are:")

for i in range(n):
    print(arr[i], end=" ")
print()

cost = 0
wcost = 0
cost_hire = 100
cost_fire = 50
best = arr[0]
cost += cost_hire
day = 1

for i in range(1, n):
    if arr[i] > best:
        print("Candidate hired", arr[i], "Candidate fired", best)
        best = arr[i]
        cost += cost_hire + cost_fire

print("Randomized", "Candidate hired", best, cost)

arr.sort()
best = arr[0]

for i in range(1, n):
    if arr[i] > best:
        print("Candidate hired", arr[i], "Candidate fired", best)
        best = arr[i]
        cost += cost_hire + cost_fire
print("Worst case", "Candidate hired",best,cost)






