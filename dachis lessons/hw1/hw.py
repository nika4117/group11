# შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით რიცხვების სია. 
# თქვენ უნდა დააბრუნოთ გაფილტრული სია, სადაც უკვე მარტო 4-ის ჯერადები იქნება.


def lst(lst):
  lst2 = []
  for i in lst:
    if i % 4 == 0:
      lst2.append(i)
  print(lst2)




list = [1,2,3,10,40,44,16]

list2 = [1,2,3,10,40,44]
lst(list)

lst(list2)







  
       




