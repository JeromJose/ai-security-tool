from scanner import scan_ports
from crypto import generate_key, encrypt_data
from analyzer import analyze_ports

target = input("Enter target IP: ")

print("\n🔍 Scanning target...")
ports = scan_ports(target)

print(f"Open Ports: {ports}")

print("\n🤖 Running security analysis...")
result = analyze_ports(ports)
print(result)

print("\n🔐 Encrypting report...")
key = generate_key()
encrypted = encrypt_data(result, key)

print("Encrypted Report:", encrypted)

# Save report to file
with open("report.txt", "w") as f:
    f.write("Open Ports: " + str(ports) + "\n")
    f.write("Analysis: " + result + "\n")
    f.write("Encrypted: " + str(encrypted))

print("\n📁 Report saved as report.txt")