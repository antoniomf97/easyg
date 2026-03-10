import pytest
from unittest.mock import patch

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
