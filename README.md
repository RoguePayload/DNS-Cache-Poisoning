# DNS Cache Poisoning Test Script

## Overview

Welcome to the DNS Cache Poisoning Test Script repository! This tool is designed to identify and exploit DNS cache poisoning vulnerabilities in public DNS servers. By using this script, ethical hackers and security professionals can test their DNS infrastructure for vulnerabilities and implement necessary protections to secure their systems.

## Features

- **Automated DNS Cache Poisoning Testing:** Easily test DNS servers for cache poisoning vulnerabilities.
- **Asynchronous Operations:** Utilizes `asyncio` for efficient and resource-friendly testing.
- **Customizable Target and Test Domains:** Specify target DNS servers and test domains for flexibility.
- **Detailed Output:** Provides clear and detailed output of the test results.

## Installation

_To get started with the DNS Cache Poisoning Test Script, follow these simple steps:_

1. **Clone the Repository:**
```
   git clone https://github.com/RoguePayload/DNS-Cache-Poisoning.git
   cd DNS-Cache-Poisoning
```
2. **Install Dependencies:**
_Ensure you have Python 3.x installed, then install the required dependencies using the provided requirements.txt file:_
```
pip install -r requirements.txt
```
## Usage 
_To use the script, simply run the following command, specifying the target domain and the test domain:_
```
python3 dns_cache_poisoning_test.py <target_domain> <test_domain>
```
**Example:**
```
python3 dns_cache_poisoning_test.py target.com yourdomain.com
```

## Requirements
_All required dependencies are listed in the requirements.txt file._

## Contributing
_We welcome contributions from the community! If you have suggestions for improvements or have identified any issues, please open an issue or submit a pull request._

## Disclaimer
_This script is intended for use by ethical hackers and security professionals with proper authorization. Unauthorized use of this script against systems you do not have explicit permission to test is illegal and unethical._

***Happy Testing & Stay Secure!***

