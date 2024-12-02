import json

with open('input_2.txt') as f:
    content = f.read().strip()
    lines = content.splitlines()

data = []
for line in lines:
    inital_list = line.strip().split()
    data.append(inital_list)

def is_safe_report(report):
    """Check if a report is safe based on the given rules."""
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return all(1 <= abs(diff) <= 3 for diff in differences)
    return False

def count_safe_reports(data):
    """Count how many reports are safe in the given data."""
    safe_count = 0
    for report in data:
        if is_safe_report(report):
            safe_count += 1
    return safe_count


def is_safe_with_dampener(report):
    """Check if a report is safe with the Problem Dampener."""
    if is_safe_report(report):
        return True  # Already safe
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False

def count_safe_reports_with_dampener(data):
    """Count how many reports are safe with the Problem Dampener."""
    safe_count = 0
    for report in data:
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count


data = [list(map(int, report)) for report in data]

safe_reports = count_safe_reports(data)
print(f"Number of safe reports: {safe_reports}")

safe_with_dampener = count_safe_reports_with_dampener(data)
print(f"Number of dampaned safe reports: {safe_with_dampener}")