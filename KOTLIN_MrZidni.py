print("---------------- Change Case Program ------------------")

inputUser = input("Masukkan kata atau kalimat : ")
inputUser = inputUser.lower()
titleCase = ""

print("Change To : \n1. UPPERCASE \n2. owercase \n3. Title Case \n")

inputPerintah = input("Masukkan perintah : ")
if inputPerintah == "1" :
    print(inputUser.upper())
elif inputPerintah == "2" :
    print(inputUser.lower())
elif inputPerintah == "3" :
    for x in inputUser.split():
        for y in x :
            if y == x[0]:
                titleCase += y.upper()
                continue
            titleCase += y.lower()
        titleCase += " "
            
print(titleCase)