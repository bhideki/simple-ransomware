import pyaes


filename = "test.png"
KEY = b"hidekipasswordal"



with open(filename, "rb") as file:
    content = file.read()


crypto_data = pyaes.AESModeOfOperationCTR(KEY).encrypt(content)

new_filename = "{}.hideki".format(filename)
with open(new_filename, "wb") as file:
    file.write(crypto_data)