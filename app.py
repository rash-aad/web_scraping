import streamlit as st
import pandas as pd
import papermill as pm
import os
import time

st.set_page_config(page_title="Lead Finder (Jupyter Powered)", layout="centered")
st.title("Web scrapper")

city = st.text_input("City", "")
keyword = st.text_input("Keyword", "")
country = st.text_input("Country", "")

if st.button("Run Lead Search"):
    with st.spinner("Fetching..."):
        pm.execute_notebook(
            input_path="leadgen.ipynb",
            output_path="output.ipynb",
            parameters=dict(city=city, keyword=keyword, country=country)
        )
        time.sleep(1)

        if os.path.exists("notebook_output.csv"):
            df = pd.read_csv("notebook_output.csv")
            if not df.empty:
                st.success(f"✅ Found {len(df)} businesses in {city}")
                st.dataframe(df)

                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button("⬇️ Download CSV", csv, "leads.csv", "text/csv")
            else:
                st.warning("⚠️ No results found.")
        else:
            st.error("❌ Failed to generate results.")
