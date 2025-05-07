# CAN Sniffer
<p align="center">
<img src="https://github.com/user-attachments/assets/1291cf51-079f-44d1-adca-f9e440341482" width="900"/>
<br>
<em>Reading live data from the CAN Bus using the hardware attachment and PyQt GUI from the laptop</em>  
<br><br>

<img src="https://github.com/user-attachments/assets/a224c216-fddd-44b4-8bc1-b42e989e5df1" width="900"/>
<br>
<em>OBD2 Port on the left, Arduino Uno in the middle and mcp2515 module on the right</em>
<br><br>

<img src="https://github.com/user-attachments/assets/22d8be4c-3309-4c7f-9ecb-5262fa9ef614" width="900"/>
<br>
<em>PyQt GUI when first launched</em>

</p>

## Getting Started

#### Hardware Requirments
1. Arduino Uno
2. OBD2 Port
3. MCP2515 CAN Bus Module

#### Wiring
| Arduino | MCP2515 |
|---------|---------|
| Pin 2 | INT |
| Pin 13 | SCK |
| Pin 11 | SI |
| Pin 12 | SO |
| Pin 10 | CS |
| 5V | VCC |
| GND | GND |

#### Steps
1. Connect the MCP2515 CAN Bus module to the arduino according to the above pinnout
2. Download repository
3. Upload the provided platformio code onto the Arduino (/PlatformIO/CAN Sniffer)
4. Open up the PyQtGUI folder from your terminal and run the following:
```shell
pipenv shell
pipenv install -r requirements.txt
python main.py
```
5. Connect OBD2 port to your car and scan away!
