import qrcode
#prompt user for input
data=input('enter the information you want to encode: ')
qr=qrcode.QRCode(version=1, box_size=10, border=5)
#add the data to qr code
qr.add_data(data)
#generate qr code
qr.make(fit=True)
#create an image from the qr code
img=qr.make_image(fill_color='black',back_colour='white')
# Save the image as a PNG file
filename = input("Enter the filename to save the QR code as: ")

img.save(f"{filename}.png")

print(f"QR code saved as {filename}.png")
# Save the image as a PNG file
filename = input("Enter the filename to save the QR code as: ")

img.save(f"{filename}.png")

print(f"QR code saved as {filename}.png")
