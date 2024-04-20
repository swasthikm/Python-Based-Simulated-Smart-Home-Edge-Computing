import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
import threading
import socket
import edge
import time

class DeviceControl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

    # Create two horizontal layouts for the rows
        row1_layout = QHBoxLayout()
        row2_layout = QHBoxLayout()
        row3_layout = QHBoxLayout()

        # Create a horizontal layout for each device with an image
        self.deviceImages = {
            'Fan': self.createDeviceLayout('Fan', 'Images/fan_off.PNG','Images/fan_off.PNG', 'Images/fan_off.PNG'),
            'Light': self.createDeviceLayout('Light', 'Images/light_off.PNG','Images/light_off.PNG', 'Images/light_on.PNG'),
            'Water Sprinkler': self.createDeviceLayout('Water Sprinkler', 'Images/Water Sprinkler_off.PNG', 'Images/Water Sprinkler_off.PNG', 'Images/Water Sprinkler_on.PNG'),
            'Door': self.createDeviceLayout('Door', 'Images/door_off.PNG','Images/door_off.PNG', 'Images/door_on.PNG'),
            'Temperature Sensor': self.createDeviceLayout('Temperature Sensor', 'Images/Temperature Sensor_off.PNG','Images/Temperature Sensor_off.PNG', 'Images/Temperature Sensor_on.PNG'),
            'Water Level Detector': self.createDeviceLayout('Water Level Detector', 'Images/Water Level Detector_off.PNG','Images/Water Level Detector_off.PNG', 'Images/Water Level Detector_on.PNG'),
            'Soil Moisture Sensor': self.createDeviceLayout('Soil Moisture Sensor', 'Images/Soil Moisture Sensor_off.PNG','Images/Soil Moisture Sensor_off.PNG', 'Images/Soil Moisture Sensor_on.PNG.PNG'),
            'TV': self.createDeviceLayout('TV', 'Images/tv_off.PNG','Images/tv_off.PNG', 'Images/tv_on.PNG'),
            'Heater': self.createDeviceLayout('Heater', 'Images/heater_off.PNG','Images/heater_off.PNG', 'Images/heater_on.PNG'),
            'AC': self.createDeviceLayout('AC', 'Images/AC_off.PNG','Images/AC_off.PNG', 'Images/AC_on.PNG'),
            'Water Pump': self.createDeviceLayout('Water Pump', 'Images/Water Pump_off.PNG', 'Images/Water Pump_normal.PNG', 'Images/Water Pump_on.PNG')
        }

        # Add the device layouts to the main layout
        for i, (device_name, (device_layout, _)) in enumerate(self.deviceImages.items()):
            if i < 4:
                row1_layout.addLayout(device_layout)
            elif i>=4 and i<8:
                row2_layout.addLayout(device_layout)
            else:
                row3_layout.addLayout(device_layout)


        main_layout.addLayout(row1_layout)
        main_layout.addLayout(row2_layout)
        main_layout.addLayout(row3_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Device Control')
        self.show()

    
    def createDeviceLayout(self, device_name, off_image, normal_image, on_image):
        # Create a horizontal layout
        hLayout = QHBoxLayout()

        # Create a label to display the image
        label = QLabel(self)
        pixmap = QPixmap(off_image)
        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.size())

        # Add the label to the layout
        hLayout.addWidget(label)

        return hLayout, label
    

    def updateDeviceState(self, device_name, state):
        _, label = self.deviceImages[device_name]

        if state == "On":
            label.setPixmap(QPixmap(f'Images/{device_name.lower()}_on.PNG'))
        elif state == "Off":
            label.setPixmap(QPixmap(f'Images/{device_name.lower()}_off.PNG'))
        else:
            label.setPixmap(QPixmap(f'Images/{device_name.lower()}_normal.PNG'))
        return
class ModuleControl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.initModulesLayout()
        self.setLayout(self.main_layout)
        self.setWindowTitle('Module Control')
        self.show()

    def initModulesLayout(self):
        modules_layout = QHBoxLayout()

        self.modules = {
            'Server': self.createModuleLayout('Server', 'Images/server_off.PNG', 'Images/server_normal.PNG', 'Images/server_on.PNG'),
            'Edge': self.createModuleLayout('Edge', 'Images/edge_off.PNG', 'Images/edge_normal.PNG', 'Images/edge_on.PNG'),
            'Devices': self.createModuleLayout('Devices', 'Images/devices_off.PNG', 'Images/devices_normal.PNG', 'Images/devices_on.PNG')
        }

        for module_name, (module_layout, _) in self.modules.items():
            modules_layout.addLayout(module_layout)

        self.main_layout.addLayout(modules_layout)

    def createModuleLayout(self, module_name, image_off, image_normal, image_on):
        hLayout = QHBoxLayout()
        label = QLabel(self)
        pixmap = QPixmap(image_off)
        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.size())
        hLayout.addWidget(label)
        return hLayout, label

    def updateModuleState(self, module_name, state):
        _, label = self.modules[module_name]
        if state == "On":
            label.setPixmap(QPixmap(f'Images/{module_name.lower()}_on.PNG'))
        elif state == "Off":
            label.setPixmap(QPixmap(f'Images/{module_name.lower()}_off.PNG'))
        else:
            label.setPixmap(QPixmap(f'Images/{module_name.lower()}_normal.PNG'))
def passd(gui,processed_data):
    print(processed_data)
    device, state = processed_data.split(':')
    gui.updateDeviceState(device, state.strip())
    return
def passd_module(module_gui,data):
    module, state = data.split(':')
    module_gui.updateModuleState(module, state.strip())
    return
def start_server(gui,module_gui):
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode('utf-8')
                passd_module(module_gui,"Server:On")
                time.sleep(5)
                data = int(data)
                passd_module(module_gui,"Server:Off")
                Message = edge.data(gui,module_gui,data)
                print(Message)
                passd_module(module_gui,"Server:On")
                time.sleep(5)
                passd_module(module_gui,"Server:Off")
                conn.sendall(Message.encode('utf-8'))
                

                #Update device states in the GUI
                
                #gui.updateDeviceState(device.strip(), state.strip()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = DeviceControl()
    module_gui = ModuleControl()
    threading.Thread(target=start_server, args=(gui,module_gui,), daemon=True).start()
    sys.exit(app.exec_())
