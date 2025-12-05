def is_report_safe_burte_force(report, remove_one_bad_level):
    isIncreasing = False
    if report[0] < report[1]:
        isIncreasing = True 
    
    for i in range(1,len(report)):
        if (report[i-1] > report[i] and isIncreasing) or (report[i-1] < report[i] and not isIncreasing) or (abs(report[i-1] - report[i]) > 3 or abs(report[i-1] - report[i]) < 1):
            
            if remove_one_bad_level:
                for j in range(0, len(report)):
                    r1 = report.copy()
                    r1.pop(j)
                    if is_report_safe(r1, False):
                        return True
            
            return False

    
    return True


def is_report_safe(report, remove_one_bad_level):
    isIncreasing = False
    if report[0] < report[1]:
        isIncreasing = True 
    
    for i in range(1,len(report)):
        if (report[i-1] > report[i] and isIncreasing) or (report[i-1] < report[i] and not isIncreasing) or (abs(report[i-1] - report[i]) > 3 or abs(report[i-1] - report[i]) < 1):
            
            if remove_one_bad_level:
                r1 = report.copy()
                r2 = report.copy()
                r3 = report.copy()
                r2.pop(i)
                r1.pop(i-1)
                r3.pop(0)
                return (is_report_safe(r1, False) or is_report_safe(r2, False)) or is_report_safe(r3, False)
            
            return False

    
    return True


def read_and_test_reports(filename):
    safe_reports = 0
    with open(filename, 'r') as file:
        for line in file:
            report = list(map(lambda i: int(i), line.strip().split(" ")))
            if is_report_safe(report, True):
                safe_reports += 1


    print(safe_reports)


read_and_test_reports("Day2/input.txt")
