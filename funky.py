import random
def Upper_case(text):
    return text.upper()
def Space_to_Smilyface(text):
    return text.replace(' ', ':)')
def V_to_W(text):
    return text.replace("V","W")
def Return_Star_front_and_back(text):
    return "*"+text+"*"
def Multiple(text):
    return text.replace("?","???").replace("!","!!!!!")
Funky_functions = [Upper_case, Space_to_Smilyface, V_to_W,Return_Star_front_and_back,Multiple]
def Funky_format(text):

    for function in range(3):
        function = random.choice(Funky_functions)
        text = function(text)
    return text


print(Multiple("KArle!!!!"))
print(Funky_format("Ahoj Karle! Pudeme dnes do kina?"))
