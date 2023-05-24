#write a program that takes a list of products as iniput and stops processing the list when it encounters the name of a product that has a certain rating specified by the user. for excamlpe, finding the first product in a list that has a rating of 4 star or above

b={}
for i in range(1,11):
    a=input("product:")
    c=int(input("rating:"))
    b.update({a:c})
    if c>=4:
        break
    print(a)
    



    