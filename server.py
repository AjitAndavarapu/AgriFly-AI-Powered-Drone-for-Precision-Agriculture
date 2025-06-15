# from flask import Flask, render_template
# import sqlite3
# import pandas as pd
# import plotly.express as px
# import plotly.io as pio

# # Initialize the Flask app
# app = Flask(__name__)

# # Database connection function
# def get_data_from_db():
#     conn = sqlite3.connect('plant_disease_data.db')
#     query = "SELECT * FROM plant_disease_data"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df

# # Helper function to map disease stages to numerical values for progress visualization
# def map_disease_stages(disease):
#     stage_mapping = {
#         'Healthy': 0,
#         'Mild': 1,
#         'Moderate': 2,
#         'Severe': 3
#     }
#     return stage_mapping.get(disease, -1)  # Default to -1 if unknown

# # Route to the dashboard
# @app.route('/')
# def dashboard():
#     # Get data from the database
#     df = get_data_from_db()

#     # ---- Visualization 1: Disease Distribution (Pie Chart) ---- #
#     healthy_count = df[df['disease'] == 'Healthy'].shape[0]
#     unhealthy_count = df[df['disease'] != 'Healthy'].shape[0]
    
#     pie_chart_data = {
#         'labels': ['Healthy', 'Diseased'],
#         'values': [healthy_count, unhealthy_count],
#     }
    
#     pie_chart = px.pie(
#         names=pie_chart_data['labels'],
#         values=pie_chart_data['values'],
#         title='Healthy vs Diseased Plants'
#     )

#     # ---- Visualization 2: Bar Chart of Disease Count ---- #
#     disease_counts = df['disease'].value_counts()
#     bar_chart = px.bar(disease_counts, x=disease_counts.index, y=disease_counts.values,
#                        labels={'x': 'Disease', 'y': 'Count'},
#                        title='Count of Each Disease')

#     # ---- Visualization 3: Disease Occurrences Over Time (Line Chart) ---- #
#     df['date'] = pd.to_datetime(df['date'])
#     disease_over_time = px.line(df, x='date', y='disease', markers=True, title='Disease Occurrences Over Time')

#     # ---- Visualization 4: Health Progress Per Plant ---- #
#     plant_ids = df['plant_id'].unique()  # Get unique plant IDs
#     plant_graphs = {}

#     # For each plant, create a line chart showing its health progress over time
#     for plant_id in plant_ids:
#         plant_df = df[df['plant_id'] == plant_id].sort_values(by='date')  # Filter by plant ID and sort by date

#         # Create a new column 'health_stage' to map the disease stage
#         plant_df['health_stage'] = plant_df['disease'].apply(map_disease_stages)

#         # Line chart for each plant's health progress over time
#         plant_chart = px.line(plant_df, x='date', y='health_stage',
#                               title=f'Health/Damage Progress for Plant ID: {plant_id}',
#                               labels={'health_stage': 'Health Stage (0=Healthy, 3=Severe)', 'date': 'Date'},
#                               markers=True)

#         # Add this chart to the dictionary of plant graphs
#         plant_graphs[plant_id] = pio.to_html(plant_chart, full_html=False)

#     # ---- Data Table: Convert DataFrame to HTML Table ---- #
#     # Create a table showing plant ID, disease, and the most recent health stage
#     latest_status_df = df.sort_values(by='date').drop_duplicates(subset=['plant_id'], keep='last')
#     table_html = latest_status_df[['plant_id', 'disease', 'date']].to_html(classes='table table-striped', index=False)

#     # Convert Plotly graphs to HTML for rendering in the template
#     pie_chart_html = pio.to_html(pie_chart, full_html=False)
#     bar_chart_html = pio.to_html(bar_chart, full_html=False)
#     line_chart_html = pio.to_html(disease_over_time, full_html=False)

#     # Render the HTML template with the plots and individual plant graphs
#     return render_template(
#         'dashboard.html',
#         pie_chart=pie_chart_html,
#         bar_chart=bar_chart_html,
#         line_chart=line_chart_html,
#         plant_graphs=plant_graphs,  # Dictionary of graphs for each plant
#         table_html=table_html
#     )

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request
# import sqlite3
# import pandas as pd
# import plotly.express as px
# import plotly.io as pio

