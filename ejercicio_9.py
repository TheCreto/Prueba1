import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure


class WatermarkFigure(Figure):  # A figure with a text watermark
    def __init__(self, *args, watermark=None, **kwargs):
        super().__init__(*args, **kwargs)
        if watermark is not None:
            bbox = dict(boxstyle='larrow', lw=3, color='yellow', ec='grey',
                        fc=(0.9, 0.9, .9, .5), alpha=0.5)
            self.text(0.5, 0.5, watermark,
                      ha='center', va='center', rotation=-60,
                      fontsize=40, color='green', alpha=0.5,
                      bbox=bbox)


plt.figure(FigureClass=WatermarkFigure, watermark='PCC')
plt.show()
