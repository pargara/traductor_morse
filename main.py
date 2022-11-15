codigoM = { "A":".-", "B":"-...",
                    "C":"-.-.", "D":"-..", "E":".",
                    "F":"..-.", "G":"--.", "H":"....",
                    "I":"..", "J":".---", "K":"-.-",
                    "L":".-..", "M":"--", "N":"-.",
                    "O":"---", "P":".--.", "Q":"--.-",
                    "R":".-.", "S":"...", "T":"-",
                    "U":"..-", "V":"...-", "W":".--",
                    "X":"-..-", "Y":"-.--", "Z":"--..",
                    ".":".-.-.-",",":"-.-.--"," ":"/"}
def encriptar(mensaje):
    cifrar = ""
    for letra in mensaje:
        if letra != "+":
            cifrar += codigoM[letra] + " "
        else:
            cifrar += ' '
    return cifrar

print(f"3 \n Hola mundo \n La mariposa revolotea, como si desesperara en este mundo \n Este es un mensaje programado en Python, pero codificado en morse")

mensaje = "Hola mundo"
resultado = encriptar(mensaje.upper())
print(resultado)
print(f"\n")

mensaje = "La mariposa revolotea, como si desesperara en este mundo."
resultado = encriptar(mensaje.upper())
print(resultado)
print(f"\n")

mensaje = "Este es un mensaje programado en Python, pero codificado en morse."
resultado = encriptar(mensaje.upper())
print(resultado)
print("\n")
