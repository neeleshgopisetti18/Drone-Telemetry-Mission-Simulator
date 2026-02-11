# Autonomous Drone Telemetry Mission Simulator

# Overview
This project here simulates real-time drone telemetry for 30 seconds using mission-based logic instead of random values.

The simulation includes:

- Altitude
- Speed
- Battery Percentage
- GPS Coordinates
- Mission Phases
- Safety Warnings

## Mission Phases

1. Takeoff (0–5s)
2. Cruising (6–15s)
3. Surveillance (16–25s)
4. Landing (26–30s)

Battery drain is calculated dynamically based on speed.

##  Technologies Used
- Python 3
- Time module
- Random module

##  How to Run

```bash
cd src
python drone_simulator.py
