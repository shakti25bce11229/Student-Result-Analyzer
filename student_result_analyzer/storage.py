import json, csv, os
from datetime import datetime
from utils import generate_id

class StudentStorage:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.students = json.load(f)
            except Exception:
                self.students = []
        else:
            self.students = []

    def _save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.students, f, indent=2, ensure_ascii=False)

    def add_student(self, student):
        student.setdefault('id', generate_id())
        student.setdefault('created_at', datetime.utcnow().isoformat())
        # compute total and percentage
        marks = student.get('marks', {})
        total = sum(marks.values()) if marks else 0
        max_total = sum([student.get('max_marks', {}).get(sub, 100) for sub in marks.keys()]) if marks else 0
        student['total'] = total
        student['max_total'] = max_total
        student['percentage'] = round((total / max_total) * 100, 2) if max_total else 0.0
        self.students.append(student)
        self._save()
        return student

    def list_students(self):
        return self.students

    def get_by_id(self, sid):
        for s in self.students:
            if s.get('id') == sid:
                return s
        return None

    def export_to_csv(self, path='results.csv'):
        # collect all subjects
        subjects = set()
        for s in self.students:
            for sub in s.get('marks', {}).keys():
                subjects.add(sub)
        subjects = sorted(list(subjects))
        headers = ['id','name'] + subjects + ['total','max_total','percentage','created_at']
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for s in self.students:
                row = {h: '' for h in headers}
                row['id'] = s.get('id')
                row['name'] = s.get('name')
                for sub in subjects:
                    row[sub] = s.get('marks', {}).get(sub, '')
                row['total'] = s.get('total', '')
                row['max_total'] = s.get('max_total', '')
                row['percentage'] = s.get('percentage', '')
                row['created_at'] = s.get('created_at', '')
                writer.writerow(row)
