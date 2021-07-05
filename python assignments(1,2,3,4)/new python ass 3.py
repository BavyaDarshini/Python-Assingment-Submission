Altitude = int(input("Enter the Altitude  : "))
if Altitude <= 1000:
    print("SAFE TO LAND")
elif Altitude > 1000 and Altitude <= 5000:
    print("BRING DOWN TO 1000")
else:
    print("GO AROUND AND TRY LATER")
