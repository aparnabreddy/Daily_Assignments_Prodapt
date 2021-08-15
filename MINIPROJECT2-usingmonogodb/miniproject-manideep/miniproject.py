import pymongo,logging,re,time,smtplib

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase= client["Gymdatabase"]
Collection_name =mydatabase["Gym"]
gymlist=[]
class Customer:
    def addCustomer(self,name,mobileNumber,emailId,Strength,Aerobics,Balance,Ca,Fm,total):
        current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
        dict1={"name":name,"mobileNumber":mobileNumber,"emailId":emailId,"Strength":Strength,"Aerobics":Aerobics,"Balance":Balance,"Ca":Ca,"Fm":Fm,"total":total,"AddOn":current_time}
        gymlist.append(dict1)
g=Customer()
def validate(name,mobileNumber,emailId):

        name1=re.search("[A-Za-z]{0,25}$",name)
        print(name1)
        mobileNumber1=re.search("^(\+91)[6-9]\d{9}$",mobileNumber)
        print(mobileNumber1)
        emailId1=re.search( "[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",emailId)
        print(emailId1)   
        if name1 and  mobileNumber1 and emailId1:
            return True
        else:
            return False  

while(True):

    print("1.Add Customer")
    print("2. view Customer")
    print("3.search customer using name")
    print("4.delete customer")
    print("5.update customer")
    print("6.Exit")
    choice=int(input("Enter your choice :"))

    if choice==1:
        name = input("Enter the name of Customer:")
        mobileNumber=input("Enter the mobilenumber:")
        emailId=input("Enter the email:")
        if validate(name,mobileNumber,emailId):

            print("MENU")
            print("1. Strength (Rs.700)")
            print("2. Aerobics (Rs.800)")
            print("3. Balance  (Rs.500)")
            print("4. coordination and agility (Rs.1000")
            print("5. Flexibility and Mobility (Rs.900")
            Strength = int(input("if u want Strength package press 1  id u dont want press 0 "))
            Aerobics = int(input("if u want Aerobics package press 1  id u dont want press 0 "))
            Balance = int(input("if u want balance  press 1  id u dont want press 0 "))
            Ca = int(input("if u want coordination and agility package press 1  id u dont want press 0 "))
            Fm = int(input("if u want Flexibilityand mobility package press 1  id u dont want press 0 "))
            # total = int(input('you have completed the order now press 6 to get your bill - '))
            total=Strength*700+Aerobics*800+Balance*500+Ca*100+Fm*900
            g.addCustomer(name,mobileNumber,emailId,Strength,Aerobics,Balance,Ca,Fm,total)
            result = Collection_name.insert_many(gymlist)
            print(result.inserted_ids)
            # total=Strength*700+Aerobics*800+Balance*500+Ca*100+Fm*900
            message="Your total amount is " +str(total)
            print(message)
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("manideepkotha324@gmail.com","mani@9324")
            connection.sendmail("manideepkotha324@gmail.com",emailId, message)
            connection.quit
            print("Mail sent successfully")
        else:
            print("Please enter correct infomation ")
            continue
                
    if choice==2:
        result = Collection_name.find()
        li=[]
        for i in result:
            li.append(i)
        print(li)
        #result.clear()
               
    if choice==3:
        p = input("enter the customer name")
        result1 = Collection_name.find({"name":p})
        li2 = []
        for i in result1:
            li2.append(i)
        print(li2)

    if choice==4:
        q= input('enter the customer name')
        result=Collection_name.delete_one({'name':q})
        print(result.deleted_count)
    if choice==5:
        name=input("enter the customer information u want to update")
        emailId=input("enter the customer email u want to update")
        result=Collection_name.update_one({"name":name},{"$set":{"emailId":emailId}})
        print("data has been modified")
        #print(result.modified_count)
    if choice==6:
         
        # for i in gymlist:
            
        #     total=Strength*700+Aerobics*800+Balance*500+Ca*100+Fm*900
        #     message="Your total amount is " +str(total)
        #     print(message)
        #     connection=smtplib.SMTP("smtp.gmail.com",587)
        #     connection.starttls()
        #     connection.login("manideepkotha324@gmail.com","mani@9324")
        #     connection.sendmail("manideepkotha324@gmail.com",i["emailId"],message)
        #     connection.quit
        #     print("Mail sent successfully")
        break