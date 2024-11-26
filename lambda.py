from tkinter.ttk import Treeview


def Druha_mocnina(cislo):
    return cislo*cislo
x = Druha_mocnina
y = x
print(Druha_mocnina(5))
print(x(3))
print(y(4))


x = lambda a : a*a
krokovaci_funkce_po_dvou = lambda x : x+2
nasobici_funkce = lambda a,b : a*b
linearni_funkce = lambda a,b,x : a*x+b
konstantni_funkce_peti = lambda : 5
print(krokovaci_funkce_po_dvou(2))
print(nasobici_funkce(2,4))
print(linearni_funkce(2,4,2))
print(konstantni_funkce_peti())

vysledky = [
    ("Karel", 31),
    ("Petr", 10),
    ("Honza", 52),
    ("Eva", 61),
    ("Katka", 0),
]
x = sorted(vysledky, key=lambda x: x[1])
print(x)
zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "category" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "category" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "category" : (4, "Sluchátka")
    }
]
x = sorted(zbozi, key=lambda x: x["price"])
y = sorted(zbozi, key=lambda x: x["name"])
z = sorted(zbozi, key=lambda x: x["category"], reverse=True)
print(x)
print(y)
print(z)

print("----------------------------")
pole = [100.10, 323.2, 355.9, 214.19, 87.0]
pole2 = []
pole3 = []
pole4 = []
def myFunc(x):
    if x >= 120.0:
        return True
    else:
        return False

percent_more = lambda x : x + x*0.3
more_than_120 = lambda x,y: list(filter(x, y))
percent_more2 = lambda x : x + x*1.2
for i in pole:

    pole2.append(percent_more(i))
print(pole2)
print(list(filter(myFunc, pole)))
print("-------------------------")
print(more_than_120(myFunc,pole))
for i in pole:
    pole3.append(percent_more2(i))
print(pole3)
