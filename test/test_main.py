from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "¡Esta es la API de mi proyecto final!"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_and_read_item():
    item_data = {"id": 1, "name": "Item1", "description": "Una descripción"}
    
    # Crear item
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data

    # Leer item creado
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == item_data

def test_read_item_not_found():
    response = client.get("/items/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item no encontrado"}

