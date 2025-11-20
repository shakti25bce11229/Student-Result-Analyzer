# Project Report: Student Result Analyzer (Pure Python)

## 1. Cover Page
Student Result Analyzer - Terminal Application (Pure Python)

## 2. Introduction
This project provides a lightweight student result recording and analysis system implemented in Python with JSON file storage.

## 3. Problem Statement
(See statement.md)

## 4. Functional Requirements
- Add student & marks
- View results
- Compute percentage and grade
- Export to CSV

## 5. Non-functional Requirements
- Usability: Simple CLI
- Performance: Fast for small datasets
- Reliability: JSON-based persistence
- Maintainability: Modular code

## 6. System Architecture
- UI (main.py) -> Feature modules -> storage.py (data layer)

## 7. Design Diagrams
(Include Use Case, Workflow, Sequence, Class diagrams in final PDF)

## 8. Design Decisions & Rationale
- JSON chosen for simplicity and portability
- Percentage and grade computed at insert time

## 9. Implementation Details
See source files.

## 10. Screenshots / Results
Run the app and capture terminal screenshots.

## 11. Testing Approach
Manual testing via CLI and sample data.

## 12. Challenges Faced
Minimal challenges—ensuring numerical validation and JSON integrity.

## 13. Learnings & Key Takeaways
File handling, modular design, basic analytics.

## 14. Future Enhancements
- Add editing/deleting students
- Add subject-wise analytics
- Add grade distribution histogram

## 15. References
- Python docs (json, csv)
