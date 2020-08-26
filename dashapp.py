{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-08-20T15:52:15.219025Z",
     "start_time": "2020-08-20T15:52:15.194026Z"
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import dash\n",
    "import dash_core_components as dcc\n",
    "import dash_html_components as html\n",
    "from dash.dependencies import Input, Output\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-08-21T00:21:58.817198Z",
     "start_time": "2020-08-21T00:20:05.348548Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    }
   ],
   "source": [
    "external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']\n",
    "\n",
    "app = dash.Dash(__name__, external_stylesheets=external_stylesheets)\n",
    "\n",
    "df = pd.read_csv('Game_of_Thrones_Script.csv')\n",
    "\n",
    "#gives list of all seasons to be used as buttons\n",
    "available_seasons = {'All': None,\n",
    "                    'Season 1': 'Season 1',\n",
    "                    'Season 2': 'Season 2',\n",
    "                    'Season 3': 'Season 3',\n",
    "                    'Season 4': 'Season 4',\n",
    "                    'Season 5': 'Season 5',\n",
    "                    'Season 6': 'Season 6',\n",
    "                    'Season 7': 'Season 7',\n",
    "                    'Season 8': 'Season 8'}\n",
    "\n",
    "app.layout = html.Div([\n",
    "   html.Div([\n",
    "    \n",
    "    dcc.Dropdown(\n",
    "    id='season_select',\n",
    "    options=[{'label': k, 'value': k} for k in available_seasons.keys()],\n",
    "    value='All'\n",
    "    ),\n",
    "    ]), \n",
    "    \n",
    "    dcc.Graph(id='season_plot')\n",
    "])\n",
    "\n",
    "@app.callback(\n",
    "    Output('season_plot', 'figure'),\n",
    "    [Input('season_select', 'value')])\n",
    "def update_graph(season):\n",
    "    if not season == 'All':\n",
    "        dfs = df[df['Season'] == season]\n",
    "        dfcount = dfs.Name.value_counts().reset_index(name=\"count\").query(\"count > 5\")[:25]\n",
    "        fig = px.bar(dfcount,\n",
    "            x = 'index',\n",
    "            y = 'count',\n",
    "            title = f'Top 25 Speaking Characters in {season}')\n",
    "        fig.update_xaxes(title='Character')\n",
    "        fig.update_yaxes(title='Number of Lines')\n",
    "        \n",
    "        return fig\n",
    "        \n",
    "    else:\n",
    "        dfcount = df.Name.value_counts().reset_index(name=\"count\").query(\"count > 5\")[:25]\n",
    "            \n",
    "        fig = px.bar(dfcount,\n",
    "            x = 'index',\n",
    "            y = 'count',\n",
    "            title = 'Top 25 Speaking Character Overall')\n",
    "        fig.update_xaxes(title='Character')\n",
    "        fig.update_yaxes(title='Number of Lines')\n",
    "    \n",
    "        return fig\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-08-20T15:19:17.749797Z",
     "start_time": "2020-08-20T15:19:17.746797Z"
    }
   },
   "outputs": [],
   "source": [
    "choice1 = 'Season 1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-08-20T15:22:19.646798Z",
     "start_time": "2020-08-20T15:22:19.640795Z"
    }
   },
   "outputs": [],
   "source": [
    "dfs = df[df['Season'] == choice1]\n",
    "eps = list(dfs['Episode'].unique())\n",
    "avail = [{k:k} for k in eps]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-08-20T15:22:23.400796Z",
     "start_time": "2020-08-20T15:22:23.395795Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'Episode 1': 'Episode 1'},\n",
       " {'Episode 2': 'Episode 2'},\n",
       " {'Episode 3': 'Episode 3'},\n",
       " {'Episode 4': 'Episode 4'},\n",
       " {'Episode 5': 'Episode 5'},\n",
       " {'Episode 6': 'Episode 6'},\n",
       " {'Episode 7': 'Episode 7'},\n",
       " {'Episode 8': 'Episode 8'},\n",
       " {'Episode 9': 'Episode 9'},\n",
       " {'Episode 10': 'Episode 10'}]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avail"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-08-20T16:03:02.707148Z",
     "start_time": "2020-08-20T16:03:02.475146Z"
    }
   },
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hoverlabel": {
          "namelength": 0
         },
         "hovertemplate": "index=%{x}<br>count=%{y}",
         "legendgroup": "",
         "marker": {
          "color": "#636efa"
         },
         "name": "",
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "tyrion lannister",
          "jon snow",
          "daenerys targaryen",
          "cersei lannister",
          "jaime lannister",
          "sansa stark",
          "arya stark",
          "davos",
          "theon greyjoy",
          "petyr baelish",
          "sam",
          "bran stark",
          "bronn",
          "man",
          "jorah mormont",
          "tywin lannister",
          "varys",
          "brienne",
          "eddard stark",
          "robb stark",
          "stannis baratheon",
          "catelyn stark",
          "ramsay bolton",
          "margaery tyrell",
          "joffrey lannister"
         ],
         "xaxis": "x",
         "y": [
          1760,
          1133,
          1048,
          1005,
          945,
          784,
          783,
          528,
          455,
          449,
          399,
          399,
          393,
          381,
          381,
          381,
          371,
          370,
          347,
          306,
          296,
          285,
          263,
          262,
          252
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "barmode": "relative",
        "height": 600,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          0.98
         ],
         "title": {
          "text": "index"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "count"
         }
        }
       }
      },
      "text/html": [
       "<div>\n",
       "        \n",
       "        \n",
       "            <div id=\"aa13315e-a3a9-473b-bd52-a98e7ac58e8c\" class=\"plotly-graph-div\" style=\"height:600px; width:100%;\"></div>\n",
       "            <script type=\"text/javascript\">\n",
       "                require([\"plotly\"], function(Plotly) {\n",
       "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    \n",
       "                if (document.getElementById(\"aa13315e-a3a9-473b-bd52-a98e7ac58e8c\")) {\n",
       "                    Plotly.newPlot(\n",
       "                        'aa13315e-a3a9-473b-bd52-a98e7ac58e8c',\n",
       "                        [{\"alignmentgroup\": \"True\", \"hoverlabel\": {\"namelength\": 0}, \"hovertemplate\": \"index=%{x}<br>count=%{y}\", \"legendgroup\": \"\", \"marker\": {\"color\": \"#636efa\"}, \"name\": \"\", \"offsetgroup\": \"\", \"orientation\": \"v\", \"showlegend\": false, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [\"tyrion lannister\", \"jon snow\", \"daenerys targaryen\", \"cersei lannister\", \"jaime lannister\", \"sansa stark\", \"arya stark\", \"davos\", \"theon greyjoy\", \"petyr baelish\", \"sam\", \"bran stark\", \"bronn\", \"man\", \"jorah mormont\", \"tywin lannister\", \"varys\", \"brienne\", \"eddard stark\", \"robb stark\", \"stannis baratheon\", \"catelyn stark\", \"ramsay bolton\", \"margaery tyrell\", \"joffrey lannister\"], \"xaxis\": \"x\", \"y\": [1760, 1133, 1048, 1005, 945, 784, 783, 528, 455, 449, 399, 399, 393, 381, 381, 381, 371, 370, 347, 306, 296, 285, 263, 262, 252], \"yaxis\": \"y\"}],\n",
       "                        {\"barmode\": \"relative\", \"height\": 600, \"legend\": {\"tracegroupgap\": 0}, \"margin\": {\"t\": 60}, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}, \"xaxis\": {\"anchor\": \"y\", \"domain\": [0.0, 0.98], \"title\": {\"text\": \"index\"}}, \"yaxis\": {\"anchor\": \"x\", \"domain\": [0.0, 1.0], \"title\": {\"text\": \"count\"}}},\n",
       "                        {\"responsive\": true}\n",
       "                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('aa13315e-a3a9-473b-bd52-a98e7ac58e8c');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })\n",
       "                };\n",
       "                });\n",
       "            </script>\n",
       "        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dfcount = df.Name.value_counts().reset_index(name=\"count\").query(\"count > 5\")[:25]\n",
    "fig = px.bar(dfcount,\n",
    "    x = 'index',\n",
    "    y = 'count')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-08-20T17:31:05.032005Z",
     "start_time": "2020-08-20T17:31:05.028007Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1.0.5'"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.__version__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-08-21T00:06:42.069386Z",
     "start_time": "2020-08-21T00:06:42.064382Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1.4.1'"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dash.__version__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-08-21T00:08:48.175858Z",
     "start_time": "2020-08-21T00:08:45.305857Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting gunicorn\n",
      "  Downloading https://files.pythonhosted.org/packages/69/ca/926f7cd3a2014b16870086b2d0fdc84a9e49473c68a8dff8b57f7c156f43/gunicorn-20.0.4-py2.py3-none-any.whl (77kB)\n",
      "Requirement already satisfied: setuptools>=3.0 in c:\\users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages (from gunicorn) (41.4.0)\n",
      "Installing collected packages: gunicorn\n",
      "Successfully installed gunicorn-20.0.4\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: Error checking for conflicts.\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_vendor\\pkg_resources\\__init__.py\", line 3012, in _dep_map\n",
      "    return self.__dep_map\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_vendor\\pkg_resources\\__init__.py\", line 2806, in __getattr__\n",
      "    raise AttributeError(attr)\n",
      "AttributeError: _DistInfoDistribution__dep_map\n",
      "\n",
      "During handling of the above exception, another exception occurred:\n",
      "\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_vendor\\pkg_resources\\__init__.py\", line 3003, in _parsed_pkg_info\n",
      "    return self._pkg_info\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_vendor\\pkg_resources\\__init__.py\", line 2806, in __getattr__\n",
      "    raise AttributeError(attr)\n",
      "AttributeError: _pkg_info\n",
      "\n",
      "During handling of the above exception, another exception occurred:\n",
      "\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_internal\\commands\\install.py\", line 517, in _warn_about_conflicts\n",
      "    package_set, _dep_info = check_install_conflicts(to_install)\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_internal\\operations\\check.py\", line 110, in check_install_conflicts\n",
      "    package_set, _ = create_package_set_from_installed()\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_internal\\operations\\check.py\", line 49, in create_package_set_from_installed\n",
      "    package_set[name] = PackageDetails(dist.version, dist.requires())\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_vendor\\pkg_resources\\__init__.py\", line 2727, in requires\n",
      "    dm = self._dep_map\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_vendor\\pkg_resources\\__init__.py\", line 3014, in _dep_map\n",
      "    self.__dep_map = self._compute_dependencies()\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_vendor\\pkg_resources\\__init__.py\", line 3023, in _compute_dependencies\n",
      "    for req in self._parsed_pkg_info.get_all('Requires-Dist') or []:\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_vendor\\pkg_resources\\__init__.py\", line 3005, in _parsed_pkg_info\n",
      "    metadata = self.get_metadata(self.PKG_INFO)\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_vendor\\pkg_resources\\__init__.py\", line 1419, in get_metadata\n",
      "    value = self._get(self._fn(self.egg_info, name))\n",
      "  File \"C:\\Users\\damni\\anaconda3\\envs\\learn-env\\lib\\site-packages\\pip\\_vendor\\pkg_resources\\__init__.py\", line 1607, in _get\n",
      "    with open(path, 'rb') as stream:\n",
      "FileNotFoundError: [Errno 2] No such file or directory: 'c:\\\\users\\\\damni\\\\anaconda3\\\\envs\\\\learn-env\\\\lib\\\\site-packages\\\\requests-2.24.0.dist-info\\\\METADATA'\n"
     ]
    }
   ],
   "source": [
    "pip install gunicorn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:learn-env] *",
   "language": "python",
   "name": "conda-env-learn-env-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
