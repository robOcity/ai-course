"""Generates the graphs used in the Adversarial Search Exercise(s)."""
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import graphviz as gv
from pathlib import Path
import pydot
from networkx.drawing.nx_agraph import graphviz_layout


def make_label(node_label, heuristic=None):
    """Create labeled nodes with optional heuristic values."""

    # TODO subscripts lost in translation / saving
    return (
        f"<<B>{node_label}</B> <SUB>{heuristic}</SUB>>"
        if heuristic
        else f"<<B>{node_label}</B>>"
    )


if __name__ == "__main__":

    # create the graph for the minimax / alpha-beta example
    h = gv.Graph(name="graph-with-labels", engine="dot")
    with h.subgraph(name="Legend") as legend:
        legend.node("Max", label=make_label("Max"))
        legend.node("Min", label=make_label("Min"), color="grey")
    h.node("A", label=make_label("A"))
    h.node("B", label=make_label("B"), color="grey")
    h.node("C", label=make_label("C"), color="grey")
    h.node("D", label=make_label("D", heuristic="8"))
    h.node("E", label=make_label("E", heuristic="2"))
    h.node("F", label=make_label("F", heuristic="6"))
    h.node("G", label=make_label("G", heuristic="8"))

    h.edge("A", "B")
    h.edge("A", "C")
    h.edge("B", "D")
    h.edge("B", "E")
    h.edge("C", "F")
    h.edge("C", "G")

    # Render the graph to file
    p = Path(".")
    filename = "minimax-7-node"
    gv_path = p / "graphs" / str(filename + ".gv")
    print(f"Saved {gv_path} as DOT file")
    h.save(filename=gv_path)
    (g,) = pydot.graph_from_dot_file(gv_path)
    img_path = p / "images" / str(filename + ".png")
    print(f"Saved {img_path} as rendered graph")
    g.write_png(img_path)
