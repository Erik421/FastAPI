import unittest
from unittest.mock import patch, MagicMock
from .test_endpoints import client, test_login
from app.api.models.currency import Convert


class TestConvert(unittest.TestCase):
    @patch("app.api.endpoints.currency.get_convert")
    def test_convert_currency(self, mock_get_convert: MagicMock):
        mock_response = "111"
        mock_get_convert.return_value = mock_response
        token = test_login()
        response = client.get(f"/currency/exchange?from_currency=TEST&to_currency=TEST&amount={mock_response}",
                              headers={"Authorization": F"Bearer {token}"})
        mock_get_convert.assert_called_once_with(Convert(from_currency="TEST", to_currency="TEST", amount=mock_response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mock_response)


class TestCurrencyList(unittest.TestCase):
    @patch("app.api.endpoints.currency.get_list")
    def test_currency_list(self, mock_get_list: MagicMock):
        mock_response = "This is list of all currency"
        mock_get_list.return_value = mock_response
        token = test_login()
        response = client.get("/currency/list", headers={"Authorization": F"Bearer {token}"})
        mock_get_list.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mock_response)