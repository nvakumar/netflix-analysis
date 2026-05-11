# 🎬 Netflix Content Analysis Dashboard

> An interactive data analysis dashboard built with Python, Pandas, and Streamlit — exploring trends across 8,807+ Netflix titles.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=flat-square&logo=plotly)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=flat-square&logo=streamlit)

---

## 🔴 Live Demo

👉 **[View Live Dashboard](#)** ← *(replace with your Streamlit/Render URL after deployment)*

---

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the Netflix Movies and TV Shows dataset from Kaggle. The goal was to uncover meaningful patterns in Netflix's content library using Python data analysis libraries and present the findings through an interactive, visually rich dashboard.

---

## 📊 Key Insights Discovered

- 🎥 **69.6% of Netflix content is Movies** vs 30.4% TV Shows
- 🌍 **USA, India, and UK** together account for **52% of all titles** (3,690 / 1,046 / 806)
- 📈 Content additions **peaked in 2019 with 2,016 titles** — a 5x growth from 2016
- 🎭 **International Movies (2,752)** and **Dramas (2,427)** are the top genres
- 🔞 **TV-MA rating covers 36.4%** of all content — Netflix primarily targets adult audiences

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Data Processing | Pandas, NumPy |
| Visualizations | Plotly (interactive charts) |
| Dashboard | Streamlit |
| Deployment | Streamlit Cloud / Render |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
netflix_analysis/
│
├── data/
│   └── netflix_titles.csv        # Dataset from Kaggle
│
├── app.py                         # Streamlit dashboard (main app)
├── analysis.py                    # Standalone EDA script
├── requirements.txt               # Python dependencies
├── .gitignore                     # Ignores venv, DS_Store etc.
└── README.md                      # Project documentation
```

---

## ⚙️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/netflix-analysis.git
cd netflix-analysis
```

**2. Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Download the dataset**

Download `netflix_titles.csv` from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) and place it in the `data/` folder.

**5. Run the dashboard**
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📷 Dashboard Preview

> *(Add a screenshot of your dashboard here after deployment)*
> To add: Take a screenshot → save as `preview.png` in root folder → uncomment below

<!-- ![Dashboard Preview](preview.png) -->

---

## 📂 Dataset

- **Source:** [Netflix Movies and TV Shows — Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Author:** Shivam Bansal
- **Size:** 8,807 rows × 12 columns
- **Columns:** `show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description`

---

## 🧠 What I Learned

- Handling **real-world messy data** — null values, multi-value columns, inconsistent formats
- **Datetime parsing** and time-series aggregation with Pandas
- Using **Pandas `.explode()`** to handle comma-separated multi-value fields
- Building **interactive dashboards** with Streamlit and Plotly
- **Deploying Python apps** on cloud platforms

---

## 👤 Author

**Chintala Naga Venkata Ajay Kumar**  
📧 nvajaykumarch@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/nvakumar)  
🐙 [GitHub](https://github.com/nvakumar)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
