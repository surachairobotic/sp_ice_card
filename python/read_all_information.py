#!/usr/bin/env python3

import time
import ctypes
sp_ice = ctypes.CDLL("C:\\Program Files\\RAYLASE\\SP-ICE\\bin\\SP-ICE.dll")

def main():
    global sp_ice
    err = sp_ice.Init_Scan_Card_Ex()
    print(str(err) + " : " + str(type(err)))
    if err != 0:
        msgs = sp_ice.Get_Error_Message(err)
        print("Err != 0 : " + str(type(msgs)))
    print("Init_Scan_Card_Ex : " + str(msgs))
    read()
    control()
    print("Remove_Scan_Card_Ex : " + str(sp_ice.Remove_Scan_Card_Ex(1)))

def control():
    global sp_ice
    print("Laser_Off : " + str(sp_ice.Laser_Off()))
    print("Laser_On : " + str(sp_ice.Laser_On()))
    time.sleep(1)
    print("Laser_Off : " + str(sp_ice.Laser_Off()))
    
    print("Set_Delays : " + str(sp_ice.Set_Delays()))
    
    print("Enable_Laser : " + str(sp_ice.Enable_Laser()))
    print("Laser_Off : " + str(sp_ice.Laser_Off()))
    print("Laser_On : " + str(sp_ice.Laser_On()))
    time.sleep(1)
    print("Laser_Off : " + str(sp_ice.Laser_Off()))
    print("Disable_Laser : " + str(sp_ice.Disable_Laser()))

def read():
    global sp_ice
    print("Hello world !!!")
    print("Get_Active_Card : " + str(sp_ice.Get_Active_Card()))
    print("Set_Active_Card : " + str(sp_ice.Set_Active_Card(1)))
    print("Get_Active_Card : " + str(sp_ice.Get_Active_Card()))
    print("Get_Counts : " + str(sp_ice.Get_Counts()))
    print("Get_CPU_Type : " + str(sp_ice.Get_CPU_Type()))
    print("Get_DLL_Version : " + str(sp_ice.Get_DLL_Version()))
    
    print("Get_Ident_Ex : " + str(sp_ice.Get_Ident_Ex()))
    print("Get_Jump_Speed : " + str(sp_ice.Get_Jump_Speed()))
    print("Get_Mark_Speed : " + str(sp_ice.Get_Mark_Speed()))
    #print("Get_Mode_Mask : " + str(sp_ice.Get_Mode_Mask()))
    print("Get_SPC1_Version : " + str(sp_ice.Get_SPC1_Version()))
    print("Get_System_Status : " + str(sp_ice.Get_System_Status()))
    print("Get_Version : " + str(sp_ice.Get_Version()))
    #print("Get_XY_Pos : " + str(sp_ice.Get_Version()))

    # RLC Only
    #print("Get_Device_Description_String : " + str(sp_ice.Get_Device_Description_String()))
    #print("Get_Driver_Version : " + str(sp_ice.Get_Driver_Version()))
    #print("Get_Firmware_Version : " + str(sp_ice.Get_Firmware_Version()))
    #print("Get_Hardware_Version : " + str(sp_ice.Get_Hardware_Version()))
    #print("Get_Library_Version : " + str(sp_ice.Get_Library_Version()))
    

if __name__ == "__main__":
    main()
    print("END !!!")
