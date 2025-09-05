letras_morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']

entrada = """-.-. --- -.. .. --. --- -- --- .-. ... . . .... ..-. .-
-.-. .. .-.. -.. . .-. . -.-. --- -. .... . -.-. . .-.
"""

resultado = ""

for morse in entrada.split():
    for letra_morse in letras_morse:
        if morse == letra_morse:
            resultado += chr(letras_morse.index(letra_morse) + 65)
            
print("Programa 1: " + resultado)


# ================= RESULTADO =================
# CODIGOMORSEEHFACILDERECONHECER
# =============================================