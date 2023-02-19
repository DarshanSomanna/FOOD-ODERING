#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from prettytable import PrettyTable

class Admin:
    Foods={}
    Food_count=0
    def __init__(self,Name,Quantity,Price,Discount,Stock):
        Admin.Food_count+=1
        self.FoodID=Admin.Food_count
        self.Name=Name
        self.Quantity=Quantity
        self.Price=Price
        self.Discount=Discount
        self.Stock=Stock
   

    def Add_food_items(self):
        with open('Foods.json','w') as outfile:
            Admin.Foods[int(Admin.Food_count)]={'Food_ID':Admin.Food_count,'Name':self.Name,'Quantity':self.Quantity,'Price':self.Price,'Discount':self.Discount,'Stock':self.Stock}
            json.dump(Admin.Foods,outfile)
            
            
    def Edit_food_items(Food_id,new_food):
        with open("Foods.json") as f:
            data=f.read()
        Food_data=json.loads(data)
        Food_data[str(Food_id)]['Name']=new_food
        with open('Foods.json', 'w') as f:
            f.write(json.dumps(Food_data))
            
            
    def display_foods():
        print('-'*30,'MENU','-'*30)
        with open('Foods.json') as f:
            data = json.load(f)

        table = PrettyTable()
        table.field_names = ["Food ID", "Name", "Quantity", "Price", "Discount", "Stock"]

        for food_id, food_data in data.items():
            row = [food_data["Food_ID"], food_data["Name"], food_data["Quantity"], food_data["Price"], food_data["Discount"], food_data["Stock"]]
            table.add_row(row)
        print(table)
        
    def remove_food(food_id):
        with open('Foods.json') as f:
            data = json.load(f)
        data.pop(str(food_id))
        
        with open('Foods.json','w') as f:
            f.write(json.dumps(data))
            


# In[2]:


F1=Admin("BIRYANI",1,250,"10%",100)


# In[3]:


F1.Add_food_items()


# In[4]:


F2=Admin("BATH",2,50,"2%",100)


# In[5]:


F2.Add_food_items()


# In[6]:


F3=Admin("CAKE",4,10,"10%",250)


# In[7]:


F3.Add_food_items()


# In[8]:


F4=Admin("VODA",5,10,"5%",500)


# In[9]:


F4.Add_food_items()


# In[10]:


F5=Admin("BURGER",4,100,"10%",500)


# In[11]:


F5.Add_food_items()


# In[12]:


#Admin.display_foods()


# In[13]:


Admin.remove_food(4)


# In[14]:


#Admin.display_foods()


# In[15]:


pip install jsom


# In[16]:


pip install prettytable


# In[ ]:





# In[ ]:




