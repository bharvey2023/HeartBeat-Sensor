# Heartbeat Sensor Data Collector

## Overview
This project uses an **Arduino-based heartbeat sensor** to measure beats per minute (BPM). The data is collected in real-time, processed in Python, and visualized on a graph. It also allows users to add their measurements to a database, demonstrating **hardware-software integration** with practical data analysis and database managment.

## Features
- Real-time BPM measurement with an Arduino and heartbeat sensor  
- Data cleaning and filtering in Python to remove noise  
- Statistical analysis: average and median BPM  
- Graphical visualization of heart rate trends over time  
- Optional save/try-again workflow for user interaction (Feature will be added later)

## Tools & Technologies
- **Programming Languages:** Arduino C, Python, SQL
- **Libraries:** matplotlib, pyserial, time  
- **Development Environments:** Arduino IDE, PyCharm IDE  
- **Hardware:** ELEGOO UNO R3 board with heartbeat sensor  

## How it Works
1. Arduino reads analog signal from the heartbeat sensor.  
2. Detects voltage spikes corresponding to heartbeats.  
3. Computes time intervals between spikes to calculate BPM.  
4. Sends data via serial to Python, which stores and analyzes it.  
5. Graphs the data and shows trends over chosen time intervals.
6. Adds data to database to track trends.

## Getting Started
1. Connect the heartbeat sensor to the Arduino (A0 for signal, plus power and ground).  
2. Upload the Arduino sketch to the board.  
3. Run the Python script to start reading and visualizing BPM data.  
4. Follow on-screen prompts to save data or take another measurement.  

## Notes
- Threshold values for spike detection may need adjusting based on your sensor and placement.  
- Maximum BPM readings are limited by sensor and environmental noise.
