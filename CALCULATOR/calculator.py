def add(a, b) :
    return a+b
def sub(a ,b) :
    return a-b
def divide(a, b) :
    return a/b
def multiply(a, b) :
    return a*b
def power(a, b) :
    return a**b
def sq_root(c) :
    return c**0.5
def percentage(a, b) :
    return (b*a)/100

with open("history.txt","a") :
    pass
def calculator() : 
    while True :

        print("================================================================ CALCULATOR ================================================================")
        print("1. ADDITION \n2. SUBSTRACTION \n3. DIVISION \n4. MULTIPLICATION \n5. POWER \n6. SQUARE ROOT \n7. PERCENTAGE \n8. VIEW HISTORY \n9. CLEAR HISTORY \n10. EXIT")
        choice = (input("enter your choice :"))





        if choice == "1" :
            print("================================================================ ADDITION ================================================================")
            try :
                add1 = int(input("enter your first number :"))
                add2 = int(input("enter your second number :"))
                result = add(add1, add2)
                with open("history.txt","a") as history :
                    history.write(f"{add1} + {add2} = {result} \n")
                print(result)
            except ValueError :
                print("invalid choice")
                
        elif choice == "2" :
            print("=============================================================== SUBSTRACTION ===============================================================")
            try :
                add1 = int(input("enter your first number :"))
                add2 = int(input("enter your second number :"))
                result = sub(add1, add2)
                with open("history.txt","a") as history :
                    history.write(f"{add1} - {add2} = {result} \n")
                print(result)
            except ValueError :
                print("invalid choice")
                
        elif choice == "3" :
            print("================================================================ DIVISION ================================================================")
            try :
                add1 = int(input("enter your numerator :"))
                add2 = int(input("enter your denominator :"))
                if add2 == 0 :
                    print("not valid")
                else :
                    result = divide(add1, add2)
                    with open("history.txt","a") as history :
                        history.write(f"{add1}/{add2} = {result} \n")
                    print(result)
            except ValueError :
                print("invalid choice")
                
        elif choice == "4" :
            print("============================================================== MULTIPLICATION ==============================================================")
            try :
                add1 = int(input("enter your first number :"))
                add2 = int(input("enter your second number :"))
                result = multiply(add1, add2)
                with open("history.txt","a") as history :
                    history.write(f"{add1}*{add2} = {result} \n")
                print(result)
            except ValueError :
                print("invalid choice")

        elif choice == '5' :
            print("================================================================ POWER ================================================================")
            try :
                add1 = int(input("enter your base :"))
                add2 = int(input("enter your exponent :"))
                result = power(add1, add2)
                with open("history.txt","a") as history :
                    history.write(f"{add1}^{add2} = {result} \n")
                print(result)
            except ValueError :
                print("invalid choice")
                    
        elif choice == '6' :
            print("================================================================ SQUARE ROOT ===============================================================")
            try :
                add1 = int(input("enter your number :"))
                if add1 < 0 :
                    print("negetive number")

                else :
                    result = sq_root(add1)
                    with open("history.txt","a") as history :
                        history.write(f"{add1}^1/2 = {result} \n")
                    print(result)
            except ValueError :
                print("invalid choice")
                
        elif choice == "7" :
            print("================================================================ PERCENTAGE ================================================================")
            try :
                add1 = int(input("enter your number :"))
                add2 = int(input("enter your percentage :"))   
                result = percentage(add1, add2)
                with open("history.txt","a") as history :
                    history.write(f"{add1} of {add2}% = {result} \n")
                print(result)
            except ValueError :
                print("invalid choice")
        elif choice == '8' :
            with open("history.txt", "r") as history :
                data = history.read()
                if data == "" :
                    print("no calculation found")
                    
                else :
                    print(data, end ="")
                    print("history printed sucessfully !!!")
                    

        elif choice == "9" :
            with open("history.txt","r") as history :
                data = history.read()
            if data == "" :
                print("no calculation found")
                

            else :
                while True :
                    choice2 = input("are you sure you want to delete your history (yes[y]/no[n]) :")

                    if choice2.lower() == "y" :
                        print("history deleted sucessfully")
                        with open("history.txt","w") as history:
                                pass
                        break
                    elif choice2.lower() == "n" :
                        print("history is not deleted")
                        break

                    else :
                        print("invalid input \ntry again !!") 
                        
        elif choice == "10" :
            print("function closed")
            return
        else :
            print("invalid number")
            


calculator()