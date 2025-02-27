import pytest
from rightmove_web_scraper.Website import Website

class TestWebsite():
    """
    Test Class for the Website class
    """

    @pytest.fixture
    def test_website(self):
        return TestWebsite()
    
    def test_get_search_url_all_options_passed(self):
        """
        Test the get_search_url method with all options passed

        A search URL should be returned with all options passed.

        Raises
        ------
        AssertionError
            If the search URL is not as expected
        """

        # Arrange
        website = Website()
        website.config['url_format'] = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E{location_identifier}&radius={search_radius}&minPrice={min_price}&maxPrice={max_price}&minBedrooms={min_bedrooms}&maxBedrooms={max_bedrooms}&_includeLetAgreed=on&includeLetAgreed={include_let_agreed}&furnishTypes={furnish_type}&channel=RENT&transactionType=LETTING&dontShow={dont_show}'

        # Act
        search_url = website.get_search_url(
            location_identifier='1',
            search_radius='0.0',
            min_price='0',
            max_price='1000',
            min_bedrooms='1',
            max_bedrooms='1',
            include_let_agreed='true',
            furnish_type='furnished',
            dont_show='retirement'
        )

        # Assert
        expected_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1&radius=0.0&minPrice=0&maxPrice=1000&minBedrooms=1&maxBedrooms=1&_includeLetAgreed=on&includeLetAgreed=true&furnishTypes=furnished&channel=RENT&transactionType=LETTING&dontShow=retirement'
        assert search_url == expected_url

    def test_get_search_url_no_location_identifier_passed(self):
        """
        Test the get_search_url method with missing options

        Test the get_search_url method when the location_iodentifier
        option is not passed. An ValueError should be raised.

        Raises
        ------
        ValueError
            If the location_identifier is not passed
        """
        
        # Arrange
        website = Website()
        website.config['url_format'] = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E{location_identifier}&radius={search_radius}&minPrice={min_price}&maxPrice={max_price}&minBedrooms={min_bedrooms}&maxBedrooms={max_bedrooms}&_includeLetAgreed=on&includeLetAgreed={include_let_agreed}&furnishTypes={furnish_type}&channel=RENT&transactionType=LETTING&dontShow={dont_show}'

        # Act + Assert
        with pytest.raises(ValueError):
            search_url = website.get_search_url(
                search_radius='0.0',
                min_price='0',
                max_price='1000',
                min_bedrooms='1',
                max_bedrooms='1',
                include_let_agreed='true',
                furnish_type='furnished',
                dont_show='retirement'
            )

    def test_get_search_url_no_search_radius_passed(self):
        """
        Test the get_search_url method with missing options

        Test the get_search_url method when the search_radius
        option is not passed. A valid search URL should be returned.

        Raises
        ------
        AssertionError
            If the search URL is not as expected
        """

        # Arrange
        website = Website()
        website.config['url_format'] = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E{location_identifier}&radius={search_radius}&minPrice={min_price}&maxPrice={max_price}&minBedrooms={min_bedrooms}&maxBedrooms={max_bedrooms}&_includeLetAgreed=on&includeLetAgreed={include_let_agreed}&furnishTypes={furnish_type}&channel=RENT&transactionType=LETTING&dontShow={dont_show}'

        # Act
        search_url = website.get_search_url(
            location_identifier='1',
            min_price='0',
            max_price='1000',
            min_bedrooms='1',
            max_bedrooms='1',
            include_let_agreed='true',
            furnish_type='furnished',
            dont_show='retirement'
        )

        # Assert
        expected_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1&radius=&minPrice=0&maxPrice=1000&minBedrooms=1&maxBedrooms=1&_includeLetAgreed=on&includeLetAgreed=true&furnishTypes=furnished&channel=RENT&transactionType=LETTING&dontShow=retirement'
        assert search_url == expected_url

    def test_get_search_url_no_min_price_passed(self):
        """
        Test the get_search_url method with missing options

        Test the get_search_url method when the min_price
        option is not passed. A valid search URL should be returned.

        Raises
        ------
        AssertionError
            If the search URL is not as expected
        """

        # Arrange
        website = Website()
        website.config['url_format'] = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E{location_identifier}&radius={search_radius}&minPrice={min_price}&maxPrice={max_price}&minBedrooms={min_bedrooms}&maxBedrooms={max_bedrooms}&_includeLetAgreed=on&includeLetAgreed={include_let_agreed}&furnishTypes={furnish_type}&channel=RENT&transactionType=LETTING&dontShow={dont_show}'

        # Act
        search_url = website.get_search_url(
            location_identifier='1',
            search_radius='0.0',
            max_price='1000',
            min_bedrooms='1',
            max_bedrooms='1',
            include_let_agreed='true',
            furnish_type='furnished',
            dont_show='retirement'
        )

        # Assert
        expected_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1&radius=0.0&minPrice=&maxPrice=1000&minBedrooms=1&maxBedrooms=1&_includeLetAgreed=on&includeLetAgreed=true&furnishTypes=furnished&channel=RENT&transactionType=LETTING&dontShow=retirement'
        assert search_url == expected_url

    def test_get_search_url_no_max_price_passed(self):
        """
        Test the get_search_url method with missing options

        Test the get_search_url method when the max_price
        option is not passed. A valid search URL should be returned.

        Raises
        ------
        AssertionError
            If the search URL is not as expected
        """

        # Arrange
        website = Website()
        website.config['url_format'] = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E{location_identifier}&radius={search_radius}&minPrice={min_price}&maxPrice={max_price}&minBedrooms={min_bedrooms}&maxBedrooms={max_bedrooms}&_includeLetAgreed=on&includeLetAgreed={include_let_agreed}&furnishTypes={furnish_type}&channel=RENT&transactionType=LETTING&dontShow={dont_show}'

        # Act
        search_url = website.get_search_url(
            location_identifier='1',
            search_radius='0.0',
            min_price='0',
            min_bedrooms='1',
            max_bedrooms='1',
            include_let_agreed='true',
            furnish_type='furnished',
            dont_show='retirement'
        )

        # Assert
        expected_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1&radius=0.0&minPrice=0&maxPrice=&minBedrooms=1&maxBedrooms=1&_includeLetAgreed=on&includeLetAgreed=true&furnishTypes=furnished&channel=RENT&transactionType=LETTING&dontShow=retirement'
        assert search_url == expected_url

    def test_get_search_url_no_min_bedrooms_passed(self):
        """
        Test the get_search_url method with missing options

        Test the get_search_url method when the min_bedrooms
        option is not passed. A valid search URL should be returned.

        Raises
        ------
        AssertionError
            If the search URL is not as expected
        """

        # Arrange
        website = Website()
        website.config['url_format'] = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E{location_identifier}&radius={search_radius}&minPrice={min_price}&maxPrice={max_price}&minBedrooms={min_bedrooms}&maxBedrooms={max_bedrooms}&_includeLetAgreed=on&includeLetAgreed={include_let_agreed}&furnishTypes={furnish_type}&channel=RENT&transactionType=LETTING&dontShow={dont_show}'

        # Act
        search_url = website.get_search_url(
            location_identifier='1',
            search_radius='0.0',
            min_price='0',
            max_price='1000',
            max_bedrooms='1',
            include_let_agreed='true',
            furnish_type='furnished',
            dont_show='retirement'
        )

        # Assert
        expected_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1&radius=0.0&minPrice=0&maxPrice=1000&minBedrooms=&maxBedrooms=1&_includeLetAgreed=on&includeLetAgreed=true&furnishTypes=furnished&channel=RENT&transactionType=LETTING&dontShow=retirement'
        assert search_url == expected_url

    def test_get_search_url_no_max_bedrooms_passed(self):
        """
        Test the get_search_url method with missing options

        Test the get_search_url method when the max_bedrooms
        option is not passed. A valid search URL should be returned.

        Raises
        ------
        AssertionError
            If the search URL is not as expected
        """

        # Arrange
        website = Website()
        website.config['url_format'] = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E{location_identifier}&radius={search_radius}&minPrice={min_price}&maxPrice={max_price}&minBedrooms={min_bedrooms}&maxBedrooms={max_bedrooms}&_includeLetAgreed=on&includeLetAgreed={include_let_agreed}&furnishTypes={furnish_type}&channel=RENT&transactionType=LETTING&dontShow={dont_show}'

        # Act
        search_url = website.get_search_url(
            location_identifier='1',
            search_radius='0.0',
            min_price='0',
            max_price='1000',
            min_bedrooms='1',
            include_let_agreed='true',
            furnish_type='furnished',
            dont_show='retirement'
        )

        # Assert
        expected_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1&radius=0.0&minPrice=0&maxPrice=1000&minBedrooms=1&maxBedrooms=&_includeLetAgreed=on&includeLetAgreed=true&furnishTypes=furnished&channel=RENT&transactionType=LETTING&dontShow=retirement'
        assert search_url == expected_url

    def test_get_search_url_no_include_let_agreed_passed(self):
        """
        Test the get_search_url method with missing options

        Test the get_search_url method when the include_let_agreed
        option is not passed. A valid search URL should be returned.

        Raises
        ------
        AssertionError
            If the search URL is not as expected
        """

        # Arrange
        website = Website()
        website.config['url_format'] = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E{location_identifier}&radius={search_radius}&minPrice={min_price}&maxPrice={max_price}&minBedrooms={min_bedrooms}&maxBedrooms={max_bedrooms}&_includeLetAgreed=on&includeLetAgreed={include_let_agreed}&furnishTypes={furnish_type}&channel=RENT&transactionType=LETTING&dontShow={dont_show}'

        # Act
        search_url = website.get_search_url(
            location_identifier='1',
            search_radius='0.0',
            min_price='0',
            max_price='1000',
            min_bedrooms='1',
            max_bedrooms='1',
            furnish_type='furnished',
            dont_show='retirement'
        )

        # Assert
        expected_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1&radius=0.0&minPrice=0&maxPrice=1000&minBedrooms=1&maxBedrooms=1&_includeLetAgreed=on&includeLetAgreed=&furnishTypes=furnished&channel=RENT&transactionType=LETTING&dontShow=retirement'
        assert search_url == expected_url

    def test_get_search_url_no_furnish_type_passed(self):
        """
        Test the get_search_url method with missing options

        Test the get_search_url method when the furnish_type
        option is not passed. A valid search URL should be returned.

        Raises
        ------
        AssertionError
            If the search URL is not as expected
        """

        # Arrange
        website = Website()
        website.config['url_format'] = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E{location_identifier}&radius={search_radius}&minPrice={min_price}&maxPrice={max_price}&minBedrooms={min_bedrooms}&maxBedrooms={max_bedrooms}&_includeLetAgreed=on&includeLetAgreed={include_let_agreed}&furnishTypes={furnish_type}&channel=RENT&transactionType=LETTING&dontShow={dont_show}'

        # Act
        search_url = website.get_search_url(
            location_identifier='1',
            search_radius='0.0',
            min_price='0',
            max_price='1000',
            min_bedrooms='1',
            max_bedrooms='1',
            include_let_agreed='true',
            dont_show='retirement'
        )

        # Assert
        expected_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1&radius=0.0&minPrice=0&maxPrice=1000&minBedrooms=1&maxBedrooms=1&_includeLetAgreed=on&includeLetAgreed=true&furnishTypes=&channel=RENT&transactionType=LETTING&dontShow=retirement'
        assert search_url == expected_url

    def test_get_search_url_no_dont_show_passed(self):
        """
        Test the get_search_url method with missing options

        Test the get_search_url method when the dont_show
        option is not passed. A valid search URL should be returned.

        Raises
        ------
        AssertionError
            If the search URL is not as expected
        """

        # Arrange
        website = Website()
        website.config['url_format'] = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E{location_identifier}&radius={search_radius}&minPrice={min_price}&maxPrice={max_price}&minBedrooms={min_bedrooms}&maxBedrooms={max_bedrooms}&_includeLetAgreed=on&includeLetAgreed={include_let_agreed}&furnishTypes={furnish_type}&channel=RENT&transactionType=LETTING&dontShow={dont_show}'

        # Act
        search_url = website.get_search_url(
            location_identifier='1',
            search_radius='0.0',
            min_price='0',
            max_price='1000',
            min_bedrooms='1',
            max_bedrooms='1',
            include_let_agreed='true',
            furnish_type='furnished'
        )

        # Assert
        expected_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1&radius=0.0&minPrice=0&maxPrice=1000&minBedrooms=1&maxBedrooms=1&_includeLetAgreed=on&includeLetAgreed=true&furnishTypes=furnished&channel=RENT&transactionType=LETTING&dontShow='
        assert search_url == expected_url