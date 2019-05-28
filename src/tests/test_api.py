import unittest

from src.dlg import app


class APITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        app.testing = True

    def test_total_endpoint_exists(self):
        resp = self.client.post("/total/")
        assert resp.status_code != 404

    def test_no_json_content(self):
        resp = self.client.post("/total/")
        assert resp.status_code == 400
        assert resp.get_json() == {
            "message": "Was expecting a mimetype of application/json"
        }

    def test_given_a_string_instead_of_list(self):
        resp = self.client.post("/total/", json="Not a list of numbers")
        assert resp.status_code == 400
        assert resp.get_json() == {
            "message": "Was expecting a list. Given: str"
        }

    def test_given_a_dict_instead_of_list(self):
        resp = self.client.post("/total/", json={"Not": "a list"})
        assert resp.status_code == 400
        assert resp.get_json() == {
            "message": "Was expecting a list. Given: dict"
        }

    def test_not_all_elements_are_numbers(self):
        resp = self.client.post("/total/", json=[1, 2, "3"])
        assert resp.status_code == 400
        assert resp.get_json() == {
            "message": "Provided list of numbers contains a non-numeric element."
        }

    def test_empty_list(self):
        resp = self.client.post("/total/", json=[])
        assert resp.status_code == 200
        assert resp.get_json()["total"] == 0

    def test_small_list_of_numbers(self):
        resp = self.client.post("/total/", json=[1, 2, 3])
        assert resp.status_code == 200
        assert resp.get_json()["total"] == 6

    def test_large_list_of_number(self):
        numbers = list(range(10000001))
        resp = self.client.post("/total/", json=numbers)
        assert resp.status_code == 200
        assert resp.get_json()["total"] == 50000005000000

    def test_negative_numbers(self):
        resp = self.client.post("/total/", json=[1, -2, 3])
        assert resp.status_code == 200
        assert resp.get_json()["total"] == 2

    def test_floats(self):
        resp = self.client.post("/total/", json=[1, 2.5, 3])
        assert resp.status_code == 200
        assert resp.get_json()["total"] == 6.5

    def test_malformed_json(self):
        resp = self.client.post("/total/", data="[1, 2, ", content_type="application/json")
        assert resp.status_code == 400
