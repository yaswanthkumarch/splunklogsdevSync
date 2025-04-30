import random
import json
import csv
import os
from datetime import datetime
#updated code
# Define log types with filename and format
log_types = [
    {"type": "application_log", "filename": "application_log.log"},
    {"type": "authentication_log", "filename": "authentication_log.json"},
    {"type": "api_access_log", "filename": "api_access_log.csv"},
    {"type": "system_error_log", "filename": "system_error_log.txt"},
    {"type": "audit_log", "filename": "audit_log.log"},
    {"type": "database_query_log", "filename": "database_query_log.json"},
    {"type": "security_log", "filename": "security_log.csv"},
    {"type": "web_server_log", "filename": "web_server_log.txt"},
    {"type": "jenkins_build_log", "filename": "jenkins_build_log.log"},
    {"type": "splunk_forwarder_log", "filename": "splunk_forwarder_log.json"},
    {"type": "iot_device_log", "filename": "iot_device_log.csv"},
    {"type": "network_traffic_log", "filename": "network_traffic_log.txt"},
    {"type": "email_server_log", "filename": "email_server_log.log"},
    {"type": "payment_gateway_log", "filename": "payment_gateway_log.json"},
    {"type": "container_kubernetes_log", "filename": "container_kubernetes_log.csv"}
]

# Sample messages for each log type
sample_messages = {
    "application_log": ["App started", "User clicked button", "App crashed"],
    "authentication_log": ["Login successful", "Login failed", "Password reset"],
    "api_access_log": ["GET /api/v1/data", "POST /api/v1/user", "DELETE /api/v1/order"],
    "system_error_log": ["Disk Full", "Memory Leak", "CPU Overload"],
    "audit_log": ["User changed settings", "Admin updated policy", "New role assigned"],
    "database_query_log": ["SELECT * FROM users", "INSERT INTO orders", "UPDATE products SET price"],
    "security_log": ["Firewall breached", "Suspicious login detected", "Antivirus scan started"],
    "web_server_log": ["200 OK /index.html", "404 Not Found /favicon.ico", "500 Server Error /api/data"],
    "jenkins_build_log": ["Build started", "Build success", "Build failed"],
    "splunk_forwarder_log": ["Forwarding event", "Connection lost", "Connection established"],
    "iot_device_log": ["Temperature sensor active", "Humidity level critical", "Motion detected"],
    "network_traffic_log": ["Packet received from 192.168.1.1", "Port scan detected", "Connection timeout"],
    "email_server_log": ["Email sent to user@example.com", "Failed to deliver email", "Inbox synced"],
    "payment_gateway_log": ["Payment successful", "Payment failed", "Refund initiated"],
    "container_kubernetes_log": ["Pod created", "Pod crashed", "Service scaled"]
}

# Function to generate random log entry
def generate_log_entry(log_type):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = random.choice(sample_messages[log_type])
    return {
        "timestamp": timestamp,
        "message": message
    }

# Check if the directory exists, if not, create it
log_directory = "C:\\logs_output"
os.makedirs(log_directory, exist_ok=True)

# Function to write log entries to a file based on type
def write_log_to_file(file_path, log_type, file_extension, mode='w'):
    if file_extension == "csv":
        with open(file_path, mode=mode, newline='') as file:
            writer = csv.writer(file)
            if mode == 'w':  # Write header only for new file
                writer.writerow(["timestamp", "message"])
            for _ in range(150):
                entry = generate_log_entry(log_type)
                writer.writerow([entry["timestamp"], entry["message"]])
    
    elif file_extension == "json":
        with open(file_path, mode=mode, newline='') as file:
            entries = []
            for _ in range(150):
                entries.append(generate_log_entry(log_type))
            json.dump(entries, file, indent=4)

    else:  # For .txt and .log files
        with open(file_path, mode=mode, newline='') as file:
            for _ in range(5000):
                entry = generate_log_entry(log_type)
                file.write(f"[{entry['timestamp']}] {entry['message']}\n")

# Create logs
def generate_logs():
    for log in log_types:
        log_type = log["type"]
        filename = os.path.join(log_directory, log['filename'])
        file_extension = filename.split(".")[-1]

        # Check if file exists to append data, otherwise create a new file
        mode = 'a' if os.path.exists(filename) else 'w'

        write_log_to_file(filename, log_type, file_extension, mode)
        print(f" Generated/Updated {filename}")

if __name__ == "__main__":
    try:
        generate_logs()
        print("\n All diversified log files generated successfully!")
    except Exception as e:
        print(f" Error generating logs: {str(e)}")
