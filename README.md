# Netflix Content Analysis Dashboard

A data analysis project built to explore patterns in Netflix's content library — what gets added, where it comes from, who it's made for, and how the platform has grown over time.

**Live App:** https://netflix-analysis-rl7d.onrender.com

---

## Why I Built This

I wanted to go beyond running `.describe()` on a dataset and actually build something visual and interactive. Netflix felt like a natural choice — the data is messy enough to be interesting (multi-value columns, inconsistent date formats, missing entries) but structured enough to yield clear insights. The goal was to handle the entire pipeline: raw CSV → cleaned data → deployed dashboard.

---

## What the Dashboard Shows

**Content Breakdown**
Movies make up 69.6% of Netflix's catalog. TV Shows account for the remaining 30.4%. This gap is larger than most people expect given how much Netflix markets its original series.

**Geographic Distribution**
The United States leads with 3,690 titles. India follows at 1,046 — a clear signal of how aggressively Netflix has invested in South Asian content over the past five years. USA, India, and the UK together account for roughly 52% of all titles on the platform.

**Growth Over Time**
Netflix's content additions grew nearly 5x between 2016 (429 titles) and 2019 (2,016 titles). Post-2019, additions declined — likely a combination of COVID-19 production shutdowns and a strategic shift toward quality over volume.

**Genre Landscape**
International Movies (2,752) and Dramas (2,427) dominate. The prominence of International Movies reflects Netflix's push into non-English markets over the last few years.

**Audience Targeting**
TV-MA is the single largest rating category at 36.4% of all content. Netflix skews heavily adult in its content strategy.

---

## Technical Details

**Stack**
- Python 3 — core language
- Pandas — data cleaning and aggregation
- NumPy — numerical operations
- Plotly — interactive chart rendering
- Streamlit — dashboard framework
- Render — cloud deployment

**Interesting problems solved**

The `listed_in` and `country` columns store multiple comma-separated values per row — for example, a single title might be tagged as `"Dramas, International Movies, Romantic Movies"`. Aggregating these correctly required splitting each field, using Pandas `.explode()` to normalize rows, and then running `.value_counts()` on the expanded series. Getting this wrong gives you completely misleading genre counts.

The `date_added` column had inconsistent formatting and a significant number of null entries. Rather than dropping nulls or filling them arbitrarily, I coerced them to NaT and excluded them only from time-series analyses — keeping the full dataset intact for everything else.

---

## Dataset

Source: [Netflix Movies and TV Shows — Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)  
Size: 8,807 rows × 12 columns  
License: Public domain / CC0

The dataset is not included in this repository. Download `netflix_titles.csv` from the link above and place it in the `data/` folder before running locally.

---

## Running Locally

```bash
git clone https://github.com/nvakumar/netflix-analysis.git
cd netflix-analysis
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# place netflix_titles.csv inside the data/ folder
streamlit run app.py
```

App runs at `http://localhost:8501`

---

## Project Structure

```
netflix-analysis/
├── data/                    # Dataset folder (not tracked in git)
├── app.py                   # Streamlit dashboard
├── analysis.py              # Standalone EDA script
├── requirements.txt         # Dependencies
├── setup.sh                 # Render deployment config
├── Procfile                 # Render process file
└── README.md
```

---

## Author

Chintala Naga Venkata Ajay Kumar  
[LinkedIn](https://linkedin.com/in/nvakumar) · [GitHub](https://github.com/nvakumar) · nvajaykumarch@gmail.com
