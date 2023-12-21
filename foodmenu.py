'''def print_menu(day):
    if day == 1:
        return "Monday's Food Menu"
    elif day == 2:
        return "Tuesday Food Menu"
    elif day == 3:
        return "Wednesday Food Menu"
    elif day == 4:
        return "Thursday Food Menu"
    elif day == 5:
        return "Friday Food Menu"
    elif day == 6:
        return "Saturday Food Menu"
    elif day == 7:
        return "Sunday Food Menu"
    else:
        return "Invalid Day"

def print_breakfast_menu(day):
    if day in [1, 2, 3, 4, 5, 6, 7]:
        print("Breakfast Menu")
        price = 0
        while True:
            menu = input("Enter a breakfast menu:")
            if menu == "poha":
                price += 20
            elif menu == "bread pakoda":
                price += 30
            elif menu == "itali":
                price += 40
            elif day == 5 and menu == "smosa":
                price += 30
            elif day == 6 and menu == "uttapa":
                price += 70
            elif day == 7 and menu == "dosa":
                price += 60
            else:
                print("Invalid")
            ans = input("Do you want to continue?(y/n)")
            if ans != 'y':
                break
        print("Price Rs=" + str(price))
    else:
        print("Invalid Day")

def print_lunch_menu(day):
    if day in [1, 2, 3, 4, 5, 6, 7]:
        if day == 1:
            print("Lunch: Potato Vegetable, Flat Bread, Rice, Dal")
        elif day == 2:
            print("Lunch: Spinach Vegetable, Flat Bread, Rice, Dal")
        elif day == 3:
            print("Lunch: Cauliflower Vegetable, Flat Bread, Rice, Dal")
        elif day == 4:
            print("Lunch: Capsicum Vegetable, Flat Bread, Rice, Dal")
        elif day == 5:
            print("Lunch: Spinach Potato Vegetable, Flat Bread, Rice, Dal")
        elif day == 6:
            print("Lunch: Spinach Paneer Vegetable, Flat Bread, Rice, Dal")
        elif day == 7:
            print("Lunch: Kofte Vegetable, Flat Bread, Rice, Dal")
    else:
        print("Invalid Day")

def print_dinner_menu(day):
    if day in [1, 2, 3, 4, 5, 6, 7]:
        if day in [1, 4]:
            print("Dinner: Brinjal Vegetable, Flat Bread, Rice, Dal")
        elif day in [2, 5]:
            print("Dinner: Cabbage Vegetable, Flat Bread, Rice, Dal")
        elif day in [3, 6]:
            print("Dinner: Tomato Vegetable, Flat Bread, Rice, Dal")
        elif day == 7:
            print("Dinner: Gaur Vegetable, Flat Bread, Rice, Dal")
    else:
        print("Invalid Day")

print("Week Days")
print("1.Monday")
print("2.Tuesday")
print("3.Wednesday")
print("4.Thursday")
print("5.Friday")
print("6.Saturday")
print("7.Sunday")

day = int(input("Enter a day:"))
time = input("Enter a time(breakfast, lunch, dinner):")

menu = print_menu(day)

if menu != "Invalid Day":
    print(menu)
    if time == "breakfast":
        print_breakfast_menu(day)
    elif time == "lunch":
        print_lunch_menu(day)
    elif time == "dinner":
        print_dinner_menu(day)
else:
    print("Invalid Day")

print("Thank You")'''
print("Week Days")
print("1.Monday")
print("2.Tuesday")
print("3.Wednesday")
print("4.Thursday")
print("5.Friday")
print("6.Saturday")
print("7.Sunday")
day=int(input("Enter a day:"))
time=input("Enter a time(breakfast,lunch,dinner):")
price=0
if day==1:
    print("Monday's Food Menu")
    if time=="breakfast":
        while True:
            menu=input("Enter a breakfast menu:")
            if menu=="poha":
                price+=20
            elif menu=="bread pakoda":
                price+=30
            elif menu=="itali":
                price+=40
            else:
                print("Invalid")
            ans=input("Do you want to continue?(y/n)")
            if ans!='y':
                break
            print("Price Rs="+str(price))
    elif time=="lunch":
        print("Lunch: Potato Vegetable, Flat Bread,Rice,Dal")
    elif time=="dinner":
        print("Dinner:Brinjal Vegetable,Flat Bread,Rice,Dal")
