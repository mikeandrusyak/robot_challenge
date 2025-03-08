from zumi.zumi import Zumi
import time
from zumi.util.screen import Screen

zumi= Zumi()
screen= Screen()
def start():
    print("start")
    print(0)
    IR, bottomR, bottomL, L, R=zumi_get_IR()
    print("all IR"+ str(IR))
    direction=[0]
    #print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
    print("first if: "+str((bottomR >=80 and bottomL>=80)))
    return IR, bottomR, bottomL, L, R , direction
def zumi_get_IR():
    IR, bottomR, bottomL, L, R=zumi_get_IR()
    return IR, bottomR, bottomL, L, R
def firstif(IR, bottomR, bottomL, L, R, direction): # bottomR >=80 and bottomL>=80
    print("firstif")
    print("zumi move forward")
    zumi.reset_gyro()
    zumi.forward(11, 0.5)
    direction.append(int(zumi.read_z_angle()))
    IR, bottomR, bottomL, L, R=zumi_get_IR()
    print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
    #print("direction: " + str(direction))
    IR, bottomR, bottomL, L, R=zumi_get_IR()
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
    if bottomR<80 or bottomL<80:
        print("first if: offtrack")
        if bottomR<80 and bottomL>85:
            while bottomR>=95 and bottomL>95:
                signal_left_on()
                zumi.turn_left(5)
                signal_left_off()
                IR, bottomR, bottomL, L, R=zumi_get_IR()
        elif bottomL<=80 and bottomR>=85:
            while bottomR>95 and bottomL<=95:
                signal_right_on()
                zumi.turn_right(5)
                signal_right_off()
                IR, bottomR, bottomL, L, R=zumi_get_IR()
    return IR, bottomR, bottomL, L, R, direction

def firstif(IR, bottomR, bottomL, L, R, direction): # bottomR >=80 and bottomL>=80
    print("firstif")
    print("zumi move forward")
    zumi.reset_gyro()
    zumi.forward(11, 0.5)
    direction.append(int(zumi.read_z_angle()))
    IR, bottomR, bottomL, L, R=zumi_get_IR()
    print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
    #print("direction: " + str(direction))
    IR, bottomR, bottomL, L, R=zumi_get_IR()
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
    if bottomR<80 or bottomL<80:
        print("first if: offtrack")
        if bottomR<80 and bottomL>85:
            while bottomR>=95 and bottomL>95:
                signal_left_on()
                zumi.turn_left(5)
                signal_left_off()
                IR, bottomR, bottomL, L, R=zumi_get_IR()
        elif bottomL<=80 and bottomR>=85:
            while bottomR>95 and bottomL<=95:
                signal_right_on()
                zumi.turn_right(5)
                signal_on_off()
                IR, bottomR, bottomL, L, R=zumi_get_IR()
    return IR, bottomR, bottomL, L, R, direction


def secondelif(IR, bottomR, bottomL, L, R, direction): #bottomR > 65 and bottomL<65
    print( "2nd elif")
    signal_right_on()
    zumi.turn_right(90)
    signal_right_off()
    IR, bottomR, bottomL, L, R=zumi_get_IR()
    if  bottomR>55 and bottomL >55:
        print(" zumi turn right")
        direction.append(int(zumi.read_z_angle()))
        zumi.reset_gyro()
        #print("direction: " + str(direction))    
        IR, bottomR, bottomL, L, R=zumi_get_IR()
        print(bottomR, bottomL)
        zumi.forward(9, 0.4)
        time.sleep(0.1)
        print("forward again, secondelif")
        IR, bottomR, bottomL, L, R=zumi_get_IR()
        print(bottomR, bottomL)
    else:
        print("shouldn't made a turn here")
        signal_left_on()
        zumi.turn_left(90)
        signal_left_off()
        while bottomR>=85 and bottomL <=85:
                signal_right_on()
                zumi.turn_right(5)
                signal_right_off()
                IR, bottomR, bottomL, L, R=zumi_get_IR()
    return IR, bottomR, bottomL, L, R, direction


