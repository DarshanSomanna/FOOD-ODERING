#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from prettytable import PrettyTable
from prettytable import from_csv


# In[2]:


def main_menu():
    print("\t(R) Register\n\t(L) logIn\n\t(E) Exit")
    input_1=input("Enter right choice:").upper()
    if len(input_1)==1:
        if input_1=='R':
            registration()
        elif input_1=='L':
            logIn()
        elif input_1=='E':
            pass
        else:
            print("Invalid Input")
            main_menu()
    else:
        print("Invalid Input")
        main_menu()


# In[3]:


def registration():
    
    Full_name=input("Name:")
    Phone_num=input("Phone number:")
    Email=input("Email:")
    Address=input("Address:")
    Password=input("Password:")
    cust[Email]={"Name":Full_name,"Contact_Number":Phone_num,"Email":Email,"Address":Address,"Password":Password,"Order history":None}
    with open('Customer.json','w') as f:
        json.dump(cust,f)        
    main_menu()


# In[4]:


def logIn():
    print('_'*30,"LOGIN",'_'*30)
    global Email
    Email=input("Email:")
    Password=input("Password:")
    with open('Customer.json','r') as f:
        cust_data=json.load(f)
    for k1,v1 in cust_data.items():
        if k1==Email and v1["Password"]==Password:
            options()
        else:
            print("\nIncorrect Credentials!\nTry again:\n")
            main_menu()


# In[5]:


def options():
    print('_'*30,"OPTIONS",'_'*30)
    print('\t(P) Place New Order\n\t(O) Order History\n\t(U) Update Profile\n\t(E) Exit')
    input_2=input('Please select your option:').upper()
    if len(input_2)==1:
        if input_2=='P':
            place_order()
        elif input_2=='O':
            order_history()
        elif input_2=='U':
            update_profile()
        elif input_2=='E':
            pass
        else:
            print("\nInvalid Input!")
            options()
    else:
        print("\nInvalid Input!")
        options()


# In[6]:


def place_order():
    global Email
    print('_'*30,"PLACE ORDER",'_'*30)
    print("Available Food_Items:")
    get_ipython().run_line_magic('run', 'Admin.ipynb')
    Admin.display_foods()
    num_of_foods=int(input("How many food items are you ordering?"))
    print("\n select your Food_Items by entering it's Food_Id:(One by one)")
    food_list=[]
    orderd_food_lst=[]
    n=1
    for i in range(num_of_foods):
        food_list.append(input("Please enter Food.no{}: ".format(n)))
        n+=1
    with open("Foods.json","r") as f:
        food_data=json.load(f)
        
    table = PrettyTable()
    table.field_names = ["Food ID", "Name", "Quantity", "Price", "Discount"]

    for food_id, food_data in food_data.items():
        if food_id in food_list:
            row = [food_data["Food_ID"], food_data["Name"], food_data["Quantity"], food_data["Price"], food_data["Discount"]]
            orderd_food_lst.append(row)
            table.add_row(row)
    print("\nFoods you've orderd:")    
    print(table)
    

    
    with open("Customer.json",'r') as file:
        cust_data=json.load(file)
    for k1,v1 in cust_data.items():
        if k1==Email:
            if v1["Order history"]==None:
                v1["Order history"]=orderd_food_lst
            else:
                for j in orderd_food_lst:
                    v1["Order history"].append(j)
    with open("Customer.json",'w') as outfile:
        json.dump(cust_data,outfile)
    options()    


# In[7]:


def order_history():
    global Email
    print('_'*30,"ORDER HISTORY",'_'*30)
    with open("Customer.json",'r') as file:
        cust_data=json.load(file)
    table = PrettyTable()
    table.field_names = ["Food ID", "Name", "Quantity", "Price", "Discount"]
    
    for k1,v1 in cust_data.items():
        if k1==Email:
            if v1["Order history"]==None:
                print("you have'nt orderd anything.")
            else:    
                for i in v1["Order history"]:
                    row=i
                    table.add_row(row)
    print(table)   
    options()   


# In[8]:


def update_profile():
    Email=input("Email:")
    Password=input("Password:")
    with open("Customer.json","r") as f:
        data=json.load(f)
    for k1,v1 in data.items():
        if k1==Email and v1["Password"]==Password:
            print("\nName:{}\nContact num:{}\nEmail:{}\nAddress:{}\nPassword:{}\n".format(v1['Name'],v1['Contact_Number'],v1['Email'],v1['Address'],v1['Password']))
        else:
            update_profile()
    print("What would you like to update?")
    print('\t(N) Name\n\t(C) Contact Number\n\t(E) Email Address\n\t(A) Address\n\t(P) Password')
    input_3=input("Please select valid option:").upper()
    if len(input_3)==1:
        if input_3=='N':
            data[Email]['Name']=input()
            dumpy(data)


        elif input_3=='C':
            data[Email]["Contact_Number"]=input()
            dumpy(data)
            print("successfully Updated")

        elif input_3=='E':
            data[Email]["Email"]=input()
            dumpy(data)
            print("successfully Updated")

        elif input_3=='A':
            data[Email]["Address"]=input()
            dumpy(data)
            print("successfully Updated")

        elif input_3=='P':
            data[Email]["Password"]=input()
            dumpy(data)
            print("successfully Updated")


        else:
            print("Please provide a valid input:")
            update_profile()

    else:
        print("Please provide a valid input:")
        update_profile()
        
    options()    

def dumpy(data):
    with open('Customer.json','w') as f:
        json.dump(data,f)   

        


# In[ ]:


if __name__=="__main__":
    print('_'*30,'Welcome','_'*30)
    cust={}
    Email=0
    main_menu()


# In[ ]:




