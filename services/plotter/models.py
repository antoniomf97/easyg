from pydantic import BaseModel
from typing import Tuple, List, Dict
import matplotlib.pyplot as plt
import pandas as pd


class Configurations(BaseModel):
    title: str = "Title"
    xlabel: str = "x"
    ylabel: str = "y"
    grid: bool = True


# class Figure(BaseModel):
#     figsize: Tuple[float, float] = None
#     dpi: float = None
#     facecolor: str = None
#     edgecolor: str = None
#     frameon: bool = True


# class Layout(BaseModel):
#     gridspec: Tuple[int, int] = (1, 1)
#     n_graphs: int = 1
#     grid: Dict[int, Tuple[Tuple[int, int], Tuple[int, int]]] = {0: ((0,0),(0,0))}


# class BasePlotConfigs(BaseModel):
#     pass


# class PlotConfigs(BasePlotConfigs):
#     color: str = 'blue'
#     marker: str = 'o'
#     markersize: float = 10
#     linestyle: str = 'solid'
#     linewidth: float = 1


# class ScatterConfigs(BasePlotConfigs):
#     s: float = 10 
#     color: str = 'blue'
#     marker: str = 'o'


# class Plot(BaseModel):
#     id: int = None
#     type: str = None
#     data: tuple = None
#     label: str = None
#     configs: BasePlotConfigs = PlotConfigs()


# class Graph(BaseModel):
#     title: str = None
#     xlabel: str = None
#     ylabel: str = None
#     grid: bool = False
#     legend: bool = False


# class Image(BaseModel):
#     figure: Figure = Figure()
#     layout: Layout = Layout()
#     graph: List[Tuple[int, Graph]] = [(1,Graph())]
#     plot: List[Tuple[int, Plot]] = [(1,Plot())]

# def get_data(file_path):
#     df = pd.read_csv(file_path, sep=",", index_col=0)
#     return df


# if __name__ == "__main__":
#     f = Figure(figsize=(8.0, 6.0))
#     l = Layout(gridspec=(3,3), n_graphs=4, grid={
#         0: ((0,0), (0,2)), 1: ((1,1),(0,0)), 
#         2:((2,2),(0,0)), 3:((1,2),(1,2))})
#     p = {0: Graph(title="g1", legend=True), 1: Graph(title="g2", xlabel="x"), 
#          2: Graph(title="g3", ylabel="y"), 3: Graph(title="g4", grid=True)}

#     file_path = "../../test/data/test.csv"
#     data = get_data(file_path)
#     plts = [PlotConfigs(data=(data.index, data.y), label="label", configs=PlotConfigs(color="green", markersize=10, linestyle="--")),
#             PlotConfigs(data=(data.index, data.w), configs=ScatterConfigs(s=50, color="red", marker='+'))]

#     # figure builder
#     fig = plt.figure(**dict(f))
#     fig.suptitle("Title")

#     # layout builder
#     gs = fig.add_gridspec(*l.gridspec)
#     axs = {}
#     for graph in range(l.n_graphs):
#         gs_x, gs_y = l.grid[graph]
#         ax = fig.add_subplot(gs[gs_x[0]:gs_x[1]+1, gs_y[0]:gs_y[1]+1])

#         d = plts[0]
#         ax.plot(*d.data, **dict(d.configs), label=d.label)

#         d = plts[1]
#         ax.scatter(*d.data, **dict(d.configs), label=d.label)

#         # graph builder
#         g = p[graph] 
#         ax.set_title(g.title)
#         ax.set_xlabel(g.xlabel)
#         ax.set_ylabel(g.ylabel)
#         ax.grid(g.grid)
#         if g.legend:
#             ax.legend()

#         axs[graph] = ax

#     plt.show()

#     img = Image()
#     print(img)




