import pytest
from rightmove_web_scraper.Website import Website

class TestWebsite():
    """
    Test Class for the Website class
    """

    @pytest.fixture
    def test_website(self):
        return TestWebsite()