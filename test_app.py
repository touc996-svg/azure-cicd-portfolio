from app import app

def test_home_page():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Azure CI/CD Portfolio" in response.data

def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_status():
    response = app.test_client().get("/api/status")
    assert response.status_code == 200
    assert response.json["status"] == "operational"
    assert response.json["project"] == "Azure CI/CD Portfolio"

def test_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    response = app.test_client().get("/api/status")
    assert response.json["environment"] == "production"
