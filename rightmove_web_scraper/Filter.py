class Filter:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def filter_by_price(self, min_price, max_price):
        """
        Filters the Accommodation database by price range

        Parameters
        ----------
        min_price : float
            The minimum price of the accommodation
        max_price : float
            The maximum price of the accommodation

        Returns
        -------
        list
            A list of dictionaries containing the filtered accommodation data
        """