# Set the working directory
working_dir = 'C:/Users/admad/Documents/VSC Workspace/LNG'



import streamlit as st
import matplotlib.pyplot as plt

# Title
st.title("Shipping Market Equilibrium Calculator")

# Inputs
fleet_size_number_supply = st.number_input("Fleet Size (Number of Ships)", value=3131, step=1, format="%d")
fleet_size_dwt_supply_in_dwt_million = st.number_input("Fleet Size Supply (Million DWT)", value=254.1, step=0.1)
utilization_constant = st.number_input("Utilization Constant", value=0.95, step=0.01)

assumed_speed = st.number_input("Assumed Speed (knots)", value=11.0, step=0.1)  # Fixed: Changed 11 to 11.0
sea_margin = st.number_input("Sea Margin", value=0.05, step=0.01)

assumed_laden_days = st.number_input("Assumed Laden Days Fraction", value=0.4, step=0.01)

demand_billion_ton_mile = st.number_input("Demand (Billion Ton Mile)", value=10396.0, step=10.0)  # Fixed: Set as float

# Calculations
dwt_utilization = (fleet_size_dwt_supply_in_dwt_million * 1_000_000 / fleet_size_number_supply) * utilization_constant
distance_travelled_per_day = assumed_speed * 24 * (1 - sea_margin)
productive_laden_days_per_year = assumed_laden_days * 365

# Maximum Supply Calculation
maximum_supply_billion_ton_mile = fleet_size_number_supply * dwt_utilization * distance_travelled_per_day * productive_laden_days_per_year / 1_000_000_000

# Equilibrium
equilibrium = demand_billion_ton_mile - maximum_supply_billion_ton_mile
result = "Excess Supply" if equilibrium < 0 else "Excess Demand"

# Display results
st.subheader("Results:")
st.write(f"**DWT Utilization (tons):** {dwt_utilization:,.2f}")
st.write(f"**Distance Travelled per Day (nm):** {distance_travelled_per_day:,.2f}")
st.write(f"**Productive Laden Days per Year:** {productive_laden_days_per_year:,.2f}")
st.write(f"**Maximum Supply (Billion Ton Mile):** {maximum_supply_billion_ton_mile:,.2f}")
st.write(f"**Equilibrium:** {equilibrium:,.2f} Billion Ton Mile")
st.write(f"**Market Condition:** {result}")

# Visualization
fig, ax = plt.subplots()
ax.bar(["Demand", "Supply"], [demand_billion_ton_mile, maximum_supply_billion_ton_mile], color=['blue', 'orange'])
ax.set_ylabel("Billion Ton Mile")
ax.set_title("Supply vs Demand")
st.pyplot(fig)
