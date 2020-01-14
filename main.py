import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import pandas as pd
import numpy as np
from ast import literal_eval

# 'rgb(8, 48, 107)'
# 'rgb(158, 202, 225)'

plotly.tools.set_credentials_file(username='joshaby', api_key='dxilAq9GcnbUbvb3HPMC')
mapbox_access_token = 'pk.eyJ1Ijoiam9zaGFieSIsImEiOiJjandxcmc1cWswMXFsNGF0OXdiN2Nhd3Q2In0.6RVKdpC5KZ3p4HEaDtXeQg'

app = dash.Dash()

Years = ['2019', '2018', '2017', 'Todos']

Figure_tips = ['Acidentes por coordenadas', 'Acidentes por estado', 'Acidentes por região']

def CreateBar1(x, y, Colors, year) :
    return go.Bar(
        x = x,
        y = y,
        text = [('Estado: %s<br>Qtde. de acidentes: %i<br>Ano: %s' %(i, j, year)) for i, j in zip(CreateText(x), y)],
            marker = dict(
                color = Colors,
                line = dict(
                    color = 'rgb(8, 48, 107)'
                )
            ),
            showlegend = False,
            hoverinfo='text'
        )

def CreateText(List1) :
    Estados = list()
    for i in List1 :
        if i == 'AC' :
            Estados.append('Acre')
        elif i == 'AL' :
            Estados.append('Alagoas')
        elif i == 'AP' :
            Estados.append('Amapá')
        elif i == 'AM' :
            Estados.append('Amazonas')
        elif i == 'BA' :
            Estados.append('Bahia')
        elif i == 'CE' :
            Estados.append('Ceará')
        elif i == 'DF' :
            Estados.append('Dístrito Federal')
        elif i == 'ES' :
            Estados.append('Espírito Santo')
        elif i == 'GO' :
            Estados.append('Goiás')
        elif i == 'MA' :
            Estados.append('Maranhão')
        elif i == 'MT' :
            Estados.append('Mato Grosso')
        elif i == 'MS' :
            Estados.append('Mato Grosso do Sul')
        elif i == 'MG' :
            Estados.append('Minas Gerais')
        elif i == 'PA' :
            Estados.append('Pará')
        elif i == 'PB' :
            Estados.append('Paraíba')
        elif i == 'PR' :
            Estados.append('Paraná')
        elif i == 'PE' :
            Estados.append('Pernambuco')
        elif i == 'PI' :
            Estados.append('Piauí')
        elif i == 'RJ' :
            Estados.append('Rio de Janeiro')
        elif i == 'RN' :
            Estados.append('Rio Grande do Norte')
        elif i == 'RS' :
            Estados.append('Rio Grande do Sul')
        elif i == 'RO' :
            Estados.append('Rondônia')
        elif i == 'RR' :
            Estados.append('Roraima')
        elif i == 'SC' :
            Estados.append('Santa Catarina')
        elif i == 'SP' :
            Estados.append('São Paulo')
        elif i == 'SE' :
            Estados.append('Sergipe')
        elif i == 'TO' :
            Estados.append('Tocantis')
    return Estados

def CreatePieAllYears(df1, df2, df3 ,WindowOpition) :
    CS = [[0.0, 'rgb(255, 255, 204)'],
                [0.35, 'rgb(161, 218, 180)'],
                [0.5, 'rgb(65, 182, 196)'],
                [0.6, 'rgb(44, 127, 184)'],
                [0.7, 'rgb(8, 104, 172)'],
                [1.0, 'rgb(37, 52, 148)']]
    if WindowOpition == 'MultiFigure' :
        width = 650
        height = 700
    elif WindowOpition == 'SingleFigure' :
        width = 1350
        height = 600
    elif WindowOpition == 'MultiFigure1' :
        width = 375
        height = 700
    Pie = {
        'data':[
            {
                'values': [len(df1[df1['uf'] == i]) for i in df1['uf'].unique()],
                'labels': CreateText(df1['uf'].unique()),
                'domain' : {'column' : 0},
                'name': '2019',
                'hoverinfo':"label+percent+name",
                'type' : 'pie',
                'marker' : {
                    'colors' : CreateColorScale([len(df1[df1['uf'] == i]) for i in df1['uf'].unique()], CS)
                }
            },
            {
                'values': [len(df2[df2['uf'] == i]) for i in df2['uf'].unique()],
                'labels': CreateText(df2['uf'].unique()),
                'domain' : {'column' : 1},
                'name': '2018',
                'hoverinfo':"label+percent+name",
                'type' : 'pie',
                'marker' : {
                    'colors' : CreateColorScale([len(df2[df2['uf'] == i]) for i in df2['uf'].unique()], CS)
                }
            },
            {
                'values': [len(df3[df3['uf'] == i]) for i in df3['uf'].unique()],
                'labels': CreateText(df3['uf'].unique()),
                'domain' : {'column' : 2},
                'name': '2017',
                'hoverinfo':"label+percent+name",
                'type' : 'pie',
                'marker' : {
                    'colors' : CreateColorScale([len(df3[df3['uf'] == i]) for i in df3['uf'].unique()], CS)
                }
            }
        ],
        'layout': {
            'title': 'Acidentes de 2019, 2018, 2017',
            'width' : width,
            'height' : height,
            'grid' : {'rows' : 1, 'columns' : 3}
        }
    }
    return Pie

