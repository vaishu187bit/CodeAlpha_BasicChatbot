"""
Unit tests for Task 4: Basic Chatbot
"""

import unittest
from chatbot import chatbot_response


class TestChatbot(unittest.TestCase):

    def test_greetings(self):
        """Test variations of hello."""
        self.assertIn("Hi there!", chatbot_response("hello"))
        self.assertIn("Hi there!", chatbot_response("Hey there"))

    def test_how_are_you(self):
        """Test response to 'how are you' as specified in task requirements."""
        res = chatbot_response("how are you")
        self.assertIn("I'm fine, thanks!", res)

    def test_bye(self):
        """Test response to 'bye' as specified in task requirements."""
        res = chatbot_response("bye")
        self.assertIn("Goodbye!", res)

    def test_identity(self):
        """Test response to identity queries."""
        res = chatbot_response("what is your name")
        self.assertIn("AlphaBot", res)

    def test_fallback(self):
        """Test unknown query fallback."""
        res = chatbot_response("some totally unknown query 12345")
        self.assertIn("I'm not sure I understand", res)

    def test_empty_input(self):
        """Test empty input handling."""
        res = chatbot_response("")
        self.assertIn("Please say something", res)


if __name__ == "__main__":
    unittest.main()
