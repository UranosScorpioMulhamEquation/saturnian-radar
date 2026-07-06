import streamlit as st
import pandas as pd
from datetime import date

# Page Configuration
st.set_page_config(page_title="Saturnian Matrix Predictive Engine", page_icon="🪐", layout="wide")

st.title("🪐 The Saturnian Matrix Predictive Engine")
st.write("""
Analyzing trajectories of systemic and structural transition based on **14 orbital resonance cycles** encompassing the Saturnian Karma coefficient (cycle duration: 4.4 years). 
The model has been updated to reflect the phased orbital effect (29.457 ÷ 3 ≈ 9.6 years). The systemic impact scales upward and downward concentrically around the 10th cycle, incorporating precise Sexagesimal (Babylonian) historical displacement and applying the **0.30 astrodynamical tolerance threshold**.
""")

# User Input
inception_date = st.date_input("Enter Date of Birth / Inception:", value=date(1981, 5, 1), min_value=date(1800, 1, 1), max_value=date(2100, 1, 1))

# Function to calculate date based on the 360-day Sexagesimal system
def calculate_sexagesimal_date(b_date, added_years):
    years_offset = int(added_years)
    remaining_years = added_years - years_offset
    
    months_offset = int(remaining_years * 12)
    remaining_months = (remaining_years * 12) - months_offset
    
    days_offset = int(remaining_months * 30)
    
    d = b_date.day + days_offset
    m = b_date.month + months_offset
    y = b_date.year + years_offset
    
    # Handle overflow
    while d > 30:
        d -= 30
        m += 1
    while m > 12:
        m -= 12
        y += 1
        
    return f"{y}-{m:02d}-{d:02d}"

if st.button("Run Systemic Analysis"):
    cycles_data = []
    tolerance = 0.30  # Target tolerance threshold
    
    for cycle in range(1, 15):
        cycle_value = cycle * 4.4  
        
        # Apply tolerance to calculate the manifestation window
        start_value = cycle_value - tolerance
        end_value = cycle_value + tolerance
        
        start_date = calculate_sexagesimal_date(inception_date, start_value)
        peak_date = calculate_sexagesimal_date(inception_date, cycle_value)
        end_date = calculate_sexagesimal_date(inception_date, end_value)
        
        # Determine impact phase based on the dynamic curve
        if cycle == 8:
            impact = "📈 Escalating Phase (Initial Structural Shift)"
        elif cycle == 9:
            impact = "🚀 Critical Escalation (Approaching Peak Resonance)"
        elif cycle == 10:
            impact = "💥 Absolute Resonance / Peak Structural Transformation"
        elif cycle == 11:
            impact = "📉 Decelerating Phase / Sub-Critical"
        elif cycle == 12:
            impact = "⏳ Diminishing Phase (End of Transformation Window)"
        else:
            impact = "Normal"
            
        cycles_data.append({
            "Cycle": f"Cycle {cycle}",
            "Peak Value (Years)": round(cycle_value, 2),
            "Window Start (-0.30)": start_date,
            "Peak Date": peak_date,
            "Window End (+0.30)": end_date,
            "Structural Impact Status": impact
        })
        
    df = pd.DataFrame(cycles_data)
    
    st.success(f"📊 Systemic transition matrix successfully generated for {inception_date.strftime('%Y-%m-%d')} incorporating the stochastic tolerance window (±{tolerance}).")
    
    st.dataframe(df, use_container_width=True)
    
    st.subheader("🎯 Dynamic Saturnian Curve Analysis (9.6-Year Window):")
    
    # Extract precise dates for pivotal cycles
    date_8 = df.loc[df['Cycle'] == 'Cycle 8', 'Peak Date'].values[0]
    date_10 = df.loc[df['Cycle'] == 'Cycle 10', 'Peak Date'].values[0]
    date_12 = df.loc[df['Cycle'] == 'Cycle 12', 'Peak Date'].values[0]
    
    st.info(f"""
    * **Ascending Curve (Cycles 8 & 9):** The structural transformation begins its gradual escalation starting from **{date_8}**.
    * **Peak Resonance (Cycle 10):** Represents the apex of the wave and the inevitable systemic reorganization on **{date_10}**.
    * **Descending Curve (Cycles 11 & 12):** The momentum decelerates and stabilizes, concluding the transition window by **{date_12}**.
    """)