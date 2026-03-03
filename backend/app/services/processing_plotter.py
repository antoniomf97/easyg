from io import BytesIO

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from app.schemas.plotter import Configurations
from app.core.exceptions import InvalidFileTypeError, FileNotProvided

matplotlib.use("Agg")


def get_data(file_path):
    df = pd.read_csv(file_path, sep=",", index_col=0)
    return df


def frame_builder(configs):
    plt.title(configs.title)
    plt.xlabel(configs.xlabel)
    plt.ylabel(configs.ylabel)
    plt.grid(configs.grid)


def plot_builder(data, index):
    for i in index:
        plt.plot(data.index, data[i], "o", label=i + " data")

    plt.legend()


async def process_plot(file, config=None):
    verify_input(file, config)

    return graph_builder(file, config)


def graph_builder(file, configs):
    fig = plt.figure()

    if not configs:
        configs = Configurations()

    data = get_data(file.file)

    frame_builder(configs=configs)
    plot_builder(data=data, index=["y", "z"])

    buffer = BytesIO()
    fig.savefig(buffer, format="png")
    plt.close(fig)

    buffer.seek(0)
    return buffer.getvalue()


def verify_input(file, config):
    if not file:
        raise FileNotProvided()

    if file.content_type not in ["text/plain", "text/csv"]:
        raise InvalidFileTypeError("File must be .csv or .txt")
