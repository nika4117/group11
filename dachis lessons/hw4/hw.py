# შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. 
# თქვენ უნდა დააბრუნოთ ამ სიის საშუალო არითმეტიკული ( ჯამი / სიგრძე )

def word(numbers):
  sum = 0
  length = len(numbers)
  for i in numbers:
    sum += i
  print(sum / length)

lst2 = [1,2,3,4,5]

word(lst2)



def word(a):
  print(a[::-1])

word("dachi")