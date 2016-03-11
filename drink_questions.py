import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": [ "glug of rum", "slug of whisky", "splash of gin" ],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

inventory = {
    "glug of rum": 3, "slug of whisky": 3, "splash of gin": 3, 
    "olive on a stick": 3, "salt-dusted rim": 3, "rasher of bacon": 3, 
    "shake of bitters": 3, "splash of tonic": 3, "twist of lemon peel": 3, 
    "sugar cube": 3, "spoonful of honey": 3, "spash of cola": 3, 
    "slice of orange": 3, "dash of cassis": 3, "cherry on top": 3
}

drink_names_1 = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
drink_names_2 = ['cat', 'dog', 'bird', 'lion', 'bear', 'hippo']

preferences = {}

regular_customers = {}

def check_inventory(drink_ingredients):
    """subtract inventory from ingredients used to contruct drink
    add to inventory when ingredients get too low"""
    for ingredient in drink_ingredients:
        if(ingredient in inventory):
            inventory[ingredient] = inventory[ingredient] - 1
            if(inventory[ingredient] < 0):
                print("Time to restock {0}!".format(ingredient))
                inventory[ingredient] = 10
    print("Inventory: {0}".format(inventory))

def get_customer_name():
    """get customer name
    run program depending on regular customers choices"""
    customer_name = input("What is your name? ")
    if(customer_name in regular_customers):
        the_usual = input("The ususal?(y/n) ")
        if(the_usual == 'y'):
            print("{0}'s usual drink: {1}".format(customer_name, regular_customers[customer_name]))
            check_inventory(regular_customers[customer_name])
        else:
            drink_questions()
            construct_drink(preferences, customer_name)
    else:
        regular_customers[customer_name] = ""
        drink_questions()
        construct_drink(preferences, customer_name)

def drink_questions():
    """ get the drink preferences of a customer with 5 questions"""
    for q_key in questions:
        response = input(questions[q_key] + " ")
        if(response == "y" or response == "yes"):
            preferences[q_key] = True
        else:
            preferences[q_key] = False
    print("Drink preferences {0}".format(preferences))
    return preferences

def construct_drink(preferences, customer_name):
    """construct drink based on preferences and regular customer name
    take stock of drink ingredient created
    update the regular customer drink"""
    drink = []
    for r_key in preferences:
        if(preferences[r_key] == True and r_key in ingredients):
            drink.append(random.choice(ingredients[r_key]))
    check_inventory(drink)
    print("Drink contructed: {0}".format(drink))
    
    random_drink_name_1 = random.choice(drink_names_1)
    random_drink_name_2 = random.choice(drink_names_2)
    drink_name = random_drink_name_1 + " " + random_drink_name_2
    print("Drink name: {0} ".format(drink_name))

    regular_customers[customer_name] = drink_name
    

if __name__ == '__main__':
    condition = True
    while(condition):
        get_customer_name()
        another_reply = input("Would you like another drink? (y/n) ")
        if(another_reply == "n" or another_reply == "no"):
            condition = False