import pytest
import app.core.exceptions as e
from app.services.processing_plotter import verify_input


class DummyFile:
    def __init__(self, content_type):
        self.content_type = content_type


class DummyConfig:
    pass


def test_verify_input_valid():
    file = DummyFile("text/csv")
    config = DummyConfig()

    verify_input(file, config)  # should not raise


def test_verify_input_no_file():
    with pytest.raises(e.FileNotProvided):
        verify_input(None, DummyConfig())


def test_verify_input_invalid_type():
    file = DummyFile("application/json")

    with pytest.raises(e.InvalidFileTypeError):
        verify_input(file, DummyConfig())


def test_verify_input_no_config():
    file = DummyFile("text/csv")

    with pytest.raises(e.ConfigsNotProvided):
        verify_input(file, None)
