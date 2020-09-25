name = input("Ingresa tu nombre")
age = input("¿Cual es tu edad?")

def whoAmI():
    print("Me llamo " + name + " y tengo " + age + " años.")


def MyHobbies(hobby1, hobby2):
    print("Me gusta " + hobby1 + " pero prefiero mucho más el " + hobby2)


def myDecade():
    return int(age) // 10

whoAmI()
MyHobbies("hacer ejercicio", "fútbol")
decades = myDecade()
print("Las decadas que he vivido son " + str(decades))

