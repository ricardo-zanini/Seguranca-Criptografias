entrada = """C5 C2 C3 C4 C9 C3 40 89 A2 40 81 A2 40 96 93 84 40 81 A2 40
C1 E2 C3 C9 C9 6B 40 82 A4 A3 40 89 A3 40 89 A2 40 81 93 94
96 A2 A3 40 85 A7 A3 89 95 83 A3 4B"""

byte_list = bytes(int(b, 16) for b in entrada.split())
text = byte_list.decode('cp037')
print("Programa 3: " + text)

# ================= RESULTADO =================
# EBCDIC is as old as ASCII, but it is almost extinct.
# =============================================