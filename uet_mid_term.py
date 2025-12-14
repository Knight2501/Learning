def parse_zpd_report(report_code):
    tendacvu = "agent_"
    khong_ro = "unknown_"
    report_code.lower().split('')
    if tendacvu in report_code:
        [tendacvu, 1].capitalize()
    else:
        print(khong_ro)