def thirdrdelif(IR, bottomR, bottomL, L, R, direction):#bottomR < 60 and bottomL<60
    print("3rd elif")
    print(R)
    if 1==1: # if it is not clear in which direction to go
        signal_right_on()
        zumi.turn_right(90)
        signal_right_off()
        print("looking right")
        IR, bottomR, bottomL, L, R=zumi_get_IR()
        print("rl: IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
        if bottomR < 80 and bottomL < 80:# wrong direction
            print("wrong direction")
            t1=zumi.read_z_angle()
            signal_left_on()
            zumi.turn_left(180)
            signal_left_off()
            t2=zumi.read_z_angle()
            print (abs(t1-t2))
            if abs(t1-t2)< 170:
                print("why wasn't that a full turn?")
                signal_left_on()
                zumi.turn_left(180-abs(t1-t2))
                signal_left_off()
            print("looking left")
            IR, bottomR, bottomL, L, R=zumi_get_IR()
            print("ll: IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
            print(bottomR < 65 and bottomL < 65)
            if bottomR < 65 and bottomL < 65:# are we right now?
                signal_right_on()
                zumi.turn_right(90)
                signal_right_on()
                print("nope")
                IR, bottomR, bottomL, L, R=zumi_get_IR()
                print("d IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
                if bottomR > 80 or bottomL > 80:
                    print("Your still on track, you should not be if you're at a curve")
                    zumi.forward(9, 0.4)
                    time.sleep(0.1)
                    direction.append(int(zumi.read_z_angle()))
                    IR, bottomR, bottomL, L, R=zumi_get_IR()
                    print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
                    #print("direction: " + str(direction))
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
                    IR, bottomR, bottomL, L, R=zumi_get_IR()
                zumi.reset_gyro()
                return IR, bottomR, bottomL, L, R, direction
            elif bottomL >90  and bottomR<90:
                while bottomL>=90 and bottomR <=90:
                    signal_left_on()
                    zumi.turn_left(5)
                    signal_left_off()
                    IR, bottomR, bottomL, L, R=zumi_get_IR()
                    print("keep turning r: "+str(bottomL)+ " - "+ str(bottomR)+"  "   +str(bottomL-bottomR ))
            else: #atleast partially on track
                IR, bottomR, bottomL, L, R=zumi_get_IR()
                print(" L: "+str(bottomL)+"R: "+str(bottomR)+ " off by: "+str(bottomL-bottomR) + "facing: "+str(zumi.read_z_angle()))
                if (bottomL in range(89,55) or bottomR in range(89,55)) and (bottomL<90 or bottomR<90):#l bottomL-bottomR<20
                    if bottomL>bottomR:
                        while bottomL>=90 and bottomR <=90:
                            signal_left_on()
                            zumi.turn_left(5)
                            signal_left_off()
                            IR, bottomR, bottomL, L, R=zumi_get_IR()
                            print("keep turning r: "+str(bottomL)+ " - "+ str(bottomR)+"  "   +str(bottomL-bottomR ))
                    elif bottomR>bottomL:
                        while bottomR>=90 and bottomL <=90:
                            signal_right_on()
                            zumi.turn_right(5)
                            signal_right_off()
                            IR, bottomR, bottomL, L, R=zumi_get_IR()
                            print("keep turning r: "+str(bottomL)+ " - "+ str(bottomR)+"  "   +str(bottomL-bottomR ))
                elif bottomL-bottomR>20 and bottomL<90 and bottomR<90:#l
                    while bottomL-bottomR>30:
                        signal_left_on()
                        zumi.turn_left(5)
                        signal_left_off()
                        IR, bottomR, bottomL, L, R=zumi_get_IR()
                        print("keep turning l: "+str(bottomL)+ " - "+ str(bottomR)+"  "  +str(bottomL-bottomR ))
                elif bottomL>90 and bottomR>90:
                    print("just some finetuning")
                    if bottomL-bottomR> 9 and bottomL-bottomR!=0:
                        signal_left_on()
                        zumi.turn_left(5)
                        signal_left_off()
                        IR, bottomR, bottomL, L, R=zumi_get_IR()
                    elif bottomR-bottomL> 9 and bottomL-bottomR!=0:
                        signal_left_on()
                        zumi.turn_left(5)
                        signal_left_off()
                        IR, bottomR, bottomL, L, R=zumi_get_IR()
        if bottomR > 80 and bottomL < 80:# zumi continue if slightly of track to the left            
            direction.append(int(zumi.read_z_angle()))  
            
            zumi.turn_right(5)
            while bottomR < 70 and bottomL > 70:
                zumi.forward(2, 0.2)
                time.sleep(0.1)
                IR, bottomR, bottomL, L, R=zumi_get_IR()
            direction.append(int(zumi.read_z_angle()))
            zumi.turn_left(3)
            IR, bottomR, bottomL, L, R=zumi_get_IR()]
            print(bottomR,bottomL)
            return IR, bottomR, bottomL, L, R, direction
        elif bottomR < 80 and bottomL > 80:#should zumi continue if slightly of track to the right
            direction.append(int(zumi.read_z_angle()))
            IR=zumi.get_all_IR_data()
            zumi.turn_left(5)
            while bottomR < 70 and bottomL > 70:
                zumi.forward(2, 0.2)
                time.sleep(0.1)
                IR, bottomR, bottomL, L, R=zumi_get_IR()
            zumi.turn_right(3)
            IR, bottomR, bottomL, L, R=zumi_get_IR()
            print(bottomR,bottomL)
            return IR, bottomR, bottomL, L, R, direction
        elif bottomR > 80 and bottomL > 80: # on track
            print("on track")
            zumi.forward(2, 0.2)
            time.sleep(0.1)
            direction.append(int(zumi.read_z_angle()))
            IR, bottomR, bottomL, L, R=zumi_get_IR()
            return IR, bottomR, bottomL, L, R, direction
        elif bottomR < 80 and bottomL <80: #
            signal_left_on()
            zumi.turn_left(90)
            signal_left_off()
            IR, bottomR, bottomL, L, R=zumi_get_IR()
            return IR, bottomR, bottomL, L, R, direction
        elif bottomL in range(60, 79) and bottomR< 60:
            print("didn't catch the curve left")
            while bottomL<80 and bottomR < 80:
                print("didn't catch the curve left")
                signal_left_on()
                zumi.turn_left(5)
                signal_left_off()
                IR, bottomR, bottomL, L, R=zumi_get_IR()
        elif bottomR in range(60, 79) and bottomL< 60:
            while bottomR<80 and bottomL < 80:
                signal_right_on()
                zumi.turn_right(5)
                signal_right_off()
                IR, bottomR, bottomL, L, R=zumi_get_IR()
        print("zumi go back")
    print("exiting 3rd if ************************")
    IR, bottomR, bottomL, L, R=zumi_get_IR()
    zumi.reset_gyro()
    return IR, bottomR, bottomL, L, R, direction






###############################################
##############################################
##################################################
################################################
def Zumi_go(speed, Test):#add variable speed for speed and duration in all zumi.forward()
    print(zumi.get_all_IR_data())# starting position
    #zumi.mpu.calibrate_MPU()
    zumi.reset_gyro()
    direction=[0]
    direction.append(int(zumi.read_z_angle()))
    IR, bottomR, bottomL, L, R, direction=start()
    for n in range(0,30):
        print(n)
        print("for loop: IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
        if (bottomR >=80 and bottomL>=80):
            IR, bottomR, bottomL, L, R, direction= firstif(IR, bottomR, bottomL, L, R, direction)
        elif bottomR < 65 and bottomL>65 and bottomL<79:
            if n< 5:
                print("couldn't walk straigth")
                while bottomR<=65:
                    signal_right_on()
                    zumi.turn_right(5)
                    signal_right_off()
                    IR, bottomR, bottomL, L, R=zumi_get_IR()
            else:
                print("WTF")
                print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
                IR, bottomR, bottomL, L, R, direction=firstelif(IR, bottomR, bottomL, L, R, direction)
        elif bottomR > 65 and bottomL<65 and bottomR<79:
            if n< 5:
                print("couldn't walk straigth**************")
                while bottomL<=65:
                    signal_left_on()
                    zumi.turn_left(5)
                    signal_left_off()
                    IR, bottomR, bottomL, L, R=zumi_get_IR()
            else:
                print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
                IR, bottomR, bottomL, L, R, direction=secondelif(IR, bottomR, bottomL, L, R, direction)
        elif bottomR < 65 and bottomL<65:
            #print(IR, bottomR, bottomL, L, R, direction)
            IR, bottomR, bottomL, L, R, direction=thirdrdelif(IR, bottomR, bottomL, L, R, direction)
        else:
            print("nothing")
            print("What happened: IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
            IR, bottomR, bottomL, L, R=zumi_get_IR()
            print("and now?: IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
            if bottomL>80 and bottomR<80:
                while (bottomL<=95 and bottomR <=95) or (bottomL>=80 and bottomR<=95):
                    signal_left_on()
                    zumi.turn_left(5)
                    signal_left_off()
                    IR, bottomR, bottomL, L, R=zumi_get_IR()
            if bottomR>80 and bottomL<80:
                while (bottomL<=95 and bottomR <=95)or (bottomR>=80 and bottomL<=95):
                    signal_right_on()
                    zumi.turn_right(5)
                    signal_right_off()
                    IR, bottomR, bottomL, L, R=zumi_get_IR()
            if bottomL<80 and bottomR<80:#l
                while bottomL>bottomR and bottomL<=80 and bottomR<=80:
                    signal_left_on()
                    zumi.turn_left(5)
                    signal_left_off()
                    print("keep turning r: "+str(bottomL)+ " - "+ str(bottomR)+"  "   +str(bottomL-bottomR ))
                    IR, bottomR, bottomL, L, R=zumi_get_IR()
                while bottomR>bottomL and bottomL<=80 and bottomR<=80:
                    signal_right_on()
                    zumi.turn_right(5)
                    signal_right_off()
                    IR, bottomR, bottomL, L, R=zumi_get_IR()
                    print("keep turning r: "+str(bottomL)+ " - "+ str(bottomR)+"  "   +str(bottomL-bottomR ))

            #elif bottomL>90 and bottomR>90:
                #    print("just some finetuning")
                #if bottomL-bottomR> 9 and bottomL-bottomR!=0:
               #     zumi.turn_left((bottomL-bottomR)/((bottomL-bottomR))/10)
               # elif bottomR-bottomL> 9 bottomL-bottomR!=0:
               #     zumi.turn_left((bottomR-bottomL)/((bottomL-bottomL))/10)
        print("sleepy time")
        time.sleep(0.1)
        print(zumi.get_all_IR_data())

Zumi_go(1,False)










