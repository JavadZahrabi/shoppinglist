#make a shopping list to hold items
shopping_list = []

#print out instructions to how use app
print("What should we pick up at the stor?")
print("Type 'DONE' to stop adding items")

while True:
    #ask for new items
    new_item = input(">")

    #to quite inputing items
    if new_item == 'DONE':
        break

    # add new item to the shopping list
    shopping_list.append(new_item)

print("Here's your list:")

for item in shopping_list:
    #print items
    print(item)

#just for test
