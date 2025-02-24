import pytest
from rightmove_web_scraper.Accommodation import Accommodation
from datetime import datetime

class TestAccommodation():
    """
    Test Class for the Accommodation class
    """

    @pytest.fixture
    def test_accommodation(self):
        return TestAccommodation()

    def test_create_accommodation_all_parameters(self):
        """
        Tests that the Accommodation object is created correctly

        In this test, all parameters are provided. The Accommodation 
        object should be created without any errors.

        Raises
        ------
        AssertionError
            If the Accommodation object is not created correctly
        """

        accommodation = Accommodation(
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            monthly_price = 1000.0,
            room_count = 2,
            bathroom_count = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            post_code = 'M1 6ER',
            status = 'Available',
        )

        assert accommodation.website == "Rightmove"
        assert accommodation.url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodation.monthly_price == 1000.0
        assert accommodation.room_count == 2
        assert accommodation.bathroom_count == 1
        assert accommodation.available_from == datetime(2025, 5, 1)
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.post_code == 'M1 6ER'
        assert accommodation.status == 'Available'

