

def is_report_safe(report):
    """
    Check if the report is safe based on the two conditions:
    1. The levels are either strictly increasing or strictly decreasing.
    2. The difference between adjacent levels is between 1 and 3.
    """
    levels = list(map(int, report.split()))
    is_increasing = all(levels[i+1] > levels[i] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i+1] for i in range(len(levels) - 1))
    if not (is_increasing or is_decreasing):
        return False

    for i in range(len(levels) - 1):
        diff = abs(levels[i+1] - levels[i])
        if diff < 1 or diff > 3:
            return False

    return True

def is_report_safe_with_dampener(report):
    """
    Check if the report can be made safe with the Problem Dampener
    (by removing at most one level).
    """
    levels = list(map(int, report.split()))
    if is_report_safe(report):
        return True
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i+1:]
        if is_report_safe(' '.join(map(str, modified_report))):
            return True
    return False

def analyze_safety_reports(input_data, with_dampener=False):
    """
    Analyze the safety of all reports in the input data.
    If with_dampener is True, consider reports that can be made safe by removing one level.
    """
    reports = input_data.strip().split('\n')
    if with_dampener:
        safe_reports = sum(1 for report in reports if is_report_safe_with_dampener(report))
    else:
        safe_reports = sum(1 for report in reports if is_report_safe(report))
    return safe_reports
try:
    with open('/content/Input.txt', 'r') as file:
        input_data = file.read()
    safe_report_count_part1 = analyze_safety_reports(input_data, with_dampener=False)
    print(f"Number of safe reports (Part 1): {safe_report_count_part1}")
    safe_report_count_part2 = analyze_safety_reports(input_data, with_dampener=True)
    print(f"Number of safe reports (Part 2): {safe_report_count_part2}")
except FileNotFoundError:
    print("Error: The file '/content/Input.txt' was not found.")