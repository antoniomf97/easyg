import pytest
from unittest.mock import patch

import app.core.exceptions as e
from app.services.processing_plotter import process_plot


class DummyFile:
    def __init__(self):
        self.file = "fake.csv"
        self.content_type = "text/csv"


class DummyConfig:
    pass


@pytest.mark.asyncio
@patch("app.services.processing_plotter.graph_builder")
async def test_process_plot_success(mock_graph_builder):
    mock_graph_builder.return_value = b"imagebytes"

    file = DummyFile()
    config = DummyConfig()

    result = await process_plot(file, config)

    assert result == b"imagebytes"
    mock_graph_builder.assert_called_once()


@pytest.mark.asyncio
async def test_process_plot_raises_when_no_file():
    with pytest.raises(e.FileNotProvided):
        await process_plot(None, DummyConfig())


@pytest.mark.asyncio
async def test_process_plot_raises_on_invalid_file_type():
    class BadFile:
        content_type = "application/pdf"

    with pytest.raises(e.InvalidFileTypeError):
        await process_plot(BadFile(), DummyConfig())


@pytest.mark.asyncio
async def test_process_plot_raises_when_no_config():
    with pytest.raises(e.ConfigsNotProvided):
        await process_plot(DummyFile(), None)
