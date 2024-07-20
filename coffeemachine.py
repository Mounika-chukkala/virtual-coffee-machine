import itemsandstock,os,time,logo
os.system('clear')
money=0
def checkstock(order):
    global products,coffees,stocks
    for i in range(len(coffees)):
        if(coffees[i]["type of coffee"]==order):
            for j in range(len(stocks)):
                for k in stocks[j]:
                    if(coffees[i][k]>stocks[j][k]):
                        shrt=coffees[i][k]-stocks[j][k]
                        print(f"you have shortage of {k} - {shrt}")
                        return -1
                    else:
                        stocks[j][k]-=coffees[i][k]
def add_coins():
    print("We only accept 1,2,5,10 rupee coins")
    one_c=int(input("Enter number of 1 rupee coins:"))*1
    two_c=int(input("Enter number of 2 rupee coins:"))*2
    five_c=int(input("Enter number of 5 rupee coins:"))*5
    ten_c=int(input("Enter number of 10 rupee coins:"))*10
    money_paid=one_c+two_c+five_c+ten_c
    return money_paid 
def stock_report():
    print("-----------****-----------")
    for i in range(len(stocks)):
        for j in stocks[i]:
            print(f"{j}= {stocks[i][j]}")
    print("----------****------------")
def add_stock():
    for i in range(len(stocks)):
        for j in stocks[i]:
            stocks[i][j]+=int(input(f"enter the amount of {j} you want to add:"))
def show_money():
    print(f"money we have is {money}")
def withdraw_money():
    global money
    amt=float(input("enter the amount of money you want to withdraw:"))
    if(amt>money):
        print(f"{amt} rupees are not in coffee machine ..try again")
        return -1
    money-=amt
    print(f"{amt} is withdrawn and you are left with {money} rupees")
money_paid=0
def pay_Amount(order):
    for i in range(len(coffees)):
        if(coffees[i]["type of coffee"]==order):
            need_to_pay=coffees[i]["price"]
    print(f"you need to pay {need_to_pay}")
    money_paid=add_coins()
    global money
    while(need_to_pay>money_paid):
        req=need_to_pay-money_paid
        print(f"you need to add {req} money")
        added_money=add_coins()
        money_paid+=added_money
    if(need_to_pay<money_paid):
        print("you have entered the money more than required")
        change=money_paid-need_to_pay
        print(f"{change} is your change")
        money_kept=money_paid-change
        money+=money_kept
    elif(need_to_pay==money_paid):
        print("thanks for ordering")
        money+=money_paid
        return money_paid
products=["steamed milk","milk foam","espresso","hot chocolate"]
stocks=[{"steamed milk":500},{"milk foam":500},{"espresso":500},{"hot chocolate":200}]
coffees=itemsandstock.item_stocks
types_of_coffees=[]
for i in range(len(coffees)):
        types_of_coffees.append(coffees[i]["type of coffee"])
# print(types_of_coffees)
machine_running=True
while(machine_running==True):
    print(f" welcome to {logo.coffee_machine}")
    person=input("\nEnter whether you are owner or customer or type 'off' to turn off the machine:\n").lower()
    if(person=="owner"):
        owner_running=True
        while(owner_running==True):
                print("---------***----------")
                option=int(input("You have the options as:\n1.want to see the stock report.\n2.want to add any stock\n3.want to see report of money you have \n 4.want to withdraw money\n 5.exit from owner profile.\nEnter your choice:"))
                print("----------***---------")
                if(option==1):
                    stock_report()
                elif(option==2):
                    add_stock()
                    wanna_see_stock=input("do you want to see stock(y/n):")
                    if(wanna_see_stock=='y'):
                        stock_report()
                elif(option==3):
                    show_money()
                elif(option==4):
                    password="Moni05..//"
                    entered=input("enter the password:\n")
                    if(password==entered):
                        m=withdraw_money()
                        if(m==-1):
                            try_Again=input("Do you want to withdraw again(y/n):").lower()
                            if(try_Again=='y'):
                                withdraw_money()
                    else:
                        print("you entered wrong password")
                        continue
                elif(option==5):
                    print("exiting from owner profile...\nBye Bye...Have a nice day")
                    time.sleep(2)
                    os.system('clear')
                    break
    elif(person=="customer"):
        customer_buying=True
        while(customer_buying==True):
            print("--------------***------------------")
            print("\tMENU")
            print("-------------***-------------------")
            for i in range(len(types_of_coffees)):
                print(f"\t{i+1}.{types_of_coffees[i]}")
            print("---------------********----------------")
            order=int(input("enter your order:"))
            pl_ord=types_of_coffees[order-1]
            is_there=checkstock(pl_ord)
            if(is_there==-1):
                print("there is shortage of stock for that coffee order something else.")
            else:
                print(f"You ordered {pl_ord}")
                pay_Amount(pl_ord)
                print(f"your {pl_ord} is ready")
            wanna_buy_again=input("do you want to buuy again ...type 'y' if yes or type 'off' to exit:").lower()
            if(wanna_buy_again=='y'):
                customer_buying=True
            elif(wanna_buy_again=='off'):
                print("thanks for using our coffee machine have a nice day...")
                time.sleep(2)
                os.system('clear')
                customer_buying=False
    elif(person=='off'):
        print("bye bye machine is turning off")
        machine_running=False
        
        