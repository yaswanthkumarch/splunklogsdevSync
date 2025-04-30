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
    "application_log": [
        "App started", "User clicked button", "App crashed", "Cache cleared",
        "New session initialized", "Application shutdown", "User logged out",
        "Module loaded", "Theme changed to dark", "Unexpected exception occurred",
        "Notification sent", "Settings saved", "App version updated",
        "App backgrounded", "Loading spinner activated"
    ],
    "authentication_log": [
        "Login successful", "Login failed", "Password reset", "2FA verification sent",
        "Account locked after 3 failed attempts", "Session expired", "New device registered",
        "User signed out", "Token refreshed", "Security question answered",
        "User registered", "Account verification email sent", "SSO login triggered"
    ],
    "api_access_log": [
        "GET /api/v1/data", "POST /api/v1/user", "DELETE /api/v1/order",
        "PUT /api/v1/profile", "PATCH /api/v1/settings", "GET /api/v1/status 503 Service Unavailable",
        "GET /api/v2/metrics", "POST /api/v1/login", "OPTIONS /api/v1/ping",
        "HEAD /api/v1/health", "GET /api/v1/export", "POST /api/v1/refresh-token"
    ],
    "system_error_log": [
        "Disk Full", "Memory Leak", "CPU Overload", "Kernel panic detected",
        "System reboot initiated", "Service not responding", "Resource threshold exceeded",
        "Page fault occurred", "Process terminated unexpectedly", "Core dump generated",
        "High load average", "Service restarted", "Swap memory full"
    ],
    "audit_log": [
        "User changed settings", "Admin updated policy", "New role assigned",
        "Group permission updated", "Audit trail generated", "User deactivated by admin",
        "Data export requested", "Access granted to restricted area", "Backup policy modified",
        "Configuration file changed", "Permission denied to guest user", "System settings updated"
    ],
    "database_query_log": [
        "SELECT * FROM users", "INSERT INTO orders", "UPDATE products SET price",
        "DELETE FROM sessions WHERE expired=1", "ALTER TABLE customers ADD COLUMN phone",
        "DROP TABLE temp_data", "JOIN customers ON orders.customer_id = customers.id",
        "CREATE INDEX ON transactions", "BEGIN TRANSACTION", "ROLLBACK TRANSACTION",
        "SELECT COUNT(*) FROM logs", "ANALYZE TABLE orders", "TRUNCATE TABLE archive_data"
    ],
    "security_log": [
        "Firewall breached", "Suspicious login detected", "Antivirus scan started",
        "Unauthorized access attempt blocked", "Security patch applied", "Encryption module initialized",
        "IP blacklisted", "Intrusion detection alert triggered", "Malware signature updated",
        "User elevated to admin", "Security policy violated", "Root access attempt"
    ],
    "web_server_log": [
        "200 OK /index.html", "404 Not Found /favicon.ico", "500 Server Error /api/data",
        "302 Redirect /login", "403 Forbidden /admin", "503 Service Unavailable /checkout",
        "301 Moved Permanently /docs", "202 Accepted /upload", "401 Unauthorized /api/private",
        "418 I'm a teapot /brew", "200 OK /home", "400 Bad Request /submit"
    ],
    "jenkins_build_log": [
        "Build started", "Build success", "Build failed", "Tests passed: 128",
        "Tests failed: 3", "Artifact uploaded to S3", "Checkout from Git successful",
        "Build queued", "Dependency install failed", "Test suite executed",
        "Code coverage report generated", "Build cancelled", "Docker image pushed"
    ],
    "splunk_forwarder_log": [
        "Forwarding event", "Connection lost", "Connection established",
        "Data queued for transmission", "TCP output group unreachable", "Forwarder restarted",
        "Forwarder started", "SSL handshake completed", "Heartbeat sent to indexer",
        "Queue full: data dropped", "Indexer acknowledgement timeout", "New data input detected"
    ],
    "iot_device_log": [
        "Temperature sensor active", "Humidity level critical", "Motion detected",
        "Device firmware updated", "Sensor disconnected", "Battery level low",
        "Light sensor triggered", "GPS coordinates updated", "Device restarted remotely",
        "Bluetooth connection established", "Data transmission delayed"
    ],
    "network_traffic_log": [
        "Packet received from 192.168.1.1", "Port scan detected", "Connection timeout",
        "VPN tunnel established", "DNS lookup failed", "ARP request from unknown MAC",
        "ICMP ping sent", "HTTP packet dropped", "New DHCP lease issued",
        "Bandwidth threshold exceeded", "Inbound traffic blocked", "Router rebooted"
    ],
    "email_server_log": [
        "Email sent to user@example.com", "Failed to deliver email", "Inbox synced",
        "SMTP connection established", "User mailbox full", "Spam filter triggered",
        "IMAP session started", "Draft saved", "Recipient address invalid",
        "TLS handshake completed", "Auto-response sent", "Attachment size too large"
    ],
    "payment_gateway_log": [
        "Payment successful", "Payment failed", "Refund initiated",
        "Chargeback requested", "Transaction pending verification",
        "3D Secure authentication required", "Currency conversion applied",
        "Payment method added", "Recurring payment setup", "Payment gateway timeout",
        "Transaction ID generated", "Fraud detection triggered"
    ],
    "container_kubernetes_log": [
        "Pod created", "Pod crashed", "Service scaled", "Deployment rollout started",
        "Container image pulled", "Node drain initiated", "Namespace deleted",
        "Resource quota exceeded", "Pod evicted", "Kubelet restart detected",
        "ConfigMap updated", "Cluster autoscaler triggered"
    ]
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
            for _ in range(150):
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