def CreatePie(df, Ano, WindowOpition) :
    CS = [[0.0, 'rgb(255, 255, 204)'],
                [0.35, 'rgb(161, 218, 180)'],
                [0.5, 'rgb(65, 182, 196)'],
                [0.6, 'rgb(44, 127, 184)'],
                [0.7, 'rgb(8, 104, 172)'],
                [1.0, 'rgb(37, 52, 148)']]
    if WindowOpition == 'MultiFigure' :
        width = 650
        height = 700
    elif WindowOpition == 'SingleFigure' :
        width = 1350
        height = 600
    elif WindowOpition == 'MultiFigure1' :
        width = 575
        height = 700
    Pie = {
        'data':[
            {
                'values': [len(df[df['uf'] == i]) for i in df['uf'].unique()],
                'labels': CreateText(df['uf'].unique()),
                'name': Ano,
                'hoverinfo':"label+percent+name",
                'type' : 'pie',
                'marker' : {
                    'colors' : CreateColorScale([len(df[df['uf'] == i]) for i in df['uf'].unique()], CS)
                }
            }
        ],
        'layout': {
            'title': 'Acidentes por' + ' % ' + 'de ' + Ano,
            'width' : width,
            'height' : height,
            'annotations' : [
                {
                    'text' : Ano,
                    'showarrow': False,
                    'x' : 0.5,
                    'y' : 0.5
                }
            ]
        }
    }
    return Pie

def CreateBarAllYears(Ano1, Ano2, Ano3, WindowOpition) :
    CS = [[0.0, 'rgb(255, 255, 204)'],
                [0.35, 'rgb(161, 218, 180)'],
                [0.5, 'rgb(65, 182, 196)'],
                [0.6, 'rgb(44, 127, 184)'],
                [0.7, 'rgb(8, 104, 172)'],
                [1.0, 'rgb(37, 52, 148)']]
    x1 = [i for i in Ano1['uf'].unique()]
    y1 = [len(Ano1[Ano1['uf'] == i]) for i in x1]
    x2 = [i for i in Ano1['uf'].unique()]
    y2 = [len(Ano2[Ano2['uf'] == i]) for i in x2]
    x3 = [i for i in Ano3['uf'].unique()]
    y3 = [len(Ano3[Ano3['uf'] == i]) for i in x3]
    Colors1 = CreateColorScale(y1, CS)
    Colors2 = CreateColorScale(y2, CS)
    Colors3 = CreateColorScale(y3, CS)
    data = [CreateBar1(x1, y1, Colors1, '2019'), CreateBar1(x2, y2, Colors2, '2018'), CreateBar1(x3, y3, Colors3,'2017')]
    if WindowOpition == 'MultiFigure' :
        width = 650
        height = 700
    elif WindowOpition == 'SingleFigure' :
        width = 1350
        height = 600
    elif WindowOpition == 'MultiFigure1' :
        width = 580
        height = 700
    layout = go.Layout(
        barmode = 'group',
        width = width,
        height = height,
        title = 'Acidentes por estados de 2019, 2018 e 2017',
        yaxis = dict(
            title = 'Número de mortes',
            titlefont = dict(
                color ='rgb(107, 107, 107)'
            )
        ),
        xaxis = dict(
            title = 'Estados por uf',
            titlefont = dict(
                color = 'rgb(107, 107, 107)'
            )
        )
    )
    return go.Figure(data = data, layout = layout)

