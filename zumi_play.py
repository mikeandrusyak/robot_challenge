print(zumi.get_all_IR_data())
#zumi.mpu.calibrate_MPU()
zumi.reset_gyro()
direction=[0]
direction.append(int(zumi.read_z_angle()))
for n in range(0,40):
    print(n)
    IR=zumi.get_all_IR_data()
    print("all IR"+ str(IR))
    bottomR=IR[1]
    bottomL=IR[3]
    #print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
    print("first if: "+str((bottomR >=90 and bottomL>=90)))
    if (bottomR >=90 and bottomL>=90):
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
#        while (bottomR <=60 and bottomL<=60):
  #          print("zumi is off track, go back")
  #          LR=zumi.get_all_IR_data()
   #         L=LR[5]
    #        R=LR[0]
     #       print("Left and Right: "+ str(L)+" , "+str(R))
      #      zumi.reverse(2, 0.4)
       #     direction.append(int(zumi.read_z_angle()))
        #    IR=zumi.get_all_IR_data()
         #   bottomR=IR[1]
          #  bottomL=IR[3]
           # if bottomR >= 90 and L> 190:
            #    zumi.turn_left(90)
             #   direction.append(int(zumi.read_z_angle()))
       #     print("IR_1: "+ str(bottom))
        #    print("direction: " + str(direction))

    elif bottomR < 80 and bottomL>90:
        print( "2nd elif")
        zumi.turn_left(90)
        direction.append(int(zumi.read_z_angle()))
        zumi.reset_gyro()
        print ("direction: " + str(direction))
        print(" zumi turn left")
        zumi.forward(9, 0.4)
        print("forward again")
    elif bottomR > 90 and bottomL<80:
        print( "3rd elif")
        zumi.turn_right(90)
        direction.append(int(zumi.read_z_angle()))
        zumi.reset_gyro()
        print("direction: " + str(direction))
        print(" zumi turn right")
        zumi.forward(9, 0.4)
        print("forward again")
    elif bottomR < 60 and bottomL<60:
        while (bottomR <60 and bottomL<60):
            print("last elif: "+str((bottomR <=60 and bottomL<=60)))
            print("zumi is off track, go back")
            IR=zumi.get_all_IR_data()
            L=LR[5]
            R=LR[0]
            print("Left and Right: "+ str(L)+" , "+str(R))
            bottomR=IR[1]
            bottomL=IR[3]
            print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
            zumi.reverse(1, 0.3)
        print("zumi is NOT off track anymore, go back")
        if IR[5]>190 and (bottomR < 60 or bottomL<60):
            zumi.turn_left(90)
            direction.append(int(zumi.read_z_angle()))
            zumi.reset_gyro()
    #elif bottomR < 60 and bottomL<60:
        #while (bottomR <60 and bottomL<60):
#            print("last elif: "+str((bottomR <=60 and bottomL<=60)))
 #           print("zumi is off track, go back")
  #          LR=zumi.get_all_IR_data()
   #         L=LR[5]
    #        R=LR[0]
     #       print("Left and Right: "+ str(L)+" , "+str(R))
      #      IR=zumi.get_all_IR_data()
            #print("all IR"+ str(IR))
       #     bottomR=IR[1]
        #    bottomL=IR[3]
        #    print("IR_0(R): "+str(bottomR)+" , "+"IR_3(L): " +str(bottomL))
         #   zumi.reverse(3, 0.4)
    print("sleepy time")
    time.sleep(0.1)
    print(zumi.get_all_IR_data())


#if zumi.get_all_IR_data() >=99:
   # print ("zumi is on track")
#if zumi.get_all_IR_data()[1] is in range(9, 15):
 #   print("zumi is offtrack, go back)
#    zumi.stop()
 #   while zumi.get_all_IR_data()[1] is in range(9, 15):
#          zumi.reverse()
#if zumi.get_all_IR_data() is in range(15, 20):
 #   print("zumi is seeing blue)
#if zumi.get_all_IR_data() is in range(38, 45):