# # Initialize the Flask app
# app = Flask(__name__)

# # Database connection function
# def get_data_from_db():
#     conn = sqlite3.connect('plant_disease_data.db')
#     query = "SELECT * FROM plant_disease_data"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df

# # Helper function to map disease stages to numerical values for health progress visualization
# def map_disease_stages(disease):
#     stage_mapping = {
#         'Healthy': 0,
#         'Mild': 1,
#         'Moderate': 2,
#         'Severe': 3
#     }
#     return stage_mapping.get(disease, -1)

# # Route to the dashboard
# @app.route('/', methods=['GET', 'POST'])
# def dashboard():
#     # Get data from the database
#     df = get_data_from_db()

#     # ---- Visualization 1: Disease Distribution (Pie Chart) ---- #
#     healthy_count = df[df['disease'] == 'Apple___healthy'].shape[0]
#     unhealthy_count = df[df['disease'] != 'Healthy'].shape[0]
    
#     pie_chart_data = {
#         'labels': ['Healthy', 'Diseased'],
#         'values': [healthy_count, unhealthy_count],
#     }
    
#     pie_chart = px.pie(
#         names=pie_chart_data['labels'],
#         values=pie_chart_data['values'],
#         title='Healthy vs Diseased Plants'
#     )

#     # ---- Visualization 2: Bar Chart of Disease Count ---- #
#     disease_counts = df['disease'].value_counts()
#     bar_chart = px.bar(disease_counts, x=disease_counts.index, y=disease_counts.values,
#                        labels={'x': 'Disease', 'y': 'Count'},
#                        title='Count of Each Disease')

#     # ---- Visualization 3: Disease Occurrences Over Time (Line Chart) ---- #
#     df['date'] = pd.to_datetime(df['date'])
#     disease_over_time = px.line(df, x='date', y='disease', markers=True, title='Disease Occurrences Over Time')

#     # ---- Visualization 4: Health Progress for First 5 Plants ---- #
#     plant_ids = df['plant_id'].unique()[:5]  # Limit to first 5 plants for display
#     plant_graphs = {}

#     for plant_id in plant_ids:
#         plant_df = df[df['plant_id'] == plant_id].sort_values(by='date')
#         plant_df['health_stage'] = plant_df['disease'].apply(map_disease_stages)
#         plant_chart = px.line(plant_df, x='date', y='health_stage',
#                               title=f'Health Progress for Plant ID: {plant_id}',
#                               labels={'health_stage': 'Health Stage (0=Healthy, 3=Severe)', 'date': 'Date'},
#                               markers=True)
#         plant_graphs[plant_id] = pio.to_html(plant_chart, full_html=False)

#     # ---- Search Feature for Specific Plants ---- #
#     search_query = request.form.get('search')
#     search_results = None

#     if search_query:
#         search_results = df[df['plant_id'].astype(str) == search_query]
#         if not search_results.empty:
#             search_results['health_stage'] = search_results['disease'].apply(map_disease_stages)
#             search_chart = px.line(search_results, x='date', y='health_stage',
#                                    title=f'Health Progress for Plant ID: {search_query}',
#                                    labels={'health_stage': 'Health Stage (0=Healthy, 3=Severe)', 'date': 'Date'},
#                                    markers=True)
#             search_graph_html = pio.to_html(search_chart, full_html=False)
#         else:
#             search_graph_html = "<p>No data found for the specified plant ID.</p>"

#     # Convert Plotly graphs to HTML for rendering in the template
#     pie_chart_html = pio.to_html(pie_chart, full_html=False)
#     bar_chart_html = pio.to_html(bar_chart, full_html=False)
#     line_chart_html = pio.to_html(disease_over_time, full_html=False)

