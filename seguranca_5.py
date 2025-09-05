
import base64

entrada = """QmFzZSA2NCBjYW4gYmUgdXNlZCB0byBlbmNvZGUgZS1tYWlsIGF0dGFjaG1lbnRzLg==
"""

base64_bytes = entrada.encode("utf-8")
texto_bytes = base64.b64decode(base64_bytes)
texto = texto_bytes.decode("utf-8")

print("Programa 5: " + texto)

# ================= RESULTADO =================
# Base 64 can be used to encode e-mail attachments.
# =============================================