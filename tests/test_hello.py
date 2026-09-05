from src.api import app #hämtar din Flask-app från src/api.py.


def test_hello():
    client = app.test_client()  # skapar en testklient som kan låtsas vara en webbläsare/curl utan att den riktiga servern behöver vara igång.

    response = client.get("/hello") # skickar en test-request till /hello.

    assert response.status_code == 200 #kontrollerar att requesten lyckades.
    assert response.get_json() == { #
        "message": "Hello World!"
    } #kontrollerar att svaret innehåller exakt rätt JSON.

