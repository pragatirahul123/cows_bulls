import random
list1=[0,1,2,3,4,5,6,7,8,9]
list2=[]
list3=[]
list4=[]
i=1
while i<=5:
    random_number=random.choice(list1)

    if random_number not in list2:
        list2.append(random_number)
        i=i+1
print(list2)

total_chance=10
count_chance=0
while count_chance<total_chance:
     number=int(input("guess number:"))
     position=int(input("guess the position:"))

     if(number in list2 ) and (list2.index(number)==position):
         list3.insert(position,number)
         print("Bulls",list3)


     elif(number in list2):
         if number not in list4:
             list4.append(number)
         print("Cows",list4)
     count_chance+=1
    print("chance that you used",total_chance-count_chance)

     if list2==list3:
         print("you won")
         break
 if list2==list3:
     print("you win game")

 else:
     print("you loose the game")























