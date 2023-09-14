import streamlit as st
import plotly.graph_objs as go
import pandas as pd


data = pd.read_csv('updated.csv') 




section = st.sidebar.radio("Choose a segment to process", ["Individual research", "Country profiling based on five indicators", "Multi-country indicator analysis"])

if section == "Individual research":
    st.title('Interactive Streamlit Dashboard with Plotly for Independent Research')
    Country = st.text_input('Enter a country name:')
    indicator = st.text_input('Enter an indicator name:')

    
    filtered_data = data[(data['Country Name'] == Country) & (data['Indicator Name'] == indicator)]

    if not filtered_data.empty:
        x_data = filtered_data.columns[2:]
        y_data = filtered_data.iloc[0, 2:]

       
        trace = go.Scatter(
            x=x_data,
            y=y_data,
            mode='lines+markers',
            marker=dict(color='blue', size=8),  
            line=dict(width=2, color='darkorange'),  
            text=x_data,
            hoverinfo='x+y',
        )

        layout = go.Layout(
            title=indicator,
            xaxis=dict(title='Years since 1990'),
            yaxis=dict(title=indicator),
            width=800,  
            height=600, 
            hovermode='x',
            xaxis_rangeslider_visible=True,
            plot_bgcolor='black',  
            paper_bgcolor='dimgray',
            font=dict(color='white')  
        )

        fig = go.Figure(data=[trace], layout=layout)

 
        st.plotly_chart(fig)
    



elif section == "Country profiling based on five indicators":
    updated = pd.read_csv('updated.csv')
    
    st.title('Multi-Indicator Country Evaluation using Streamlit and Plotly Visualizations')

    Country = st.text_input('Enter a country name:')
    indicators = []
    for i in range(1, 6):
        indicator = st.text_input(f'Enter Indicator {i}: ')
        indicators.append(indicator)


    figures = []

  
    for indicator in indicators:
        filtered_data = updated[(updated['Country Name'] == Country) & (updated['Indicator Name'] == indicator)]

        if not filtered_data.empty:
            fig = go.Figure()

            trace = go.Scatter(
                x=filtered_data.columns[2:],
                y=filtered_data.iloc[0, 2:],
                mode='lines',
                name=indicator
            )
            fig.add_trace(trace)

            fig.update_layout(
                title=f'{indicator} for {Country}',
                xaxis=dict(title='Years since 1990'),
                yaxis=dict(title='Value'),
                showlegend=True
            )

           
            figures.append(fig)
        


    for fig in figures:
        st.plotly_chart(fig)
    fig = go.Figure()
    
    for indicator in indicators:
        filtered_data = updated[(updated['Country Name'] == Country) & (updated['Indicator Name'] == indicator)]

        if not filtered_data.empty:
         
            fig.add_trace(
                go.Scatter(
                    x=filtered_data.columns[2:],
                    y=filtered_data.iloc[0, 2:],
                    mode='lines',
                    name=indicator,
                    line=dict(width=2)
                )
            )
        


    fig.update_layout(
        title=f'{Country} - {", ".join(indicators)}',
        xaxis=dict(title='Years since 1990'),
        yaxis=dict(title='Value'),
        showlegend=True,
        legend=dict(x=1, y=0.5) 
    )

  
    st.plotly_chart(fig)



elif section == "Multi-country indicator analysis":
    updated = pd.read_csv('updated.csv')  
    
    st.title('Multi-Country Metric Evaluation through Streamlit with Interactive Plotly')
    indicator = st.text_input('Enter a Indicator name:')

    countrys = []
    for i in range(1, 6):
        country = st.text_input(f'Enter Country {i}: ')
        countrys.append(country)


    for country in countrys:
        filtered_data = updated[(updated['Country Name'] == country) & (updated['Indicator Name'] == indicator)]

        if not filtered_data.empty:
            fig = go.Figure()
            trace = go.Scatter(
                x=filtered_data.columns[2:],
                y=filtered_data.iloc[0, 2:],
                mode='lines',
                name=country
            )
            fig.add_trace(trace)

            fig.update_layout(
                title=f'{country} for {indicator}',
                xaxis=dict(title='Years since 1990'),
                yaxis=dict(title='Value'),
                showlegend=True
            )

            st.plotly_chart(fig)

       

    fig = go.Figure()

    for country in countrys:
        filtered_data = updated[(updated['Country Name'] == country) & (updated['Indicator Name'] == indicator)]

        if not filtered_data.empty:

            fig.add_trace(
                go.Scatter(
                    x=filtered_data.columns[2:],
                    y=filtered_data.iloc[0, 2:],
                    mode='lines',
                    name=country,
                    line=dict(width=2)
                )
            )
        


    fig.update_layout(
        title=f'{indicator} - {"".join(country)}',
        xaxis=dict(title='Years since 1990'),
        yaxis=dict(title='Value'),
        showlegend=True,
        legend=dict(x=1, y=0.5)  
    )


    st.plotly_chart(fig)

