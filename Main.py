
# import package
import turtle 
import time
import random
import turtle as trtl
import csv
import sys
import smtplib, ssl
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
t = turtle
 
with open('IDS.csv', "r") as f:
    reader = csv.reader(f)
    data = list(reader)

ids = list(data[0])
# screen object
wn = turtle.Screen()
screen_w = 631
screen_h = 820
wn.setup(width=screen_w, height=screen_h)
wn.bgpic('Group 14UITEST.png') 

from turtle import listen, onkey, onkeypress
OrderInputOfNumb = []
IDInputOfNumb = []
def write1():
    t.write('1', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    OrderInputOfNumb.append('1')
    IDInputOfNumb.append('1')
def write2():
    t.write('2', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    OrderInputOfNumb.append('2')
    IDInputOfNumb.append('2')
def write3():
    t.write('3', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    OrderInputOfNumb.append('3')
    IDInputOfNumb.append('3')
def write4():
    t.write('4', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    OrderInputOfNumb.append('4')
    IDInputOfNumb.append('4')
def write5():
    t.write('5', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    OrderInputOfNumb.append('5')
    IDInputOfNumb.append('5')
def write6():
    t.write('6', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    OrderInputOfNumb.append('6')
    IDInputOfNumb.append('6')
def write7():
    t.write('7', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    OrderInputOfNumb.append('7')
    IDInputOfNumb.append('7')
def write8():
    t.write('8', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    OrderInputOfNumb.append('8')
    IDInputOfNumb.append('8')
def write9():
    t.write('9', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    OrderInputOfNumb.append('9')
    IDInputOfNumb.append('9')
def write0():
    t.write('0', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    OrderInputOfNumb.append('0')
    IDInputOfNumb.append('0')
'''
onkey(write1, '1')
onkey(write2, '2')
onkey(write3, '3')
onkey(write4, '4')
onkey(write5, '5')
onkey(write6, '6')
onkey(write7, '7')
onkey(write8, '8')
onkey(write9, '9')
onkey(write0, '0')
listen()
'''



def loading(speedofload,colorofload):
  t.hideturtle()
  t.pensize(5)
  t.pencolor(colorofload)
  t.penup()
  t.goto(90,0)
  t.setheading(45)
  t.pendown()
  def branch():
    t.speed(speedofload)
    for i in range(3):
      for i in range(3):
          t.forward(30)
          t.backward(30)
          t.right(45)
      t.left(90)
      t.backward(30)
      t.left(45)
    t.right(90)
    t.forward(90)
  for i in range(8):
      branch()
      t.left(45)

def initialload():
  loading(0,'white')
  loading(0,'#425996')
 # loading(0, "#84A6FF")

def order():
  id = ids[0]
  ids.pop(0)
  with open('IDS.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(ids)

  print("Your order ID is " + str(id))
  Crocadile_Roast = 18
  Seared_Beef = 15
  Baked_Frog =  17
  Stuffed_Duck = 22
  Soaked_Chicken = 16
  Baby_Kangaroo = 36

  Meat_strips = 14
  Meat_Salad = 16

  Exotic_Tropical_Drink = 8
  Jack_Sparrow_Rum = 12
  James_Bonds_Beer = 12

  ##foodmathtotal
  food_list1 = ["N/A","Crocadile Roast", "Seared Beef", "Baked Frog", "Stuffed Duck", "Soaked Chicken","Baby Kangaroo", "Meat strips", "Meat Salad", "Exotic Tropical Drink", "Jack Sparrow Rum", "James Bonds Beer" ]
  food_list = ["N/A",Crocadile_Roast, Seared_Beef, Baked_Frog, Stuffed_Duck, Soaked_Chicken, Baby_Kangaroo, Meat_strips, Meat_Salad, Exotic_Tropical_Drink, Jack_Sparrow_Rum, James_Bonds_Beer]
  item_number = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eigth', 'ninth', 'tenth', 'eleventh']
  global n_one
  n_one = 0
  global total_price
  total_price = 0
  ###RECCOMENDATION CODE
  RandomIndexNumber = random.randint(1,11)
  ReccomendationOfTheDay = food_list1[int(RandomIndexNumber)]
  print("Our reccomendation of the day is " + str(ReccomendationOfTheDay) + " which is item #" + str(RandomIndexNumber))
  OrderOfPerson = []

  t.speed(0)
  t.hideturtle
  wn.clear()
  wn.bgpic('Group 18.png')
  t.pencolor('#425996')
  t.penup()
  t.goto(-250, 150)    
  def Part1():
      global food_choice
      food_choice = 0
      onkey(write1, '1')
      onkey(write2, '2')
      onkey(write3, '3')
      onkey(write4, '4')
      onkey(write5, '5')
      onkey(write6, '6')
      onkey(write7, '7')
      onkey(write8, '8')
      onkey(write9, '9')
      onkey(write0, '0')
      listen()
      def orderclicktrack(x, y):
        if 100<x<250 and 140<y<250:
          global OrderInputOfNumb
          print(OrderInputOfNumb)
          print(x)
          print(y)
          if len(OrderInputOfNumb) == 1:
            global food_choice
            food_choice = int(OrderInputOfNumb[0])
          else:
            food_choice = int(OrderInputOfNumb[0] + OrderInputOfNumb[1])
        if food_choice !=0:
          while True:
            #food_choice = t.textinput('Ordering Window', 'What is your ' + item_number[n_one] + ' item? ')
            try:
              print("You ordered " + food_list1[int(food_choice)])
              OrderOfPerson.append(food_list1[int(food_choice)])
              food_choice = int(food_choice)
              OrderInputOfNumb = []
              wn.clear()
              wn.bgpic('Group 18.png')
              t.pencolor('#425996')
              t.penup()
              t.goto(-250, 150)
            except ValueError or Exception:
              print("Enter a Value")
              continue
            global n_one
            global total_price
            n_one += 1
            total_price += food_list[food_choice]
            ##PAYMENT/FINISHING
            #wn.clear()
            #wn.bgcolor('#84A6FF')
            print("Your order: " + ", ".join(OrderOfPerson))

            end = t.textinput('Order Status','Would you like to end the order? (Y/N): ') 
            if end.lower() == 'y':
              print('Your total price is: ' + str(total_price))
              print("Now paying by card...")
              time.sleep(1)
              print("Charging card ending in " + str(random.randint(1000,9999)))  
              time.sleep(1)
              print("Your food will be ready in 5 seconds. An email will be sent when it is done.")
              ##SAVING PART DO NOT TOUCH --RAMI N vv
              fields = [str(id), 'Price'] 
              rows = [str(id),str(total_price)]
              with open('Orders.csv', 'a') as f:
                write = csv.writer(f)
                write.writerow(rows)
              ''' 
              with open('time.csv', 'a') as fg:
                write = csv.writer(fg)
                rowstime = [str(id), "20"]
                write.writerow(rowstime)
                '''




              port = 465  
              password = "cesnored for security purposes"

            
              context = ssl.create_default_context()

              with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login("censored@gmail.com", password)
                sender_email = "censored@gmail.com"   
                message = """\
                  Subject: The Meat Project

                  
                  Your order has been finished. 
                  Thank you for shopping with the Meat Project, and we hope you enjoy your food. """
                orderofpersontstring = ", ".join(OrderOfPerson)
                while True:
                  try:
                    emailf = str(input("Please type your email(Check your spam/School emails will not work): "))
                    receiver_email = emailf 
                    server.sendmail(sender_email, receiver_email, (message + "Your id is "+ str(id) + ", and the total price was $" + str(total_price)) + ". Your order consisted of " + str(orderofpersontstring)+".")
                    print("An email has been sent to " + str(emailf))
                    print("Thanks for shopping at the BHS Meat Project")
                    sys.exit()
                    break
                  except Exception:
                    print("Please enter a valid email")
                break 
            else:
              print("Please input what you would like to order on the screen")
              Part1()
              break
              
      wn.onclick(orderclicktrack)
      
      
  Part1()    
  

def track():
 def Part3(): 
  wn.clear()
  t.hideturtle()
  wn.bgpic('Group 18ID.png')
  t.pencolor('#425996')
  screen_w = 620
  screen_h = 820
  wn.setup(width=screen_w, height=screen_h)
  t.penup()
  t.goto(-240, 150)
  global IDInputOfNumb
  IDInputOfNumb = []
  def trackclick(x, y):
    if 100<x<250 and 140<y<250:
      if len(IDInputOfNumb) == 1:
        global N
        N = int(IDInputOfNumb[0])
        Part4()
      else:
        N = int((IDInputOfNumb[0] + IDInputOfNumb[1]))
        Part4()
      print("Alright! Please enter your tracking order!")
  onkey(write1, '1')
  onkey(write2, '2')
  onkey(write3, '3')
  onkey(write4, '4')
  onkey(write5, '5')
  onkey(write6, '6')
  onkey(write7, '7')
  onkey(write8, '8')
  onkey(write9, '9')
  onkey(write0, '0')
  listen()
  wn.onclick(trackclick)
 def Part4(): 
  global TriesAtTrack
  TriesAtTrack = 0
  while True:
    try:
      time.sleep(0.5)
      with open("Orders.csv") as f1:
        freader = csv.reader(f1)
        line1 = []
        for line in freader:
          line1.append(line)
        for stuff in line1:
          lol = int(line1.index(stuff))  % 2
          if int(lol) ==0:
            stuff = str(stuff)
            stuff = stuff.replace("[", '')
            stuff = stuff.replace("]", '')
            stuff = stuff.replace("'", '')
            stuff = stuff.replace("'", '')
            stuff = stuff.replace(' ', '')
            stuff = stuff.replace((","),'')
            stuff = list(stuff)
            if int(N) == int(stuff[0]):
              if int(len(stuff)) == 3:
                print("Your order number is " + str(stuff[0]) + ", and you payed $" + str(str(stuff[1]) + str(stuff[2])))
                wn.bye()
                sys.exit()
                
              else:
                print("Your order number is " + str(stuff[0]) + ", and you payed $" + str(str(stuff[1])))
                wn.bye()
                sys.exit()
        TriesAtTrack = TriesAtTrack + 1        
        print("Order not found")
        if TriesAtTrack >= 3:
          print("You have exceeded the limit of incorrect tracking per session.")
          wn.bye()
          break
          sys.exit()
        Part3()
        break
    except ValueError or Exception:
      TriesAtTrack = TriesAtTrack + 1  
      print("Please input Integers only!")
      if TriesAtTrack >= 3:
          print("You have exceeded the limit of incorrect tracking per session.")
          wn.bye()
          sys.exit()
      Part3()
      break
 Part3()


def clickdetectormain(x, y):
  t.hideturtle()
  t.shape('circle')
  t.pencolor('#425996')
  turtle.speed(0)
  t.penup()
  turtle.goto(x, y)
  print(str(x) + " " + str(y))
  if -164<x<165 and -30<y<90:
    print("clicked order")
    wn.clear()
    wn.bgcolor('#84A6FF')
    initialload()
    ##temporary

   # wn.bye()

    ##temporary
    order()
  elif -164<x<164 and -210<y<-90:
    print("clicked track")
    wn.clear()
    wn.bgcolor('#84A6FF')
    initialload()
    ##temporary

    #wn.bye()

    ##temporary
    track()
  elif -164<x<164 and -390<y<-280:
    print("clicked about")
    wn.clear()
    wn.bgcolor('#84A6FF')
    wn.clear()
    wn.bgpic('Group 18.png')
    t.pencolor('white')
    t.penup()
    t.goto(-250, 150)
    '''
    t.write('1', font=('Roboto', 50))
    t.penup()
    t.forward(40)
    t.write('2', font=('Roboto', 50))
  '''
# onclick action 
wn.onclick(clickdetectormain)
wn.mainloop()