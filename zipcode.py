from banner import banner

banner("Newaygo County Zip Code Sorter" , "Dylan Cook")

print("Welcome to The Newaygo Zip Code Sorter")

while True:
    zipcode = int(input("Please enter a zip code. "))

    if zipcode == 49412 :
        print("Zip Code 49412 belongs to Fremont")
    elif zipcode == 49413 :
        print("Zip Code 49413 belongs to Fremont")
    elif zipcode == 49337 :
        print("Zip Code 49337 belongs to Newaygo and Croton")
    elif zipcode == 49309 :
        print("Zip Code 49309 belongs to Bitely")
    elif zipcode == 49312 :
        print("Zip Code 49312 belongs to Brohman")
    elif zipcode == 49327 :
        print("Zip Code 49327 belongs to Grant")
    elif zipcode == 49349 :
        print("Zip Code 49349 belongs to White Cloud")
    else:
        print("Zip Code is not in Newaygo County")
    yesno = input("Would you like to enter another Zip Code? (Y/N)")
    if yesno == "y"
        continue
    else:
        break
