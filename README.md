## Predictive Obstacle Avoidance in Mobile Robots Using Distance Trend Estimation
## Overview
This project implements a predictive obstacle avoidance system on the PiCar-4WD robotic platform. Unlike traditional reactive methods, it analyzes trends in distance measurements from an ultrasonic sensor to anticipate obstacles and avoid collisions smoothly using curved turns and directional memory.

## Features
- Rolling window analysis of ultrasonic sensor data for trend detection
- Predictive slowing down and turning before obstacles become too close
- Curved turning for smoother navigation
- Directional memory to prevent repetitive turns and oscillations
- Lightweight real-time control loop compatible with Raspberry Pi 4

## Hardware Requirements
- Raspberry Pi 4 Model B
- PiCar-4WD chassis
- 4WD HAT motor driver
- Ultrasonic distance sensor
- Servo motors for sensor positioning

## Software Dependencies
- Python 3
- picar-4wd library
- numpy
- matplotlib (optional, for visualization)
- picamera2 (optional, for camera access)

Install dependencies with:
pip install picar-4wd numpy matplotlib
sudo apt install -y python3-picamera2

## File Structure
- obstacle_avoidance_v4.py — Main control script

## Usage
1. Connect all hardware components as per setup instructions.
2. Install required software dependencies.
3. Run the main script: python3 obstacle_avoidance_v4.py
4. The robot will start sensing obstacles and navigating accordingly.

## Troubleshooting
- Verify all hardware connections, especially sensor wiring.
- Confirm all dependencies are installed (use pip freeze).
- Ensure 4WD HAT is correctly seated on Raspberry Pi.
- Monitor console output for error messages.

## Project Links
- Demo video: https://drive.google.com/drive/folders/1OlYnkVLHJsQCYfffj7z3sVwW8uTbGoqI?usp=share_link

## Contact
For questions or support, contact: Ammad Haq (r.m.a.u.haq@umail.leidenuniv.nl)

