import unittest
from unittest.mock import Mock
from process import WrappedClient

class TestWrappedClient(unittest.TestCase):
    def test_send_converts_types(self):
        # Create an instance of WrappedClient with a mocked MetricsClient
        wrapped_client = WrappedClient()
        wrapped_client.client = Mock()  # Mocking the behavior of MetricsClient

        # Call the send method
        wrapped_client.send("value", 1)

        # Verify that the send method was called with parameters converted to strings
        wrapped_client.client.send.assert_called_with("value", '1')


if __name__ == "__main__":
    unittest.main()

