import device
import Server
import time

def data(gui,module_gui,d):
    Server.passd_module(module_gui,"Edge:On")
    time.sleep(5)
    processed_data = ""
    data = int(d/10)
    status = "On" if d%10==1 else "Off"
    #print(data,"data", status,"status")
    Server.passd_module(module_gui,"Edge:Off")
    if data == 1:
        Server.passd_module(module_gui,"Devices:On")
        time.sleep(5)
        processed_data, Message = device.simulate_fan(status)
        Server.passd(gui,processed_data)
        Server.passd_module(module_gui,"Devices:Off")
        #print(Message)
    elif data == 2:
        Server.passd_module(module_gui,"Devices:On")
        time.sleep(5)
        processed_data, Message = device.simulate_lamp(status)
        Server.passd(gui,processed_data)
        Server.passd_module(module_gui,"Devices:Off")
        #print(processed_data)
    elif data == 3:
        Server.passd_module(module_gui,"Devices:On")
        time.sleep(5)
        Server.passd_module(module_gui,"Devices:Off")
        processed_data, Message = edge_water_level(module_gui,device.simulate_water_level())
        Server.passd(gui,processed_data)
        
        #print(processed_data)
    elif data == 5:
        Server.passd_module(module_gui,"Devices:On")
        time.sleep(5)
        Server.passd_module(module_gui,"Devices:Off")
        processed_data, Message = edge_soil_moisture(module_gui,device.simulate_soil_moisture())
        Server.passd(gui,processed_data)
        
        #print(processed_data)
    elif data == 6:
        Server.passd_module(module_gui,"Devices:On")
        time.sleep(5)
        processed_data, Message = device.simulate_tv(status)
        Server.passd(gui,processed_data)
        Server.passd_module(module_gui,"Devices:Off")
        #print(processed_data)
    elif data == 7:
        Server.passd_module(module_gui,"Devices:On")
        time.sleep(5)
        processed_data, Message = device.simulate_door(status)
        #print(processed_data)
        Server.passd(gui,processed_data)
        Server.passd_module(module_gui,"Devices:Off")
    if data == 4:
        Server.passd_module(module_gui,"Devices:On")
        time.sleep(5)
        Server.passd_module(module_gui,"Devices:Off")
        Message = edge_temperature(gui,module_gui,device.simulate_temperature_sensor())
    Server.passd_module(module_gui,"Edge:On")
    time.sleep(5)
    Server.passd_module(module_gui,"Edge:Off")
    return Message
                    

def edge_temperature(gui,module_gui,temp):
    Server.passd_module(module_gui,"Edge:On")
    time.sleep(5)
    Server.passd_module(module_gui,"Edge:Off")
    if temp <= 16:
        Server.passd_module(module_gui,"Devices:On")
        time.sleep(5)
        Processed_data,FB = device.simulated_heater("On")
        #print(Processed_data)
        Server.passd(gui,Processed_data)
        Processed_data,FB1 = device.simulated_Air_condition("Off")
        #print(Processed_data)
        Server.passd(gui,Processed_data)
        Server.passd_module(module_gui,"Devices:Off")
    else:
        Server.passd_module(module_gui,"Devices:On")
        time.sleep(5)
        Processed_data,FB = device.simulated_Air_condition("On")
        #print(Processed_data)
        Server.passd(gui,Processed_data)
        Processed_data,FB1 = device.simulated_heater("Off")
        #print(Processed_data)
        Server.passd(gui,Processed_data)
        Server.passd_module(module_gui,"Devices:Off")
    Message = FB+ FB1 +" "+" Current Temperature is " +" "+ str(temp) 
    return Message

def edge_water_level(module_gui,level):
    Server.passd_module(module_gui,"Edge:On")
    time.sleep(5)
    Server.passd_module(module_gui,"Edge:Off")
    Server.passd_module(module_gui,"Devices:On")
    time.sleep(5)
    if level <=10:
        Processed_data,FB = device.simulated_water_pump("On")
    elif level>90:
        Processed_data,FB = device.simulated_water_pump("Off")
    else:
        Processed_data,FB =  "Water Pump:"+"normal", " Enough Water in tank " 
    Server.passd_module(module_gui,"Devices:Off")
    Message = FB  + " Water level is "+ str(level) +"%"
    return Processed_data,Message


def edge_soil_moisture(module_gui,water):
    Server.passd_module(module_gui,"Edge:On")
    time.sleep(5)
    Server.passd_module(module_gui,"Edge:Off")
    Server.passd_module(module_gui,"Devices:On")
    time.sleep(5)
    Server.passd_module(module_gui,"Devices:Off")
    if water > 600:
        Processed_data,FB = device.simulated_water_spinkler("On")
    elif water >= 370 and water <= 600:
        Processed_data,FB = "Water Sprinkler:Off","SOil is Humid"
    else : 
        Processed_data,FB =  device.simulated_water_spinkler("Off")
    Message =  FB  + " SOil Water Content is " + str(water) +" mm of water depth"
    return Processed_data,Message


