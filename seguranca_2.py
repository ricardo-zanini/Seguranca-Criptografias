entrada = """41 53 43 49 49 20 63 6f 64 65 20 69 73 20 6f 6c 64 2c 20 62
75 74 20 73 74 69 6c 6c 20 77 69 64 65 6c 79 20 75 73 65 64
2e 20 48 6f 77 65 76 65 72 2c 20 74 68 65 20 6e 65 78 74 20
74 77 6f 20 70 68 72 61 73 65 73 20 61 72 65 20 6f 6c 64 65
72 20 74 68 61 6e 20 41 53 43 49 49 21"""

resultado = ""
for byte in entrada.split():
    valor = chr(int(byte, 16))
    resultado += valor
print("Programa 2: " + resultado)

# ================= RESULTADO =================
# ASCII code is old, but still widely used. However, the next two phrases are older than ASCII!
# =============================================