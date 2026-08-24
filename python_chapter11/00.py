tags=["Python","AI","Python","Data","AI"]



#list 기능만 써서 unique_tags를 구현 하시오.

unique_tags=[]

for i in range(5):
    if tags[i] in unique_tags:
        pass
    else:
        unique_tags.append(tags[i])


print(unique_tags)


#힌트 1개 씀
#힌트 딱 하나만 줄게! 👀 기존 tags에서 삭제하려고 하지 말고, 빈 리스트를 하나 새로 만들어봐.
# unique_tags = []

#그리고 tags를 하나씩 보면서,"이 값이 unique_tags에 아직 없다면 어떻게 해야 할까?"
#여기까지만 생각해봐! 😎