def play():
  import time
  import click
  import random
  def BLK():
    print('')
  t = time
  c = click
  Cash = 100
  Debt = 100
  Menu_Access = 9
  Chance_Key = 0
  input_key = 0
  clear_check = 0
  Customer_Chance = [1,0,1,1,0,1,0,1]
  Products_Inventory = {"Pants":5,"Skirt":0,'W-Tshirt':0,'B-Tshirt':0,'Jeans':0,'W-Fabric':0,'B-Fabric':0,'P-Fabric':0,'Denim':0}
  Products_Prices = {"Pants":10.50,"Skirt":11.25,'W-Tshirt':19.25,'B-Tshirt':19.56,'Jean':14.67}
  Buy_Prices_Garments = {'1':13.45,'2':13.56,'3':14.78}
  Buy_Prices_Fabrics = {'1': 4,'2':4,'3':4,'4':3.20}
  Menu = ['Diomboulou Clothing Store',"________________________","","",'1. Sell','2. Buy',"3. Make",'4. Account','5. About Us']
  Sell_Menu = ['Fabrics and Garments Shop','_________________________','','','1.Garments','2.Fabrics']
  Garments_Menu = ['Garments Available','__________________','','','1. White T-shirt','2 .Blue T-shirt','3. Jeans']
  Fabrics_Menu = ['Fabrics Available','_________________','','','1. White Fabric','2. Blue Fabric','3. Pink Fabric','4. Denim']
  def INRT():
    input_key = ''
  
  t.sleep(3)
  while True : 
    for x in range(Menu_Access):
      print(Menu[x])
    BLK()
    input_key = input('Your Choice: ')
  
    if input_key == '1':
      c.clear()
      print('Inventory')
      print('_________')
      print('')
      print('Pants:'+ str(Products_Inventory['Pants']))
      print('')
      print('Skirt:'+ str(Products_Inventory['Skirt']))
      BLK()
      print('White T-Shirt: '+ str(Products_Inventory['W-Tshirt']))
      BLK()
      print('Blue T-Shirt: '+str(Products_Inventory['B-Tshirt']))
      BLK()
      print('Jeans: '+str(Products_Inventory['Jeans']))
      for x in range(3):
        BLK()
      print('What to Sell?')
      print('')
      input_key = ''
      input_key = input('Your Choice: ')
      if input_key.lower() == 'pants':
        if Products_Inventory['Pants']>0:
          Chance_Key = random.randint(0,7)
          if Customer_Chance[Chance_Key] ==  1:
            t.sleep(2)
            c.clear()
            print('A customer checks out your store and decides to buy a pant')
            Products_Inventory['Pants'] =int(Products_Inventory['Pants'])-1
            t.sleep(2)
            if Debt >0:
              Cash +=0.5*(Products_Prices['Pants'])
              Debt -= 0.5*(Products_Prices['Pants'])
            elif Debt <= 0:
              Cash += Products_Prices['Pants']
            t.sleep(3)
            c.clear()
            print('Cash:' + str(Cash))
            print('Debt:'+ str(Debt))
            t.sleep(6)
            c.clear()
          else:
            print(' No one seems interested in your store for now')
            t.sleep(4)
            c.clear()
      elif input_key.lower() == 'skirt':
        if Products_Inventory['Skirt'] >0:
          Chance_Key = random.randint(0,7)
          if Customer_Chance[Chance_Key] == 1:
            t.sleep(2)
            print('A customer checks out your store and decides to buy a Skirt')
            if Debt >0:
              Cash +=0.5*(Products_Prices['Skirt'])
              Debt -= 0.5*(Products_Prices['Skirt'])
            elif Debt <= 0:
              Cash += Products_Prices['Skirt']
            t.sleep(3)
            c.clear()
            Products_Inventory['Skirt'] =(Products_Inventory['Skirt'])-1
            print('Cash:' + str(Cash))
            print('Debt:'+ str(Debt))
            t.sleep(6)
            c.clear() 
          else:
            print(' No one seems interested in your store for now')
            t.sleep(4)
            c.clear()
      elif input_key.lower() == 'white t-shirt':
        if Products_Inventory['W-Tshirt'] >0:
          Chance_Key = random.randint(0,7)
          if Customer_Chance[Chance_Key] == 1:
            t.sleep(2)
            c.clear()
            print('A customer checks out your store and decides to buy a White T-Shirt')
            t.sleep(3)
            c.clear()
            if Debt >0:
              Cash +=0.5*(Products_Prices['W-Tshirt'])
              Debt -= 0.5*(Products_Prices['W-Tshirt'])
            elif Debt <= 0:
              Cash += Products_Prices['W-Tshirt']
            t.sleep(3)
            c.clear()
            Products_Inventory['W-Tshirt'] =(Products_Inventory['W-Tshirt'])-1
            print('Cash:' + str(Cash))
            print('Debt:'+ str(Debt))
            t.sleep(6)
            c.clear() 
          else:
            print(' No one seems interested in your store for now')
          t.sleep(4)
          c.clear()   
      elif input_key.lower() == 'blue t-shirt':
        if Products_Inventory['B-Tshirt'] >0:
          Chance_Key = random.randint(0,7)
          if Customer_Chance[Chance_Key] == 1:
            t.sleep(2)
            c.clear()
            print('A customer checks out your store and decides to buy a Blue T-Shirt')
            t.sleep(3)
            c.clear()
            if Debt >0:
              Cash +=0.5*(Products_Prices['B-Tshirt'])
              Debt -= 0.5*(Products_Prices['B-Tshirt'])
            elif Debt <= 0:
              Cash += Products_Prices['B-Tshirt']
            t.sleep(3)
            c.clear()
            Products_Inventory['B-Tshirt'] =(Products_Inventory['B-Tshirt'])-1
            print('Cash:' + str(Cash))
            print('Debt:'+ str(Debt))
            t.sleep(6)
            c.clear() 
          else:
            print(' No one seems interested in your store for now')
          t.sleep(4)
          c.clear()   
      elif input_key.lower() == 'jeans':
        if Products_Inventory['Jeans'] >0:
          Chance_Key = random.randint(0,7)
          if Customer_Chance[Chance_Key] == 1:
            t.sleep(2)
            c.clear()
            print('A customer checks out your store and decides to buy a Jean')
            t.sleep(3)
            c.clear()
            if Debt >0:
              Cash +=0.5*(Products_Prices['Jeans'])
              Debt -= 0.5*(Products_Prices['Jeans'])
            elif Debt <= 0:
              Cash += Products_Prices['Jeans']
            t.sleep(3)
            c.clear()
            Products_Inventory['Jeans'] =(Products_Inventory['Jeans'])-1
            print('Cash:' + str(Cash))
            print('Debt:'+ str(Debt))
            t.sleep(6)
            c.clear() 
          else:
            print(' No one seems interested in your store for now')
          t.sleep(4)
          c.clear()   
    elif input_key == '2':
      c.clear()
      for x in range(len(Sell_Menu)):
        print(Sell_Menu[x])
      input_key= ''
      BLK()
      input_key = input('Your Choice: ')
      c.clear()
      if input_key == '1':
        for x in range(len(Garments_Menu)):
          print(Garments_Menu[x]) 
        input_key = input('What to buy: ')
        if input_key == '1':
          c.clear()
          print('You select White T-Shirt and proceed to pay the person running the store')
          t.sleep(4)
          
          c.clear()
          if Cash > Buy_Prices_Garments['1']:
            Cash -= Buy_Prices_Garments['1']
            Products_Inventory['W-Tshirt'] += 1
          else:
            BLK()
            print('Not Enough Cash')
          t.sleep(1)
          print('Cash:'+ str(Cash))
          t.sleep(2)
          c.clear()
          print('Inventory:')
          BLK()
          print(Products_Inventory)
          t.sleep(5)
        elif input_key == '2':
          c.clear()
          print('You select a Blue T-Shirt and proceed to pay the person running the store')
          t.sleep(4)
          
          c.clear()
          if Cash > Buy_Prices_Garments['2']:
            Cash -= Buy_Prices_Garments['2']
            Products_Inventory['B-Tshirt'] += 1
          else:
            BLK()
            print('Not Enough Cash')
          t.sleep(1)
          print('Cash:'+ str(Cash))
          t.sleep(2)
          c.clear()
          print('Inventory:')
          BLK()
          print(Products_Inventory)
          t.sleep(3)
        elif input_key == '3':
          c.clear()
          print('You select a Jean and proceed to pay the person running the store')
          t.sleep(4)
          
          c.clear()
          if Cash > Buy_Prices_Garments['3']:
            Cash -= Buy_Prices_Garments['3']
            Products_Inventory['Jeans'] += 1
          else:
            BLK()
            print('Not Enough Cash')
          t.sleep(1)
          print('Cash:'+ str(Cash))
          t.sleep(2)
          c.clear()
          print('Inventory:')
          BLK()
          print(Products_Inventory)
          t.sleep(3)
        c.clear()
      if input_key == '2':
        for x in range(len(Fabrics_Menu)):
          print(Fabrics_Menu[x])
      input_key = ''
      input_key = input('Your Choice: ')
      if input_key == '1':
        c.clear()
        INRT()
        input_key = input("How many: ")
        print('You take some white fabric')
        t.sleep(4)
        
        c.clear()
        Cash -= Buy_Prices_Fabrics['1']* int(input_key)
        Products_Inventory['W-Fabric'] += int(input_key)
        t.sleep(1)
        print('Cash:'+ str(Cash))
        t.sleep(2)
        c.clear()
        print('Inventory:')
        BLK()
        print(Products_Inventory)
        t.sleep(5)
      elif input_key == '2':
        INRT()
        input_key = input("How many: ")
        print('You take some blue fabric')
        t.sleep(4)
        c.clear()
        Cash -= Buy_Prices_Fabrics['2']* int(input_key)
        Products_Inventory['B-Fabric'] += int(input_key)
        print('Cash:'+ str(Cash))
        t.sleep(2)
        c.clear()
        print('Inventory:')
        BLK()
        print(Products_Inventory)
        t.sleep(3)
      elif input_key == '3':
        INRT()
        input_key = input("How many: ")
        print('You take some Pink fabric')
        t.sleep(4)
        
        c.clear()
        Cash -= Buy_Prices_Fabrics['3']* int(input_key)
        Products_Inventory['P-Fabric'] += int(input_key)
        print('Cash:'+ str(Cash))
        t.sleep(2)
        c.clear()
        print('Inventory:')
        BLK()
        print(Products_Inventory)
        t.sleep(3)
      elif input_key == '4':
        INRT()
        input_key = input("How many: ")
        print('You take some Denim')
        t.sleep(4)
        
        c.clear()
        Cash -= Buy_Prices_Fabrics['4']* int(input_key)
        Products_Inventory['Denim'] += int(input_key)
        print('Cash:'+ str(Cash))
        t.sleep(2)
        c.clear()
        print('Inventory:')
        BLK()
        print(Products_Inventory)
        t.sleep(3)
      c.clear()  
    elif input_key == '3':
      c.clear()
      print('Available Crafts')
      print('________________')
      print('')
      if Products_Inventory['W-Fabric'] > 0:
        clear_check += 1
      if Products_Inventory['B-Fabric'] > 0:
        clear_check += 1
      if Products_Inventory['P-Fabric'] > 0:
        clear_check += 1
      if Products_Inventory['Denim'] > 1:
        clear_check += 1
      
      if clear_check <= 0:
        BLK()
        print('No Craft Available')
      else:
        if Products_Inventory['W-Fabric'] > 0:
          print('Craft: White T-Shirt')
          print('1x White Fabric')
          print('')
        if Products_Inventory['B-Fabric'] > 0:
          print('Craft: Blue T-Shirt')
          print('1x Blue Fabric')
          print('')
        if Products_Inventory['P-Fabric'] > 0:
          print('Craft: Skirt')
          print('1x Pink Fabric')
          print('')
        if Products_Inventory['Denim'] > 1:
          print('Craft: Jeans')
          print('2x Denim ')
          print('')
        input_key = input('What to Make: ')  
        if input_key.lower() == 'white t-shirt' and Products_Inventory['W-Fabric'] >0:
          c.clear()
          Products_Inventory['W-Fabric'] -= 1
          for x in range(6):
            print('Making Garment')
            t.sleep(0.3)
            c.clear()
            print('Making Garment.')
            t.sleep(0.3)
            c.clear()
            print('Making Garment..')
            t.sleep(0.3)
            c.clear()
            print('Making Garment...')
            t.sleep(0.3)
            c.clear() 
          print('Garment Finished!')
          t.sleep(1)
          BLK()
          print('Adding to Inventory')
          Products_Inventory['W-Tshirt'] += 1
          t.sleep(1)
          BLK()
          c.clear()
          print(Products_Inventory)
        if input_key.lower() == 'blue t-shirt' and Products_Inventory['B-Fabric'] >0:
          c.clear()
          Products_Inventory['B-Fabric'] -= 1
          for x in range(6):
            print('Making Garment')
            t.sleep(0.3)
            c.clear()
            print('Making Garment.')
            t.sleep(0.3)
            c.clear()
            print('Making Garment..')
            t.sleep(0.3)
            c.clear()
            print('Making Garment...')
            t.sleep(0.3)
            c.clear() 
          print('Garment Finished!')
          t.sleep(1)
          BLK()
          print('Adding to Inventory')
          Products_Inventory['B-Tshirt'] += 1
          t.sleep(1)
          BLK()
          c.clear()
          print(Products_Inventory)  
        if input_key.lower() == 'skirt' and Products_Inventory['P-Fabric'] >0:
          c.clear()
          Products_Inventory['P-Fabric'] -= 1
          for x in range(6):
            print('Making Garment')
            t.sleep(0.3)
            c.clear()
            print('Making Garment.')
            t.sleep(0.3)
            c.clear()
            print('Making Garment..')
            t.sleep(0.3)
            c.clear()
            print('Making Garment...')
            t.sleep(0.3)
            c.clear() 
          print('Garment Finished!')
          t.sleep(1)
          BLK()
          print('Adding to Inventory')
          Products_Inventory['Skirt'] += 1
          t.sleep(1)
          BLK()
          c.clear()
          print(Products_Inventory)  
        if input_key.lower() == 'jeans'and Products_Inventory['Denim'] >0:
          c.clear()
          Products_Inventory['Denim'] -= 1
          for x in range(6):
            print('Making Garment')
            t.sleep(0.3)
            c.clear()
            print('Making Garment.')
            t.sleep(0.3)
            c.clear()
            print('Making Garment..')
            t.sleep(0.3)
            c.clear()
            print('Making Garment...')
            t.sleep(0.3)
            c.clear() 
          print('Garment Finished!')
          t.sleep(1)
          BLK()
          print('Adding to Inventory')
          Products_Inventory['Jeans'] += 1
          t.sleep(1)
          BLK()
          c.clear()
          print(Products_Inventory)  
            
          t.sleep(10)
          c.clear()
    elif input_key == '4':
      c.clear()
      print('Statistics')
      print('__________')
      
      BLK()
      print('Cash: '+str(Cash))
      BLK()
      print('Debt: '+str(Debt))
      BLK()
      print('Inventory:')
      BLK()
      print(Products_Inventory)
      t.sleep(10)
    elif input_key == '5':
      c.clear()
      print('About Us: 08-Koute Diomboulou Group')
      print('__________________________________')
      BLK()
      BLK()
      print('The 08-Koute Diomboulou group is a group of people living in Senegal')
      BLK()
      print('They all have started up a business and become micro-entrepreneurs')
      BLK()
      print('But they do not have enough money to start their business')
      BLK()
      print("Some countries stil encourage Male Dominancy so it is very hard for Women to start Businesses ")
      BLK()
      print('The Communities present in the town of Dioboulou support each other but the overall condition of the town is not good due to the low HDI scores present in Senegal ')
      BLK()
      print("Our School District has given our Team 200 dollars to loan to a group/person in need of money")
      BLK()
      print("We believe that donating Money to this group will benefit its Community present around them")
      BLK()
      print("This game is based on a loan that asked from the 08-Koute Diomboulou. It asked for a couple thousand for a clothing store ")
      BLK()
      print('We hope that this loan will help make impact on this community')
      t.sleep(25)
      c.clear()
    elif input_key == '69':
      print("So you've found a secret")
      BLK()
      t.sleep(3)
      print('Impressive')
      BLK()
      t.sleep(3)
      BLK()
      print('Here is mine')
      t.sleep(3)
      BLK()
      print("I never actually liked shereena, all of it was a complex plan put together for revenge but it failed because to early exposure")
      t.sleep(6)
      BLK()
      print("If you are reading this you might as well keep this a secret")
      t.sleep(3)
      c.clear()
    else:
      print('There was no operation found corropsonding to the numeral submited')
    t.sleep(3)
    c.clear()            
    
    
    
  
  
