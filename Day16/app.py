import streamlit as st
from factorial import fact  # Import the fact function from the factorial module
def main():
    st.set_page_config(page_title="Eye-Catching Factorial App", page_icon="🧮")

    st.markdown("""
    <style>
    body {
        background-color: #F0F8FF; /* Light background */
        color: #333;            /* Dark text */
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        background-color: #0080FF; /* Blue button */
        color: white;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

    st.header("Eye-Catching Factorial Calculator")  
    st.subheader("Discover the power of factorials!") 

    st.container()  # Input container
    number = st.number_input("Enter a number:", min_value=0, max_value=900)

    st.container()  # Calculation container
    if st.button("Calculate"):
            result = fact(number)
            st.write(f"The factorial of {number} is {result}")
            st.balloons()

if __name__ == "__main__":
    main()