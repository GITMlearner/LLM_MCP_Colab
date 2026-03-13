from fastmcp import FastMCP
import paho.mqtt.client as mqtt
import time
import sys

# Initialize the MCP Server (NO PRINT STATEMENTS ALLOWED HERE)
mcp = FastMCP("AgriBot_Cloud")

BROKER = "broker.emqx.io"
PORT = 1883

@mcp.tool()
def publish_to_cloud(topic: str, message: str) -> str:
    """Publishes a message to an MQTT topic on the internet."""
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    try:
        # Use a short timeout for the connection
        client.connect(BROKER, PORT, keepalive=10)
        result = client.publish(topic, str(message))
        
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            return f"Published to {topic}"
        return f"Error code: {result.rc}"
    except Exception as e:
        return f"Connection Failed: {str(e)}"
    finally:
        client.disconnect()

if __name__ == "__main__":
    # We must run the server silently for stdio transport
    mcp.run()