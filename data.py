"""
In-memory "database" for the Applications API.

This is mock/sample data only (per the task brief — no real database is used).
`applications_db` is a simple list of dicts that lives in server memory and resets
whenever the app restarts. `next_id` tracks the next id to assign to new records.
"""

from datetime import datetime, timezone

applications_db: list[dict] = [
    {
        "id": 2,
        "fullName": "Ama Serwaa Owusu",
        "email": "amaserwaa@gmail.com",
        "phone": "0245567812",
        "whatsappNumber": "0245567812",
        "university": "University of Ghana",
        "course": "Computer Engineering",
        "level": "2nd Year",
        "track": "Embedded Systems",
        "motivation": "I want to gain hands-on experience in embedded systems and IoT development.",
        "portfolioLink": "https://github.com/amase",
        "resumeLink": "https://linkedin.com/in/amase",
        "joinInnovationClub": True,
        "status": "accepted",
        "submittedAt": "2026-05-04T10:12:45Z",
    },
    {
        "id": 3,
        "fullName": "Yaw Mensah",
        "email": "yawmensah@gmail.com",
        "phone": "0558876123",
        "whatsappNumber": "0558876123",
        "university": "KNUST",
        "course": "Electrical Engineering",
        "level": "4th Year",
        "track": "Radar & RF Systems",
        "motivation": "To improve my knowledge in RF systems, radar engineering, and wireless communications.",
        "portfolioLink": "https://github.com/yawmensah",
        "resumeLink": "https://linkedin.com/in/yawmensah",
        "joinInnovationClub": True,
        "status": "pending",
        "submittedAt": "2026-05-05T08:45:30Z",
    },
    {
        "id": 4,
        "fullName": "Priscilla Adjei",
        "email": "priscilla.adjei@gmail.com",
        "phone": "0203344556",
        "whatsappNumber": "0203344556",
        "university": "Ashesi University",
        "course": "Software Engineering",
        "level": "3rd Year",
        "track": "Backend Engineering",
        "motivation": "I want to strengthen my backend engineering skills using FastAPI and modern software architecture.",
        "portfolioLink": "https://github.com/priscillaadjei",
        "resumeLink": "https://linkedin.com/in/priscillaadjei",
        "joinInnovationClub": True,
        "status": "accepted",
        "submittedAt": "2026-05-06T14:18:22Z",
    },
    {
        "id": 5,
        "fullName": "Daniel Kofi Asante",
        "email": "danielasante@gmail.com",
        "phone": "0277788990",
        "whatsappNumber": "0277788990",
        "university": "UENR",
        "course": "Biomedical Engineering",
        "level": "2nd Year",
        "track": "Biomedical Systems",
        "motivation": "To explore biomedical monitoring systems and healthcare technology innovations.",
        "portfolioLink": "https://github.com/danielasante",
        "resumeLink": "https://linkedin.com/in/danielasante",
        "joinInnovationClub": False,
        "status": "rejected",
        "submittedAt": "2026-05-07T11:05:10Z",
    },
]

# Next id to hand out to a newly created application (max existing id + 1)
next_id: int = max((a["id"] for a in applications_db), default=0) + 1


def get_next_id() -> int:
    global next_id
    current = next_id
    next_id += 1
    return current


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