def CreateBar(df, year, WindowOpition) :
    if WindowOpition == 'MultiFigure' :
        width = 650
        height = 700
    elif WindowOpition == 'SingleFigure' :
        width = 1350
        height = 600
    elif WindowOpition == 'MultiFigure1' :
        width = 575
        height = 700
    CS = [[0.0, 'rgb(255, 255, 204)'],
                [0.35, 'rgb(161, 218, 180)'],
                [0.5, 'rgb(65, 182, 196)'],
                [0.6, 'rgb(44, 127, 184)'],
                [0.7, 'rgb(8, 104, 172)'],
                [1.0, 'rgb(37, 52, 148)']]
    x = [i for i in df['uf'].unique()]
    y = [len(df[df['uf'] == i]) for i in x]
    Colors = CreateColorScale(y, CS)
    data = [
        CreateBar1(x, y, Colors, year)
    ]
    layout = go.Layout(
        width = width,
        height = height,
        title = 'Acidentes por estados de ' + year,
        yaxis = dict(
            title = 'Número de mortes',
            titlefont = dict(
                color = 'rgb(107, 107, 107)'
            )
        ),
        xaxis = dict(
            title = 'Estados por uf',
            titlefont = dict(
                color = 'rgb(107, 107, 107)'
            )
        )
    )
    return go.Figure(data = data, layout = layout)

def SourcesEstados(jf) :
    Sources = list()
    for i in jf['features']:
        Sources.append({"type": "FeatureCollection", 'features': [i]})
    return Sources

def GeneratingRGBCOLOR(Valor, ValorMinimo, ValorMaximo, Colors):
    if ValorMinimo <= ValorMaximo :
        plotly_scale, plotly_colors = list(map(float, np.array(Colors)[:,0])), np.array(Colors)[:,1]
        colors_01=np.array(list(map(literal_eval,[color[3:] for color in plotly_colors] )))/255.
        v = (Valor - ValorMinimo) / float((ValorMaximo - ValorMinimo))
        idx = 0
        while(v > plotly_scale[idx+1]):
            idx+=1
        left_scale_val = plotly_scale[idx]
        right_scale_val = plotly_scale[idx+ 1]
        vv = (v - left_scale_val) / (right_scale_val - left_scale_val)
        val_color01 = colors_01[idx]+vv*(colors_01[idx + 1]-colors_01[idx])
        val_color_0255 = list(map(np.uint8, 255*val_color01+0.5))
        return 'rgb'+str(tuple(val_color_0255))

def CreateColorScale(MortesEstados, CS) :
    Colors = list()
    for i in MortesEstados :
        Colors.append(GeneratingRGBCOLOR(i, min(MortesEstados), max(MortesEstados), CS))
    return Colors

