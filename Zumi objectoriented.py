from zumi.zumi import Zumi
import time
from zumi.util.screen import Screen

zumi= Zumi()
screen= Screen()
def start():
    print(n)
    IR=zumi.get_all_IR_data()
    print("all IR"+ str(IR))
    bottomR=IR[1]
    bottomL=IR[3]
    #print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
    print("first if: "+str((bottomR >=80 and bottomL>=80)))
    return IR, bottomR, bottomL
def firstif():#zumi needs to go forward
    print("zumi move forward")
    zumi.forward(9, 0.4)
    direction.append(int(zumi.read_z_angle()))
    IR=zumi.get_all_IR_data()
    bottomR=IR[1]
    bottomL=IR[3]
    print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
    print("direction: " + str(direction))
    LR=zumi.get_all_IR_data()
    L=LR[5]
    R=LR[0]
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
    return IR, bottomR, bottomL, L, R

def firstelif(): #bottomR < 60 and bottomL>60 zumi needs to turn left
    print( "2nd elif")
    zumi.turn_left(90)
    direction.append(int(zumi.read_z_angle()))
    zumi.reset_gyro()
    print ("direction: " + str(direction))
    print(" zumi turn left")
    zumi.forward(9, 0.4)
    print("forward again")
    return direction

def secondelif(): #bottomR > 60 and bottomL<60 zumi needs to turn right
    print( "2nd elif")
    zumi.turn_right(90)
    direction.append(int(zumi.read_z_angle()))
    zumi.reset_gyro()
    print("direction: " + str(direction))
    print(" zumi turn right")
    zumi.forward(9, 0.4)
    print("forward again")
    return direction


def thirdrdelif(IR, bottomR, bottomL, direction, L, R): #bottomR < 60 and bottomL < 60: zumi has reached the end of the line,
    #  turn left or right or turn back
    print("3rd elif")
    print("R"+str(R))
    print("L"+str(L))
    if R > 180:
        zumi.turn_right(90)
        direction.append(int(zumi.read_z_angle()))
        zumi.reset_gyro()
        IR = zumi.get_all_IR_data()
        bottomR = IR[1]
        bottomL = IR[3]
        print("IR_0(R): " + str(bottomR) + " , " + "IR_3(L): " + str(bottomL))
        # if bottomR >=90 and bottomL>=90:
        print(L)
    elif L < 180 and 1 == 1:
        zumi.turn_left(90)
        direction.append(int(zumi.read_z_angle()))
        zumi.reset_gyro()
        IR = zumi.get_all_IR_data()
        bottomR = IR[1]
        bottomL = IR[3]
        print("IR_0(R): " + str(bottomR) + " , " + "IR_3(L): " + str(bottomL))
        print("last elif: " + str((bottomR <= 60 and bottomL <= 60)))
        print("zumi is off track, go back")
        IR = zumi.get_all_IR_data()
        L = LR[5]
        R = LR[0]
        print("Left and Right: " + str(L) + " , " + str(R))
    else: # if it is not clear in which direction to go
        zumi.turn_right(90)

        IR = zumi.get_all_IR_data()
        bottomR = IR[1]
        bottomL = IR[3]
        if bottomR < 80 or bottomL < 80:
            zumi.turn_left(180)
            IR = zumi.get_all_IR_data()
            bottomR = IR[1]
            bottomL = IR[3]
            if bottomR < 80 or bottomL < 80:
                zumi.turn_right(90)
        if bottomR > 80 and bottomL < 80:#should zumi continue if slightly of track
            zumi.reverse(1, 0.2)
        print("zumi go back")
    print("zumi is NOT off track anymore, go forward again")
    IR = zumi.get_all_IR_data()
    L = LR[5]  # left
    R = LR[0]

    #if IR[5] > 190 and (bottomR > 60 or bottomL > 60): #this code should be outdated
   #     print("hello")
   #     zumi.turn_left(90)
   #     direction.append(int(zumi.read_z_angle()))
   #     zumi.reset_gyro()
   #     print("direction: " + str(direction))
   #     print("zumi turn left")
    #    IR = zumi.get_all_IR_data()
    #    bottomR = IR[1]
    #    bottomL = IR[3]
    #    print()
   #     if (bottomR < 60 and bottomL < 60):
   #         print("did I go to far or not far enough?")
   #         zumi.turn_right(90)
    #        zumi.forward(2, 0.2)
    #        zumi.turn_left(90)
    #        IR = zumi.get_all_IR_data()
    #        bottomR = IR[1]
   #         bottomL = IR[3]
   #         if bottomR < 60 and bottomL < 60:
   #             print("go back further")
    #            zumi.turn_right(90)
   #             zumi.reverse(2, 0.2)
    #elif IR[0] > 190 and (bottomR > 60 or bottomL > 60):
    #    print("hello")
    #    zumi.turn_right(90)
    #    direction.append(int(zumi.read_z_angle()))
    #    zumi.reset_gyro()
    #    print("direction: " + str(direction))
    #    print("zumi turn left")
    #    IR = zumi.get_all_IR_data()
   #     bottomR = IR[1]
    #    bottomL = IR[3]
    #    print()
    #    if (bottomR < 60 and bottomL < 60):
     #       print("did I go to far or not far enough?")
     #       zumi.turn_right(90)
    #        zumi.forward(2, 0.2)
     #       zumi.turn_left(90)
       #     IR = zumi.get_all_IR_data()
       #     bottomR = IR[1]
      #      bottomL = IR[3]
      #      if bottomR < 60 and bottomL < 60:
      #          print("go back further")
      #          zumi.turn_right(90)
      #          zumi.reverse(2, 0.2)
    return IR, bottomR, bottomL, L, R, direction

