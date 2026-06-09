
import streamlit as st
import pandas as pd
import pickle
from datetime import datetime

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Smart City Traffic Intelligence System",
    page_icon="🚦",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
}

.metric-container {
    background-color: #1a1f2e;
    padding: 1rem;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD MODEL
# ==========================================

with open("models/traffic_model.pkl", "rb") as file:
    model = pickle.load(file)

# ==========================================
# HEADER
# ==========================================

st.title("🚦 Smart City Traffic Intelligence System")

st.caption(
    "AI-Powered Urban Traffic Forecasting, Peak Detection and Traffic Monitoring"
)

st.markdown("---")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.header("⚙ Traffic Inputs")

junction = st.sidebar.selectbox(
    "Select Junction",
    [1, 2, 3, 4]
)

selected_date = st.sidebar.date_input(
    "Select Date"
)

selected_time = st.sidebar.time_input(
    "Select Time"
)

st.sidebar.markdown("---")

st.sidebar.subheader("📈 Model Performance")

st.sidebar.success("R² Score : 0.969")
st.sidebar.info("MAE : 2.37 Vehicles")

st.sidebar.markdown("---")

st.sidebar.subheader("🏙 Control Center")

st.sidebar.write(
    "Monitor traffic congestion and predict future traffic demand."
)

# ==========================================
# FEATURE ENGINEERING
# ==========================================

dt = datetime.combine(
    selected_date,
    selected_time
)

year = dt.year
month = dt.month
day = dt.day
hour = dt.hour

dayofweek = dt.weekday()

is_weekend = 1 if dayofweek >= 5 else 0

weekofyear = dt.isocalendar().week

quarter = ((month - 1) // 3) + 1

# Season

if month in [12, 1, 2]:
    season = 0

elif month in [3, 4, 5]:
    season = 1

elif month in [6, 7, 8, 9]:
    season = 2

else:
    season = 3

# Rush Hour

if (8 <= hour <= 10) or (17 <= hour <= 20):
    rushhour = 1
else:
    rushhour = 0

# Holidays

holiday_dates = [
    "2015-01-26",
    "2015-08-15",
    "2015-10-02",
    "2016-01-26",
    "2016-08-15",
    "2016-10-02",
    "2017-01-26",
    "2017-08-15"
]

holiday_dates = pd.to_datetime(
    holiday_dates
)

selected_timestamp = pd.Timestamp(
    selected_date
).normalize()

is_holiday = int(
    selected_timestamp in holiday_dates
)

# ==========================================
# PREDICTION BUTTON
# ==========================================

if st.button("🚀 Predict Traffic"):

    features = [[
        junction,
        year,
        month,
        day,
        hour,
        dayofweek,
        is_weekend,
        is_holiday,
        weekofyear,
        quarter,
        season,
        rushhour
    ]]

    prediction = model.predict(
        features
    )[0]

    # ======================================
    # TRAFFIC LEVEL
    # ======================================

    if prediction <= 10:
        level = "LOW"
        color = "🟢"

    elif prediction <= 20:
        level = "MEDIUM"
        color = "🟡"

    elif prediction <= 40:
        level = "HIGH"
        color = "🟠"

    else:
        level = "PEAK"
        color = "🔴"

    risk_score = min(
        prediction / 50 * 100,
        100
    )

    # ======================================
    # KPI CARDS
    # ======================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🚗 Vehicles",
            f"{prediction:.0f}"
        )

    with col2:
        st.metric(
            "📍 Junction",
            junction
        )

    with col3:
        st.metric(
            "⏰ Hour",
            hour
        )

    with col4:
        st.metric(
            "🚦 Status",
            level
        )

    st.markdown("---")

    # ======================================
    # TRAFFIC UTILIZATION
    # ======================================

    st.subheader("📊 Traffic Risk Score")

    st.progress(
        int(risk_score)
    )

    st.write(
        f"Risk Score : {risk_score:.1f}%"
    )

    st.markdown("---")

    # ======================================
    # SUMMARY
    # ======================================

    st.subheader("📋 Prediction Summary")

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:

        st.info(
            f"""
            Junction : {junction}

            Date : {selected_date}

            Time : {selected_time}
            """
        )

    with summary_col2:

        st.success(
            f"""
            Predicted Vehicles : {prediction:.0f}

            Traffic Level : {color} {level}
            """
        )

    st.markdown("---")

    # ======================================
    # TRAFFIC ALERT
    # ======================================

    st.subheader("🚨 Smart Alert System")

    if prediction > 40:

        st.error(
            "PEAK TRAFFIC EXPECTED"
        )

    elif prediction > 20:

        st.warning(
            "HIGH TRAFFIC EXPECTED"
        )

    else:

        st.success(
            "NORMAL TRAFFIC CONDITIONS"
        )

    # ======================================
    # GOVERNMENT RECOMMENDATION ENGINE
    # ======================================

    st.subheader("🧠 Traffic Management Recommendation")

    if prediction > 40:

        st.error("""
        • Deploy traffic police

        • Increase signal duration

        • Activate alternate routes

        • Issue congestion alert
        """)

    elif prediction > 20:

        st.warning("""
        • Monitor traffic flow

        • Prepare diversion plans

        • Optimize signals
        """)

    else:

        st.success("""
        • Normal operation

        • No intervention required
        """)

    st.markdown("---")

    # ======================================
    # FEATURE VIEWER
    # ======================================

    with st.expander(
        "🔍 View Engineered Features"
    ):

        feature_df = pd.DataFrame({
            "Feature": [
                "Junction",
                "Year",
                "Month",
                "Day",
                "Hour",
                "DayOfWeek",
                "IsWeekend",
                "IsHoliday",
                "WeekOfYear",
                "Quarter",
                "Season",
                "RushHour"
            ],
            "Value": [
                junction,
                year,
                month,
                day,
                hour,
                dayofweek,
                is_weekend,
                is_holiday,
                weekofyear,
                quarter,
                season,
                rushhour
            ]
        })

        st.dataframe(
            feature_df,
            use_container_width=True
        )

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Smart City Traffic Intelligence System | Built using Python, Streamlit, Scikit-Learn and Machine Learning"
)
