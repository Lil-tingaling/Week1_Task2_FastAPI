# Applications API — Week 1 Task (Zaptek Research Brief)

A backend API built with **FastAPI** and **Python**, using mock/sample data (in-memory,
no real database) to practice API architecture, routing, CRUD operations, and validation.

## Project structure

```
fastapi_project/
├── main.py           # FastAPI app + all routes
├── models.py         # Pydantic schemas (request/response validation)
├── data.py           # In-memory mock data store (seeded from the brief's sample data)
├── requirements.txt  # Dependencies
└── README.md
```

## Running locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open:
- **Swagger UI (interactive docs):** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Endpoints

| Method | Path                  | Description                                   |
|--------|-----------------------|------------------------------------------------|
| GET    | `/`                   | Health check                                   |
| GET    | `/applications`       | List all applications (filter by `status`, `university`, `track`) |
| GET    | `/applications/{id}`  | Get a single application by id                 |
| POST   | `/applications`       | Create a new application                       |
| PUT    | `/applications/{id}`  | Partially update an application                |
| DELETE | `/applications/{id}`  | Delete an application                          |

### Example: filter by status
```
GET /applications?status=accepted
```

### Example: create an application
```bash
curl -X POST http://127.0.0.1:8000/applications \
  -H "Content-Type: application/json" \
  -d '{
    "fullName": "Kwame Boateng",
    "email": "kwame@example.com",
    "phone": "0201234567",
    "whatsappNumber": "0201234567",
    "university": "University of Ghana",
    "course": "Computer Science",
    "level": "1st Year",
    "track": "Backend Engineering",
    "motivation": "I want to learn backend engineering with FastAPI.",
    "joinInnovationClub": true
  }'
```

## Validation & error handling

- Pydantic enforces field types, required fields, email format, and phone number format
  (`0XXXXXXXXX`). Invalid input returns **422 Unprocessable Entity** with details on which
  field failed.
- Requesting a non-existent application id returns **404 Not Found**.
- `PUT` with an empty body returns **400 Bad Request**.
- `DELETE` returns **204 No Content** on success.

## Note on data persistence

Data is stored in a Python list in memory (`data.py`). This means:
- It resets to the seed data every time the server restarts.
- It is **not** shared across multiple server instances/workers.

This is intentional for this task (the brief specifies mock/sample data instead of a real
database) — swapping in a real database later would mean replacing the functions in
`data.py` with actual DB queries, without needing to change `main.py`'s route logic much.

## Deploying to Render

1. Push this project to a GitHub repository.
2. On [Render](https://render.com), create a **New Web Service** and connect the repo.
3. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Deploy. Render will give you a public URL like `https://your-app.onrender.com`.
5. Share `https://your-app.onrender.com/docs` so others can try the live API.
