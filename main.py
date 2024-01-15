import pandas

df=pandas.read_csv("hotels.csv", dtype={"id" : str})
df_card=pandas.read_csv("cards.csv",dtype=str).to_dict(orient="records")
df_cardSecurity=pandas.read_csv("card-security.csv",dtype=str).to_dict(orient="records")

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id=hotel_id
        self.name=df.loc[df["id"]==self.hotel_id, "name"].squeeze()

    def book(self):
        # "Book hotel by changing availability to no"
        df.loc[df["id"]==self.hotel_id,"available"]="no"
        df.to_csv("hotels.csv",index=False)

    def available(self):
        # "Checks availability of hotel"
        availability=df.loc[df["id"]==self.hotel_id,"available"].squeeze()
        if availability=="yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name=customer_name
        self.hotel=hotel_object
    def generate(self):
        content=f"""
        Thanks For your Reservation!
        Here are your booking data:
        Name:{self.customer_name}
        Hotel name:{self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self,number):
        self.number=number

    def card_validate(self,expiration,holder,cvc):
        card_data={"number":self.number,"expiration":expiration,"holder":holder,"cvc":cvc}
        if card_data in df_card:
            return True
        else:
            return False


class SecureCreditCard:
    def check_card(self,number,password):
        security_data={"number":number,"password":password}
        if security_data in df_cardSecurity:
            return True
        else:
            return False


class SpaPackage:
    def __init__(self,name,hotel):
        self.name=name
        self.hotel=hotel
    def custmoner_ans(self,ans):
        if ans=="yes":
            content = f"""
            Thanks For your Spa Reservation!
            Here are your booking data:
            Name:{self.name}
            Hotel name:{self.hotel.name}"""
            print(content)
        else:
            print("Hotel booked Successfully")


print(df)
hotel_ID=input("Enter ID of the Hotel:")
if hotel_ID in df.loc[df["id"]==hotel_ID,"id"].squeeze():
    hotel=Hotel(hotel_ID)

    if hotel.available():
        credit_number=input("Enter your card number:")
        password=input("Enter card password:")
        secure_card=SecureCreditCard()
        if secure_card.check_card(credit_number,password):
            credit_card=CreditCard(credit_number)
            if credit_card.card_validate("12/26","JOHN SMITH","123"):
                hotel.book()
                name=input("Enter your name:")
                reservation_ticket=ReservationTicket(name,hotel)
                print(reservation_ticket.generate())
                spa_ques=input("Do you want to book Spa package?:")
                spa_package=SpaPackage(name,hotel)
                spa_package.custmoner_ans(spa_ques)
            else:
                print("There was a problem with your payment")
        else:
            print("Wrong card number or password")
    else:
        print("Hotel is not free")
else:
    print("Hotel ID is wrong, Please enter again.")
