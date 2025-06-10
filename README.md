# robot_challenge - autonomous driving with Zumi

This project is part of a FHNW module assignment where our Zumi robot performs autonomous line following, obstacle interaction, QR code and face detection, and custom maneuvers based on sensor input.

## Overview
Zumi is programmed to:
- Follow a black line using IR sensors
- React to obstacles and detect QR codes or faces
- Execute maneuvers like turning, dancing, and navigating circles
- Log all events with timestamps
- Save all activities in a `.csv` file

The logic is implemented in `src/main_jupyter.ipynb`.

## Features
- **Line Following**: IR-based correction to stay on a black line
- **Obstacle Detection**: Stops and waits until the object is removed
- **QR Code & Face Recognition**: Uses Zumi's camera to detect commands or faces
- **Custom Commands**: Executes actions based on QR codes (e.g., "Left Circle", "Zumi is happy today!")
- **360° Dance + Emotion**: Turns with personality animations
- **Navigation Logic**: Handles forks and end-of-line cases
- **Data Logging**: All events are logged with timestamps and saved to a CSV file

## 📁 Project Structure
Zumi-Project/
├── src/
│   └── main.jupyter.ipynb      # Main notebook containing all logic
├── submissions/                # Output CSV logs and final results
├── old experiments/            # Archived earlier versions and prototypes
└── README.md                   # Project overview and instructions

## Requirements
- Zumi robot with camera and IR sensors
- Python packages:
  - `zumi` *(included in Zumi's development environment)*
  - `opencv-python`
  - `pandas`
- Jupyter Notebook

## Running the code
1. Connect Zumi to your computer via Wi-Fi or USB
2. Open src/main.jupyter.ipynb in Jupyter
3. Run all cells step-by-step (top-down)
4. Zumi will begin following the line and reacting to its environment

## Team (in alphabetical order)
Lea Schönauer
Markus Barten (until 27 May 25)
Mykhailo Andrusiak
Simone Wullschleger

## Acknowledgments
Subject matter experts: Susanne Suter and Yves Bächtiger

Robolink Zumi Documentation
https://docs.robolink.com/docs/Zumi/Python/Function-Documentation
Robolink lessons on:
http://zumidashboard.ai/