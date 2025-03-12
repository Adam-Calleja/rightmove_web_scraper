import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from rightmove_web_scraper.Logger import Logger

class TestLogger():
    """
    Test Class for the Logger class
    """

    @pytest.fixture
    def test_logger(self):
        return TestLogger()
    
    @pytest.fixture
    def temp_logger(tmp_path):
        """
        Ficture to create a temporary log file and Logger instance.
        """

        log_file = tmp_path / "test.log"
        return Logger(str(log_file)), log_file
    
    @pytest.fixture
    def read_log(log_file):
        """
        Fixture to read the contents of the log file
        """

        with open(log_file, "r") as file:
            return file.readlines()
        
    def test_create_logger(self):
        """
        Test that the Logger class can be instantiated as expected

        Raises
        ------
        AssertionError
            If the Logger class is not instantiated correctly
        """

        # Arrange
        log_file = "test.log"

        # Act
        logger = Logger(log_file)

        # Assert
        assert logger is not None
        assert logger.log_file == log_file
    
    def test_log_info(self, temp_logger):
        """
        Test that the log_info method logs the correct message

        Raises
        ------
        AssertionError
            If the message logged is not the expected message
        """

        # Arrange
        logger, log_file = temp_logger

        # Act
        logger.log_info("Test Message")

        # Assert
        log_content = self.read_log(log_file)
        assert any("[INFO]" in line and "Test Message" in line for line in log_content)

    def test_log_warning(self, temp_logger):
        """
        Test that the log_warning method logs the correct message

        Raises
        ------
        AssertionError
            If the message logged is not the expected message
        """

        # Arrange
        logger, log_file = temp_logger

        # Act
        logger.log_warning("Test Message")

        # Assert
        log_content = self.read_log(log_file)
        assert any("[WARNING]" in line and "Test Message" in line for line in log_content)

    def test_log_error(self, temp_logger):
        """
        Test that the log_error method logs the correct message

        Raises
        ------
        AssertionError
            If the message logged is not the expected message
        """

        # Arrange
        logger, log_file = temp_logger

        # Act
        logger.log_error("Test Message")

        # Assert
        log_content = self.read_log(log_file)
        assert any("[ERROR]" in line and "Test Message" in line for line in log_content)

    def test_log_debug(self, temp_logger):
        """
        Test that the log_debug method logs the correct message

        Raises
        ------
        AssertionError
            If the message logged is not the expected message
        """

        # Arrange
        logger, log_file = temp_logger

        # Act
        logger.log_debug("Test Message")

        # Assert
        log_content = self.read_log(log_file)
        assert any("[DEBUG]" in line and "Test Message" in line for line in log_content)

