from zumi.zumi import Zumi
import time
from zumi.util.screen import Screen

zumi= Zumi()
screen= Screen()
def start():
    print("start")
    print(0)
    IR=zumi.get_all_IR_data()
    print("all IR"+ str(IR))
    bottomR=IR[1]
    bottomL=IR[3]
    L = IR[5]  # left
    R = IR[0]
    #print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
    print("first if: "+str((bottomR >=80 and bottomL>=80)))
    return IR, bottomR, bottomL, L, R , direction

def firstif(IR, bottomR, bottomL, L, R, direction): # bottomR >=80 and bottomL>=80
    print("firstif")
    print("zumi move forward")
    zumi.reset_gyro()
    zumi.forward(9, 0.4)
    direction.append(int(zumi.read_z_angle()))
    IR=zumi.get_all_IR_data()
    bottomR=IR[1]
    bottomL=IR[3]
    print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
    print("direction: " + str(direction))
    IR=zumi.get_all_IR_data()
    L=IR[5]
    R=IR[0]
    print("Right and Left: "+ str(L)+" , "+str(R))
    if (direction[-1]+1)<0:
        print("didn't move straight, slightly off left")
        print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
        zumi.turn_left((direction[-1]+1))
        zumi.reset_gyro()
        print (zumi.get_all_IR_data())
    if (direction[-1]+1)>0:
        print("didn't move straight, slightly off right")
        zumi.turn_right((direction[-1]+1))
        zumi.reset_gyro()
        print (zumi.get_all_IR_data())
    return IR, bottomR, bottomL, L, R, direction

def firstelif(IR, bottomR, bottomL, L, R, direction): #bottomR < 60 and bottomL>60 zumi turns left
    print( "1st elif")
    zumi.turn_left(90)
    print(" zumi turn left")
    direction.append(int(zumi.read_z_angle()))
    zumi.reset_gyro()
    print ("direction: " + str(direction))
    IR=zumi.get_all_IR_data()
    bottomR=IR[1]
    bottomL=IR[3]
    #zumi.forward(9, 0.4)
    print("forward again, firstelif")
    return IR, bottomR, bottomL, L, R, direction


def secondelif(IR, bottomR, bottomL, L, R, direction): #bottomR > 65 and bottomL<65
    print( "2nd elif")
    zumi.turn_right(90)
    print(" zumi turn right")
    direction.append(int(zumi.read_z_angle()))
    zumi.reset_gyro()
    print("direction: " + str(direction))    
    IR=zumi.get_all_IR_data()
    bottomR=IR[1]
    bottomL=IR[3]
    print(bottomR, bottomL)
    zumi.forward(9, 0.4)
    print("forward again, secondelif")
    IR=zumi.get_all_IR_data()
    bottomR=IR[1]
    bottomL=IR[3]
    print(bottomR, bottomL)
    return IR, bottomR, bottomL, L, R, direction


