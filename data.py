import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])  
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    return None

def plot_graphs(df, graph_type, x_col, y_col, hue_col):
    if graph_type == "Line Chart":
        fig = px.line(df, x=x_col, y=y_col, color=hue_col)
    elif graph_type == "Bar Chart":
        fig = px.bar(df, x=x_col, y=y_col, color=hue_col, barmode="group")
    elif graph_type == "Histogram":
        fig = px.histogram(df, x=x_col, color=hue_col)
    elif graph_type == "Box Plot":
        fig = px.box(df, x=x_col, y=y_col, color=hue_col)
    elif graph_type == "Scatter Plot":
        fig = px.scatter(df, x=x_col, y=y_col, color=hue_col)
    elif graph_type == "Pie Chart":
        fig = px.pie(df, names=x_col, values=y_col)
    elif graph_type == "Heatmap":
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        st.pyplot(plt)
        return
    elif graph_type == "Violin Plot":
        fig = px.violin(df, x=x_col, y=y_col, color=hue_col, box=True)
    elif graph_type == "Density Contour":
        fig = px.density_contour(df, x=x_col, y=y_col)
    elif graph_type == "Bubble Chart":
        fig = px.scatter(df, x=x_col, y=y_col, size=y_col, color=hue_col)
    elif graph_type == "Funnel Chart":
        fig = px.funnel(df, x=x_col, y=y_col)
    elif graph_type == "Radar Chart":
        fig = px.line_polar(df, r=y_col, theta=x_col, line_close=True)
    elif graph_type == "TreeMap":
        fig = px.treemap(df, path=[x_col], values=y_col)
    elif graph_type == "Sunburst Chart":
        fig = px.sunburst(df, path=[x_col, hue_col], values=y_col)
    elif graph_type == "Strip Plot":
        fig = px.strip(df, x=x_col, y=y_col, color=hue_col)
    elif graph_type == "ECDF":
        fig = px.ecdf(df, x=x_col)
    elif graph_type == "3D Scatter":
        fig = px.scatter_3d(df, x=x_col, y=y_col, z=df.columns[2], color=hue_col)
    elif graph_type == "Area Chart":
        fig = px.area(df, x=x_col, y=y_col, color=hue_col)
    else:
        st.error("Invalid Graph Type")
        return
    st.plotly_chart(fig)

def main():
    st.title("Dataset Visualizer with 19 Graphs")
    df = load_data()
    if df is not None:
        st.write("Dataset Preview:", df.head())
        graph_types = ["Line Chart", "Bar Chart", "Histogram", "Box Plot", "Scatter Plot", "Pie Chart", 
                       "Heatmap", "Violin Plot", "Density Contour", "Bubble Chart", "Funnel Chart", "Radar Chart", 
                       "TreeMap", "Sunburst Chart", "Strip Plot", "ECDF", "3D Scatter", "Area Chart"]
        graph_type = st.selectbox("Select Graph Type", graph_types)
        x_col = st.selectbox("Select X-axis Column", df.columns)
        y_col = st.selectbox("Select Y-axis Column", df.columns)
        hue_col = st.selectbox("Select Category Column (Optional)", [None] + list(df.columns))
        if st.button("Generate Graph"):
            plot_graphs(df, graph_type, x_col, y_col, hue_col)
    else:
        st.info("Please upload a dataset to proceed.")

if __name__ == "__main__":
    main()