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
                website = None,
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
                website = "Rightmove",
                url = None,
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
                website = "Rightmove",
                url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
                monthly_price = None,
                room_count = 2,
                bathroom_count = 1,
                available_from = datetime(2025, 5, 1),
                deposit = 1045,
                council_tax_band = 'A',
                furnish_type = 'Furnished',
                post_code = 'M1 6ER',
                status = 'Available',
            )

    def test_create_accommodation_no_room_count(self):
        """
        Tests the creation of an Accommodation object without the room_count parameter

        In this test, no room_count is provided. A TypeError should be raised.

        Raises
        ------
        TypeError
            If the room_count parameter is not provided
        """

        with pytest.raises(TypeError):
            accommodation = Accommodation(
                website = "Rightmove",
                url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
                monthly_price = 1000.0,
                room_count = None,
                bathroom_count = 1,
                available_from = datetime(2025, 5, 1),
                deposit = 1045,
                council_tax_band = 'A',
                furnish_type = 'Furnished',
                post_code = 'M1 6ER',
                status = 'Available',
            )

    def test_create_accommodation_no_bathroom_count(self):
        """
        Tests the creation of an Accommodation object without the bathroom_count parameter

        In this test, no bathroom_count is provided. The Accommodation object should be 
        created without any errors.

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
            bathroom_count = None,
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
        assert accommodation.bathroom_count == None
        assert accommodation.available_from == datetime(2025, 5, 1)
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.post_code == 'M1 6ER'
        assert accommodation.status == 'Available'

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
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            monthly_price = 1000.0,
            room_count = 2,
            bathroom_count = 1,
            available_from = None,
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
        assert accommodation.available_from == None
        assert accommodation.deposit == 1045
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.post_code == 'M1 6ER'
        assert accommodation.status == 'Available'

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
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            monthly_price = 1000.0,
            room_count = 2,
            bathroom_count = 1,
            available_from = datetime(2025, 5, 1),
            deposit = None,
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
        assert accommodation.deposit == None
        assert accommodation.council_tax_band == 'A'
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.post_code == 'M1 6ER'
        assert accommodation.status == 'Available'

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
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            monthly_price = 1000.0,
            room_count = 2,
            bathroom_count = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = None,
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
        assert accommodation.council_tax_band == None
        assert accommodation.furnish_type == 'Furnished'
        assert accommodation.post_code == 'M1 6ER'
        assert accommodation.status == 'Available'

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
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            monthly_price = 1000.0,
            room_count = 2,
            bathroom_count = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = None,
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
        assert accommodation.furnish_type == None
        assert accommodation.post_code == 'M1 6ER'
        assert accommodation.status == 'Available'

    def test_create_accommodation_no_post_code(self):
        """
        Tests the creation of an Accommodation object without the post_code parameter

        In this test, no post_code is provided. A TypeError should be raised.

        Raises
        ------
        TypeError
            If the post_code parameter is not provided
        """

        with pytest.raises(TypeError):
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
                post_code = None,
                status = 'Available',
            )

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
                status = None,
            )

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
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            monthly_price = 1000.0,
            room_count = 2,
            bathroom_count = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Unfurnished',
            post_code = 'M1 6ER',
            status = 'Available',
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
            website = "Rightmove",
            url = "https://www.rightmove.co.uk/property-to-rent/property-12345678.html",
            monthly_price = 1000.0,
            room_count = 2,
            bathroom_count = 1,
            available_from = datetime(2025, 5, 1),
            deposit = 1045,
            council_tax_band = 'A',
            furnish_type = 'Part Furnished',
            post_code = 'M1 6ER',
            status = 'Available',
        )

        assert accommodation.is_furnished() == True
