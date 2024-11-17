# Feeding Station Automation Using Raspberry Pi

This project automates an animal feeding station using a Raspberry Pi, a PIR (Passive Infrared) sensor for motion detection, and a dispenser mechanism. When the PIR sensor detects movement, the dispenser is activated for 5 seconds to release food or water for animals.

Here, another file called simulator has been uploaded where you can manually enter values to see the working on system.

## Features
- Detects animal presence using a PIR motion sensor.
- Activates a dispenser for a specified duration (default: 5 seconds).
- Outputs real-time detection messages to the console.
- Gracefully handles program interruptions and cleans up GPIO settings.

## Prerequisites
### Hardware Components
- Raspberry Pi (any compatible model)
- PIR Sensor
- Dispenser mechanism (can be simulated using an LED or motor)
- Jumper wires and breadboard for connections
- Power source for the Raspberry Pi


### Software
- Raspbian OS or any Raspberry Pi-compatible Linux distribution.
- Python 3 installed on the Raspberry Pi.

## Circuit Diagram
1. **PIR Sensor**:
   - Connect **VCC** to Raspberry Pi's 3.3V or 5V pin.
   - Connect **GND** to a ground pin on the Raspberry Pi.
   - Connect the **OUT** pin to GPIO 17 on the Raspberry Pi.

2. **Dispenser (or LED)**:
   - Connect the **positive leg** of the LED to GPIO 27.
   - Connect the **negative leg** to a resistor and then to GND.
   - For motors, use a relay or motor driver module between GPIO 27 and the motor.

## Installation
1. Clone this repository or copy the Python script to your Raspberry Pi.
2. Ensure the Raspberry Pi GPIO library is installed:
   ```bash
   sudo apt update
   sudo apt install python3-rpi.gpio
   python3 pet_feeding_station
