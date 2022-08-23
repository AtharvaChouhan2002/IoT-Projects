from re import X
import serial
import time
import pyautogui as pg
from array import *

arduinoData=serial.Serial("com5",9600)

move=array("i",[0 for i in range(999999)])
        

time.sleep(3)
i=0
while True:
    
    
    while(arduinoData.inWaiting()==0):
        pass
    datapacket=arduinoData.readline()

    datapacket=str(datapacket,"utf-8")
    
    splitpacket=datapacket.split(",")
    x=float(splitpacket[0])
    y=float(splitpacket[1])
    z=float(splitpacket[2])
    print(x,y,z)

    if -8000<=x<=7000 and -9000<=y<=6000:
        print("Neutral")
        move[i]=0
        
        
    
    if x>10000 and -9000<=y<=6000:
        print("Left")
        move[i]=1
        
        
        
    if x<-6000 and -9000<=y<=6000:
        print("Right")
        move[i]=3
            
    if y>6000 and -8000<=x<=7000:
        print("Up")
        move[i]=2
        
        
    if y<-12000 and -8000<=x<=7000 :
        print("Down")
        move[i]=4
    
    

    
    
    if move[i]==0:
        pass

    elif move[i]!=move[i-1] :

        if move[i]==1:
            pg.press("a")
        elif move[i]==2:
            pg.press("w")
        elif move[i]==3:
            pg.press("d")
        elif move[i]==4:
            pg.press("s")
    

    
    
    i+=1
        
        
        
    
    