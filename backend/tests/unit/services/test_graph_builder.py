import io
import pytest
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from unittest.mock import MagicMock, patch

from app.services.processing_plotter import (
    get_data,
    frame_builder,
    plot_builder,
    graph_builder,
)

matplotlib.use("Agg")


# ---------------------------------------------------------------------------
# get_data
# ---------------------------------------------------------------------------


def _make_csv_file(content: str):
    """Return a file-like object wrapping the given CSV string."""
    return io.StringIO(content)


def test_get_data_returns_dataframe():
    csv = "idx,y,z\n1,2,3\n4,5,6\n"
    df = get_data(_make_csv_file(csv))
    assert isinstance(df, pd.DataFrame)


def test_get_data_correct_values():
    csv = "idx,y,z\n1,10,20\n2,30,40\n"
    df = get_data(_make_csv_file(csv))
    assert list(df["y"]) == [10, 30]
    assert list(df["z"]) == [20, 40]


def test_get_data_uses_first_column_as_index():
    csv = "myindex,y,z\nA,1,2\nB,3,4\n"
    df = get_data(_make_csv_file(csv))
    assert df.index.name == "myindex"
    assert list(df.index) == ["A", "B"]


# ---------------------------------------------------------------------------
# frame_builder
# ---------------------------------------------------------------------------


class DummyConfigs:
    title = "My Title"
    xlabel = "X Axis"
    ylabel = "Y Axis"
    grid = True


def test_frame_builder_sets_title():
    plt.figure()
    frame_builder(DummyConfigs())
    assert plt.gca().get_title() == "My Title"
    plt.close()


def test_frame_builder_sets_labels():
    plt.figure()
    frame_builder(DummyConfigs())
    ax = plt.gca()
    assert ax.get_xlabel() == "X Axis"
    assert ax.get_ylabel() == "Y Axis"
    plt.close()


# ---------------------------------------------------------------------------
# plot_builder
# ---------------------------------------------------------------------------


def test_plot_builder_creates_lines():
    csv = "idx,y,z\n1,2,3\n4,5,6\n"
    df = get_data(_make_csv_file(csv))

    fig, ax = plt.subplots()
    plt.sca(ax)
    plot_builder(df, ["y", "z"])

    # one Line2D per column
    assert len(ax.get_lines()) == 2
    plt.close(fig)


def test_plot_builder_line_labels():
    csv = "idx,y,z\n1,2,3\n4,5,6\n"
    df = get_data(_make_csv_file(csv))

    fig, ax = plt.subplots()
    plt.sca(ax)
    plot_builder(df, ["y", "z"])

    labels = [line.get_label() for line in ax.get_lines()]
    assert "y data" in labels
    assert "z data" in labels
    plt.close(fig)


# ---------------------------------------------------------------------------
# graph_builder
# ---------------------------------------------------------------------------


class DummyFile:
    def __init__(self, content: str):
        self.file = io.StringIO(content)
        self.content_type = "text/csv"


class ValidConfigs:
    title = "Title"
    xlabel = "x"
    ylabel = "y"
    grid = True
    plot_color = "blue"


def test_graph_builder_returns_png_bytes():
    csv = "idx,y,z\n1,2,3\n4,5,6\n"
    result = graph_builder(DummyFile(csv), ValidConfigs())
    assert isinstance(result, bytes)
    # PNG magic bytes
    assert result[:4] == b"\x89PNG"


def test_graph_builder_closes_figure():
    """After graph_builder runs there should be no leaked figures."""
    csv = "idx,y,z\n1,2,3\n4,5,6\n"
    before = len(plt.get_fignums())
    graph_builder(DummyFile(csv), ValidConfigs())
    after = len(plt.get_fignums())
    assert after == before