#     # Render the HTML template with the plots, individual plant graphs, and search results
#     return render_template(
#         'dashboard.html',
#         pie_chart=pie_chart_html,
#         bar_chart=bar_chart_html,
#         line_chart=line_chart_html,
#         plant_graphs=plant_graphs,  # Dictionary of graphs for each plant
#         search_query=search_query,
#         search_graph_html=search_graph_html if search_query else None
#     )

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)




#stable version

# from flask import Flask, render_template, request
# import sqlite3
# import pandas as pd
# import plotly.express as px
# import plotly.io as pio
# import plotly.graph_objects as go

# # Initialize the Flask app
# app = Flask(__name__)

# # Database connection function
# def get_data_from_db():
#     conn = sqlite3.connect('plant_disease_data.db')
#     query = "SELECT * FROM plant_disease_data"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df

# # Helper function to map disease stages to numerical values for health progress visualization
# def map_disease_stages(disease):
#     stage_mapping = {
#         'Apple___healthy': 0,
#         'Apple___Apple_scab': 1,
#         'Apple___Cedar_apple_rust': 2,
#         'Apple___Black_rot': 3
#     }
#     return stage_mapping.get(disease, -1)

# # Route to the dashboard
# @app.route('/', methods=['GET', 'POST'])
# def dashboard():
#     # Get data from the database
#     df = get_data_from_db()

#     # ---- Visualization 1: Disease Distribution (Pie Chart) ---- #
#     healthy_count = df[df['disease'] == 'Apple___healthy'].shape[0]
#     unhealthy_count = df[df['disease'] != 'Apple___healthy'].shape[0]
    
#     pie_chart_data = {
#         'labels': ['Healthy', 'Diseased'],
#         'values': [healthy_count, unhealthy_count],
#     }
    
#     pie_chart = px.pie(
#         names=pie_chart_data['labels'],
#         values=pie_chart_data['values'],
#         title='Healthy vs Diseased Plants'
#     )

#     # ---- Visualization 2: Bar Chart of Disease Count ---- #
#     disease_counts = df['disease'].value_counts()
#     bar_chart = px.bar(disease_counts, x=disease_counts.index, y=disease_counts.values,
#                        labels={'x': 'Disease', 'y': 'Count'},
#                        title='Count of Each Disease')

#     # # ---- Visualization 3: Disease Occurrences Over Time (Line Chart) ---- #
#     # # Convert 'date' column to datetime format
#     df['date'] = pd.to_datetime(df['date'])
#     # Count the number of diseases per day
#     disease_over_time_df = df.groupby('date').size().reset_index(name='disease_count')
    
#     disease_over_time = px.line(disease_over_time_df, x='date', y='disease_count',
#                                 markers=True, title='Disease Occurrences Over Time',
#                                 labels={'disease_count': 'Number of Occurrences', 'date': 'Date'})

#     # # ---- Visualization 4: Health Progress for First 5 Plants ---- #
#     # plant_ids = df['plant_id'].unique()[:5]  # Limit to first 5 plants for display
#     # plant_graphs = {}

#     # for plant_id in plant_ids:
#     #     plant_df = df[df['plant_id'] == plant_id].sort_values(by='date')
#     #     plant_df['health_stage'] = plant_df['disease'].apply(map_disease_stages)
        
#     #     # Filter out invalid stages (-1) if they exist
#     #     plant_df = plant_df[plant_df['health_stage'] >= 0]
        
#     #     plant_chart = px.line(plant_df, x='date', y='health_stage',
#     #                           title=f'Health Progress for Plant ID: {plant_id}',
#     #                           labels={'health_stage': 'Health Stage (0=Healthy, 3=Severe)', 'date': 'Date'},
#     #                           markers=True)
#     #     plant_graphs[plant_id] = pio.to_html(plant_chart, full_html=False)

#     # ---- Visualization 4: Health Progress for First 5 Plants with Bar Chart and Arrow ---- #
#     plant_ids = df['plant_id'].unique()[:5]  # Limit to first 5 plants for display
#     plant_graphs = {}

