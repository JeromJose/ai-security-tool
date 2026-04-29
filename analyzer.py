def analyze_ports(open_ports):
    suspicious = []

    # Basic anomaly rule
    for port in open_ports:
        if port in [21, 23, 445]:  # risky ports
            suspicious.append(port)

    if len(open_ports) > 10:
        return "High Risk: Too many open ports"
    
    if suspicious:
        return f"Suspicious ports detected: {suspicious}"
    
    return "No major threats detected"