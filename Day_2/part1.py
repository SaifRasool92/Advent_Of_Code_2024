
def is_report_safe(report):
    """
    Determine if a report is safe based on two criteria:
    1. Levels are either all increasing or all decreasing
    2. Adjacent levels differ by at least 1 and at most 3
    """
    levels = list(map(int, report.split()))
    if not levels:
        return False
    is_increasing = all(levels[i+1] > levels[i] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i+1] for i in range(len(levels) - 1))
    if not (is_increasing or is_decreasing):
        return False
    for i in range(len(levels) - 1):
        diff = abs(levels[i+1] - levels[i])
        if diff < 1 or diff > 3:
            return False
    return True

def analyze_safety_reports(input_data):
    """
    Analyze the safety of all reports in the input data
    """
    reports = input_data.strip().split('\n')

    safe_reports = sum(1 for report in reports if is_report_safe(report))

    return safe_reports
try:
    with open('/content/Input.txt', 'r') as file:
        input_data = file.read()
    safe_report_count = analyze_safety_reports(input_data)
    print(f"Number of safe reports: {safe_report_count}")
except FileNotFoundError:
    print("Error: The file '/content/Input.txt' was not found.")