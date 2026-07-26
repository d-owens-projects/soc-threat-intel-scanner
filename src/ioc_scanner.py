import re
import json

def load_iocs():
    with open("../feeds/iocs.txt", "r") as f:
        lines = f.readlines()
    iocs = [line.strip() for line in lines if line.strip()]
    return iocs

def load_logs():
    with open("../logs/system.log", "r") as f:
        logs = f.readlines()
    return logs

def scan_logs_for_iocs(logs, iocs):
    alerts = []
    for line in logs:
        for ioc in iocs:
            if ioc in line:
                alerts.append({
                    "ioc": ioc,
                    "log_line": line.strip(),
                    "alert": "IOC match found in log"
                })
    return alerts

def save_report(alerts):
    with open("../output/ioc_report.json", "w") as f:
        json.dump(alerts, f, indent=4)

def main():
    iocs = load_iocs()
    logs = load_logs()
    alerts = scan_logs_for_iocs(logs, iocs)
    save_report(alerts)
    print("IOC scan complete. Report saved.")

if __name__ == "__main__":
    main()
