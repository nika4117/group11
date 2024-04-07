name = "nika"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "nika" არის ცვლადისთვის მნიშვნელობა

surname = "iskandarashvili"

print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "nika" #ეს არის str ( string  ) ტიპის ცვლადი
age = 16 # ეს არის int ( integer ) მთელი რიცხვი
height = 175.5 #ეს არის float ტიპის ცვლადი ( ათწილადი )
#boolean (bool) ტიპის ცვლადი

knows_programming = True # True ან false
is_ugly = False  #snakecase( უბრალოდ წერის სტილი სტანდარტულად )

isUgly = False # ჯავასკრიპტული camelcase


#print  ( name + " " + surname )

# #სტრინგი არის ბრჭყალებში მოქცეული სიმბოლო
#print(name + age ) 

# print(type(age))
# print(type(name))
# print(type(surname))
# print(type(height))
# print(type(knows_programming))

#print(name + " " + str(age))

#print(name + " " + surname + " " + str(age) + " " + str(height))

print("my name is " + name + " " + surname + " and i'm " + str(age) + "years old." + " I am " + str(height) + "cm tall.")