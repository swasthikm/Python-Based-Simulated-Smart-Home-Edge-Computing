import random


def simulate_temperature_sensor():
    Message = random.randint(-20, 30)
    return Message
def simulate_water_level():
    Message = random.randint(0,100)
    print(Message)
    return Message
def simulate_soil_moisture():
    Message = random.randint(0, 1000)
    return Message
def simulate_fan(status):
    print(status)
    if(status == "On"):
        Message = " Fan On"
    else:
        Message = " Fan Off"
    print(Message)
    processed_data = "Fan:"+status
    return processed_data,Message
def simulate_lamp(status):
    if(status == "On"):
        Message = "Lamp On"
    else:
        Message = "Lamp Off"
    processed_data = "Light:"+ status
    return processed_data,Message
def simulate_tv(status):
    if(status == "On"):
        Message = "TV On"
    else:
        Message = "TV Off"
    processed_data = "TV:"+status
    return processed_data,Message
def simulate_door(status):
    if(status == "On"):
        Message = "Door Open"
    else:
        Message = "Door Close"
    processed_data = "Door:"+str(status)
    return processed_data,Message
def simulated_heater(status):
    if(status == "On"):
        Message = "Heater Turned On"
    else:
        Message = "Heater Turned Off"
    processed_data = "Heater:"+str(status)
    return processed_data,Message
def simulated_Air_condition(status):
    if(status == "On"):
        Message = "AC Turned On"
    else:
        Message = "AC Turned Off"
    processed_data = "AC:"+str(status)
    return processed_data,Message
def simulated_water_pump(status):
    if(status == "On"):
        Message = " Pump On"
    else:
        Message = " Pump Off"
    processed_data = "Water Pump:" + str(status)
    return processed_data,Message
def simulated_water_spinkler(status):
    if(status == "On"):
        Message ="Spinkler Is on"
    else:
        Message ="Spinkler Is off"
    print(status)
    processed_data = "Water Sprinkler:" + str(status)
    return processed_data,Message