def CreateChoroplethMap(Ano, WindowOpition) :
    jf = pd.read_json('Data/Geojson-Files/Estados/Estados.json')
    CS = [[0.0, 'rgb(255, 255, 204)'],
                [0.35, 'rgb(161, 218, 180)'],
                [0.5, 'rgb(65, 182, 196)'],
                [0.6, 'rgb(44, 127, 184)'],
                [0.7, 'rgb(8, 104, 172)'],
                [1.0, 'rgb(37, 52, 148)']]
    if Ano == '2019' :
        MortesEstados = [141,495,63,117,2792,1317,793,2022,2569,850,6681,1155,1643,648,1203,2047,989,5729,3445,962,1225,187,3509,6231,510,3327,393]
    elif Ano == '2018' :
        MortesEstados = [618,1625,347,543,8966,3983,2186,6146,8205,3326,21844,3701,5748,3114,3746,6433,3324,18238,10760,3280,4191,616,10878,19339,1298,10539,1592]
    elif Ano == '2017' :
        MortesEstados = [791,2022,325,431,11314,4595,2713,6870,9966,3799,28815,4631,7584,3682,4343,7819,3702,23816,13202,3336,4513,737,14994,23355,1756,13354,1892]
    if WindowOpition == 'MultiFigure' :
        width = 650
        height = 700
    elif WindowOpition == 'SingleFigure' :
        width = 1250
        height = 600
    elif WindowOpition == 'MultiFigure1' :
        width = 575
        height = 700
    Colors = CreateColorScale(MortesEstados, CS)
    SourceG = SourcesEstados(jf)
    CoordenadasEstados = {'AC': [ -8.77, -70.55]
  , 'AL': [ -9.71, -35.73], 'AP': [  1.41, -51.77]
  , 'AM': [ -3.07, -61.66], 'BA': [-12.96, -38.51]
  , 'CE': [ -3.71, -38.54], 'DF': [-15.83, -47.86]
  , 'ES': [-19.19, -40.34], 'GO': [-16.64, -49.31]
  , 'MA': [ -2.55, -44.30], 'MG': [-18.10, -44.38]
  , 'MS': [-20.51, -54.54], 'MT': [-12.64, -55.42]
  , 'PA': [ -5.53, -52.29], 'PB': [ -7.06, -35.55]
  , 'PE': [ -8.28, -35.07], 'PI': [ -8.28, -43.68]
  , 'PR': [-24.89, -51.55], 'RJ': [-22.84, -43.15]
  , 'RN': [ -5.22, -36.52], 'RO': [-11.22, -62.80]
  , 'RR': [  1.89, -61.22], 'RS': [-30.01, -51.22]
  , 'SC': [-27.33, -49.44], 'SE': [-10.90, -37.07]
  , 'SP': [-23.55, -46.64], 'TO': [-10.25, -48.25]}
    data = go.Data([
        go.Scattermapbox(
            lat = [(CoordenadasEstados[i][0]) for i in CoordenadasEstados.keys()],
            lon = [(CoordenadasEstados[i][1]) for i in CoordenadasEstados.keys()],
            mode = 'markers',
            marker = dict(
                size = 5,
                color = 'rgb(0,0,0)'
            ),
            text = [('Estado: %s<br>Qtde. de acidentes: %i' %(i, j)) for i, j in zip(CreateText(CoordenadasEstados.keys()), MortesEstados)],
            hoverinfo='text'
        )
    ])
    layout = go.Layout(
        autosize = False,
        width = width,
        height = height,
        title = go.layout.Title(
            text = 'Acidentes por estados de ' + Ano + ' por choropleth map'
        ),
        hovermode='closest',
        mapbox = dict(
            layers = [
                dict(
                    sourcetype = 'geojson',
                    source = SourceG[i],
                    type = 'fill',
                    color = Colors[i]
                ) for i in range(0, 27)
            ],
            accesstoken = mapbox_access_token,
            bearing=0,
            center=dict(
                lat = -20.00,
                lon = -40.00,
            ),
            pitch = 0,
            zoom = 3,
            style = 'light'
        ),
    )
    return go.Figure(data = data, layout = layout)

