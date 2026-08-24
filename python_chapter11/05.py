scores = [55, 72, 88, 91, 67, 100, 79]

for score in scores:
    print(score)

for score in scores:
    if score>=80:
        print(score)

for score in scores:
    if score<60:
        print(score)

count=0
for score in scores:
    if score>=80:
        count+=1

print(count)