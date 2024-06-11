time_of_service=int(input("number of years: "))
salary=int(input("salary: "))

if time_of_service > 10:
  bonus= (salary*0.1)
  print (bonus)

elif time_of_service >= 6 and time_of_service <=10:
  bonus= (salary*0.08)
  print (bonus)

elif time_of_service >= 6:
  bonus= (salary*0.05)
  print (bonus)