#elif bottomR < 60 and bottomL < 60: #both are off probably in another loop
def LRoB(IR, bottomR, bottomL, L, R, direction) #zumi needs to turn left right or turn back it was
    # originaly meant to prevent a specific fail state that might now be obsolet
    print("last elif: " + str((bottomR <= 60 and bottomL <= 60)))
        if R > 180:
            zumi.turn_right(90)
            print("right")
            IR = zumi.get_all_IR_data()
            bottomR = IR[1]
            bottomL = IR[3]
            print("IR_0(R): " + str(bottomR) + " , " + "IR_3(L): " + str(bottomL))
            if bottomR >= 90 and bottomL >= 90:
                print("forward")
                zumi.forward(2, 0.2)
            if bottomR >= 90 or bottomL >= 90:
                print("close enough")
                zumi.forward(2, 0.2)
            # elif L<180 and 2==2:
            # zumi.turn_left(90)
            print("right")
            IR = zumi.get_all_IR_data()
            bottomR = IR[1]
            bottomL = IR[3]
            print("IR_0(R): " + str(bottomR) + " , " + "IR_3(L): " + str(bottomL))
            if bottomR >= 90 and bottomL >= 90:
                print("forward")
                zumi.forward(2, 0.2)
            if bottomR >= 90 or bottomL >= 90:
                print("close enough")
                zumi.forward(2, 0.2)
        while (bottomR < 60 and bottomL < 60):
            print("last elif: " + str((bottomR <= 60 and bottomL <= 60)))
            print("zumi is off track, go back")
            LR = zumi.get_all_IR_data()
            L = LR[5]
            R = LR[0]
            print("Left and Right: " + str(L) + " , " + str(R))
            IR = zumi.get_all_IR_data()
            # print("all IR"+ str(IR))
            bottomR = IR[1]
            bottomL = IR[3]
            print("IR_0(R): " + str(bottomR) + " , " + "IR_3(L): " + str(bottomL))
            zumi.reverse(3, 0.4)
            if R > 180:
                zumi.turn_right(90)
                print("right")
                IR = zumi.get_all_IR_data()
                bottomR = IR[1]
                bottomL = IR[3]
                print("IR_0(R): " + str(bottomR) + " , " + "IR_3(L): " + str(bottomL))
                if bottomR >= 90 and bottomL >= 90:
                    print("forward")
                    zumi.forward(2, 0.2)
                if bottomR >= 90 or bottomL >= 90:
                    print("close enough")
                    zumi.forward(2, 0.2)
                zumi.forward(2, 0.2)
            elif L > 180:
                zumi.turn_left(90)
                print("right")
                IR = zumi.get_all_IR_data()
                bottomR = IR[1]
                bottomL = IR[3]
                print("IR_0(R): " + str(bottomR) + " , " + "IR_3(L): " + str(bottomL))

                if bottomR >= 90 and bottomL >= 90:
                    print("forward")
                    zumi.forward(2, 0.2)
                elif bottomR >= 90 or bottomL >= 90:
                    print("close enough")
                    zumi.forward(2, 0.2)
            if bottomR >= 90 and bottomL >= 90:
                print("forward")
                zumi.forward(2, 0.2)
            if bottomR >= 90 or bottomL >= 90:
                print("close enough")
                zumi.forward(2, 0.2)






###############################################
##############################################
##################################################
################################################
print(zumi.get_all_IR_data())
# zumi.mpu.calibrate_MPU()
zumi.reset_gyro()
direction = [0]
direction.append(int(zumi.read_z_angle()))
for n in range(0, 40):
    IR, bottomR, bottomL = start()
    if (bottomR >= 80 and bottomL >= 80): #zumi needs to go forward
        IR, bottomR, bottomL, L, R = firstif()
    elif bottomR < 60 and bottomL > 60: #turn Left
        direction = firstelif()
    elif bottomR > 60 and bottomL < 60: #turn Right
        direction = secondelif()
    elif bottomR < 60 and bottomL < 60:  #turn left or right or turn back
        IR, bottomR, bottomL, L, R, direction = thirdrdelif(IR, bottomR, bottomL, direction, L, R)

    print("sleepy time")
    time.sleep(0.1)
    print(zumi.get_all_IR_data())











