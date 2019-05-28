import unittest

from src.dlg import app


class APITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        app.config['TESTING'] = True

    def test_total_endpoint_exists(self):
        resp = self.client.post("/total/")
        assert resp.status_code != 404