def TextScatterMap(df) :
    Id, Data, Dia, Hora, Uf, Br, Km, Municipio, CausaAcidente, TipoAcidente, FaseDia, Condicao = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list()
    TipoPista, TracadoPista, TipoVeiculo, MarcaVeiculo, AnoVeiculo, EstadoFisico, Idade, Sexo, Ilesos, FeridosLeves, FeridosGraves, Mortos = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list()
    for a,b,c,d,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,w in zip(df['id'],df['data_inversa'],df['dia_semana'],df['horario'],df['br'],df['km'],df['municipio'],df['causa_acidente']
    ,df['tipo_acidente'],df['fase_dia'],df['condicao_metereologica'],df['tipo_pista'],df['tracado_via'],df['tipo_veiculo'],df['marca'],df['ano_fabricacao_veiculo'],df['estado_fisico']
    ,df['idade'],df['sexo'],df['ilesos'],df['feridos_leves'],df['feridos_graves'],df['mortos']) :
        Id.append(str(a))
        Data.append(str(b))
        Dia.append(c)
        Hora.append(str(d))
        Br.append(str(f))
        Km.append(g)
        Municipio.append(h)
        CausaAcidente.append(i)
        TipoAcidente.append(j)
        FaseDia.append(k)
        Condicao.append(l)
        TipoPista.append(m)
        TracadoPista.append(n)
        MarcaVeiculo.append(p)
        AnoVeiculo.append(str(q))
        EstadoFisico.append(r)
        Idade.append(str(s))
        Sexo.append(t)
        if u == 0 :
            Ilesos.append('Não')
        else :
            Ilesos.append('Sim')
        if v == 0 :
            FeridosLeves.append('Não')
        else :
            FeridosLeves.append('Sim')
        if w == 0 :
            FeridosGraves.append('Não')
        else :
            FeridosGraves.append('Sim')
        if x == 0 :
            Mortos.append('Não')
        else :
            Mortos.append('Sim')
    Uf = CreateText(df['uf'])
    return ['Dados:<br>\rId: %s<br>\rData: %s<br>\rDia: %s<br>\rHora: %s<br>\rEstado: %s<br>\rBr: %s<br>\rKm: %s<br>\rMunicipio: %s<br>\rCausa do Acidente: %s<br>\rTipo do Acidente: %s<br>\rFase do dia: %s<br>\rCondição meteorológica: %s<br>\rTipo de pista: %s<br>\rTraçado da via: %s<br>\rTipo do veículo: %s<br>\rMarca: %s<br>\rAno de fabricação: %s<br>\rEstado físico: %s<br>\rIdade: %s<br>\rSexo: %s<br>\rIleso: %s<br>\rFerimento leve: %s<br>\rFerimento grave: %s<br>\rMorto: %s<br>\r'
        %(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,w)
        for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,w in zip(Id,Data,Dia,Hora,Uf,Br,Km,Municipio,CausaAcidente,TipoAcidente,FaseDia,Condicao,TipoPista,TracadoPista,TipoVeiculo,MarcaVeiculo,AnoVeiculo,EstadoFisico,Idade,Sexo,Ilesos,FeridosLeves,FeridosGraves,Mortos)]

def CreateScatterMap(df, WindowOpition, Ano) :
    if WindowOpition == 'MultiFigure' :
        width = 650
        height = 700
    elif WindowOpition == 'SingleFigure' :
        width = 1250
        height = 600
    elif WindowOpition == 'MultiFigure1' :
        width = 575
        height = 700
    data = go.Data([
        go.Scattermapbox(
            lat = df['latitude'],
            lon = df['longitude'],
            mode = 'markers',
            marker = go.scattermapbox.Marker(size = 8),
            text = TextScatterMap(df)
        )
    ])
    layout = go.Layout(
        autosize = False,
        width = width,
        height = height,
        title = 'Acidentes por coordenadas de ' + Ano,
        mapbox = go.layout.Mapbox(
            accesstoken = mapbox_access_token,
            bearing = 0,
            center = go.layout.mapbox.Center(
                lat = -20.00,
                lon = -40.00,
            ),
            zoom = 3,
            style = 'light'
        )
    )
    return go.Figure(data = data, layout = layout)

app.layout = html.Div([
    html.H1(children = '\n\nAcidentes nas rodovias\n\n\n\n', style = {'textAlign' : 'center'}),
    html.Div([
        html.Div([
            html.Label('Selecione um ano: '),
            dcc.Dropdown(
                id = 'years',
                options = [{'label': i, 'value': i} for i in Years]
            )
        ], className = 'six columns'),
        html.Div([
            html.Div(id = 'Label1'),
            dcc.Dropdown(id ='select_figure')
            ], className = 'six columns')
        ], className = 'row'),
        html.Div([
            html.Div(
                [
                    html.Div(id = 'figure01')
                ],
                className = 'six columns'
            ),
            html.Div(
                [
                    html.Div(id = 'figure02')
                ],
                className = 'six columns'
            ),
        ], className = 'row'),
        html.Div([
            html.Div(
                [
                    html.Div(id = 'figure11')
                ],
            ),
            html.Div(
                [
                    html.Div([html.Div(id = 'figure12')], style = {'textAlign' : 'center'})
                ]
            ),
        ]),
        html.Div([
            html.Div(
                [
                    html.Div(id = 'figure1')
                ],
                className = 'four columns'
            ),
            html.Div(
                [
                    html.Div(id = 'figure2')
                ],
                className = 'four columns'
            ),
            html.Div(
                [
                    html.Div(id = 'figure3')
                ],
                className = 'four columns'
            )
        ], className = 'row'),
        html.Div([
            html.Div(
                [
                    html.Div(id = 'figure4')
                ]
            ),
            html.Div(
                [
                    html.Div(id = 'figure5')
                ]
            ),
            html.Div(
                [
                    html.Div([html.Div(id = 'figure6')], style = {'textAlign' : 'center'})
                ]
            ),
            html.Div(
                [
                    html.Div([html.Div(id = 'figure7')], style = {'textAlign' : 'center'})
                ]
            ),
            html.Div(
                [
                    html.Div([html.Div(id = 'figure8')], style = {'textAlign' : 'center'})
                ]
            )
        ])
    ])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

