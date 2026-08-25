#sentense = "나는 대한민국 서울 구로에서 파이썬 공부를 하고 있습니다."
#words = sentense.split()

#print(type(words))
#print(words)

#sentense에서 3회 이상 등장하는 단어는 무엇일까요? 각 단어와 빈도수를 출력하시오.
#1.딕셔너리 이용 -배운거 내에서
#2. 안배운 개념 써도 되니까 가장 간단한 코드로

sentenses= "오늘 나는 친구와 함께 학교에 갔다. 학교에 도착한 후 친구와 도서관에서 공부를 시작했다. 오늘 공부할 내용은 파이썬과 데이터 분석이었다. 파이썬은 처음 배울 때는 어렵게 느껴졌지만 계속 공부하다 보니 조금씩 재미있어졌다. 친구도 파이썬을 공부하고 있어서 모르는 문제가 생기면 서로 질문하고 답을 찾아보았다. 점심시간에는 친구와 학교 근처 식당에 가서 점심을 먹었다. 점심을 먹으면서 오늘 공부한 내용에 대해 이야기했다. 오후에는 다시 도서관으로 돌아와 데이터 분석 과제를 진행했다. 데이터 분석을 하면서 여러 가지 코드를 작성했고 결과가 제대로 나오는지 확인했다. 가끔 코드에서 오류가 발생했지만 오류의 원인을 하나씩 찾아보면서 문제를 해결했다. 공부가 끝난 후에는 친구와 카페에 갔다. 카페에서 음료를 마시며 오늘 하루를 돌아보았다. 오늘은 해야 할 일이 많아서 조금 피곤했지만 새로운 내용을 많이 배울 수 있어서 만족스러웠다. 앞으로도 파이썬 공부를 꾸준히 하면서 다양한 문제를 직접 해결해 보고 싶다."


word= sentenses.split()

dic={}

for i in word:
    dic[i]=0

for i in word:
    if i in dic:
        dic[i]+=1


for key, value in dic.items():
    if value>=3:
        print(key,value)


from collections import Counter

word = sentenses.split()
count = Counter(word)

for key, value in count.items():
    if value >= 3:
        print(key, value)