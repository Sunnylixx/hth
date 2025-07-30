food="cheese cake"
    # 012345678910

# food[start:stop]
print(food[0:3])
print(food[-1])
first_char=food[0]
last_char=food[-1]
combined_chars=first_char+last_char
print(combined_chars)
food_words=food.split()
print(food_words)#output:['cheese','cake']
rejoined_food="".join(food_words)
print(rejoined_food)#output:cheese cake 
number_list=[1,2,3,4,5]
new_number=6
number_list.append(new_number)
print(number_list)
element_to_add=6 
number_list.insert(3,element_to_add)
print(number_list)
removed_element=number_list.pop()
print(number_list)
print(removed_element)
number_list.remove(2)
print(number_list)
first_three=number_list[:3]
print(first_three)
last_three=number_list[-3:]
print(last_three)
books={'Franz Kafka':'The Metamorphosis','Osamu Dazai':'No Lobger Human',"Fyodor Dostoevsky":"Crime and Punishment"}
book_keys_view=books.keys()
book_keys_list=list(book_keys_view)
print(book_keys_list)
books_values_view=books.values()
print(books_values_view)
authur=books.get("The Metamorphosis")
authur=books.get("No Longer Human")
authur=books.get("Crimes and Punishment")
keys=list(books.keys)
keys_to_remove=keys[2]
removed_value=books.pop(keys_to_remove)
print(books)
first_key=next(iter(books))
del books[first_key]
print(books)