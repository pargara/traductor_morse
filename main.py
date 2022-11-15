codigoM = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}
def encriptar(mensaje):
    cifrar = ''
    for letra in mensaje:
        if letra != ' ':
            cifrar += codigoM[letra] + ' '
        else:
            cifrar += ' '
    return cifrar

mensaje = "Hey dude"
resultado = encriptar(mensaje.upper())
print(resultado)
