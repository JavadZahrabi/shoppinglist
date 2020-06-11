# have a Help command
def show_help():
    #print out the instructions on how use app
    print("""
    Enter 'DONE' to stop adding items
    Enter 'SHOW' to show the shopping list
    Enter 'HELP' to show app instruction
    """)
    print("What should we pick up at the stor?")


#have a SHOW command
def show_list():
    print("Here is your list:")
    for item in shopping_list:
        print(item)


#add new item to shopping list
def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {}." .format(new_item, len(shopping_list)))


#make a shopping list to hold items
shopping_list = []

show_help()



while True:
    #ask for new items
    new_item = input(">")

    #to quite inputing items
    if new_item == 'DONE':
        show_list()
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)

#just for test ssh key