def thirdrdelif(IR, bottomR, bottomL, L, R, direction):#bottomR < 60 and bottomL<60
    print("3rd elif")
    print(R)
    if 1==1: # if it is not clear in which direction to go
        zumi.turn_right(90)
        print("looking right")
        IR = zumi.get_all_IR_data()
        bottomR = IR[1]
        bottomL = IR[3]
        print("rl: IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
        if bottomR < 80 and bottomL < 80:# wrong direction
            print("wrong direction")
            t1=zumi.read_z_angle()
            zumi.turn_left(180)
            t2=zumi.read_z_angle()
            print (abs(t1-t2))
            if abs(t1-t2)< 170:
                print("why wasn't that a full turn?")
                zumi.turn_left(180-abs(t1-t2))
            print("looking left")
            IR = zumi.get_all_IR_data()
            bottomR = IR[1]
            bottomL = IR[3]
            print("ll: IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
            print(bottomR < 65 and bottomL < 65)
            if bottomR < 65 and bottomL < 65:# are we right now?
                zumi.turn_right(90)
                print("nope")
                IR=zumi.get_all_IR_data()
                bottomR=IR[1]
                bottomL=IR[3]
                print("d IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
                if bottomR > 80 or bottomL > 80:
                    print("close enough just contine")
                    zumi.forward(9, 0.4)
                    direction.append(int(zumi.read_z_angle()))
                    IR=zumi.get_all_IR_data()
                    bottomR=IR[1]
                    bottomL=IR[3]
                    print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
                    print("direction: " + str(direction))
                    if bottomR > 80 and bottomL < 80: #trying to get closer
                        zumi.turn_right(3)
                    if bottomR < 80 and bottomL > 80:
                        zumi.turn_left(3)
                if bottomR < 80 and bottomL < 80: #of track also the wrong direction take a step back
                    #zumi.turn_right(90)
                    print(" zumi turn right")
                    zumi.reset_gyro()
                    zumi.reverse(2,0.4)
                    print("zumi turn back")
                    IR=zumi.get_all_IR_data()
                    bottomR=IR[1]
                    bottomL=IR[3]
                zumi.reset_gyro()
                return IR, bottomR, bottomL, L, R, direction
            else: #atleast partially on track
                IR=zumi.get_all_IR_data()
                bottomR=IR[1]
                bottomL=IR[3]
                print(" L: "+str(bottomL)+"R: "+str(bottomR)+ " off by:"+str(bottomL-bottomR) + "facing: "+str(zumi.read_z_angle()))
                if bottomL-bottomR<20 and bottomL<90 and bottomR<90:#l
                    while bottomL-bottomR<20:
                        zumi.turn_right(5)
                        print("keep turning r: "+str(bottomL)+ " - "+ str(bottomR)+"  "   +str(bottomL-bottomR ))
                elif bottomL-bottomR>20 and bottomL<90 and bottomR<90:#l
                    while bottomL-bottomR>30:
                        zumi.turn_left(5)
                        print("keep turning l: "+str(bottomL)+ " - "+ str(bottomR)+"  "  +str(bottomL-bottomR ))
                elif bottomL>90 and bottomR>90:
                    print("just some finetuning")
                    if bottomL-bottomR> 9 and bottomL-bottomR!=0:
                        zumi.turn_left((bottomL-bottomR)/((bottomL-bottomR))/10)
                    elif bottomR-bottomL> 9 bottomL-bottomR!=0:
                        zumi.turn_left((bottomR-bottomL)/((bottomL-bottomL))/10)
        if bottomR > 80 and bottomL < 80:# zumi continue if slightly of track to the left
            
            direction.append(int(zumi.read_z_angle()))           
            zumi.turn_right(5)
            while bottomR < 70 and bottomL > 70:
                zumi.forward(1, 0.2)
                IR=zumi.get_all_IR_data()
                bottomR=IR[1]
                bottomL=IR[3]
            direction.append(int(zumi.read_z_angle()))
            zumi.turn_left(3)
            IR=zumi.get_all_IR_data()
            bottomR=IR[1]
            bottomL=IR[3]
            print(bottomR,bottomL)
            return IR, bottomR, bottomL, L, R, direction
        elif bottomR < 80 and bottomL > 80:#should zumi continue if slightly of track to the right
            direction.append(int(zumi.read_z_angle()))
            IR=zumi.get_all_IR_data()
            zumi.turn_left(5)
            while bottomR < 70 and bottomL > 70:
                zumi.forward(1, 0.2)
                IR=zumi.get_all_IR_data()
                bottomR=IR[1]
                bottomL=IR[3]
            zumi.turn_right(3)
            IR=zumi.get_all_IR_data()
            bottomR=IR[1]
            bottomL=IR[3]
            print(bottomR,bottomL)
            return IR, bottomR, bottomL, L, R, direction
        elif bottomR > 80 and bottomL > 80: # on track
            print("on track")
            zumi.forward(1, 0.2)
            direction.append(int(zumi.read_z_angle()))
            IR=zumi.get_all_IR_data()
            bottomR=IR[1]
            bottomL=IR[3]
            return IR, bottomR, bottomL, L, R, direction
        elif bottomR < 80 and bottomL <80: #
            zumi.turn_left(90)
            all_lights_on()
            all_lights_off()
            all_lights_on()
            all_lights_off()
            return IR, bottomR, bottomL, L, R, direction
        print("zumi go back")
    print("zumi is NOT off track anymore, go forward again")
    IR = zumi.get_all_IR_data()
    L = IR[5]  # left
    R = IR[0]
    zumi.reset_gyro()
    return IR, bottomR, bottomL, L, R, direction






###############################################
##############################################
##################################################
################################################
print(zumi.get_all_IR_data())
#zumi.mpu.calibrate_MPU()
zumi.reset_gyro()
direction=[0]
direction.append(int(zumi.read_z_angle()))
IR, bottomR, bottomL, L, R, direction=start()
for n in range(0,40):
    print(n)
    print("for loop: IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
    if (bottomR >=80 and bottomL>=80):
        IR, bottomR, bottomL, L, R, direction= firstif(IR, bottomR, bottomL, L, R, direction)
    elif bottomR < 65 and bottomL>65:
        if n< 5:
            print("couldn't walk straigth")
            while bottomR<65:
                zumi.turn_right(5)
                IR=zumi.get_all_IR_data()
                bottomR=IR[1]
                bottomL=IR[3]
        else:
            print("WTF")
            print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
            IR, bottomR, bottomL, L, R, direction=firstelif(IR, bottomR, bottomL, L, R, direction)
    elif bottomR > 65 and bottomL<65:
        if n< 5:
            print("couldn't walk straigth")
            while bottomL<65:
                zumi.turn_left(5)
                IR=zumi.get_all_IR_data()
                bottomR=IR[1]
                bottomL=IR[3]
        else:
            print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
            IR, bottomR, bottomL, L, R, direction=secondelif(IR, bottomR, bottomL, L, R, direction)
    elif bottomR < 65 and bottomL<65:
        #print(IR, bottomR, bottomL, L, R, direction)
        IR, bottomR, bottomL, L, R, direction=thirdrdelif(IR, bottomR, bottomL, L, R, direction)
    else:
        print("nothing")
        print("What happened: IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
        IR=zumi.get_all_IR_data()
        bottomR=IR[1]
        bottomL=IR[3]
        print("and now?: IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
        if bottomL>70 and bottomL-bottomR>10 and bottomR<70:
            while bottomL<85 and bottomR <85:
                zumi.turn_left(5)
                IR=zumi.get_all_IR_data()
                bottomR=IR[1]
                bottomL=IR[3]
        if bottomR>70 and bottomR-bottomL>10 and bottomL<70:
            while bottomL<85 and bottomR <85:
                zumi.turn_right(5)
                IR=zumi.get_all_IR_data()
                bottomR=IR[1]
                bottomL=IR[3]
        if bottomL-bottomR<20 and bottomL<90 and bottomR<90:#l
            while bottomL-bottomR<20:
                zumi.turn_right(5)
                print("keep turning r: "+str(bottomL)+ " - "+ str(bottomR)+"  "   +str(bottomL-bottomR ))
        elif bottomL-bottomR>20 and bottomL<90 and bottomR<90:#l
            while bottomL-bottomR>30:
                zumi.turn_left(5)
                print("keep turning l: "+str(bottomL)+ " - "+ str(bottomR)+"  "  +str(bottomL-bottomR ))
        #elif bottomL>90 and bottomR>90:
            #    print("just some finetuning") #the zumi enviroment gives an indent error I can't tell if the tabstopps are off.... 
            #if bottomL-bottomR> 9 and bottomL-bottomR=!0:
           #     zumi.turn_left((bottomL-bottomR)/((bottomL-bottomR))/10)
           # elif bottomR-bottomL> 9 bottomL-bottomR=!0:
           #     zumi.turn_left((bottomR-bottomL)/((bottomL-bottomL))/10)
    print("sleepy time")
    time.sleep(0.1)
    print(zumi.get_all_IR_data())











