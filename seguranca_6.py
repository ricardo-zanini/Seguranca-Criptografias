entrada = """WKLV LV WKH RQOB OLQH WKDW UHDOOB XVHV FUBSWRJUDSKB"""
saida = ""
for c in entrada:
    if c != " ":
        saida += chr(ord(c) - 3)
    else:
        saida += " "

print("Programa 6: " + saida)

# ================= RESULTADO =================
# THIS IS THE ONL? LINE THAT REALL? USES CR?PTOGRAPH?
# =============================================