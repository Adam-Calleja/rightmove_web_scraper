import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

        assert accommodation.title == "Flat 101, Test Street, Test Town"   
        assert accommodation.website == "Rightmove"
        assert accommodation.url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodation.latitude == 53.483959
        assert accommodation.longitude == -2.244644
        assert accommodation.monthly_price == 1000.0
        assert accommodation.bedrooms == 2
        assert accommodation.bathrooms == 1
        assert accommodation.available_from == datetime(2025, 5, 1)
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.status == 'Available'
        assert accommodation.property_type == 'Flat'

    def test_create_accommodation_no_title(self):
        """
        Tests the creation of an Accommodation object without the title parameter

        In this test, no title is provided. A TypeError should be raised.

        Raises
        ------
        TypeError
            If the title parameter is not provided
        """

        with pytest.raises(TypeError):
            accommodation = Accommodation(
                title = None,
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

    def test_create_accommodation_no_website(self):
        """
        Tests the creation of an Accommodation object without the website parameter

        In this test, no website is provided. A TypeError should be raised.

        Raises
        ------
        TypeError
            If the website parameter is not provided
        """

        with pytest.raises(TypeError):
            accommodation = Accommodation(
                title = "Flat 101, Test Street, Test Town"  ,
                website = None,
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

    def test_create_accommodation_no_url(self):
        """
        Tests the creation of an Accommodation object without the url parameter

        In this test, no url is provided. A TypeError should be raised.

        Raises
        ------
        TypeError
            If the url parameter is not provided
        """
        
        with pytest.raises(TypeError):
            accommodation = Accommodation(
                title = "Flat 101, Test Street, Test Town"  ,
                website = "Rightmove",
                url = None,
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

    def test_create_accommodation_no_latitude(self):
        """
        Tests the creation of an Accommodation object without the latitude parameter

        In this test, no latitude is provided. The Accommodation object should be
        created without any errors.

        Raises
        ------
        AssertionError
            If the Accommodation object is not created correctly    
        """
        
        accommodation = Accommodation(
            title = "Flat 101, Test Street, Test Town"  ,
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = None,
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

        assert accommodation.title == "Flat 101, Test Street, Test Town"   
        assert accommodation.website == "Rightmove"
        assert accommodation.url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodation.latitude == None
        assert accommodation.longitude == -2.244644
        assert accommodation.monthly_price == 1000.0
        assert accommodation.bedrooms == 2
        assert accommodation.bathrooms == 1
        assert accommodation.available_from == datetime(2025, 5, 1)
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.status == 'Available'
        assert accommodation.property_type == 'Flat'

    def test_create_accommodation_no_longitude(self):
        """
        Tests the creation of an Accommodation object without the longitude parameter

        In this test, no longitude is provided. The Accommodation object should be
        created without any errors.

        Raises
        ------
        AssertionError
            If the Accommodation object is not created correctly
        """

        accommodation = Accommodation(
            title = "Flat 101, Test Street, Test Town"  ,
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = None,
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

        assert accommodation.title == "Flat 101, Test Street, Test Town"   
        assert accommodation.website == "Rightmove"
        assert accommodation.url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodation.latitude == 53.483959
        assert accommodation.longitude == None
        assert accommodation.monthly_price == 1000.0
        assert accommodation.bedrooms == 2
        assert accommodation.bathrooms == 1
        assert accommodation.available_from == datetime(2025, 5, 1)
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.status == 'Available'
        assert accommodation.property_type == 'Flat'

    def test_create_accommodation_no_monthly_price(self):
        """
        Tests the creation of an Accommodation object without the monthly_price parameter

        In this test, no monthly_price is provided. A TypeError should be raised.

        Raises
        ------
        TypeError
            If the monthly_price parameter is not provided
        """

        with pytest.raises(TypeError):
            accommodation = Accommodation(
                title = "Flat 101, Test Street, Test Town"  ,
                website = "Rightmove",
                url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
                latitude = 53.483959,
                longitude = -2.244644,
                monthly_price = None,
                bedrooms = 2,
                bathrooms = 1,
                available_from = datetime(2025, 5, 1),
                deposit = 1045,
                council_tax_band = 'A',
                furnish_type = 'Furnished',
                status = 'Available',
                property_type = 'Flat',
            )

    def test_create_accommodation_no_bedrooms(self):
        """
        Tests the creation of an Accommodation object without the bedrooms parameter

        In this test, no bedrooms is provided. A TypeError should be raised.

        Raises
        ------
        TypeError
            If the bedrooms parameter is not provided
        """

        with pytest.raises(TypeError):
            accommodation = Accommodation(
                title = "Flat 101, Test Street, Test Town"  ,
                website = "Rightmove",
                url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
                latitude = 53.483959,
                longitude = -2.244644,
                monthly_price = 1000.0,
                bedrooms = None,
                bathrooms = 1,
                available_from = datetime(2025, 5, 1),
                deposit = 1045,
                council_tax_band = 'A',
                furnish_type = 'Furnished',
                status = 'Available',
                property_type = 'Flat',
            )

    def test_create_accommodation_no_bathrooms(self):
        """
        Tests the creation of an Accommodation object without the bathrooms parameter

        In this test, no bathrooms is provided. The Accommodation object should be 
        created without any errors.

        Raises
        ------
        AssertionError
            If the Accommodation object is not created correctly
        """

        accommodation = Accommodation(
            title = "Flat 101, Test Street, Test Town"  ,
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 1000.0,
            bedrooms = 2,
            bathrooms = None,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        assert accommodation.title == "Flat 101, Test Street, Test Town"
        assert accommodation.website == "Rightmove"
        assert accommodation.url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodation.latitude == 53.483959
        assert accommodation.longitude == -2.244644
        assert accommodation.monthly_price == 1000.0
        assert accommodation.bedrooms == 2
        assert accommodation.bathrooms == None
        assert accommodation.available_from == datetime(2025, 5, 1)
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.status == 'Available'
        assert accommodation.property_type == 'Flat'

    def test_create_accommodation_no_available_from(self):
        """
        Tests the creation of an Accommodation object without the available_from parameter

        In this test, no available_from is provided. The Accommodation object should be
        created without any errors.

        Raises
        ------
        AssertionError
            If the Accommodation object is not created correctly
        """

        accommodation = Accommodation(
            title = "Flat 101, Test Street, Test Town"  ,
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 1000.0,
            bedrooms = 2,
            bathrooms = 1,
            available_from = None,
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        assert accommodation.title == "Flat 101, Test Street, Test Town"
        assert accommodation.website == "Rightmove"
        assert accommodation.url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodation.latitude == 53.483959
        assert accommodation.longitude == -2.244644
        assert accommodation.monthly_price == 1000.0
        assert accommodation.bedrooms == 2
        assert accommodation.bathrooms == 1
        assert accommodation.available_from == None
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.status == 'Available'
        assert accommodation.property_type == 'Flat'

    def test_create_accommodation_no_deposit(self):
        """
        Tests the creation of an Accommodation object without the deposit parameter

        In this test, no deposit is provided. The Accommodation object should be
        created without any errors.

        Raises
        ------
        AssertionError
            If the Accommodation object is not created correctly
        """

        accommodation = Accommodation(
            title = "Flat 101, Test Street, Test Town"  ,
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 1000.0,
            bedrooms = 2,
            bathrooms = 1,
            available_from = datetime(2025, 5, 1),
            deposit = None,
            council_tax_band = 'A',
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        assert accommodation.title == "Flat 101, Test Street, Test Town"
        assert accommodation.website == "Rightmove"
        assert accommodation.url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodation.latitude == 53.483959
        assert accommodation.longitude == -2.244644
        assert accommodation.monthly_price == 1000.0
        assert accommodation.bedrooms == 2
        assert accommodation.bathrooms == 1
        assert accommodation.available_from == datetime(2025, 5, 1)
        assert accommodation.deposit == None
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.status == 'Available'
        assert accommodation.property_type == 'Flat'

    def test_create_accommodation_no_council_tax_band(self):
        """
        Tests the creation of an Accommodation object without the council_tax_band parameter

        In this test, no council_tax_band is provided. The Accommodation object should be
        created without any errors.

        Raises
        ------
        AssertionError
            If the Accommodation object is not created correctly
        """

        accommodation = Accommodation(
            title = "Flat 101, Test Street, Test Town"  ,
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            latitude = 53.483959,
            longitude = -2.244644,
            monthly_price = 1000.0,
            bedrooms = 2,
            bathrooms = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = None,
            furnish_type = 'Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        assert accommodation.title == "Flat 101, Test Street, Test Town"
        assert accommodation.website == "Rightmove"
        assert accommodation.url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodation.latitude == 53.483959
        assert accommodation.longitude == -2.244644
        assert accommodation.monthly_price == 1000.0
        assert accommodation.bedrooms == 2
        assert accommodation.bathrooms == 1
        assert accommodation.available_from == datetime(2025, 5, 1)
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == None
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.status == 'Available'
        assert accommodation.property_type == 'Flat'

    def test_create_accommodation_no_furnish_type(self):
        """
        Tests the creation of an Accommodation object without the furnish_type parameter

        In this test, no furnish_type is provided. The Accommodation object should be
        created without any errors.

        Raises
        ------
        AssertionError
            If the Accommodation object is not created correctly
        """

        accommodation = Accommodation(
            title = "Flat 101, Test Street, Test Town"  ,
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
            furnish_type = None,
            status = 'Available',
            property_type = 'Flat',
        )

        assert accommodation.title == "Flat 101, Test Street, Test Town"
        assert accommodation.website == "Rightmove"
        assert accommodation.url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodation.latitude == 53.483959
        assert accommodation.longitude == -2.244644
        assert accommodation.monthly_price == 1000.0
        assert accommodation.bedrooms == 2
        assert accommodation.bathrooms == 1
        assert accommodation.available_from == datetime(2025, 5, 1)
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == None
        assert accommodation.status == 'Available'
        assert accommodation.property_type == 'Flat'

    def test_create_accommodation_no_status(self):
        """
        Tests the creation of an Accommodation object without the status parameter

        In this test, no status is provided. A TypeError should be raised.

        Raises
        ------
        TypeError
            If the status parameter is not provided
        """

        with pytest.raises(TypeError):
            accommodation = Accommodation(
                title = "Flat 101, Test Street, Test Town"  ,
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
                status = None,
                property_type = 'Flat',
            )

    def test_create_accommodation_no_property_type(self):
        """
        Tests the creation of an Accommodation object without the property_type parameter

        In this test, no property_type is provided. Tbe Accommodation object should be
        created without any errors.

        Raises
        ------
        AssertionError
            If the Accommodation object is not created correctly
        """

        accommodation = Accommodation(
            title = "Flat 101, Test Street, Test Town"  ,
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
            property_type = None,
        )

        assert accommodation.title == "Flat 101, Test Street, Test Town"
        assert accommodation.website == "Rightmove"
        assert accommodation.url == "https://www.rightmove.co.uk/property-to-rent/property-12345678.html"
        assert accommodation.latitude == 53.483959
        assert accommodation.longitude == -2.244644
        assert accommodation.monthly_price == 1000.0
        assert accommodation.bedrooms == 2
        assert accommodation.bathrooms == 1
        assert accommodation.available_from == datetime(2025, 5, 1)
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.status == 'Available'
        assert accommodation.property_type == None

    def test_is_furnished(self):
        """
        Tests the is_furnished method

        In this test, the furnish_type is provided as 'Furnished'. The is_furnished
        method should return True.

        Raises
        ------
        AssertionError
            If the is_furnished method does not return True
        """

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

        assert accommodation.is_furnished() == True

    def test_is_not_furnished(self):
        """
        Tests the is_furnished method

        In this test, the furnish_type is provided as 'Unfurnished'. The is_furnished
        method should return False.

        Raises
        ------
        AssertionError
            If the is_furnished method does not return False
        """

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
            furnish_type = 'Unfurnished',
            status = 'Available',
            property_type = 'Flat',
        )

        assert accommodation.is_furnished() == False

    def test_is_part_furnished(self):
        """
        Tests the is_furnished method

        In this test, the furnish_type is provided as 'Part Furnished'. The is_furnished
        method should return True.

        Raises
        ------
        AssertionError
            If the is_furnished method does not return True
        """

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
            furnish_type = 'Part Furnished',
            status = 'Available',
            property_type = 'Flat',
        )

        assert accommodation.is_furnished() == True
