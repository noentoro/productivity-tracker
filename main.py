import pandas as pd

df = pd.DataFrame(
    {'Week': ['W1', 'W2', 'W3', 'W4'],
     'Task 1': [1, 2, 3, 4],
     'Task 2': [1, 2, 3, 4],
     'Task 3': [1, 2, 3, 4]
     }
)
print(df)

import plotly.graph_objects as go

fig = go.Figure()
for i in range(len(df)):
    for j in range(len(df.columns)):
        if df.iloc[i, j] != 0:
            fig.add_bar(x=[i], y=[df.iloc[i, j]], name=df.columns[j])

fig.show()
