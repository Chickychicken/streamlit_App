import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import io

web_apps = st.sidebar.selectbox("Select Web Apps",
                                ("Exploratory Data Analysis", "Distributions"))


if web_apps == "Exploratory Data Analysis":

    uploaded_file = st.sidebar.file_uploader("Choose a file")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        show_df = st.checkbox("Show Data Frame", key="disabled")

        if show_df:
            st.write(df)

        chart_type = st.sidebar.selectbox(
            'Select Chart Type', ("Line Chart", "Histogram"))
        
        if chart_type == "Line Chart":
            numerical_column = st.sidebar.selectbox(
                'Select a Numerical Column', df.select_dtypes(include=['int64', 'float64']).columns)
            categorical_column = st.sidebar.selectbox(
                'Select a Categorical Column', df.select_dtypes(include=['object', 'category']).columns)

            line_title = st.text_input('Set Title', 'Line Chart')
            line_xtitle = st.text_input('Set x-axis Title', categorical_column)
            line_ytitle = st.text_input('Set y-axis Title', numerical_column)

            fig, ax = plt.subplots()
            ax.plot(df[categorical_column], df[numerical_column])
            ax.set_title(line_title)
            ax.set_xlabel(line_xtitle)
            ax.set_ylabel(line_ytitle)

            st.pyplot(fig)
            filename = "line_plot.png"
            fig.savefig(filename, dpi=300)
            with open("line_plot.png", "rb") as file:
                btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="line_plot.png",
                    mime="image/png"

                )
        elif chart_type == "Histogram":
            numerical_column = st.sidebar.selectbox(
                'Select a Column', df.select_dtypes(include=['int64', 'float64']).columns)

            choose_color = st.color_picker('Pick a Color', "#69b3a2")
            choose_opacity = st.slider(
                'Color Opacity', min_value=0.0, max_value=1.0, step=0.05)

            hist_bins = st.slider('Number of bins', min_value=5,
                                  max_value=150, value=30)
            hist_title = st.text_input('Set Title', 'Histogram')
            hist_xtitle = st.text_input('Set x-axis Title', numerical_column)

            fig, ax = plt.subplots()
            ax.hist(df[numerical_column], bins=hist_bins,
                    edgecolor="black", color=choose_color, alpha=choose_opacity)
            ax.set_title(hist_title)
            ax.set_xlabel(hist_xtitle)
            ax.set_ylabel('Count')

            st.pyplot(fig)
            filename = "plot.png"
            fig.savefig(filename, dpi=300)

            with open("plot.png", "rb") as file:
                btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="plot.png",
                    mime="image/png"
                )
