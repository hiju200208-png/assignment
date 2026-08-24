scores = [70, 80, 90]

scores[0] = 75

scores[2] = 95

scores[1] = 85

print(scores)



#시작:

#scores[0] = 75 후:
[75,80,90]


#scores[2] = 95 후:
[75,80,95]

#scores[1] = 85 후:
[75,85,95]


#추가 Challenge

foods = ["김밥", "라면", "떡볶이", "우동"]

 

#다음 조건을 만족하도록 인덱스를 이용해 값만 수정하세요.
#라면 → 파스타
#우동 → 냉면
foods[1]="파스타"
foods[3]="냉면"
print(foods)


