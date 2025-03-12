from rightmove_web_scraper.Accommodation import Accommodation
import sqlite3
from datetime import datetime
from typing import List

class Database:

    def __init__(self, db_file: str) -> None:
        self.db_file = db_file
        self.connection = None

    def connect(self) -> None:
        """ Connect to the SQLite database. """

        self.connection = sqlite3.connect(self.db_file)
        self._create_table()

    def _create_table(self) -> None:
        """Create the accommodations table if it doesn't exist."""

        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accommodations (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                website TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE,
                latitude REAL,
                longitude REAL,
                monthly_price REAL NOT NULL,
                bedrooms INTEGER NOT NULL,
                bathrooms INTEGER,
                available_from TEXT,
                deposit REAL,
                council_tax_band TEXT,
                furnish_type TEXT,
                status TEXT NOT NULL,
                property_type TEXT
            )
        ''')
        self.connection.commit()

    def save_accommodation(self, accommodation: Accommodation) -> None:
        """Save an accommodation to the database."""

        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO accommodations (
                title, website, url, latitude, longitude, monthly_price, bedrooms, bathrooms, available_from, deposit, council_tax_band, furnish_type, status, property_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            accommodation.title, accommodation.website, accommodation.url, accommodation.latitude, accommodation.longitude, accommodation.monthly_price, accommodation.bedrooms, accommodation.bathrooms, accommodation.available_from.strftime('%Y-%m-%d'), accommodation.deposit, accommodation.council_tax_band, accommodation.furnish_type, accommodation.status, accommodation.property_type
        ))
        self.connection.commit()

    def delete_accommodation(self, accommodation: Accommodation) -> None:
        """Delete an accommodation from the database."""
        
        cursor = self.connection.cursor()
        cursor.execute('''
            DELETE FROM accommodations WHERE title = ?
        ''', (accommodation.title,))
        self.connection.commit()

    def get_accommodations(self) -> List[Accommodation]:
        """Retrieve all accommodations from the database."""

        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM accommodations')
        rows = cursor.fetchall()
        accommodations = []
        for row in rows:
            accommodations.append(Accommodation(
                title=row[1], website=row[2], url=row[3], latitude=row[4], longitude=row[5], monthly_price=row[6], bedrooms=row[7], bathrooms=row[8], available_from=datetime.strptime(row[9], '%Y-%m-%d'), deposit=row[10], council_tax_band=row[11], furnish_type=row[12], status=row[13], property_type=row[14]
            ))
        return accommodations