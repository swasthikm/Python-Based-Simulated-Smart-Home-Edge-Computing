import socket
import random
import time
import tkinter as tk

host = '127.0.0.1'
port = 12345

# Dictionary to store device states 
device_states = {
    'Fan': False,
    'Light': False,
    'Tank_Water_level':False,
    'Temperature_sensor':False,
    'Soil_moisture_level':False,
    'TV': False,
    'Door': False
}

def update_display(display):
    display_var.set(display)

def send_message(device_name):
    device_states[device_name] = not device_states[device_name]  # Toggle state
    print(device_name,"state",device_states[device_name])
    print(f"Sending Device control: {device_name} (State: {device_states[device_name]})")
    Select = device_name
    if Select == 'Fan':
        if device_states[device_name]:
            Device = 11
        else:
            Device = 10
    elif Select == 'Light':
        if device_states[device_name]:
            Device = 21
        else:
            Device = 20
    elif Select == 'Tank_Water_level':
        if device_states[device_name]:
            Device = 31
        else:
            Device = 30
    elif Select == 'Temperature_sensor':
        if device_states[device_name]:
            Device = 41
        else:
            Device = 40
    elif Select == 'Soil_moisture_level':
        if device_states[device_name]:
            Device = 51
        else:
            Device = 50
    elif Select == 'TV':
        if device_states[device_name]:
            Device = 61
        else:
            Device = 60
    elif Select == 'Door':
        if device_states[device_name]:
            Device = 71
        else:
            Device = 70
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(str(Device).encode('utf-8'))
        processed_data = client_socket.recv(1024).decode('utf-8')
        print(processed_data)
        update_display(processed_data)

root = tk.Tk()
root.title("Smart Home")

display_var = tk.StringVar()
display_box = tk.Label(root, textvariable=display_var, font=("Arial", 12), relief="solid", padx=100, pady=10,bg="#007bff", fg="black")
display_box.pack(pady=20)

# Create buttons for each device
devices = ['Fan', 'Light', 'Tank_Water_level', 'Temperature_sensor','Soil_moisture_level', 'TV', 'Door']
# Create buttons in a horizontal layout
button_frame = tk.Frame(root)
button_frame.pack()

for i, device_name in enumerate(devices):
    button = tk.Button(
        button_frame,
        text=device_name,
        background= '#007bff',
        foreground= '#ffffff',
        activebackground = '#0056b3' ,
        activeforeground = '#ffffff',
        command=lambda device_name=device_name: send_message(device_name),  # Capture correct value
        width=18  
    )
    button.pack(side=tk.BOTTOM, padx=5)
update_display("Smart Home Control")
root.mainloop() 



