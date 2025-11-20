"""Student Result Analyzer - Terminal Application (Pure Python)
Run: python main.py
"""
from storage import StudentStorage
from add_student import add_student
from view_results import view_all, view_student, class_summary
from analyzer import compute_grade
from utils import pause

def main_menu():
    storage = StudentStorage('students.json')
    while True:
        print('\n=== STUDENT RESULT ANALYZER ===')
        print('1. Add student & marks')
        print('2. View all results')
        print('3. View student by ID')
        print('4. Class summary (topper, averages)')
        print('5. Export results to CSV')
        print('0. Exit')
        choice = input('Choose: ').strip()
        if choice == '1':
            add_student(storage)
        elif choice == '2':
            view_all(storage)
            pause()
        elif choice == '3':
            view_student(storage)
            pause()
        elif choice == '4':
            class_summary(storage)
            pause()
        elif choice == '5':
            path = input('Enter CSV filename (eg results.csv): ').strip() or 'results.csv'
            storage.export_to_csv(path)
            print(f'Exported to {path}')
            pause()
        elif choice == '0':
            print('Goodbye!')
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main_menu()
