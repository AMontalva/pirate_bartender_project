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

ingredients_stock = {
    "glug of rum": 10, "slug of whisky": 5, "splash of gin": 10, 
    "olive on a stick": 10, "salt-dusted rim": 5, "rasher of bacon": 10, 
    "shake of bitters": 10, "splash of tonic": 5, "twist of lemon peel": 10, 
    "sugar cube": 10, "spoonful of honey": 5, "spash of cola": 10, 
    "slice of orange": 10, "dash of cassis": 5, "cherry on top": 10
}

response_dict = {}

regular_customers = {}

def take_stock(ingredient_list):
    for ingredient in ingredient_list:
        if(ingredient in ingredients_stock):
            ingredients_stock[ingredient] = ingredients_stock[ingredient] - 1
    print(ingredients_stock)

def get_customer_name():
    customer_name = input("What is your name? ")
    if(customer_name in regular_customers):
        the_usual = input("The ususal?(y/n) ")
        if(the_usual == 'y'):
            print(regular_customers[customer_name])
            take_stock(regular_customers[customer_name])
        else:
            drink_questions()
            construct_drink(response_dict, customer_name)
    else:
        regular_customers[customer_name] = ""
        drink_questions()
        construct_drink(response_dict, customer_name)


def drink_questions():
    for q_key in questions:
        response = input(questions[q_key] + " ")
        if(response == "y" or response == "yes"):
            response_dict[q_key] = True
        else:
            response_dict[q_key] = False
    return response_dict

# drink_questions()


def construct_drink(response_dict, customer_name):
    drink = []
    print(response_dict)
    for r_key in response_dict:
        print(response_dict[r_key])
        if(response_dict[r_key] == True and r_key in ingredients):
            drink.append(random.choice(ingredients[r_key]))
    take_stock(drink)
    print(drink)
    regular_customers[customer_name] = drink
    
# construct_drink(response_dict)


if __name__ == '__main__':
    condition = True
    while(condition):
        get_customer_name()
        another_reply = input("Would you like another drink? (y/n) ")
        if(another_reply == "n" or another_reply == "no"):
            condition = False