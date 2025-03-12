import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from rightmove_web_scraper.Filter import Filter
from rightmove_web_scraper.Accommodation import Accommodation
from rightmove_web_scraper.Database import Database
from datetime import datetime

class TestFilter():
    """
    Test Class for the Filter class
    """

    @pytest.fixture
    def test_filter(self):
        return TestFilter()
    
    @pytest.fixture
    def temp_db(self, tmp_path):
        """
        Creates a temporary database for testing
        """
        
        db_file = tmp_path / "test.db"
        db = Database(str(db_file))
        db.connect()

        return db, db_file
    
    def test_filter_by_price(self, temp_db):
        """
        Test the filter_by_price method

        Test that the filter_by_price method filters the 
        Accommodation objects by price correctly.

        Raises
        ------
        AssertionError
            If the list of Accommodation objects is not filtered correctly
        """

        # Arrange
        db, _ = temp_db
        filter = Filter(db.connection)

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

        db.save_accommodation(accommodation_1)
        db.save_accommodation(accommodation_2)
        db.save_accommodation(accommodation_3)
        db.save_accommodation(accommodation_4)
        db.save_accommodation(accommodation_5)

        expected_accommodations = [accommodation_2, accommodation_3, accommodation_4]

        # Act
        filtered_accommodations = filter.filter_by_price(500.0, 1000.0)

        # Assert
        self.assertCountEqual(filtered_accommodations, expected_accommodations)

    def test_filter_by_location(self, temp_db):
        """
        Test the filter_by_location method

        Test that the filter_by_location method filters the 
        Accommodation objects by location correctly.

        Raises
        ------
        AssertionError
            If the list of Accommodation objects is not filtered correctly
        """

        # Arrange
        db, _ = temp_db
        filter = Filter(db.connection)

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
            latitude = 53.488959,
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

        accommodation_3 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.234644,
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

        db.save_accommodation(accommodation_1)
        db.save_accommodation(accommodation_2)
        db.save_accommodation(accommodation_3)

        expected_accommodations = [accommodation_1, accommodation_2]

        # Act
        filtered_accommodations = filter.filter_by_location(53.483959, -2.244644, 1.0)

        # Assert
        self.assertCountEqual(filtered_accommodations, expected_accommodations)

    def test_filter_by_bedrooms(self, temp_db):
        """
        Test the filter_by_bedrooms method

        Test that the filter_by_bedrooms method filters the 
        Accommodation objects by number of bedrooms correctly.

        Raises
        ------
        AssertionError
            If the list of Accommodation objects is not filtered correctly
        """

        # Arrange
        db, _ = temp_db
        filter = Filter(db.connection)

        accommodation_1 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 300.0,
            bedrooms = 1,
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

        accommodation_3 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 300.0,
            bedrooms = 3,
            bathrooms = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        db.save_accommodation(accommodation_1)
        db.save_accommodation(accommodation_2)
        db.save_accommodation(accommodation_3)

        expected_accommodations = [accommodation_2, accommodation_3]

        # Act
        filtered_accommodations = filter.filter_by_bedrooms(2, 3)

        # Assert
        self.assertCountEqual(filtered_accommodations, expected_accommodations)

    def test_filter_by_bathrooms(self, temp_db):
        """
        Test the filter_by_bathrooms method

        Test that the filter_by_bathrooms method filters the 
        Accommodation objects by number of bathrooms correctly.

        Raises
        ------
        AssertionError
            If the list of Accommodation objects is not filtered correctly
        """

        # Arrange
        db, _ = temp_db
        filter = Filter(db.connection)

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
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 2,
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
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 2,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        db.save_accommodation(accommodation_1)
        db.save_accommodation(accommodation_2)
        db.save_accommodation(accommodation_3)

        expected_accommodations = [accommodation_2, accommodation_3]

        # Act
        filtered_accommodations = filter.filter_by_bathrooms(2, 2)

        # Assert
        self.assertCountEqual(filtered_accommodations, expected_accommodations)

    def test_filter_by_furnish_type(self, temp_db):
        """
        Test the filter_by_furnish_type method

        Test that the filter_by_furnish_type method filters the 
        Accommodation objects by the furnish type correctly.

        Raises
        ------
        AssertionError
            If the list of Accommodation objects is not filtered correctly
        """

        # Arrange
        db, _ = temp_db
        filter = Filter(db.connection)

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
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 2,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Unfurnished',
            status = 'Available',
            property_type = 'Flat',
        )

        accommodation_3 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 2,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Part Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        db.save_accommodation(accommodation_1)
        db.save_accommodation(accommodation_2)
        db.save_accommodation(accommodation_3)

        expected_accommodations = [accommodation_1]

        # Act
        filtered_accommodations = filter.filter_by_furnish_type('Furnished')

        # Assert
        self.assertCountEqual(filtered_accommodations, expected_accommodations)

    def test_filter_by_date(self, temp_db):
        """
        Test the filter_by_date method

        Test that the filter_by_date method filters the 
        Accommodation objects by the availability date correctly.

        Raises
        ------
        AssertionError
            If the list of Accommodation objects is not filtered correctly
        """

        # Arrange
        db, _ = temp_db
        filter = Filter(db.connection)

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
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 2,
            available_from = datetime(2025, 1, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Unfurnished',
            status = 'Available',
            property_type = 'Flat',
        )

        accommodation_3 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 2,
            available_from = datetime(2025, 8, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Part Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        db.save_accommodation(accommodation_1)
        db.save_accommodation(accommodation_2)
        db.save_accommodation(accommodation_3)

        expected_accommodations = [accommodation_1]

        # Act
        filtered_accommodations = filter.filter_by_furnish_type('01-05-2025', '01-06-2025')

        # Assert
        self.assertCountEqual(filtered_accommodations, expected_accommodations)

    def test_filter_by_status(self, temp_db):
        """
        Test the filter_by_status method

        Test that the filter_by_status method filters the 
        Accommodation objects by their status correctly.

        Raises
        ------
        AssertionError
            If the list of Accommodation objects is not filtered correctly
        """

        # Arrange
        db, _ = temp_db
        filter = Filter(db.connection)

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
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 2,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Unfurnished',
            status = 'Unavailable',
            property_type = 'Flat',
        )

        accommodation_3 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 2,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Part Furnished',
            status = 'Unavailable',
            property_type = 'Flat',
        )

        db.save_accommodation(accommodation_1)
        db.save_accommodation(accommodation_2)
        db.save_accommodation(accommodation_3)

        expected_accommodations = [accommodation_1]

        # Act
        filtered_accommodations = filter.filter_by_furnish_type('Available')

        # Assert
        self.assertCountEqual(filtered_accommodations, expected_accommodations)

    def test_apply_filters(self, temp_db):
        """
        Test the apply_filters method

        Test that the apply_filters method correctly applies multiple filters 
        to a list of Accommodation objects.

        Raises
        ------
        AssertionError
            If the list of Accommodation objects is not filtered correctly
        """

        # Arrange
        db, _ = temp_db

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
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 2,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Unfurnished',
            status = 'Unavailable',
            property_type = 'Flat',
        )

        accommodation_3 = Accommodation(
            title = "Flat 101, Test Street, Test Town",
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 300.0,
            bedrooms = 2,
            bathrooms = 2,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Part Furnished',
            status = 'Unavailable',
            property_type = 'Flat',
        )

        db.save_accommodation(accommodation_1)
        db.save_accommodation(accommodation_2)
        db.save_accommodation(accommodation_3)

        filters = {
            'bathrooms': (1, 1),
            'status': "Available"
        }

        expected_accommodations = [accommodation_1]

        # Act
        filtered_accommodations = Filter.apply_filters(filters)

        # Assert
        self.assertCountEqual(filtered_accommodations, expected_accommodations)