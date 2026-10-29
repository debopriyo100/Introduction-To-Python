a = float(input("Enter your Grade: "))


if a < 0 or a > 20:
    print ("Invalid Grade")
elif a >= 16:
    print ("Very Good")

elif a >= 14:
    print ("Good")
elif a >= 12:
    print ("Fairly Good")
elif a >=10:
    print ("Pass")

else : 
    print ("Fail")