
import os
import pandas as pd
import streamlit as st

st.markdown(
    """
    <style>
    div[data-baseweb="select"] {
        border: 2px solid #4CAF50 !important; /* Green Border */
        border-radius: 4px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
CSV_FILE = "user_data.csv"

st.title("Streamlit Multi-Level Menu Logger")

# 1. First-Level Menu Selection
main_menu_options = ["Hardware", "Software", "Support"]
selected_main = st.selectbox("Select a Category:", main_menu_options)

# 2. Dynamic Second-Level Menu Selection based on First Selection
if selected_main == "Hardware":
    sub_menu_options = ["Laptops", "Desktops", "Printers"]
elif selected_main == "Software":
    sub_menu_options = ["Operating Systems", "Office Suites", "Developer Tools"]
else:  # Support
    sub_menu_options = ["Technical Issue", "Billing Inquiry", "Feedback"]

selected_sub = st.selectbox(f"Select a {selected_main} item:", sub_menu_options)

# 3. User Input Text Field
user_input = st.text_input("Enter your comments or notes:")

# 4. Save Logic
if st.button("Submit Data"):
    if user_input.strip() == "":
        st.warning("Please enter some text before submitting.")
    else:
        # Create a dictionary including both menu tiers
        new_data = {
            "Main Category": selected_main,
            "Sub Category": selected_sub,
            "User Input": user_input,
        }

        df_new = pd.DataFrame([new_data])

        if not os.path.exists(CSV_FILE):
            df_new.to_csv(CSV_FILE, index=False)
        else:
            df_new.to_csv(CSV_FILE, mode="a", header=False, index=False)

        st.success("Data successfully saved!")

# 5. Display existing data
if os.path.exists(CSV_FILE):
    st.subheader("Current Stored Data")
    st.dataframe(pd.read_csv(CSV_FILE))

st.cache_data.clear()
st.cache_resource.clear()