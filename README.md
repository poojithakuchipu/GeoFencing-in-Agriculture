# GeoFencing-in-Agriculture
IoT-based Geofencing system for smart agriculture using Arduino, GSM, and IR sensors to monitor farm boundaries, prevent intrusions, and provide real-time alerts for enhanced crop and livestock security.

🌱 Geofencing in Agriculture

IoT-based farm security and monitoring system using Arduino, GSM, and IR sensors.

This project implements a geofencing system for agriculture that detects intrusions (humans, animals, or unauthorized movement) and sends real-time alerts to farmers via SMS and phone calls. The system ensures farm security, livestock safety, and efficient monitoring without the need for manual supervision.

📌 Features

🚜 Farm Security – Detects intrusions and triggers alerts.

📲 Real-Time SMS & Calls – Uses GSM module for instant notifications.

🔔 Buzzer Alerts – Local audible alarm on intrusion.

🌞 Scalable & Cost-Effective – Built with affordable components like Arduino Uno, IR sensors, and GSM module.

♻️ Sustainable – Can be powered via solar panels for off-grid farms.

🐄 Livestock Safety – Prevents straying and protects against theft.

## 🖼️ Block Diagram.
          ┌────────────┐
          │  IR Sensor │
          └─────┬──────┘
                │
                ▼
        ┌──────────────┐
        │   Arduino    │
        │   (Uno R3)   │
        └─────┬───┬────┘
              │   │
     ┌────────┘   └─────────┐
     ▼                      ▼
┌─────────────┐      ┌─────────────┐
│    Buzzer   │      │   GSM Mod.  │
│  (Alert)    │      │ (SMS + Call)│
└─────────────┘      └──────┬──────┘
                            │
                            ▼
                     📱 Farmer Mobile


🛠️ Hardware Components

Arduino Uno – Microcontroller (system brain).

GSM Module (SIM900 / SIM800) – Sends SMS and calls.

IR Sensor – Detects motion at the boundary.

Buzzer – Audible intrusion alert.

Power Supply / Battery / Solar – Provides system power.

Wires, Enclosure Box, PCB – Supporting components.

🔌 Circuit Connections

IR Sensor Pin → Arduino Pin 2

Buzzer Pin → Arduino Pin 3

GSM Tx → Arduino Pin 10

GSM Rx → Arduino Pin 11

Power Supply → Arduino + GSM + Sensors

💻 Code Overview
const int irSensorPin = 2;   // IR Sensor input pin
const int buzzerPin  = 3;   // Buzzer output pin
const int gsmTx      = 10;  // GSM Module Tx pin
const int gsmRx      = 11;  // GSM Module Rx pin


setup(): Initializes GSM, IR sensor, buzzer, and sends startup SMS.

loop(): Continuously monitors IR sensor → triggers buzzer + SMS + call on intrusion.

sendSMS(): Sends custom SMS to farmer.

makeCall(): Places a call to alert the farmer.

📲 Sample Alerts

SMS Alert:

Alert! Intrusion detected in the farm.


Call Alert:

Automatic call placed to farmer’s registered number.

🚀 How to Run

Connect components as per circuit diagram.

Insert SIM card into GSM module.

Upload the Arduino sketch using Arduino IDE.

Open Serial Monitor (9600 baud) → You’ll see:

System Ready...
GeoFencing System is Active.


On intrusion → buzzer rings + SMS & call alert.

📊 Project Benefits

✅ Improved Security – Protects crops, livestock, and equipment.

✅ Cost-Effective – Cheaper than CCTV & electric fencing.

✅ 24/7 Monitoring – Works day & night.

✅ Eco-Friendly – Supports solar power.

✅ Farmer Friendly – Easy setup, minimal maintenance.

📖 Future Enhancements

🌐 Cloud integration for data logging & remote monitoring.

🤖 AI-based intrusion classification (animals vs humans).

🛰️ GPS-enabled tracking of livestock & equipment.

📡 IoT dashboard for real-time farm analytics.

👨‍💻 Authors

Team DPR – Batch 4

Department of ECE, MRECW

📜 License

This project is licensed under the MIT License – free to use, modify, and distribute.
