import requests
import json

IOT_AGENT_IP = "10.100.111.54"
CONTEXT_BROKER_IP = "10.100.111.211"

# Configuration
provision_headers = {
    "Content-Type": "application/json",
    "fiware-service": "robotService",
    "fiware-servicepath": "/"
}

get_headers = {
    "fiware-service": "robotService",
    "fiware-servicepath": "/",
    "Accept": "application/json"
}

# Function to provision service group
def provision_service_group(iot_agent_ip, context_broker_ip):
    service_group_url = f"http://{iot_agent_ip}:31001/iot/services"
    service_group_data = {
        "services": [
            {
                "apikey": "robot_api_key", # Note: Requires API KEY for provision
                "cbroker": f"http://{context_broker_ip}:1026",
                "entity_type": "RobotState",
                "resource": "/robot"
            }
        ]
    }
    response = requests.post(service_group_url, headers=provision_headers, data=json.dumps(service_group_data))
    if response.status_code == 201:
        print("Service group provisioned successfully.")
    else:
        print(f"Failed to provision service group: {response.status_code} - {response.text}")

# Function to provision device with specific device_id and entity_name
def provision_device(iot_agent_ip, device_id, entity_name):
    device_url = f"http://{iot_agent_ip}:31001/iot/devices"
    device_data = {
        "devices": [
            {
                "device_id": device_id,
                "entity_name": entity_name,
                "entity_type": "RobotState",
                "protocol": "PDI-IoTA-Json",
                "transport": "MQTT",
                "timezone": "Europe/Berlin",
                "attributes": [
                    { "object_id": "x", "name": "x", "type": "Number" },
                    { "object_id": "y", "name": "y", "type": "Number" },
                    { "object_id": "angle", "name": "angle", "type": "Number" },
                    { "object_id": "timestamp", "name": "timestamp", "type": "String" }
                ],
                "static_attributes": [
                    { "name": "refStore", "type": "Relationship", "value": "urn:ngsi-ld:Store:001" }
                ]
            }
        ]
    }
    response = requests.post(device_url, headers=provision_headers, data=json.dumps(device_data))
    if response.status_code == 201:
        print(f"Device {device_id} provisioned successfully.")
    else:
        print(f"Failed to provision device {device_id}: {response.status_code} - {response.text}")


# Main workflow to provision multiple devices and verify entities
def main(iot_agent_ip, context_broker_ip):
    provision_service_group(iot_agent_ip, context_broker_ip)
    
    devices = [
        {"device_id": "robot001", "entity_name": "urn:ngsi-ld:Robot:001"},
        {"device_id": "robot002", "entity_name": "urn:ngsi-ld:Robot:002"},
        {"device_id": "robot003", "entity_name": "urn:ngsi-ld:Robot:003"}
    ]

    for device in devices:
        provision_device(iot_agent_ip, device["device_id"], device["entity_name"])
    
if __name__ == "__main__":
    main(IOT_AGENT_IP, CONTEXT_BROKER_IP)
