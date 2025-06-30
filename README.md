# Time-Series-Analysis

# 🌿 CO₂ Capture Plant: Real-Time Monitoring, Forecasting & Optimization

This project simulates, monitors, forecasts, and optimizes the operations of a CO₂ capture plant using Python, InfluxDB, Grafana, and machine learning.

---

## 📦 Project Features

- 🔄 Real-time simulation of plant data (air intake, absorption, desorption, tank output)
- 📈 Visualization with Grafana dashboards
- 🧠 Forecasting CO₂ levels using Prophet
- 🤖 Optimization of process parameters to maximize CO₂ output
- 📤 Data export from InfluxDB to CSV for analysis
- 🧩 Modbus-ready integration for real-world sensor data


---

## 🖼️ Dashboard Preview

This real-time Grafana dashboard visualizes sensor data across all plant units — including air intake, CO₂ absorption, desorption, and output tanks.  
It also supports alerts, gauge views, and historical trends across multiple units.

---
![Dashboard_Overview](Dashboard_Preview1.png)
![Dashboard_Overview](Dashboard_Preview2.png)
---

---

## 🖼️ Plant Setup

This schematic illustrates the complete CO₂ capture plant process:

1. Air Intake Units (x6):
Pull atmospheric air into the system using suction units. These feed high-flow, filtered air toward the absorption stage.

2. CO₂ Absorption Chamber:
The incoming air passes through a packed bed structure where CO₂ is absorbed using a chemical medium.

3. Desorption Tank (Alkaline Water):
The absorbed CO₂ is released into an alkaline water-based desorption tank, where gas separation occurs.

4. Output Storage Units (H₂, CO₂, O₂):
Separated gases are directed into dedicated storage tanks for Hydrogen, Carbon Dioxide, and Oxygen, monitored for level and purity.


<p align="center">
  <img src="CO2_Plant_Setup.jpg" alt="Plant Overview Dashboard" width="100%">
</p>

---

## ⚙️ Architecture Overview

```mermaid
graph TD
  A[Python Simulator ] --> B[InfluxDB]
  B --> C[Grafana Dashboard]
  B --> D[CSV Export]
  D --> E[ML Forecasting + Optimization]




