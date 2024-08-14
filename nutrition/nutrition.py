def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "necatrine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pinneaple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }

    user_input = input("Item: ").lower()

    for fruit in fruits:
        if user_input == fruit:
            print(fruits[fruit])
            
main()
