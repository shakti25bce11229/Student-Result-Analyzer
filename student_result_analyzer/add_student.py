def add_student(storage):
    print('\n--- Add Student & Marks ---')
    name = input('Student name: ').strip()
    if not name:
        print('Name required.')
        return
    # Input subjects and marks; simple loop
    print('Enter subjects and marks. Leave subject blank to finish.')
    marks = {}
    max_marks = {}
    while True:
        sub = input('Subject name (blank to stop): ').strip()
        if not sub:
            break
        try:
            mark = float(input(f'Marks obtained in {sub}: ').strip() or '0')
            mx = float(input(f'Max marks for {sub} (default 100): ').strip() or '100')
        except ValueError:
            print('Invalid number, try again.')
            continue
        marks[sub] = mark
        max_marks[sub] = mx
    if not marks:
        print('No subjects entered.')
        return
    student = {
        'name': name,
        'marks': marks,
        'max_marks': max_marks
    }
    saved = storage.add_student(student)
    print(f"Student saved with ID: {saved.get('id')}, Percentage: {saved.get('percentage')}")
