import datetime

class Accommodation:

    def __init__(self, title: str, website: str, url: str, latitude: float, longitude: float, monthly_price: float, bedrooms: int, bathrooms: int, available_from: datetime.datetime, deposit: float, council_tax_band: str, furnish_type: str, status: str, property_type: str) -> None:
        self.title = title
        self.website = website
        self.url = url
        self.latitude = latitude
        self.longitude = longitude
        self.monthly_price = monthly_price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.available_from = available_from
        self.deposit = deposit
        self.council_tax_band = council_tax_band
        self.furnish_type = furnish_type
        self.status = status
        self.property_type = property_type

        if self.title is None:
            raise TypeError("Title cannot be None")
        elif self.website is None:
            raise TypeError("Website cannot be None")
        elif self.url is None:
            raise TypeError("URL cannot be None")
        elif self.monthly_price is None:
            raise TypeError("Monthly price cannot be None")
        elif self.bedrooms is None:
            raise TypeError("Bedrooms cannot be None")
        elif self.status is None:
            raise TypeError("Status cannot be None")
        
    def __eq__(self, other) -> bool:
        """
        Compares two Accommodation objects for equality

        Parameters
        ----------
        other : Accommodation
            The other Accommodation object to compare

        Returns
        -------
        bool
            True if the two Accommodation objects are equal, False otherwise
        """

        if isinstance(other, Accommodation):
            return self.title == other.title and self.website == other.website and self.url == other.url and self.latitude == other.latitude and self.longitude == other.longitude and self.monthly_price == other.monthly_price and self.bedrooms == other.bedrooms and self.bathrooms == other.bathrooms and self.available_from == other.available_from and self.deposit == other.deposit and self.council_tax_band == other.council_tax_band and self.furnish_type == other.furnish_type and self.status == other.status and self.property_type == other.property_type
        return False

    def __hash__(self) -> int:
        """
        Returns the hash value of the Accommodation object

        Returns
        -------
        int
            The hash value of the Accommodation object
        """

        return hash((self.title, self.website, self.url, self.latitude, self.longitude, self.monthly_price, self.bedrooms, self.bathrooms, self.available_from, self.deposit, self.council_tax_band, self.furnish_type, self.status, self.property_type))
        
    def is_furnished(self) -> bool:
        """ 
        Returns True if the accommodation is furnished or part furnished. 
        
        Returns
        -------
        bool
            True if the accommodation is furnished or part furnished, False
            otherwise.
        """
        
        return self.furnish_type == "Furnished" or self.furnish_type == "Part Furnished"
        