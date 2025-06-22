# ULS Sensor Fault Simulation System

This repository contains the source code, hardware design files, and documentation for the ULS Sensor Fault Simulation System, developed as part of the Microcontroller Systems course at Tecnológico de Monterrey and presented to Valeo.

## Overview

The purpose of this system is to simulate different fault conditions in ultrasonic sensors typically used in automotive parking assist systems. Using an ATmega328P microcontroller and a set of relays and transistors, this system allows simulation of the following four states:

- Short to Battery
- Short to Ground
- Open Circuit
- Connected (Functional Sensor)

This enables engineers to safely test and validate ECU behavior without modifying real components or setups.

## Features

- Real-time fault simulation for up to 12 sensors
- Serial (UART) communication with a PC
- Graphical user interface for intuitive control
- Custom PCB design (not implemented in current prototype)
- Modular breadboard-based hardware setup
- Terminal and GUI-based control

## Repository Structure

```
Valeo-ULS-Simulation/
├── firmware/                # Embedded C code for ATmega328P
├── interface/               # Python GUI and FastAPI server
├── pcb-design/              # PCB layout files
├── docs/
│   ├── TecDeMonterreyValeo.pdf         # Final project presentation
│   ├── ValeoDocumentaciónF.pdf         # Technical documentation
├── README.md
```

## Microcontroller Logic

The system receives 2-character commands through UART. Each command follows this format:

`<number><code>`

Where:
- `<number>` is the sensor number (1–4 in current prototype)
- `<code>` is one of the following:
  - `V` = Short to battery
  - `G` = Short to ground
  - `C` = Open circuit
  - `S` = Connected (normal operation)

Example commands:
- `1V` → Sensor 1: short to battery  
- `2G` → Sensor 2: short to ground  
- `3C` → Sensor 3: open circuit  
- `4S` → Sensor 4: connected  

Invalid commands are ignored with a warning.

## GUI Control

The interface, built in Python using FastAPI, allows users to simulate sensor conditions by clicking buttons. It sends commands to the microcontroller over the serial port.

To run the interface:

```bash
cd interface
python app.py
```

Make sure the correct serial port is configured in `app.py`.

## Hardware Overview

The breadboard prototype uses the following components:

- ATmega328P microcontroller
- 3 relays per sensor (THD-1201L)
- 2N2222 transistors (for switching)
- 1kΩ resistors (base current limiting)
- 1N4148 diodes (flyback protection)
- 12V and 5V power supplies

Relays were selected over multiplexers to ensure better current conduction and realistic ECU response.

Although a PCB was designed and sent for manufacturing, the current working prototype is implemented on a breadboard.

## Authors

- Arturo Urías  
- Ale Montelongo  
- Gabriel Lascurain
- Ana Carolina Coronel
- Yumee Chung
- Victoria Lilian Robles Vargas
- Josemaría De Alba Arguelles

Supervised by:  
Professor Agustín Domínguez

## Acknowledgments

Special thanks to Valeo and Tecnológico de Monterrey for the opportunity to work on a real-world engineering problem involving embedded systems and automotive testing.

## License

This project is intended for academic and educational purposes. For reuse or adaptation, please credit the original authors and supervising professor.
