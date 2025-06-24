# estordia

This project provides a simple FastAPI backend. To run the development server:

```bash
uvicorn backend.app:app --reload
```

## Example request

Create a new item by sending its name:

```bash
curl -X POST http://localhost:8000/items \
    -H "Content-Type: application/json" \
    -d '{"name": "example"}'
```

