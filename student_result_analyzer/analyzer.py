def compute_grade(percentage):
    try:
        p = float(percentage)
    except Exception:
        return 'N/A'
    if p >= 90:
        return 'A+'
    if p >= 80:
        return 'A'
    if p >= 70:
        return 'B+'
    if p >= 60:
        return 'B'
    if p >= 50:
        return 'C'
    return 'F'
