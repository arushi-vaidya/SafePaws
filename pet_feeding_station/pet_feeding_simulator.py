import time

# Simulated PIR sensor and dispenser actions
PIR_SENSOR_PIN = 17 
DISPENSER_PIN = 27   

# Simulate the PIR sensor being triggered (use `True` to simulate detection)
sensor_triggered = False

def activate_dispenser():
    print("Dispenser activated!")
    time.sleep(5)  # Simulate dispenser being on for 5 seconds
    print("Dispenser deactivated.")

try:
    while True:
        # Simulate sensor detection
        sensor_triggered = input("Is there an animal? (yes/no): ").strip().lower() == "yes"
        
        if sensor_triggered:
            print("Animal detected at feeding station!")
            activate_dispenser()
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Feeding station deactivated.")
