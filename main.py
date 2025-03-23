from fastapi import FastAPI

app = FastAPI()

# Sample data for orders and feedback
orders = [
    {"id": 1, "customer": "John Doe", "items": ["Pizza", "Burger"], "status": "Delivered"},
    {"id": 2, "customer": "Jane Smith", "items": ["Pasta", "Coke"], "status": "Pending"},
]

feedback = [
    {"id": 1, "customer": "John Doe", "rating": 5, "comment": "Great food!"},
    {"id": 2, "customer": "Jane Smith", "rating": 4, "comment": "Good but delivery was late."},
]

@app.get("/orders")
def get_orders():
    return {"orders": orders}

@app.get("/feedback")
def get_feedback():
    return {"feedback": feedback}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
