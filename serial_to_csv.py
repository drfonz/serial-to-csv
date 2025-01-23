import serial
import argparse
import os
import sys
from datetime import datetime

def read_header():
    """Read header from header.txt file."""
    try:
        with open('header.txt', 'r') as f:
            return f.readline().strip()
    except FileNotFoundError:
        print("Warning: header.txt not found. Using empty header.")
        return ""

def create_unique_filename(label: str, output_folder: str) -> str:
    """Create a unique filename with the specified format."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{label}.{timestamp}.csv"
    return os.path.join(output_folder, filename)

def main():
    parser = argparse.ArgumentParser(description='Log serial port data to CSV file.')
    parser.add_argument('--port', required=True, help='Serial port (e.g., COM1)')
    parser.add_argument('--baud', type=int, required=True, help='Baud rate')
    parser.add_argument('--output', required=True, help='Output folder path')
    parser.add_argument('--label', required=True, help='Filename label')
    
    args = parser.parse_args()
    
    # Ensure output directory exists
    os.makedirs(args.output, exist_ok=True)
    
    # Read header
    header = read_header()
    
    # Create output file
    output_file = create_unique_filename(args.label, args.output)
    print(f"Logging to: {output_file}")
    
    try:
        with serial.Serial(args.port, args.baud, timeout=1) as ser, \
             open(output_file, 'w') as f:
            # Write header if it exists
            if header:
                f.write(f"{header}\n")
                f.flush()
            
            print("Listening to serial port. Press Ctrl+C to stop.")
            while True:
                if ser.in_waiting:
                    try:
                        line = ser.readline().decode('utf-8').strip()
                        if line:
                            f.write(f"{line}\n")
                            f.flush()  # Ensure data is written immediately
                            print(line)
                    except UnicodeDecodeError:
                        print("Warning: Received non-UTF8 data")
                        continue
                    
    except serial.SerialException as e:
        print(f"Error: Could not open port {args.port}: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nLogging stopped by user")
        sys.exit(0)

if __name__ == '__main__':
    main() 