# Dictionaries are more like lists however we use {} 



### here we can see the differance between a list and a dictionary 

# my_cat = ["salem", "black", "moody"]

# my_cat = {
# "name":"salem",
# "colour":"black",
# "mood":"sassy"}

## the bit of data on the left hand side of the : is a key and the bit on the right side of the : is a value

# to updatea a value in a dictionary we would write it like 
# my_cat = ["name"] = "Whiskers" this is how to updatre a value by using the key 

##### Activity one

from itertools import count


pet_one = {
    "species":"Cat",
    "name":"Thomas",
    "colour":"black and white",
    "age":"17 years old"

}

pet_two = {
    "species":"Dog",
    "name":"Rocky",
    "colour":"black",
    "age":"6 months"
}

pet_three = {
    "species":"Cat",
    "name":"jinx",
    "colour":"black",
    "age":"3 years old"
}

# i am going to update a few of my items in my dictinoary

# pet_one = ["name"] = "Tim Tom"
print(pet_one["name"])

# print(list(pet_one)) this shows the values in the dictinoary as a list when printed  

# print(my_cat.keys()) 
#Expected: dict_keys(['name', 'colour', 
# 'mood']) 
# print(my_cat.values()) 
#Expected: dict_values(['Salem', 'black', 
# 'sassy']) 
# print(my_cat.items()) 
#Expected: dict_items([('name', 'Salem'), 
# ('colour', 'black'), ('mood', 'sassy')])

# for j in my_cat.keys():
    # print(j)


## this is how we loop throguh our dictionary this would loop through th ekeys and 
# .values would loop throught he values and ext..
# to remove keys we just use .pop
# we specify the item we want to delete by using its key
# there is also delete method shown as 
# del 
#

###### Activity Two


countries = {
    "United Kingdom":"London",
    "France":"Paris",
    "Germnay":"Berlin",
    "Spain":"Madrid",
    "Italy":"Rome"
}

x = countries.setdefault("Austrelia", "Canberra")
y = countries.setdefault("China", "Beijing")

countries["United Kingdom"] = "English"
countries["France"] = "French"
countries["Germnay"] = "German"
countries["Spain"] = "Spanish"
countries["Austrelia"] = "English"
countries["China"] = "Mandarin"


print(list(countries.items()))


#### Activtiy Three

fav_songs = [
    {
        "artist":"Agasint the current",
        "song_name":"weapon",
        "genre":"pop rock",
        "release_year":"2021"
    }
    
]