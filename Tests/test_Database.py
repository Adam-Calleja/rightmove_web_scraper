import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import sqlite3
from rightmove_web_scraper.Database import Database
from rightmove_web_scraper.Accommodation import Accommodation
from datetime import datetime

class TestDatabase():
    """
    Test Class for the Database class
    """

    @pytest.fixture
    def test_database(self):
        return TestDatabase()
    
    @pytest.fixture
    def temp_db(self, tmp_path):
        """
        Creates a temporary database for testing
        """
        
        db_file = tmp_path / "test.db"
        db = Database(str(db_file))
        db.connect()

        return db, db_file
    
    def test_connect(self, temp_db):
        """
        Tests the connect method 

        Raises
        ------
        AssertionError
            If the connection is not established
        """

        # Arrange
        db, db_file = temp_db
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Act
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accommodations'")
        result = cursor.fetchone()

        # Assert
        assert result is not None

    def test_save_accommodation(self, temp_db):
        """
        Tests the save_accommodation method 

        Raises
        ------
        AssertionError
            If the accommodation is not saved
        """

        # Arrange
        db, _ = temp_db
        accommodation = Accommodation(
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

        # Act
        db.save_accommodation(accommodation)
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM accommodations WHERE title='Flat 101, Test Street, Test Town'")
        result = cursor.fetchone()

        # Assert
        assert result is not None
        assert result[0] == 1
        assert result[1] == "Flat 101, Test Street, Test Town"
        assert result[2] == "Rightmove"
        assert result[3] == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert result[4] == 53.483959
        assert result[5] == -2.244644
        assert result[6] == 1000.0
        assert result[7] == 2
        assert result[8] == 1
        assert result[9] == "2025-05-01"
        assert result[10] == 1045
        assert result[11] == 'A'
        assert result[12] == 'Furnished'
        assert result[13] == 'Available'
        assert result[14] == 'Flat'

    def test_save_accommodation_duplicate(self, temp_db):
        """
        Tests the save_accommodation method with a duplicate accommodation

        Raises
        ------
        AssertionError
            If the duplicate accommodation is saved
        """

        # Arrange
        db, _ = temp_db
        accommodation = Accommodation(
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

        db.save_accommodation(accommodation)

        # Act
        db.save_accommodation(accommodation)
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM accommodations WHERE title='Flat 101, Test Street, Test Town'")
        result = cursor.fetchall()

        # Assert
        assert len(result) == 1

    def test_delete_accommodation(self, temp_db):
        """
        Tests the delete_accommodation method 

        Raises
        ------
        AssertionError
            If the accommodation is not deleted
        """

        # Arrange
        db, _ = temp_db
        accommodation = Accommodation(
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

        db.save_accommodation(accommodation)

        # Act
        db.delete_accommodation(accommodation)
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM accommodations WHERE title='Flat 101, Test Street, Test Town'")
        result = cursor.fetchone()

        # Assert
        assert result is None

    def test_get_accommodations(self, temp_db):
        """
        Tests the get_accommodations method 

        Raises
        ------
        AssertionError
            If the accommodations are not retrieved
        """

        # Arrange
        db, _ = temp_db
        accommodation = Accommodation(
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

        db.save_accommodation(accommodation)

        # Act
        accommodations = db.get_accommodations()

        # Assert
        assert len(accommodations) == 1
        assert accommodations[0].title == "Flat 101, Test Street, Test Town"
        assert accommodations[0].website == "Rightmove"
        assert accommodations[0].url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodations[0].latitude == 53.483959
        assert accommodations[0].longitude == -2.244644
        assert accommodations[0].monthly_price == 1000.0
        assert accommodations[0].bedrooms == 2
        assert accommodations[0].bathrooms == 1
        assert accommodations[0].available_from == datetime(2025, 5, 1)
        assert accommodations[0].deposit == 1045
        assert accommodations[0].council_tax_band == 'A'
        assert accommodations[0].furnish_type == 'Furnished'
        assert accommodations[0].status == 'Available'
        assert accommodations[0].property_type == 'Flat'