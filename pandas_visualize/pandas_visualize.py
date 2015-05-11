from IPython.html.widgets import interact,SelectMultiple,IntSlider
from IPython.display import display
import pandas as pd

from IPython.utils.traitlets import link

def iview(self, width = 400):
    f = lambda rows_start, rows_end,cols: display(self[list(cols)].iloc[rows_start:rows_end])
    rs = IntSlider(min=0, max=self.shape[0], width=width)
    re = IntSlider(min=0, max=self.shape[0], width= width)
    link((re, 'min'), (rs, 'value'))
    interact(f,
             cols=SelectMultiple(options=self.columns.tolist()),
             rows_start=rs,
             rows_end=re, width=width)

pd.DataFrame.iview = iview
