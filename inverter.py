def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

string = input(str('Digite uma palavra: '))
string_invertida = inverter_string(string)

print("String original:", string)
print("String invertida:", string_invertida)
