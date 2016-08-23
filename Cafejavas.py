import random

questions = {
    "Tea": "Would you like a cup of tea?",
    "Coffee": "Do you like a cup of coffee?",
    "Juice": "Would you like a glass of juice?",
    "Mojito": "Would you like a mojito?"
}

ingredients = {
    "Tea": ["Ginger", "cinnamon", "Fennel seed"],
    "Coffee": ["carmon", "Black pepper", "cream"],
    "Juice": ["Pineapple", "mabgo", "Passion"],
    "Mojito": ["Sprite", "Lemon", "Mint"]
   
}

def find_preferences():
    preferences = {}
    for type, question in questions.items():
        print(question)
        preferences[type] = input().lower() in ["y", "yes"]
        print("")
    return(preferences)

def make_drink(preferences):
    drink = []
    for ingredient_type, liked in preferences.items():
        if not liked:
            continue


        drink.append(random.choice(ingredients[ingredient_type]))
    return(drink)



def main():
    preferences = find_preferences()
    drink = make_drink(preferences)
    print("One drink coming up.")
    print("it's full of good stuff.   The recipe is:")
    for ingredient in drink:
        print("A {}".format(ingredient))

if __name__ == '__main__':
    main()