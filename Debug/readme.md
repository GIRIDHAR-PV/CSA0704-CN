 # IoT Network Troubleshooting & Fault Rectification Lab

## Repository Overview
This repository contains the systematic troubleshooting, fault resolution, and verification for 4 Cisco Packet Tracer IoT scenarios.

### Repository Structure
* **`scenarios/`**: Contains the 4 debugged Cisco Packet Tracer (`.pkt`) files.
---

## Scenario Analysis & Solutions

### Scenario 1: Control Devices with Home Gateway
* **Description:** Home automation setup connecting smart devices (Light, Garage Door, Lawn Sprinkler, Door) to a Home Gateway.
* **Fault Identified:** Door (`IoT9`) missing configuration/connectivity fix.
* **Fix Applied:** Configured network interface and wireless connection to Home Gateway (`DLC100`).
* **Verification:** Successful ICMP ping replies and populated ARP table for IP range `192.168.25.x`.

![Scenario 1 Verification]()
---

### Scenario 2: Smart House with Switch, AP, and Server
* **Description:** Smart home network utilizing a Central Switch, Access Point, and Registration Server (`192.168.1.1`).
* **Fault Identified:** Unregistered smart end-nodes (Webcams, Fan, Door, Window) unable to communicate through the Access Point.
* **Fix Applied:** Configured IP addressing (`192.168.1.11`), gateway routes, and wireless parameters across access point clients.
* **Verification:** Full connectivity verified via ping tests from `PC0` (`192.168.1.11`) to all connected IoT nodes (`192.168.1.12`, `13`, `14`, `16`).

![Scenario 2 Verification]()
---

### Scenario 3: Fire Extinguisher & Safety System
* **Description:** Safety network involving Smoke Detectors, Sirens, Fire Sprinklers, and an Old Car node.
* **Fault Identified:** The Old Car (`IoT6`) lacked a Wireless Module, preventing it from associating with the wireless Home Gateway.
* **Fix Applied:** Installed/Switched the interface module to a compatible wireless module (`PT-IOT-NM-1W`) and configured network settings.
* **Verification:** Successful ping execution and full ARP resolution across all IoT safety nodes (`192.168.25.100` – `107`).

![Scenario 3 Verification]()

---

### Scenario 4: Smart Parking & Access Control
* **Description:** RFID-based access control system featuring Motion Detectors, Garage Door, RFID Reader, and RFID Cards.
* **Fault Identified:** RFID Card (`IoT2`) failed to communicate with the Home Gateway due to a missing/mismatched wireless module.
* **Fix Applied:** Installed the correct wireless module (`PT-IOT-NM-1W`) on the RFID Card and re-established association with `DLC100`.
* **Verification:** Ping test from `Laptop0` (`192.168.25.102`) to RFID Card (`192.168.25.100`) returned 0% packet loss with active dynamic ARP entry.

![Scenario 4 Verification]()

---

## Verification Summary
All 4 scenarios have been tested in **Realtime** and **Simulation** modes:
1. **0% Packet Loss:** All ping tests across hosts and IoT end-devices returned `Lost = 0 (0% loss)`.
2. **ARP Table Resolution:** Confirmed via `arp -a` in Command Prompt to ensure MAC-to-IP binding across gateways and switches.
