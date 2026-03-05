from mcp.server.fastmcp import FastMCP
import serial

# 1. Setup the Server
mcp = FastMCP("arduino_code")

# 2. Setup Serial (Change 'COM5' to your actual port)
try:
    ser = serial.Serial('COM5', 9600, timeout=1)
except:
    ser = None

@mcp.tool()
def blink_led() -> str:
    """Blinks the built-in LED on the Arduino board."""
    if ser and ser.is_open:
        ser.write(b'B')  # Send a single 'B' for Blink
        return "Blink command sent to Arduino!"
    return "Error: Arduino not connected."

if __name__ == "__main__":
    mcp.run()