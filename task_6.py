"""
Завдання:
Вам дано масив players із віком футболістів
players = [19, 19, 26, 25, 20 , 18,  30, 24, 27]
Вам потрібно обчислити і вивести на екран наступні значення:
3. Середній вік футболістів і вивести на екран це на екран.
Також обчислити значення, що дорівнює середньому віку
віднявши від нього максимальний вік.
"""
players = [19, 19, 26, 25, 20, 18, 30, 24, 27]

def middle_age(arr):
    acc = 0
    for i in arr:
        acc = acc + i
    return acc / len(arr)

#print(f"Середній вік: {middle_age(players):.2f}")

def age_difference(middle, arr):
    difference = middle - max(arr)
    return difference

#print(f"Різниця середнього від максимального віку: {age_difference(middle_age(players), players):.2f}")

"""
Дано два датасети( два списки(масиви, лісти) словників),вам потрібно порахувати, визначити 
та вивести на екран наступні речі:
3. Визначити меню із найменшою калорійністю(калорійність страви і напою потрібно додавати).
4. Вивести на екран всі меню калорійність яких менша 300 (калорійність страви і напою потрібно додавати).
"""
dishesh = [
    {
        'drink': 'orange_juice',
        'calorie_drink': 128,
        'food': 'spaghetti',
        'calorie_food': 450
    },
    {
        'drink': 'apple_juice',
        'calorie_drink': 102,
        'food': 'italian_spaghetti',
        'calorie_food': 555
    },
    {
        'drink': 'tea',
        'calorie_drink': 2,
        'food': 'boiled_potatoes',
        'calorie_food': 160
    },
    {
        'drink': 'double_tea',
        'calorie_drink': 4,
        'food': 'dumplings',
        'calorie_food': 477
    },
    {
        'drink': 'green_tea',
        'calorie_drink': 0,
        'food': 'fish',
        'calorie_food': 250
    }
]


def low_calorie(dishesh):
    arr = None

    for i in dishesh:
        if not arr:
            arr = i
        elif arr['calorie_food'] + arr['calorie_drink'] > i['calorie_food'] + i['calorie_drink']:
            arr = i

    return (f"Menu with the least calories: {arr['drink']} and {arr['food']} "
           f"total {arr['calorie_drink'] +arr['calorie_food']} calories")

print(low_calorie(dishesh))

"""
def low_calorie_menus(dishesh, calorie):
    arr = []
    for i in dishesh:
        if i['calorie_food'] + i['calorie_drink'] < calorie:
            arr.append(i)
    return arr

def details_calorie_menus(menu):
    for i in menu:
        print(f"{i['drink']} and {i['food']} have {i['calorie_drink'] + i['calorie_food']} calories")

details_calorie_menus(low_calorie_menus(dishesh, 300))
"""
"""
print(low_calorie(dishesh))
# Функція показує роботу метода max()
def max_number(arr):
    num = 0
    for i in arr:
        if i > num:
            num = i
    return num

"""