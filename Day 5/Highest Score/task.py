student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

print(sum(student_scores))

# other way to find sum using for loop
score = 0
for total in student_scores:
    score += total
print(score)

print(max(student_scores))
print(min(student_scores))

# other way to find max nad min using for loop
max_score = 0
for highest in student_scores:
    if highest > max_score:
        max_score = highest

print(max_score)

# max example:
scores = [8, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for high in scores:
    if high > max_score:
        max_score = high

print(max_score)

# min ex
scores1 = [80, 8, 65, 89, 86, 55, 91, 64, 89]
min_score = scores1[0]
for small in scores1:
    if small < min_score:
        min_score = small

print(min_score)