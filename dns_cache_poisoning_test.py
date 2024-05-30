import asyncio
import subprocess
import time
import sys
import socket
from termcolor import colored

async def run_dig_command(target_domain, test_domain):
    # Use Cloudflare DNS to resolve the target domain
    command = f"dig @1.1.1.1 {target_domain}"
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    output = stdout.decode()

    # Extract IP addresses from the output
    target_ips = []
    for line in output.splitlines():
        if line.startswith(target_domain):
            parts = line.split()
            if len(parts) >= 5 and parts[3] == 'A':
                target_ips.append(parts[4])
    
    if not target_ips:
        print(colored("Failed to resolve IP addresses for the target domain.", "red"))
        return
    
    for target_ip in target_ips:
        print(colored(f"Resolved IP for {target_domain}: {target_ip}", "green"))

        # Perform the DNS query using dig with the resolved IP
        command = f"dig @{target_ip} {test_domain}"
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        # Print the results with colored text
        print(colored(f"Command executed: {command}", "cyan"))
        print(colored(f"stdout:\n{stdout.decode()}", "blue"))
        if stderr:
            print(colored(f"stderr:\n{stderr.decode()}", "red"))

        # Check if the response is valid
        if "NOERROR" in stdout.decode() and test_domain in stdout.decode():
            print(colored("DNS server is allowing recursive queries for third-party domains.", "green"))
        else:
            print(colored("DNS server is not allowing recursive queries for third-party domains.", "red"))

def main():
    if len(sys.argv) < 2:
        print(colored("Usage: python poc_scripting.py <target_domain> [test_domain]", "yellow"))
        sys.exit(1)
    
    target_domain = sys.argv[1]
    test_domain = sys.argv[2] if len(sys.argv) > 2 else "echopointsolutions.org"
    
    print(colored(f"Target domain: {target_domain}", "green"))
    print(colored(f"Test domain: {test_domain}", "green"))

    asyncio.run(run_dig_command(target_domain, test_domain))

if __name__ == "__main__":
    main()
