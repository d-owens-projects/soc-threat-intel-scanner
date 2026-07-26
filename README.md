Threat Intelligence IOC Scanner:
A lightweight Python-based security automation tool that ingests threat intelligence indicators (IPs, domains, hashes), scans local system logs, and generates alerts when matches are found. This project demonstrates real SOC automation, threat intel ingestion, and log analysis skills.

## OVERVIEW ##

Security analysts frequently need to check whether internal logs contain known malicious indicators. This tool automates that workflow by:

1. Loading threat intelligence feeds
2. Parsing local system logs
3. Searching for IOC matches
4. Producing a clean JSON alert report
It’s simple, fast, and easy to extend with additional feeds or log sources.

## FEATURES ##

1. IOC feed ingestion (IPs, domains, hashes)
2. Log scanning and pattern matching
3. JSON alert report generation
4. Easy-to-read Python architecture
5. Fully customizable feed and log sources

## PROJECT STRUCTURE ##

threat-intel-scanner/
│
├── src/
│   └── ioc_scanner.py
│
├── logs/
│   └── system.log
│
├── feeds/
│   └── iocs.txt
│
└── output/
    └── ioc_report.json


## HOW IT WORKS ##

1. Load IOC Feed: Reads feeds/iocs.txt and extracts all indicators.

2. Load Logs: Reads logs/system.log line-by-line.

3. Scan for Matches: If any IOC appears in a log line, an alert is created.

4. Generate Report: All alerts are saved to output/ioc_report.json.

## RUNNING THE TOOL ##
From the src directory: python ioc_scanner.py

Expected Output: IOC scan complete. Report saved.

Results appear: output/ioc_report.json

## EXAMPLE OUTPUT ##

[
    {
        "ioc": "185.244.25.3",
        "log_line": "2024-07-26 Connection to 185.244.25.3 allowed",
        "alert": "IOC match found in log"
    }
]

## SkILLS DEMONSTRATED ##

Threat intelligence ingestion
IOC parsing
Log analysis
Python automation
JSON reporting
GitHub project structuring
