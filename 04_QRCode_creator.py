import qrcode

url = input("Enter the URL to generate QR code: ").strip()
file_name = input("Enter the name of the file where your QR-code will be saved: ").strip()

qr = qrcode.QRCode(
    version=4,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls error correction level
    box_size=10,  # controls how many pixels each "box" of the QR code is
    border=4,  # controls the thickness of the border
)

qr.add_data(url)

qr.make()

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{file_name}.png")
print(f"QR-Code saved as: {file_name}.png")
