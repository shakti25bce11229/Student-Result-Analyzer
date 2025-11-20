from analyzer import compute_grade

def view_all(storage):
    students = storage.list_students()
    if not students:
        print('No student data.')
        return
    for s in students:
        print('-'*40)
        print(f"ID: {s.get('id')}")
        print(f"Name: {s.get('name')}")
        for sub, m in s.get('marks', {}).items():
            print(f"  {sub}: {m} / {s.get('max_marks', {}).get(sub, 100)}")
        print(f"Total: {s.get('total')} / {s.get('max_total')}")
        print(f"Percentage: {s.get('percentage')}%")
        print(f"Grade: {compute_grade(s.get('percentage'))}")

def view_student(storage):
    sid = input('Enter student ID: ').strip()
    if not sid:
        print('ID required.')
        return
    s = storage.get_by_id(sid)
    if not s:
        print('Student not found.')
        return
    print('-'*40)
    print(f"ID: {s.get('id')}")
    print(f"Name: {s.get('name')}")
    for sub, m in s.get('marks', {}).items():
        print(f"  {sub}: {m} / {s.get('max_marks', {}).get(sub, 100)}")
    print(f"Total: {s.get('total')} / {s.get('max_total')}")
    print(f"Percentage: {s.get('percentage')}%")
    print(f"Grade: {compute_grade(s.get('percentage'))}")

def class_summary(storage):
    students = storage.list_students()
    if not students:
        print('No student data.')
        return
    # Topper by percentage
    topper = max(students, key=lambda x: x.get('percentage', 0))
    avg = sum([s.get('percentage',0) for s in students]) / len(students)
    print('\nClass Summary:')
    print(f"Total students: {len(students)}")
    print(f"Topper: {topper.get('name')} (ID: {topper.get('id')}) - {topper.get('percentage')}%") 
    print(f"Average Percentage: {round(avg,2)}%") 
