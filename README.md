# Student Health FastAPI 
 
Repository Name: student-health-fastapi 
Description: FastAPI backend for student health records, individual lookup, and sorting by height, weight, and BMI. 
 
Endpoints: 
- GET / 
- POST / 
- GET /view 
- GET /students/{students_id} 
- GET /sort?sort_by=bmi&order=desc 
 
Run: 
pip install fastapi uvicorn 
uvicorn app:app --reload
