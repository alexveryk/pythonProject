'''
3.Дано послідовність слів, відокремлених пропусками, в кінці крапка.
Замінити зі стрічки всі попередні входження літери “a” на “z”.
'''

text = ("Qui aliquid deserunt id reprehenderit corrupti ut perferendis aliquam est modi veritatis "
        "eum inventore velit on eveniet animi aut eaque similique ad recusandae doloremque est quibusdam "
        "expedita aut delectus beatae. ")

count_value = text.lower().count("a")
modified_text = text.lower().replace("a", "z").capitalize()

print("Symbols have been replaced:", count_value, "\nChanged text: ",modified_text)