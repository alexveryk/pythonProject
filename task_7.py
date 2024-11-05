some_text = ("Qui aliquid deserunt id reprehenderit corrupti ut perferendis aliquam est modi veritatis "
        "eum inventore velit on eveniet animi aut eaque similique ad recusandae doloremque est quibusdam "
        "expedita aut delectus beatae. ")

def modified_text(text):
    count_value = text.lower().count("a")
    modified = text.lower().replace("a", "z").capitalize()
    print("Symbols have been replaced:", count_value, "\nChanged text: ", modified)

modified_text(some_text)