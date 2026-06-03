import json

def analyze_resources():

    with open("data/infrastructure.json") as f:
        data = json.load(f)

    findings = []

    for server in data:

        # CPU Analysis
        if server["cpu_usage"] < 15:
            findings.append({
                "instance": server["instance_name"],
                "issue": "Underutilized CPU",
                "monthly_cost": server["monthly_cost"],
                "recommendation": "Downgrade instance size"
            })

        # Memory Analysis
        if server["memory_usage"] < 25:
            findings.append({
                "instance": server["instance_name"],
                "issue": "Low memory utilization",
                "monthly_cost": server["monthly_cost"],
                "recommendation": "Reduce allocated memory"
            })

    return findings
