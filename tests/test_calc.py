from src.api import app

def test_calc_route():
    client = app.test_client()

    response = client.post("/calc", json={
        "expression": "3 + 5"
    })

    assert response.status_code == 200
    assert response.get_json()["result"] == "8"