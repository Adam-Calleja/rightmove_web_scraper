import pytest
from rightmove_web_scraper.Filter import Filter
from rightmove_web_scraper.Accommodation import Accommodation
from datetime import datetime
from unittest import TestCase

class TestFilter(TestCase):
    """
    Test Class for the Filter class
    """

    @pytest.fixture
    def test_filter(self):
        return TestFilter()
    
    def test_filter_by_price(self):
        """
        Test the filter by price method

        Test that the filter by price method filters the 
        Accommodation objects by price correctly.

        Raises
        ------
        AssertionError
            If the list of Accommodation objects is not filtered correctly
        """

        # Arrange
        filter = Filter()

        accommodation_1 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        accommodation_2 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 500.0,
            bedrooms = 2,
            bathrooms = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        accommodation_3 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 750.0,
            bedrooms = 2,
            bathrooms = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        accommodation_4 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 1000.0,
            bedrooms = 2,
            bathrooms = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        accommodation_5 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 1500.0,
            bedrooms = 2,
            bathrooms = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        expected_accommodations = [accommodation_2, accommodation_3, accommodation_4]

        # Act
        filtered_accommodations = filter.filter_by_price([accommodation_1, accommodation_2, accommodation_3, accommodation_4, accommodation_5], 500.0, 1000.0)

        # Assert
        self.assertCountEqual(filtered_accommodations, expected_accommodations)