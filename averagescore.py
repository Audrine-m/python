math=int(input("enter score: "))
Eng=int(input("enter score: "))
German=int(input("enter score: "))

average=((math+Eng+German)/3)
print(average)

if average>70 and average <100:
   grade=("A")
   print (grade)
elif average >60 and average <=70:
      grade=("B")
      print (grade)
elif average >50 and average <=60:
      grade=("C")
      print (grade)
elif average >40 and average <=50:
      grade=("D")
      print (grade)
elif average >0 and average <=40:
      grade=("Fail")
      print (grade)







