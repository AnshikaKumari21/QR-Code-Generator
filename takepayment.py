import qrcode

#taking UPI ID as a input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=Name&am=Amount&cu=CURRENCY&tn=MESSAGE
#pa, pn, am , cu, tn all these are the parameters of the UPI QR code
#pa = payee address (UPI Id)
#pn = payee Name
#am=amount
#cu = currency
#tn=transaction note
#mc= mechant code

#payment URL based on the UPI ID and the Payment app
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#generating QR code for Phonepe
phonepe_qr = qrcode.make(phonepe_url)

#generating QR code for Paytm
paytm_qr=qrcode.make(paytm_url)


#generating QR code for Google Pay
google_pay_qr=qrcode.make(google_pay_url)

#to save the QR codes as PNG files, you can use the save() method of the QR code object, as shown above. The generated PNG files will be saved in the current working directory with the specified names (phonepe_qr.png, paytm.png, google_pay.png).
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm.png")
google_pay_qr.save("google_pay.png")



#to display the QR codes, you can use an image viewer or open the generated PNG files, for that yoy need to install PIL/Pillow library
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

