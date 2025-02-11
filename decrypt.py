import pyaes



filename = "test.png.hideki"
KEY = b"hidekipasswordal"

with open(filename, "rb") as file:
    content = file.read()

decrypt_data = pyaes.AESModeOfOperationCTR(KEY).decrypt(content)

new_filename = filename.replace(".hideki", "")
with open(new_filename, "wb") as file:
    file.write(decrypt_data)