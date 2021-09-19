import easygui as eg
import time 
import sys

import shower_cost as sc

# title page:
cont_app = True
title0 = "Welcome to the Green Machine"
img0 = "../img/cover.png"
msg0 = "Pick an action to begin!"

#check if continue or something else
def cont(): #checks if user wants to continue
    msg2 = "Do you want to continue?"
    title2 = "Please Confirm"
    if eg.ccbox(msg2, title2):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)           # user chose Cancel

while cont_app: 
  pick_btn = eg.buttonbox(msg = msg0, image = img0, title = title0, choices=["Shower", "Lights", "Electricity", "Leaderboard", "Exit"])
  if pick_btn == "Shower":
  #first page 
    title1 = "Green shower"

    start_time = None
    msg1 = "Click to start recording time!"
    shower_cont = True
    img1 = "../img/shower.png"

    start = eg.buttonbox(msg1, image = img1, title = title1, choices=["Start Shower"])
    if start:
        start_time = time.mktime(time.localtime()) 
        current_price = sc.return_current_price()

    #second page 
    end = eg.buttonbox(image = img1, title = title1, choices=["End Shower"])
    if end:
        end_time = time.mktime(time.localtime())

    duration = end_time - start_time
    dur_msg = "Your Shower was "+ str(duration/60000) + " minutes long and cost $" + str(duration/60000*0.5*current_price/100) + " per kWh"

    eg.msgbox(dur_msg)
    
    #third page

    #temp_msg = "Did you use HOT or COLD water?"
    #hot_cold = eg.choicebox(temp_msg, choices = [1,2,3,4,5,6,7,8,9,10])
    

  elif pick_btn == "Lights":
    lights_msg = "The price for having a light on is $0.001 per kwh/min"
    eg.msgbox(lights_msg)

  elif pick_btn == "Electricity":
    elec_msg = "The price for electricity is $0.22 per kWh"
    eg.msgbox(elec_msg)
  
  elif pick_btn == "Leaderboard":
    lb_msg = "Will be implemented soon :) "
    eg.msgbox(lb_msg)

  elif pick_btn == "Exit":
    sys.exit(0)




