class Accommodation:

    def __init__(self, title, website, url, latitude, longitude, monthly_price, bedrooms, bathrooms, available_from, deposit, council_tax_band, furnish_type, status, property_type):
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
        
    def is_furnished(self):
        """ Returns True if the accommodation is furnished or part furnished. """
        return self.furnish_type == "Furnished" or self.furnish_type == "Part Furnished"
        