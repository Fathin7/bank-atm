class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def check_balance(self):
        print("Your Balance is 1000000")

    def withdrawal(self,amount):
        new_amount=1000000-amount
        print("You Have Withdrawn Amount"+str(amount) +".Your Remaining Balance Is "+str(new_amount))

def main():
    cardnumber=input("insert your card number:-")
    pin_number=input("enter your pin_number:-")

    new_user=Atm(cardnumber,pin_number)

    print("Choose your Activity")
    print("1.Balance Enquiry  2.Withdrawal")
    activity=int(input("enter activity number:-"))

    if(activity==1):
        new_user.check_balance()
    elif(activity==2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawal(amount)
    else:
        print("enter a valid number")


if __name__=="__main__":
    main()