import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Step 1: Load CSV data and preprocess it
data = pd.read_csv('Day_Ahead_Actual_Load.csv')
data["Time (CET/CEST)"] = data["Time (CET/CEST)"].str.extract(r"(\d{2}:\d{2})")
df = pd.DataFrame(data)

# Step 2: Create the Streamlit app
def main():
    st.title("Day-Ahead Total Load Forecast vs Actual Total Load")
    st.sidebar.title("Graph Selection")

    graph_selection = st.sidebar.radio("Select a graph:", ("Day-Ahead vs Actual Line Plot", "Day-Ahead Scatter Plot", "Actual Scatter Plot", "Both Scatter Plots"))

    if graph_selection == "Day-Ahead vs Actual Line Plot":
        display_line_plot()
    elif graph_selection == "Day-Ahead Scatter Plot":
        display_day_ahead_scatter_plot()
    elif graph_selection == "Actual Scatter Plot":
        display_actual_scatter_plot()
    else:
        display_both_scatter_plots()

# Step 3: Display Day-Ahead vs Actual Line Plot
def display_line_plot():
    fig = go.Figure()

    x = df["Time (CET/CEST)"]
    y_day_ahead = df["Day-ahead Total Load Forecast [MW] - BZN|BE"]
    y_actual = df["Actual Total Load [MW] - BZN|BE"]

    fig.add_trace(go.Scatter(x=x, y=y_day_ahead, mode='lines', line=dict(color='yellow', width=2), name='Day-ahead Forecast'))
    fig.add_trace(go.Scatter(x=x, y=y_actual, mode='lines', line=dict(color='blue', width=2), name='Actual Load'))

    fig.update_layout(title="Day-Ahead Total Load Forecast vs Actual Total Load",
                      xaxis_title="Time",
                      yaxis_title="Total Load [MW]",
                      xaxis=dict(tickangle=-45),
                      legend=dict(x=0.05, y=0.98),
                      margin=dict(l=50, r=20, t=60, b=20))

    st.plotly_chart(fig)

# Step 4: Display Day-Ahead Scatter Plot
def display_day_ahead_scatter_plot():
    fig = go.Figure()

    x = df["Time (CET/CEST)"]
    y = df["Day-ahead Total Load Forecast [MW] - BZN|BE"]

    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='blue'), name='Day-ahead Forecast'))

    fig.update_layout(title="Scatter Plot: Day-Ahead Total Load Forecast",
                      xaxis_title="Time",
                      yaxis_title="Day-Ahead Total Load",
                      xaxis=dict(tickangle=-45))

    st.plotly_chart(fig)

# Step 5: Display Actual Scatter Plot
def display_actual_scatter_plot():
    fig = go.Figure()

    x = df["Time (CET/CEST)"]
    y = df["Actual Total Load [MW] - BZN|BE"]

    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='green'), name='Total Actual Forecast'))

    fig.update_layout(title="Scatter Plot: Actual Total Load Forecast",
                      xaxis_title="Time",
                      yaxis_title="Actual Total Load",
                      xaxis=dict(tickangle=-45))

    st.plotly_chart(fig)

# Step 6: Display Both Scatter Plots
def display_both_scatter_plots():
    fig = go.Figure()

    x = df["Time (CET/CEST)"]
    y_actual = df["Actual Total Load [MW] - BZN|BE"]
    y_forecast = df["Day-ahead Total Load Forecast [MW] - BZN|BE"]

    fig.add_trace(go.Scatter(x=x, y=y_actual, mode='markers', marker=dict(color='red'), name='Actual Load'))
    fig.add_trace(go.Scatter(x=x, y=y_forecast, mode='markers', marker=dict(color='blue'), name='Day-ahead Forecast'))

    fig.update_layout(title="Day-Ahead Total Load vs Actual Total Load",
                      xaxis_title="Time",
                      yaxis_title="Total Load",
                      xaxis=dict(tickangle=-45),
                      legend=dict(x=0.05, y=0.98, bgcolor='rgba(255,255,255,0.5)'),
                      margin=dict(l=50, r=20, t=60, b=20))

    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
