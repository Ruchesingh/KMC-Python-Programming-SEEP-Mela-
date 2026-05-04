#smart home device system
 #multilevel inheritance Exercise
 
class Device():
 device_id = "RS1234"
 status = "OFF"

 def turn_on(self):
        self.status = "ON"
        return f"Device {self.device_id} is turned ON"
 def turn_off(self):
        self.status = "OFF"
        return f"Device {self.device_id} is turned OFF"
        
class SmartDevice(Device):
    connectivity = "bluetooth"
    connected = False

    def connect(self):
        if self.status == "ON":
            self.connected = True
            return f"{self.device_id} connected via {self.connectivity}"
        else:
            return "Turn on the device first to connect"
        
class SmartThermostat(SmartDevice):
    temperature = 50

    def set_temperature(self, temp):
        if temp > self.temperature:
            return self.turn_on()
        else:
            return self.turn_off()
    
    def display(self):
        return f"Device Id: {self.device_id}\nStatus: {self.status}\nConnectivity: {self.connectivity}"
        

obj = SmartThermostat()
obj.set_temperature(90)
print(obj.display())       
    
              