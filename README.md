# Serial to CSV Logger

Simple Python utility that logs serial port data to CSV files. Designed for capturing sensor data with timestamps and accelerometer readings.

## Features
- Direct serial port data logging to CSV
- Configurable CSV headers via `header.txt`
- Automatic file naming with format: `label.timestamp.csv`
- Real-time data display while logging

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Edit `header.txt` to define your CSV header. Default header:
```
time,x_accel,y_accel,z_accel
```

## Usage

Run the script with the following arguments:
```bash
python serial_to_csv.py --port COM1 --baud 9600 --output ./data --label single-tap
```

Arguments:
- `--port`: Serial port (e.g., COM1, /dev/ttyUSB0)
- `--baud`: Baud rate of the serial connection
- `--output`: Output directory for CSV files
- `--label`: Label for the output file (e.g., single-tap, double-tap)

The script will create files like: `single-tap.20240319_123456.csv`

Press Ctrl+C to stop logging. 