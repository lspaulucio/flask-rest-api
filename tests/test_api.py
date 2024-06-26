import pytest
from api import create_app
from api.utils.helpers import cpf_validator


class TestApplication:
    @pytest.fixture
    def client(self):
        app = create_app("config.MockConfig")
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "name": "Jose dos Santos",
            "cpf": "054.085.300-35",
            "mail": "contato@jasantos.com",
            "birthDate": "1990-05-14",
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "name": "Jose dos Santos",
            "cpf": "641.396.500-27",
            "mail": "contato@jasantos.com",
            "birthDate": "1990-05-14",
        }

    def test_get_users(self, client):
        response = client.get("api/v1/users/")
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post("/api/v1/users/", json=valid_user)
        assert response.status_code == 204

        response = client.post("/api/v1/users/", json=invalid_user)
        assert response.status_code == 400
        assert b"Invalid CPF! Please enter with a valid one!" in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get("/api/v1/users/%s" % valid_user["cpf"])
        assert response.status_code == 200
        assert response.json[0]["name"] == "Jose dos Santos"
        assert response.json[0]["cpf"] == "054.085.300-35"
        assert response.json[0]["mail"] == "contato@jasantos.com"

        birth_date = response.json[0]["birthDate"]["$date"]
        assert birth_date == "1990-05-14T00:00:00Z"

        response = client.get("/api/v1/users/%s" % invalid_user["cpf"])
        assert response.status_code == 404
        assert b"User not found in database!" in response.data

    def test_cpf_validator(self):
        assert cpf_validator("908.451.920-51") is True
        assert cpf_validator("908.451.920-50") is False
        assert cpf_validator("908.451.920-51a") is False

    def test_patch_valid_user(self, client, valid_user):
        valid_user["name"] = "Matheus"
        response = client.patch("/api/v1/users/", json=valid_user)
        assert response.status_code == 200
        response = client.get("/api/v1/users/%s" % valid_user["cpf"])
        assert response.json[0]["name"] == "Matheus"

    def test_patch_invalid_user_mail(self, client, valid_user):
        valid_user["mail"] = "teste.com.br"
        response = client.patch("/api/v1/users/", json=valid_user)
        assert response.status_code == 304

    def test_patch_invalid_user_cpf(self, client, invalid_user):
        response = client.patch("/api/v1/users/", json=invalid_user)
        assert b"Invalid CPF" in response.data
        assert response.status_code == 400

    def test_delete_user(self, client, valid_user):
        response = client.delete("/api/v1/users/%s" % valid_user["cpf"])
        assert response.status_code == 200

        response = client.delete("/api/v1/users/%s" % valid_user["cpf"])
        assert b"not found" in response.data
        assert response.status_code == 400
