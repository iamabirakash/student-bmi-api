from pathlib import Path
import json

from fastapi import FastAPI, HTTPException, Query, status

app = FastAPI(title="Abir")


@app.get("/")
def health():
    return {"message": "API is running"}


@app.post("/", tags=["main"], status_code=status.HTTP_201_CREATED)
def index_post_view(data: str):
    return {"msg": data}


def load_data():
    data_file = Path(__file__).resolve().parent / "data.json"
    with data_file.open("r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/view")
def view():
    return load_data()


@app.get("/students/{students_id}")
def view_students(students_id: str):
    data = load_data()
    student_key = students_id.strip().upper()
    if not student_key.startswith("P"):
        student_key = f"P{student_key}"

    if student_key in data:
        return data[student_key]

    raise HTTPException(status_code=404, detail="student not found")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query("bmi", description="Sort by: height, weight, bmi"),
    order: str = Query("asc", description="asc or desc"),
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Choose from {valid_fields}",
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be 'asc' or 'desc'",
        )

    data = load_data()
    rows = [{"id": student_id, **student} for student_id, student in data.items()]
    return sorted(
        rows,
        key=lambda x: x[sort_by],
        reverse=(order == "desc"),
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
