import pytest
from rightmove_web_scraper.ZooplaWebsite import ZooplaWebsite

class TestZooplaWebsite():
    """
    Test Class for the ZooplaWebsite class
    """

    @pytest.fixture
    def test_zooplawebsite(self):
        return TestZooplaWebsite()
    
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
        zoopla_website = ZooplaWebsite()
        location = "manchester"

        # Act
        location_identifier, display_name = zoopla_website.get_location_identifier(location)

        # Assert
        assert location_identifier == "manchester"

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
        zoopla_website = ZooplaWebsite()
        location = "manchester"

        # Act
        location_identifier, display_name = zoopla_website.get_location_identifier(location)

        # Assert
        assert display_name == "Manchester, Greater Manchester"