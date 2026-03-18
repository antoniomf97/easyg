import pytest
from pydantic import ValidationError

from app.schemas.input import InputData
from app.schemas.plotter import Configurations

# ---------------------------------------------------------------------------
# InputData
# ---------------------------------------------------------------------------


def test_input_data_valid():
    data = InputData(values=[1.0, 2.0, 3.0])
    assert data.values == [1.0, 2.0, 3.0]


def test_input_data_coerces_ints_to_floats():
    data = InputData(values=[1, 2, 3])
    assert data.values == [1.0, 2.0, 3.0]


def test_input_data_empty_list():
    data = InputData(values=[])
    assert data.values == []


def test_input_data_invalid_type():
    with pytest.raises(ValidationError):
        InputData(values=["a", "b"])


def test_input_data_missing_field():
    with pytest.raises(ValidationError):
        InputData()


# ---------------------------------------------------------------------------
# Configurations
# ---------------------------------------------------------------------------


def test_configurations_defaults():
    cfg = Configurations()
    assert cfg.title == "Title"
    assert cfg.xlabel == "x"
    assert cfg.ylabel == "y"
    assert cfg.grid is True
    assert cfg.plot_color == "blue"


def test_configurations_partial_override():
    cfg = Configurations(title="My Chart", grid=False)
    assert cfg.title == "My Chart"
    assert cfg.grid is False
    # other fields keep their defaults
    assert cfg.xlabel == "x"
    assert cfg.ylabel == "y"


def test_configurations_full_override():
    cfg = Configurations(
        title="T",
        xlabel="X",
        ylabel="Y",
        grid=False,
        plot_color="red",
    )
    assert cfg.title == "T"
    assert cfg.xlabel == "X"
    assert cfg.ylabel == "Y"
    assert cfg.grid is False
    assert cfg.plot_color == "red"
