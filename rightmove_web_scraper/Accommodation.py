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
        
    def is_furnished(self) -> bool:
        """ Returns True if the accommodation is furnished or part furnished. """
        
        return self.furnish_type == "Furnished" or self.furnish_type == "Part Furnished"
        