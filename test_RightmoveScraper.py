import pytest

from RightmoveScraper import RightmoveScraper

class TestRightmoveScraper:
    """
    Test class for the WebScraper class.
    """

    def test_get_url(self):
        """
        Test the get_url method.
        """
        
        search_radius = "This area only"
        min_price = 1000
        max_price = 1300
        min_bedrooms = 1
        max_bedrooms = 2
        property_type = "Any"
        added = "Anytime"
        location = "Manchester"
        include_let_agreed = False

        url = RightmoveScraper.get_url(location, search_radius, min_price, max_price, min_bedrooms, max_bedrooms, property_type, added, include_let_agreed)

        assert url == "https://www.rightmove.co.uk/property-to-rent/find.html?searchLocation=Manchester+City+Centre&useLocationIdentifier=true&locationIdentifier=REGION%5E94019&radius=0.0&minPrice=1000&maxPrice=1200&minBedrooms=1&maxBedrooms=2&_includeLetAgreed=on&includeLetAgreed=false"

