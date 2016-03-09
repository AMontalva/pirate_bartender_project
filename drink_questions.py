import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def drink_questions():
    response_dict = {}
    for q_key in questions:
        response = input(questions[q_key] + " ")
        if(response == "y" or response == "yes"):
            response_dict[q_key] = True
        else:
            response_dict[q_key] = False
    return response_dict

# drink_questions()

def construct_drink():
    drink = []
    response_dict = drink_questions()
    print(response_dict)
    for r_key in response_dict:
        print(response_dict[r_key])
        if(response_dict[r_key] == True and r_key in ingredients):
            drink.append(random.choice(ingredients[r_key]))
    print(drink)
    
construct_drink()

# if __name__ == '__main__':
#     drink_questions()