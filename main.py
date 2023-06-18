from dash import Dash, html, dcc
#import dash_dangerously_set_inner_html as ddsih
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
import pandas as pd
import pygwalker as pyg
import dash_bootstrap_components as dbc


df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
walker = pyg.walk(df, return_html=True)
#walker2 = pyg.walk(df)
#walker_html = walker2.to_html()

def simple_card(main_body):
    return dbc.Card(
    [
        #dbc.CardImg(src=img_path, top=True, style={'width': '100%', 'max-width': '300px', 'height': 'auto'}),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                main_body,
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'box-shadow': '0px 0px 10px 0px rgba(0,0,0,0.2)',
            'border-radius': '30px',
            'overflow': 'hidden',
            'padding': '20px 20px 20px 20px',
            'height': "100%", 
            'width': "100%",
            "background-color": "green"
        },
)

app = Dash(__name__)
app.scripts.config.serve_locally = True
app.layout = html.Div(
        #simple_card(DangerouslySetInnerHTML(walker)),
        html.Iframe(srcDoc=walker, style={'height':'100vh' , 'width':'100vw'})
        
        #dcc.Markdown(walker, dangerously_allow_html =True)
        , style = {'height':'100vh' , 'width':'100vw'}
    
)

if __name__ == "__main__":
    app.run_server(debug=True)

