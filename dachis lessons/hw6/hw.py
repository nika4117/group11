# შექმენით ფუნქცია, რომელიც მიიღებს რიცხვების სიას და თქვენ დააბრუნებთ მის გაფილტრულ ვერსიას,
# რომელსაც არ ექნება დუპლიკატები (ერთი და იგივე ელემენტები).


def dup(lst):
  lst3 = set(lst)
  print(list(lst3))

lstt = [1,2,3,4,5,2,2,2]
dup(lstt)
    for char in row:
        if len(row) % 2 != 0:
            lst.append(row[-1])
            row.replace(row[-1],"")
        else:
            if char == "R":
                if row[row.index(char) + 1] == "G":
                    lst.append("B")
                elif char == "R":
                    lst.append
                elif row[row.index(char) + 1] == "B":
                    lst.append("G")
            elif char == "G":
                if row[row.index(char) + 1] == "G":
                    lst.append("G")
                elif row[row.index(char) + 1] == "R":
                    lst.append("B")

                elif row[row.index(char) + 1] == "B":
                    lst.append("R")
            elif char == "B":
                if row[row.index(char) + 1] == "G":
                    lst.append("R")
                elif row[row.index(char) + 1] == "R":
                    lst.append("G")

                elif row[row.index(char) + 1] == "B":
                    lst.append("B")          
    m = set(lst)
    return list(m)
        

i = [] 
print(len(i))

