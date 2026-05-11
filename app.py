import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Netflix Analysis | Ajay Kumar",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CUSTOM CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;600;700&display=swap');

/* Base */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0a0a;
    color: #f5f5f5;
}
.stApp { background-color: #0a0a0a; }

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a0000 0%, #0a0a0a 100%);
    border-right: 1px solid #E50914;
}
[data-testid="stSidebar"] * { color: #f5f5f5 !important; }

/* Hero Banner */
.hero {
    background: linear-gradient(135deg, #E50914 0%, #8B0000 50%, #0a0a0a 100%);
    border-radius: 16px;
    padding: 40px;
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "NETFLIX";
    position: absolute;
    right: -20px;
    top: -20px;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 160px;
    color: rgba(255,255,255,0.04);
    letter-spacing: 10px;
    pointer-events: none;
}
.hero h1 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 52px;
    letter-spacing: 4px;
    margin: 0;
    line-height: 1;
    color: white;
}
.hero p {
    font-size: 15px;
    color: rgba(255,255,255,0.7);
    margin-top: 8px;
    font-weight: 300;
}

/* Metric Cards */
.metric-row {
    display: flex;
    gap: 16px;
    margin-bottom: 30px;
}
.metric-card {
    flex: 1;
    background: linear-gradient(135deg, #1a1a1a, #111);
    border: 1px solid #2a2a2a;
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    transition: border-color 0.3s;
}
.metric-card:hover { border-color: #E50914; }
.metric-card .value {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 42px;
    color: #E50914;
    line-height: 1;
}
.metric-card .label {
    font-size: 12px;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 6px;
}

/* Section Headers */
.section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 26px;
    letter-spacing: 3px;
    color: #f5f5f5;
    border-left: 4px solid #E50914;
    padding-left: 14px;
    margin: 30px 0 16px 0;
}

/* Chart Cards */
.chart-card {
    background: #111;
    border: 1px solid #1f1f1f;
    border-radius: 12px;
    padding: 20px;
}

/* Insight Box */
.insight-box {
    background: linear-gradient(135deg, #1a0000, #0f0f0f);
    border: 1px solid #E50914;
    border-radius: 10px;
    padding: 16px 20px;
    margin-top: 16px;
    font-size: 13px;
    color: #ccc;
    line-height: 1.7;
}
.insight-box strong { color: #E50914; }

/* Footer */
.footer {
    text-align: center;
    padding: 30px;
    color: #444;
    font-size: 12px;
    letter-spacing: 1px;
    border-top: 1px solid #1a1a1a;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ── LOAD DATA ───────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv('data/netflix_titles.csv')
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    return df

df = load_data()

# ── SIDEBAR ─────────────────────────────────────────────────────────────────
st.sidebar.markdown("## 🎬 FILTERS")
content_type = st.sidebar.selectbox("Content Type", ["All", "Movie", "TV Show"])
if content_type != "All":
    filtered = df[df['type'] == content_type]
else:
    filtered = df

year_range = st.sidebar.slider(
    "Year Added",
    int(df['year_added'].dropna().min()),
    int(df['year_added'].dropna().max()),
    (2010, 2021)
)
filtered = filtered[
    (filtered['year_added'] >= year_range[0]) &
    (filtered['year_added'] <= year_range[1])
]

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style='font-size:12px; color:#666; line-height:1.8;'>
📊 <b style='color:#E50914'>Dataset</b>: Kaggle Netflix Shows<br>
📁 <b style='color:#E50914'>Rows</b>: 8,807 titles<br>
🐍 <b style='color:#E50914'>Stack</b>: Python, Pandas, Plotly<br>
👤 <b style='color:#E50914'>Built by</b>: Ajay Kumar
</div>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>NETFLIX CONTENT ANALYSIS</h1>
    <p>Exploratory Data Analysis on 8,807+ titles across 190+ countries · Built by Chintala Naga Venkata Ajay Kumar</p>
</div>
""", unsafe_allow_html=True)

# ── METRIC CARDS ─────────────────────────────────────────────────────────────
total = len(filtered)
movies = len(filtered[filtered['type'] == 'Movie'])
shows = len(filtered[filtered['type'] == 'TV Show'])
countries = filtered['country'].dropna().str.split(',').explode().str.strip().nunique()

st.markdown(f"""
<div class="metric-row">
    <div class="metric-card">
        <div class="value">{total:,}</div>
        <div class="label">Total Titles</div>
    </div>
    <div class="metric-card">
        <div class="value">{movies:,}</div>
        <div class="label">Movies</div>
    </div>
    <div class="metric-card">
        <div class="value">{shows:,}</div>
        <div class="label">TV Shows</div>
    </div>
    <div class="metric-card">
        <div class="value">{countries}</div>
        <div class="label">Countries</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── CHART THEME ───────────────────────────────────────────────────────────────
CHART_THEME = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#aaa', family='Inter')
)

# ── ROW 1: PIE + BAR ──────────────────────────────────────────────────────────
st.markdown('<div class="section-title">CONTENT BREAKDOWN</div>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1.6])

with col1:
    type_counts = filtered['type'].value_counts().reset_index()
    type_counts.columns = ['Type', 'Count']
    fig1 = go.Figure(go.Pie(
        labels=type_counts['Type'],
        values=type_counts['Count'],
        hole=0.55,
        marker=dict(colors=['#E50914', '#8B0000'],
                    line=dict(color='#0a0a0a', width=3)),
        textfont=dict(color='white', size=13),
        textinfo='label+percent'
    ))
    fig1.update_layout(**CHART_THEME, showlegend=False,
                       annotations=[dict(text=f"<b>{total:,}</b><br>Titles",
                                        x=0.5, y=0.5, font=dict(size=16, color='white'),
                                        showarrow=False)])
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    country_df = filtered['country'].dropna().str.split(',').explode().str.strip()
    top_c = country_df.value_counts().head(10).reset_index()
    top_c.columns = ['Country', 'Count']
    fig2 = go.Figure(go.Bar(
        x=top_c['Count'], y=top_c['Country'],
        orientation='h',
        marker=dict(
            color=top_c['Count'],
            colorscale=[[0, '#5a0000'], [0.5, '#B20710'], [1, '#E50914']],
            line=dict(width=0)
        ),
        text=top_c['Count'],
        textposition='outside',
        textfont=dict(color='#aaa', size=11)
    ))
    fig2.update_layout(**CHART_THEME,
                       xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                       yaxis=dict(showgrid=False, tickfont=dict(size=12)),
                       margin=dict(t=20, b=20, l=130, r=60))
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
<div class="insight-box">
💡 <strong>Key Insight:</strong> 69.6% of Netflix content is Movies vs 30.4% TV Shows.
The <strong>United States</strong> dominates with 3,690 titles, followed by <strong>India (1,046)</strong> and <strong>UK (806)</strong> —
together accounting for <strong>52% of all content</strong>.
</div>
""", unsafe_allow_html=True)

# ── ROW 2: LINE CHART ─────────────────────────────────────────────────────────
st.markdown('<div class="section-title">GROWTH OVER TIME</div>', unsafe_allow_html=True)

yearly = filtered.dropna(subset=['year_added'])
yearly = yearly[
    (yearly['year_added'] >= year_range[0]) &
    (yearly['year_added'] <= year_range[1])
]
yc = yearly.groupby(['year_added', 'type']).size().reset_index(name='Count')

fig3 = go.Figure()
for t, color in [('Movie', '#E50914'), ('TV Show', '#ff6b6b')]:
    d = yc[yc['type'] == t]
    fig3.add_trace(go.Scatter(
        x=d['year_added'], y=d['Count'],
        name=t, mode='lines+markers',
        line=dict(color=color, width=3),
        marker=dict(size=8, symbol='circle',
                    line=dict(color='white', width=2)),
        fill='tozeroy',
        fillcolor=color.replace(')', ',0.08)').replace('rgb', 'rgba') if 'rgb' in color
                 else f"rgba(229,9,20,0.08)" if color == '#E50914' else "rgba(255,107,107,0.05)"
    ))
fig3.update_layout(
    **CHART_THEME,
    legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#aaa')),
    xaxis=dict(showgrid=False, tickfont=dict(size=11), zeroline=False),
    yaxis=dict(showgrid=True, gridcolor='#1f1f1f', tickfont=dict(size=11), zeroline=False),
    margin=dict(t=20, b=40, l=60, r=20),
    hovermode='x unified'
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
<div class="insight-box">
💡 <strong>Key Insight:</strong> Netflix content additions <strong>peaked in 2019 with 2,016 titles</strong>,
showing 5x growth from 2016 (429 titles). Content additions slightly declined post-2019,
likely due to COVID-19 production disruptions.
</div>
""", unsafe_allow_html=True)

# ── ROW 3: GENRES + RATINGS ───────────────────────────────────────────────────
st.markdown('<div class="section-title">GENRES & RATINGS</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2)

with col3:
    genre_df = filtered['listed_in'].dropna().str.split(',').explode().str.strip()
    top_g = genre_df.value_counts().head(10).reset_index()
    top_g.columns = ['Genre', 'Count']
    fig4 = go.Figure(go.Bar(
        x=top_g['Count'], y=top_g['Genre'],
        orientation='h',
        marker=dict(
            color=top_g['Count'],
            colorscale=[[0, '#3a0000'], [1, '#E50914']],
            line=dict(width=0)
        ),
        text=top_g['Count'],
        textposition='outside',
        textfont=dict(color='#aaa', size=11)
    ))
    fig4.update_layout(
        **CHART_THEME,
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, tickfont=dict(size=11)),
        margin=dict(t=10, b=20, l=170, r=60)
    )
    st.plotly_chart(fig4, use_container_width=True)

with col4:
    valid = ['TV-MA', 'TV-14', 'TV-PG', 'R', 'PG-13', 'TV-Y7', 'TV-Y', 'PG', 'TV-G', 'NR', 'G']
    rating_df = filtered[filtered['rating'].isin(valid)]
    rc = rating_df['rating'].value_counts().reset_index()
    rc.columns = ['Rating', 'Count']
    fig5 = go.Figure(go.Bar(
        x=rc['Rating'], y=rc['Count'],
        marker=dict(
            color=rc['Count'],
            colorscale=[[0, '#3a0000'], [1, '#E50914']],
            line=dict(width=0)
        ),
        text=rc['Count'],
        textposition='outside',
        textfont=dict(color='#aaa', size=11)
    ))
    fig5.update_layout(
        **CHART_THEME,
        xaxis=dict(showgrid=False, tickfont=dict(size=11), zeroline=False),
        yaxis=dict(showgrid=True, gridcolor='#1f1f1f', showticklabels=False, zeroline=False),
        margin=dict(t=10, b=40, l=20, r=20)
    )
    st.plotly_chart(fig5, use_container_width=True)

st.markdown("""
<div class="insight-box">
💡 <strong>Key Insight:</strong> <strong>International Movies (2,752)</strong> and <strong>Dramas (2,427)</strong> are
the dominant genres. For ratings, <strong>TV-MA accounts for 36.4%</strong> of all content,
indicating Netflix primarily targets adult audiences.
</div>
""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    BUILT BY CHINTALA NAGA VENKATA AJAY KUMAR &nbsp;·&nbsp;
    DATA SOURCE: KAGGLE NETFLIX DATASET &nbsp;·&nbsp;
    STACK: PYTHON · PANDAS · PLOTLY · STREAMLIT
</div>
""", unsafe_allow_html=True)