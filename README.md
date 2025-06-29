🔍 AI-Driven Local Lead Generation Tool

This project is a submission for the Caprae Capital AI-Readiness Challenge. It uses real-world business data and Google APIs to generate high-value local leads based on user input.

---

 📌 What It Does

- 🌐 Takes `city`, `keyword`, and `country` as input
- 🛰️ Uses **Google Places API** to find businesses in the area
- ☎️ Extracts phone numbers and websites using **Place Details API**
- 📦 Displays results in a Streamlit frontend
- 📄 Saves the results as a downloadable CSV

---

📂 Folder Structure

web_scraping/
├── app.py # Streamlit frontend
├── leadgen.ipynb # Jupyter backend with Papermill parameters
├── requirements.txt # Python dependencies
├── README.md # This file


---

## 🧪 How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/rash-aad/web_scraping.git
cd web_scraping


2.install dependencies:
pip install -r requirements.txt

3.Run the Streamlit app:
streamlit run app.py


🧠 Technologies Used
streamlit — for user-friendly interface

papermill — to execute the backend notebook dynamically

requests — for calling Google APIs

pandas — for data handling

Google Places API — to search businesses and fetch contact details

✅ Features
📍 Up to 60 leads per search using pagination

🧠 Fully dynamic: works for any city, any keyword

🔁 Backend logic lives in a Jupyter Notebook — clean and modular

💡 Great starting point for CRM enrichment tools

📌 Notes
Make sure to insert your own Google Places API key in the notebook

You can find the key usage in your Google Cloud Console

Free tier covers ~5,000 detailed queries per month