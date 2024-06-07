import paho.mqtt.client as mqtt
import json

# MQTT settings
MQTT_BROKER = "10.100.111.54"
MQTT_PORT = 1883

# Function to publish MQTT message for a specific device
def publish_mqtt_message(device_id, x, y, angle, timestamp):
    topic = f"/iot/json/{device_id}/attrs"
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    message = json.dumps({
        "x": x,
        "y": y,
        "angle": angle,
        "timestamp": timestamp
    })
    client.publish(topic, message)
    client.disconnect()

# Function to publish data for multiple robot_ids. Update this for Robot State Tracker
def main():
    device_data = [
        {"device_id": "robot001", "x": 2.0, "y": 4.5, "angle": 1.25, "timestamp": "2024-06-01T10:15:00Z"},
        {"device_id": "robot002", "x": 3.0, "y": 5.5, "angle": 1.50, "timestamp": "2024-06-01T10:20:00Z"},
        {"device_id": "robot003", "x": 4.0, "y": 6.5, "angle": 1.75, "timestamp": "2024-06-01T10:25:00Z"}
    ]

    for data in device_data:
        publish_mqtt_message(data["device_id"], data["x"], data["y"], data["angle"], data["timestamp"])

if __name__ == "__main__":
    main()

