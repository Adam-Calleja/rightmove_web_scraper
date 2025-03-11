import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from rightmove_web_scraper.RightmoveWebsite import RightmoveWebsite

class TestRightmoveWebsite():
    """
    Test Class for the RightmoveWebsite class
    """

    @pytest.fixture
    def test_rightmovewebsite(self):
        return TestRightmoveWebsite()
    
    def test_get_location_identifier_correct_identifier(self):
        """
        Test the get_location_identifier method

        Tests that the get_location_identifier method returns
        the correct location identifier for a given location.
        Raises:
        ------
        AssertionError
            If the location identifier is not equal to the expected value.
        """

        # Arrange
        rightmove_website = RightmoveWebsite()
        location = "manchester"

        # Act
        location_identifier, display_name = rightmove_website.get_location_identifier(location)

        # Assert
        assert location_identifier == "904"

    def test_get_location_identifier_correct_display_name(self):
        """
        Test the get_location_identifier method

        Tests that the get_location_identifier method returns
        the correct display name for a given location.

        Raises:
        ------
        AssertionError
            If the display name is not equal to the expected value.
        """

        # Arrange
        rightmove_website = RightmoveWebsite()
        location = "manchester"

        # Act
        location_identifier, display_name = rightmove_website.get_location_identifier(location)

        # Assert
        assert display_name == "Manchester, Greater Manchester"