#     for plant_id in plant_ids:
#         # Filter and sort data for the specific plant
#         plant_df = df[df['plant_id'] == plant_id].sort_values(by='date')
#         plant_df['health_stage'] = plant_df['disease'].apply(map_disease_stages)

#         # Filter out invalid stages (-1) if they exist
#         plant_df = plant_df[plant_df['health_stage'] >= 0]

#         # Create a bar chart for health progress over time
#         plant_chart = go.Figure()

#         # Add bar trace
#         plant_chart.add_trace(go.Bar(
#             x=plant_df['date'], 
#             y=plant_df['health_stage'], 
#             text=plant_df['disease'],  # Show disease names on hover
#             marker=dict(color=plant_df['health_stage'], colorscale='Viridis'),  # Color based on severity
#             name=f'Plant {plant_id}'
#         ))

#         # Add arrows indicating health progression between stages
#         for i in range(1, len(plant_df)):
#             plant_chart.add_annotation(
#                 dict(
#                     x=plant_df['date'].iloc[i],
#                     y=plant_df['health_stage'].iloc[i],
#                     ax=plant_df['date'].iloc[i - 1],
#                     ay=plant_df['health_stage'].iloc[i - 1],
#                     xref='x',
#                     yref='y',
#                     axref='x',
#                     ayref='y',
#                     showarrow=True,
#                     arrowhead=3,
#                     arrowsize=1,
#                     arrowwidth=2,
#                     arrowcolor="red"
#                 )
#             )

#         # Customize the layout
#         plant_chart.update_layout(
#             title=f'Health Progress for Plant ID: {plant_id}',
#             xaxis_title='Date',
#             yaxis_title='Health Stage (0=Healthy, 3=Severe)',
#             yaxis=dict(tickvals=[0, 1, 2, 3], ticktext=['Healthy', 'Apple Scab', 'Cedar Apple Rust', 'Black Rot']),
#             showlegend=False,
#             height=400
#         )

#         # Store the chart in the plant_graphs dictionary
#         plant_graphs[plant_id] = pio.to_html(plant_chart, full_html=False)



#     # ---- Search Feature for Specific Plants ---- #
#     search_query = request.form.get('search')
#     search_results = None

#     if search_query:
#         search_results = df[df['plant_id'].astype(str) == search_query]
#         if not search_results.empty:
#             search_results['health_stage'] = search_results['disease'].apply(map_disease_stages)
#             search_results = search_results[search_results['health_stage'] >= 0]  # Filter out invalid stages
#             search_chart = px.line(search_results, x='date', y='health_stage',
#                                    title=f'Health Progress for Plant ID: {search_query}',
#                                    labels={'health_stage': 'Health Stage (0=Healthy, 3=Severe)', 'date': 'Date'},
#                                    markers=True)
#             search_graph_html = pio.to_html(search_chart, full_html=False)
#         else:
#             search_graph_html = "<p>No data found for the specified plant ID.</p>"

#     # ---- Visualization 5: Correlation Heatmap (New Visualization) ---- #
#     # Encode disease stages numerically for heatmap
#     df['health_stage'] = df['disease'].apply(map_disease_stages)
#     correlation_matrix = df[['plant_id', 'health_stage', 'date']].corr()  # Use the relevant columns for correlation

#     heatmap = px.imshow(correlation_matrix,
#                         title='Correlation Heatmap',
#                         labels=dict(color='Correlation'),
#                         x=['Plant ID', 'Health Stage', 'Date'],
#                         y=['Plant ID', 'Health Stage', 'Date'])

#     # Convert Plotly graphs to HTML for rendering in the template
#     pie_chart_html = pio.to_html(pie_chart, full_html=False)
#     bar_chart_html = pio.to_html(bar_chart, full_html=False)
#     line_chart_html = pio.to_html(disease_over_time, full_html=False)
#     heatmap_html = pio.to_html(heatmap, full_html=False)

