Network Speed Tester 🚀

A simple Python CLI tool that measures your internet connection speed including Ping, Download Speed, and Upload Speed using global speed test servers.

This project uses the Python implementation of Speedtest CLI to test network performance.

Features

Measure Ping (Latency)

Test Download Speed

Test Upload Speed

Clean CLI output

Easy to run and lightweight

Project Structure
network-speed-tester
│
├── speed_test.py
├── requirements.txt
├── README.md
└── .gitignore
Requirements

Python 3.8+

Internet connection

Python Dependencies

speedtest-cli

requests

rich

Installation

Clone the repository:

git clone https://github.com/vinaybenni/project.git

Go to the project directory:

cd network-speed-tester

Install dependencies:

pip install -r requirements.txt
Run the Project
python speed_test.py

Example Output:

Starting Network Speed Test...

Ping: 18 ms
Download Speed: 94.23 Mbps
Upload Speed: 42.81 Mbps
How It Works

The program connects to the nearest speed test server.

It measures latency (Ping).

It downloads test data to calculate download speed.

It uploads test data to calculate upload speed.

Dependencies
Library	Purpose
speedtest-cli	Network speed testing
requests	HTTP requests
rich	Better CLI output formatting