import streamlit as st
import altair as alt
import pandas as pd

def main():
    st.title("Bar Chart Creator")

    # User inputs
    st.sidebar.header("Input Data")
    
    categories = st.sidebar.text_input("Enter categories (comma-separated)", "A,B,C,D")
    values = st.sidebar.text_input("Enter values (comma-separated)", "10,20,30,40")

    if st.sidebar.button("Generate Chart"):
        # Process input data
        try:
            category_list = [cat.strip() for cat in categories.split(',')]
            value_list = [float(val.strip()) for val in values.split(',')]

            if len(category_list) != len(value_list):
                st.error("The number of categories must match the number of values.")
                return

            # Create a DataFrame
            df = pd.DataFrame({
                'Category': category_list,
                'Value': value_list
            })

            # Create a bar chart using Altair
            chart = alt.Chart(df).mark_bar().encode(
                x=alt.X('Category:O', title='Category'),
                y=alt.Y('Value:Q', title='Value'),
                color='Category:N'
            ).properties(
                title='Bar Chart'
            )

            # Display the chart
            st.altair_chart(chart, use_container_width=True)

        except ValueError:
            st.error("Invalid input. Please make sure values are numeric.")

if __name__ == "__main__":
    main()