#     # Render the HTML template with the plots, individual plant graphs, and search results
#     return render_template(
#         'dashboard.html',
#         pie_chart=pie_chart_html,
#         bar_chart=bar_chart_html,
#        line_chart=line_chart_html,
#         plant_graphs=plant_graphs,  # Dictionary of graphs for each plant
#         search_query=search_query,
#         search_graph_html=search_graph_html if search_query else None,
#       heatmap=heatmap_html  # Add the heatmap to the template
#     )

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)


# #better version
from flask import Flask, render_template, request
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

# # Initialize the Flask app
app = Flask(__name__)

# Database connection function
def get_data_from_db():
    conn = sqlite3.connect('plant_disease_data.db')
    query = "SELECT * FROM plant_disease_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Helper function to map disease stages to numerical values for health progress visualization
def map_disease_stages(disease):
    stage_mapping = {
        'Apple___healthy': 0,
        'Apple___Apple_scab': 1,
        'Apple___Cedar_apple_rust': 2,
        'Apple___Black_rot': 3
    }
    return stage_mapping.get(disease, -1)

# Route to the dashboard
@app.route('/', methods=['GET', 'POST'])
def dashboard():
    # Get data from the database
    df = get_data_from_db()

    # ---- Visualization 1: Disease Distribution (Pie Chart) ---- #
    healthy_count = df[df['disease'] == 'Apple___healthy'].shape[0]
    unhealthy_count = df[df['disease'] != 'Apple___healthy'].shape[0]
    
    pie_chart_data = {
        'labels': ['Healthy', 'Diseased'],
        'values': [healthy_count, unhealthy_count],
    }
    
    pie_chart = px.pie(
        names=pie_chart_data['labels'],
        values=pie_chart_data['values'],
        title='Healthy vs Diseased Plants'
    )

    # ---- Visualization 2: Bar Chart of Disease Count ---- #
    disease_counts = df['disease'].value_counts()
    bar_chart = px.bar(disease_counts, x=disease_counts.index, y=disease_counts.values,
                       labels={'x': 'Disease', 'y': 'Count'},
                       title='Count of Each Disease')

    # ---- Visualization 4: Health Progress for First 5 Plants with Bar Chart and Arrow ---- #
    #plant_ids = df['plant_id'].unique()[3:9]  # Limit to first 5 plants for display
    plant_ids = df['plant_id'].unique()[4:9] 
    plant_graphs = {}

    for plant_id in plant_ids:
        # Filter and sort data for the specific plant
        plant_df = df[df['plant_id'] == plant_id].sort_values(by='date')
        plant_df['date'] = pd.to_datetime(plant_df['date'])  # Ensure 'date' column is in datetime format
        plant_df['health_stage'] = plant_df['disease'].apply(map_disease_stages)

        # Filter out invalid stages (-1) if they exist
        plant_df = plant_df[plant_df['health_stage'] >= 0]

        # Create a bar chart for health progress over time
        plant_chart = go.Figure()

        # Add bar trace
        plant_chart.add_trace(go.Bar(
            x=plant_df['date'], 
            y=plant_df['health_stage'], 
            text=plant_df['disease'],  # Show disease names on hover
            marker=dict(color=plant_df['health_stage'], colorscale='Viridis'),  # Color based on severity
            name=f'Plant {plant_id}'
        ))

        # Add arrows indicating health progression between stages
        for i in range(1, len(plant_df)):
            plant_chart.add_annotation(
                dict(
                    x=plant_df['date'].iloc[i],
                    y=plant_df['health_stage'].iloc[i],
                    ax=plant_df['date'].iloc[i - 1],
                    ay=plant_df['health_stage'].iloc[i - 1],
                    xref='x',
                    yref='y',
                    axref='x',
                    ayref='y',
                    showarrow=True,
                    arrowhead=3,
                    arrowsize=1,
                    arrowwidth=2,
                    arrowcolor="red"
                )
            )

        # Customize the layout
        plant_chart.update_layout(
            title=f'Health Progress for Plant ID: {plant_id}',
            xaxis_title='Date',
            yaxis_title='Health Stage (0=Healthy, 3=Severe)',
            yaxis=dict(tickvals=[0, 1, 2, 3], ticktext=['Healthy', 'Apple Scab', 'Cedar Apple Rust', 'Black Rot']),
            showlegend=False,
            height=400
        )

        # Store the chart in the plant_graphs dictionary
        plant_graphs[plant_id] = pio.to_html(plant_chart, full_html=False)

    # ---- Search Feature for Specific Plants ---- #
    search_query = request.form.get('search')
    search_graph_html = None  # Initialize search graph variable

    if search_query:
        search_results = df[df['plant_id'].astype(str) == search_query]
        if not search_results.empty:
            search_results['date'] = pd.to_datetime(search_results['date'])  # Ensure 'date' is in datetime format
            search_results['health_stage'] = search_results['disease'].apply(map_disease_stages)
            search_results = search_results[search_results['health_stage'] >= 0]  # Filter out invalid stages
            
            # Create a bar chart for the searched plant's health progress over time (same as Visualization 4)
            search_chart = go.Figure()

            search_chart.add_trace(go.Bar(
                x=search_results['date'], 
                y=search_results['health_stage'], 
                text=search_results['disease'],  # Show disease names on hover
                marker=dict(color=search_results['health_stage'], colorscale='Viridis'),  # Color based on severity
                name=f'Plant {search_query}'
            ))

            for i in range(1, len(search_results)):
                search_chart.add_annotation(
                    dict(
                        x=search_results['date'].iloc[i],
                        y=search_results['health_stage'].iloc[i],
                        ax=search_results['date'].iloc[i - 1],
                        ay=search_results['health_stage'].iloc[i - 1],
                        xref='x',
                        yref='y',
                        axref='x',
                        ayref='y',
                        showarrow=True,
                        arrowhead=3,
                        arrowsize=1,
                        arrowwidth=2,
                        arrowcolor="red"
                    )
                )

            search_chart.update_layout(
                title=f'Health Progress for Plant ID: {search_query}',
                xaxis_title='Date',
                yaxis_title='Health Stage (0=Healthy, 3=Severe)',
                yaxis=dict(tickvals=[0, 1, 2, 3], ticktext=['Healthy', 'Apple Scab', 'Cedar Apple Rust', 'Black Rot']),
                showlegend=False,
                height=400
            )
            
            search_graph_html = pio.to_html(search_chart, full_html=False)
        else:
            search_graph_html = "<p>No data found for the specified plant ID.</p>"

    # ---- Visualization 5: Correlation Heatmap (New Visualization) ---- #
    # Encode disease stages numerically for heatmap
    df['health_stage'] = df['disease'].apply(map_disease_stages)
    
    # Only include numeric columns for correlation matrix
    correlation_matrix = df[['plant_id', 'health_stage']].corr()

    heatmap = px.imshow(correlation_matrix,
                        title='Correlation Heatmap',
                        labels=dict(color='Correlation'),
                        x=['Plant ID', 'Health Stage'],
                        y=['Plant ID', 'Health Stage'])

    # Convert Plotly graphs to HTML for rendering in the template
    pie_chart_html = pio.to_html(pie_chart, full_html=False)
    bar_chart_html = pio.to_html(bar_chart, full_html=False)
    heatmap_html = pio.to_html(heatmap, full_html=False)

    
    # ---- Display all the data in a table ---- #
    # Convert the dataframe to HTML table format for rendering
    # table_html = df.to_html(classes='table table-striped', index=False)
    # Filter out plant_id 4 data
   # Python code to filter the DataFrame based on plant_id != "4" and prepare data for disease filtering
    df_filtered = df[df['plant_id'] != "4"]

    # Convert the filtered DataFrame to HTML with default table
    table_html = df_filtered.to_html(classes='table table-striped', index=False)

    # Render the HTML template with the plots, individual plant graphs, and search results
    return render_template(
        'dashboard2.html',
        pie_chart=pie_chart_html,
        bar_chart=bar_chart_html,
        plant_graphs=plant_graphs,  # Dictionary of graphs for each plant
        search_query=search_query,
        search_graph_html=search_graph_html,
        heatmap=heatmap_html, 
        table_html=table_html
    )

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)




