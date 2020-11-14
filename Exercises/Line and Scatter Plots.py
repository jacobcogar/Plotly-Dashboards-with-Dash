import numpy as np
import pandas as pd
import plotly.offline as pyo
 
# create fake data:
np.random.seed(42)
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
pyo.plot([{
    'x': df.index,
    'y': df[col],
    'name': col
} for col in df.columns])

import plotly.graph_objs as go

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]

pyo.plot(data, filename='scatter1.html')