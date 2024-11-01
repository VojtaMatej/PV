import re


def append_jecna_postfix(username: str) -> str:
    if not re.match(r"[A-Za-z0-9]",username):
      raise Exception("Invalid username")
    return username + '@spsejecna.cz'

def append_seznam_postfix(username: str) -> str:
    if not re.match(r"[A-Za-z0-9]",username):
        raise Exception("Invalid username")
    return username + '@seznam.cz'


appender_postfix = append_jecna_postfix
print(appender_postfix("Novak"))
appender_post = append_seznam_postfix
print(appender_post("Novak"))

print("-------------------------------------------")
def create_email(appender_function, username : str) -> str:
    return appender_function(username)
appender_postfix = append_jecna_postfix
email1 = create_email(appender_postfix, "novak")
print(email1)  # Mělo by vrátit: novak@spsejecna.cz

appender_postfix = append_seznam_postfix
email2 = create_email(appender_postfix, "novak")
print(email2)  # Mělo by vrátit: novak@seznam.cz
print("-------------------------------------------")
def formatuj_prijimeni_prvni(jmeno, prijmeni :str) -> str:
    return prijmeni +" "+ jmeno
def formatuj_monogram(jmeno, prijmeni :str) -> str:
    return jmeno[0]+". " + prijmeni[0] + "."
def vyber_formatovaci_funkci(delka):
    if delka < 4:
        return formatuj_monogram
    else:
        return formatuj_prijimeni_prvni
print(formatuj_prijimeni_prvni("Karel", "Novak"))
print(formatuj_monogram("Karel", "Novak"))
print("----------------")
fomatovac  = vyber_formatovaci_funkci(3)
print(fomatovac("karel", "Novak"))
