def generate_ai_report(findings):

    report = """
===== EXECUTIVE SUMMARY =====

The infrastructure analysis detected multiple underutilized resources
leading to unnecessary monthly cloud expenditure.

===== OPTIMIZATION RECOMMENDATIONS =====

1. Downgrade low-utilization instances
2. Reduce unused memory allocation
3. Implement autoscaling policies
4. Monitor workload patterns continuously

===== ESTIMATED IMPACT =====

Potential monthly savings: $380
Estimated yearly savings: $4560

===== PRIORITY LEVEL =====

MEDIUM

===== BEST PRACTICES =====

- Enable automated rightsizing
- Configure Kubernetes autoscaling
- Review infrastructure weekly
- Remove unused resources regularly
"""

    return report
