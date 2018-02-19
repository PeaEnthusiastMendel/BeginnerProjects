##Exersice 3
##http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
##List less than ten

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
limit = int(input("Choose a limit (recommended is 10: "))
for i in range(len(a)):
    if a[i] < limit:
        b.append(i)

print(b)
        