elif day==2:
    print("Tuesday Food Menu")
    if time=="breakfast":
        while True:
            menu=input("Enter a breakfast menu:")
            if menu=="poha":
                price+=20
            elif menu=="bread pakoda":
                price+=30
            elif menu=="itali":
                price+=40
            else:
                print("Invalid")
            ans=input("Do you want to continue?(y/n)")
            if ans!='y':
                break
        print("Price Rs="+str(price))
    elif time=="lunch":
        print("Lunch: Spinach Vegetable, Flat Bread,Rice,Dal")
    elif time=="dinner":
        print("Dinner: Cabbage Vegetable,Flat Bread,Rice,Dal")
elif day==3:
    print("Wednesday Food Menu")
    if time=="breakfast":
        while True:
            menu=input("Enter a breakfast menu:")
            if menu=="poha":
                price+=20
            elif menu=="bread pakoda":
                price+=30
            elif menu=="itali":
                price+=40
            else:
                print("Invalid")
            ans=input("Do you want to continue?(y/n)")
            if ans!='y':
                break
            print("Price Rs="+str(price))
    elif time=="lunch":
            print("Lunch: Cauliflower Vegetable, Flat Bread,Rice,Dal")
    elif time=="dinner":
        print("Dinner:tomato Vegetable,Flat Bread,Rice,Dal")
elif day==4:
    print("Thursday Food Menu")
    if time=="breakfast":
        while True:
            menu=input("Enter a breakfast menu:")
            if menu=="poha":
                price+=20
            elif menu=="bread pakoda":
                price+=30
            elif menu=="itali":
                price+=40
            else:
                print("Invalid")
            ans=input("Do you want to continue?(y/n)")
            if ans!='y':
                break
        print("Price Rs="+str(price))
    elif time=="lunch":
        print("Lunch: Capsicum Vegetable, Flat Bread,Rice,Dal")
    elif time=="dinner":
        print("Dinner:Brinjal Vegetable,Flat Bread,Rice,Dal")
elif day==5:
    print("Friday Food Menu")
    if time=="breakfast":
        while True:
            menu=input("Enter a breakfast menu:")
            if menu=="poha":
                price+=20
            elif menu=="bread pakoda":
                price+=40
            elif menu=="itali":
                price+=40
            elif menu=="smosa":
                price+=30
            else:
                print("Invalid")
            ans=input("Do you want to continue?(y/n)")
            if ans!='y':
                break
        print("Price Rs="+str(price))
    elif time=="lunch":
        print("Lunch: Spinach Potato Vegetable, Flat Bread,Rice,Dal")
    elif time=="dinner":
        print("Dinner:Brinjal Vegetable,Flat Bread,Rice,Dal")
elif day==6:
    print("Saturday Food Menu")
    if time=="breakfast":
        while True:
            menu=input("Enter a breakfast menu:")
            if menu=="poha":
                price+=20
            elif menu=="bread pakoda":
                price+=30
            elif menu=="itali":
                price+=40
            elif menu=="uttapa":
                price+=70
            else:
                print("Invalid")
            ans=input("Do you want to continue?(y/n)")
            if ans!='y':
                break
        print("Price Rs="+str(price))
    elif time=="lunch":
        print("Lunch: Spinach Paneer Vegetable, Flat Bread,Rice,Dal")
    elif time=="dinner":
        print("Dinner:Lady Finger Vegetable,Flat Bread,Rice,Dal")
elif day==7:
    print("Sunday Food Menu")
    if time=="breakfast":
        while True:
            menu=input("Enter a breakfast menu:")
            if menu=="poha":
                price+=20
            elif menu=="bread pakoda":
                price+=30
            elif menu=="itali":
                price+=40
            elif menu=="dosa":
                price+=60
            else:
                print("Invalid")
            ans=input("Do you want to continue?(y/n)")
            if ans!='y':
                break
        print("Price Rs="+str(price))
    elif time=="lunch":
        print("Lunch: Kofte Vegetable, Flat Bread,Rice,Dal")
    elif time=="dinner":
        print("Dinner:Gaur Vegetable,Flat Bread,Rice,Dal")
else:
    print("Invalid")
print("Thank You")

