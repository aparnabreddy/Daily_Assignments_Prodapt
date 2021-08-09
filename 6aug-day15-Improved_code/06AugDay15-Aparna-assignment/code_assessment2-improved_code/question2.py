import re, smtplib, logging
while(True):
    Name=input("Please Enter your Name :")
    Email=input("Please Enter the Email Id :")
    regex = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    validation=re.match(regex,Email)
    if validation:
        class tea:
            def tea_price(self):
                self.tea=7
                return self.tea

        class Coffee:
            def coffee_price(self):
                self.coffe=10 
                return self.coffe
        
        class Masala_Dosa:
            def dosa_price(self):
                self.dosa=50
                return self.dosa
        class Bill_Order(Coffee,tea,Masala_Dosa):
             pass

        billing=Bill_Order()
        cost=0

        while(True):
            print("1. Tea (Rs.7)")
            print("2. Coffee (Rs.10)")
            print("3. Masala Dosa (Rs.50)")
            print("4. View Bill and Email ")
            try:
                choice=int(input("Enter your Order choice:"))
            except ValueError:
                logging.error("Choice should be an integer")
            
            if choice==1:
                print("\nTea selected")
                tea1=billing.tea_price()
                cost+=tea

                    
            if choice==2:
                print("\nCoffee selected")
                coffee=billing.coffee_price()
                cost+=coffee

            if choice==3:
                print("\nMasala Dosa Selected")
                dosa=billing.dosa_price()
                cost+=dosa
                
            if choice==4:
                print("Your Bill ")
                print("Rs",cost)
                message=str(cost)
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("sowmya070721@gmail.com","sowmya@0707")
                connection.sendmail("aparnabreddy26@gmail.com",Email,message)
                print("Email sent successfully")
                connection.quit()
                break
        break 
    else:
        print("Please Enter valid email id and try again")
        continue