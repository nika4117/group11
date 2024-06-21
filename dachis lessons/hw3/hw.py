
# მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები. ეს რიცხვები გადაეცით ფუნქციას,
# for ციკლით სიაში შეინახეთ მათ შორის არსებული რიცხვები. შემდეგ მოახდინეთ გაფილტვრა,
# ისევ for ციკლით განიხილეთ თითოეული რიცხვი - თუ რიცხვი ლუწი იქნება, ახალ სიაში დაამატეთ 
# მისი მეორე ხარისხი
# ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი კვადრატული ფესვი (0.5 ხარისხი).


def number(first ,last):
  even = []
  odd = []
  for i in range(first, last + 1):
    if i % 2 == 0:
      even.append(i**2)
    else:
      odd.append(i**0.5)
  for i in even:
    print(i)
  for i in odd:
    print(i)


first2 = int(input("enter first number: "))

last2 = int(input("enter last number: "))

number(first2, last2)