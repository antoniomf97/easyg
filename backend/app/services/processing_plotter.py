from io import BytesIO

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

import app.core.exceptions as e

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


def graph_builder(file, configs):
    # get data
    data = get_data(file.file)

    # build image
    fig = plt.figure()
    frame_builder(configs=configs)
    plot_builder(data=data, index=["y", "z"])

    # store image on buffer
    buffer = BytesIO()
    fig.savefig(buffer, format="png")
    plt.close(fig)

    buffer.seek(0)
    return buffer.getvalue()


def verify_input(file, config):
    if not file:
        raise e.FileNotProvided()

    if file.content_type not in ["text/plain", "text/csv"]:
        raise e.InvalidFileTypeError("File must be .csv or .txt")

    if config is None:
        raise e.ConfigsNotProvided("Configuration file must not be empty")


async def process_plot(file, config):
    verify_input(file, config)

    return graph_builder(file, config)
