import unittest
from unittest.mock import patch

from app import create_app


class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('app.views.handle_cursor_movement')
    def test_move_cursor_endpoint(self, mock_handle_cursor_movement):
        mock_handle_cursor_movement.return_value = None

        data = {'toggle': True}
        response = self.client.post('/start', json=data)

        self.assertEqual(response.status_code, 200)
        mock_handle_cursor_movement.assert_called_once_with(True)
