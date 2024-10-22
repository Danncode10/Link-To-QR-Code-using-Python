import qrcode

#Get the URL input from the user
url_input = input("Enter the URL you want to generate a QR code for: ")

#Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Less error correction (saves space)
    box_size=10,  # Size of each box in the QR code
    border=4,  # Thickness of the border
)
qr.add_data(url_input)
qr.make(fit=True)  # Automatically fit the QR code

#Create the image
img = qr.make_image(fill='black', back_color='white')

# Save the image as Output.jpeg
img.save("Output.jpeg")

print("QR code generated and saved as Output.jpeg")