@app.callback(
    [Output('Label1', 'children'),
    Output('select_figure', 'options')],
    [Input('years', 'value')])
def Dropdown2(Figure):
    return html.Label('Selecione uma opção: '), [{'label': i, 'value': i} for i in Figure_tips]

@app.callback(
    Output('figure1', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure(options, year) :
    if options == 'Acidentes por coordenadas' :
        if year == 'Todos' :
            df = pd.read_csv('Data/Csv-Files/newacidentes2019.csv')
            return dcc.Graph(
                figure = CreateScatterMap(df, 'MultiFigure', '2019')
            )
    elif options == 'Acidentes por estado' :
        if year == 'Todos' :
             return dcc.Graph(
                figure = CreateChoroplethMap('2019', 'MultiFigure1')
            )

@app.callback(
    Output('figure2', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure1(options, year) :
    if options == 'Acidentes por coordenadas' :
        if year == 'Todos' :
            df = pd.read_csv('Data/Csv-Files/newacidentes2018.csv')
            return dcc.Graph(
                figure = CreateScatterMap(df, 'MultiFigure', '2018')
            )
    elif options == 'Acidentes por estado' :
        if year == 'Todos' :
            return dcc.Graph(
                figure = CreateChoroplethMap('2018', 'MultiFigure1')
            )

@app.callback(
    Output('figure3', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure4(options, year) :
    if options == 'Acidentes por coordenadas' :
        if year == 'Todos' :
            df = pd.read_csv('Data/Csv-Files/newacidentes2017.csv')
            return dcc.Graph(
                figure = CreateScatterMap(df, 'SingleFigure', '2017')
            )
    elif options == 'Acidentes por estado' :
        if year == 'Todos' :
            return dcc.Graph(
                figure = CreateChoroplethMap('2017', 'MultiFigure1')
            )

@app.callback(
    Output('figure4', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure5(options, year) :
    if options == 'Acidentes por estado' :
        if year == 'Todos' :
            df1 = pd.read_csv('Data/Csv-Files/newacidentes2019.csv')
            df2 = pd.read_csv('Data/Csv-Files/newacidentes2018.csv')
            df3 = pd.read_csv('Data/Csv-Files/newacidentes2017.csv')
            return dcc.Graph(
                figure = CreateBarAllYears(df1, df2, df3, 'SingleFigure')
            )

@app.callback(
    Output('figure5', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure9(options, year) :
    if options == 'Acidentes por estado' :
        if year == 'Todos' :
            df1 = pd.read_csv('Data/Csv-Files/newacidentes2019.csv')
            df2 = pd.read_csv('Data/Csv-Files/newacidentes2018.csv')
            df3 = pd.read_csv('Data/Csv-Files/newacidentes2017.csv')
            return dcc.Graph(
                figure = CreatePieAllYears(df1,df2,df3, 'SingleFigure')
            )

@app.callback(
    Output('figure6', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure11(options, year) :
    if options == 'Acidentes por estado' :
        if year == 'Todos' :
            df1 = pd.read_csv('Data/Csv-Files/newacidentes2019.csv')
            Acidentes1 = len(df1)
            Mortes1 = len(df1[df1['mortos'] == 1])
            Ilesos1 = len(df1[df1['ilesos'] == 1])
            FeridosI1 = len(df1[df1['feridos_leves'] == 1])
            FeridosG1 = len(df1[df1['feridos_graves'] == 1])
            Total1 = Ilesos1 + FeridosG1 + FeridosI1
            return ('Ano: 2019 Total de acidentes: %i Total de mortes: %i Total de sobrevivente:\n\tilesos: %i\n\tferidos leves: %i\n\tferidos graves: %i\n\tTotal: %i' %(Acidentes1, Mortes1, Ilesos1, FeridosI1, FeridosG1, Total1))

@app.callback(
    Output('figure7', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure12(options, year) :
    if options == 'Acidentes por estado' :
        if year == 'Todos' :
            df2 = pd.read_csv('Data/Csv-Files/newacidentes2018.csv')
            Acidentes2 = len(df2)
            Mortes2 = len(df2[df2['mortos'] == 1])
            Ilesos2 = len(df2[df2['ilesos'] == 1])
            FeridosI2 = len(df2[df2['feridos_leves'] == 1])
            FeridosG2 = len(df2[df2['feridos_graves'] == 1])
            Total2 = Ilesos2 + FeridosG2 + FeridosI2
            return ('Ano: 2018 Total de acidentes: %i Total de mortes: %i Total de sobrevivente:\n\tilesos: %i\n\tferidos leves: %i\n\tferidos graves: %i\n\tTotal: %i' %(Acidentes2, Mortes2, Ilesos2, FeridosI2, FeridosG2, Total2))

@app.callback(
    Output('figure8', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure13(options, year) :
    if options == 'Acidentes por estado' :
        if year == 'Todos' :
            df3 = pd.read_csv('Data/Csv-Files/newacidentes2017.csv')
            Acidentes3 = len(df3)
            Mortes3 = len(df3[df3['mortos'] == 1])
            Ilesos3 = len(df3[df3['ilesos'] == 1])
            FeridosI3 = len(df3[df3['feridos_leves'] == 1])
            FeridosG3 = len(df3[df3['feridos_graves'] == 1])
            Total3 = Ilesos3 + FeridosG3 + FeridosI3
            return ('Ano: 2017 Total de acidentes: %i Total de mortes: %i Total de sobrevivente:\n\tilesos: %i\n\tferidos leves: %i\n\tferidos graves: %i\n\tTotal: %i' %(Acidentes3, Mortes3, Ilesos3, FeridosI3, FeridosG3, Total3))

@app.callback(
    Output('figure01', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure6(options, year) :
    if options == 'Acidentes por coordenadas' :
        if year == '2019' or year == '2018' or year == '2017' :
            df = pd.read_csv('Data/Csv-Files/newacidentes'+ year +'.csv')
            return dcc.Graph(
                figure = CreateScatterMap(df, 'SingleFigure', year)
            )
    elif options == 'Acidentes por estado' :
        if year == '2019' or year == '2018' or year == '2017' :
            return dcc.Graph(
                figure = CreateChoroplethMap(year, 'MultiFigure')
            )

@app.callback(
    Output('figure02', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure7(options, year) :
    if options == 'Acidentes por estado' :
        if year == '2019' or year == '2018' or year == '2017' :
            df = pd.read_csv('Data/Csv-Files/newacidentes'+ year +'.csv')
            return dcc.Graph(
                figure = CreateBar(df, year, 'MultiFigure')
            )

@app.callback(
    Output('figure11', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure8(options, year) :
    if options == 'Acidentes por estado' :
        if year == '2019' or year == '2018' or year == '2017' :
            df = pd.read_csv('Data/Csv-Files/newacidentes'+ year +'.csv')
            return dcc.Graph(
                figure = CreatePie(df, year, 'SingleFigure')
            )

@app.callback(
    Output('figure12', 'children'),
    [Input('select_figure', 'value'),
    Input('years', 'value')])
def show_figure10(options, year) :
    if options == 'Acidentes por estado' :
        if year == '2019' or year == '2018' or year == '2017' :
            df = pd.read_csv('Data/Csv-Files/newacidentes'+ year +'.csv')
            Acidentes = len(df)
            Mortes = len(df[df['mortos'] == 1])
            Ilesos = len(df[df['ilesos'] == 1])
            FeridosI = len(df[df['feridos_leves'] == 1])
            FeridosG = len(df[df['feridos_graves'] == 1])
            Total = Ilesos + FeridosG + FeridosI
            return ('Total de acidentes: %i Total de mortes: %i Total de sobrevivente:\n\tilesos: %i\n\tferidos leves: %i\n\tferidos graves: %i\n\tTotal: %i' %(Acidentes, Mortes, Ilesos, FeridosI, FeridosG, Total))

if __name__ == '__main__':
    app.run_server(debug = True)
