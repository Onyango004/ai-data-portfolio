import unittest
from redact import redact


class TestRedact(unittest.TestCase):
    def check(self, text, expected):
        self.assertEqual(redact(text)[0], expected)

    def test_email(self):
        self.check("Mail me at jane.doe@example.com", "Mail me at [EMAIL]")

    def test_phone_local(self):
        self.check("Call 0712 345 678 now", "Call [PHONE] now")

    def test_phone_international(self):
        self.check("Call +254 712 345 678 now", "Call [PHONE] now")

    def test_national_id(self):
        self.check("My ID No: 12345678.", "My [NATIONAL_ID].")

    def test_title_name(self):
        self.check("Ask Mr Otieno Kamau about it", "Ask [NAME] about it")

    def test_ip_and_url(self):
        self.check("Server 192.168.1.10 at https://example.com/a", "Server [IP] at [URL]")

    def test_clean_text_unchanged(self):
        self.check("The meeting is at 3pm on Tuesday.", "The meeting is at 3pm on Tuesday.")


if __name__ == "__main__":
    unittest.main()
