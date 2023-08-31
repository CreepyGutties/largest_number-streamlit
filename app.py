import streamlit as st

def find_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    st.title("Find the Largest Number")
    st.write("Enter three numbers and find the largest among them.")

    num1 = st.text_input("Enter the first number:")
    num2 = st.text_input("Enter the second number:")
    num3 = st.text_input("Enter the third number:")

    if st.button("Find Largest"):
        if is_numeric(num1) and is_numeric(num2) and is_numeric(num3):
            largest_num = find_largest(float(num1), float(num2), float(num3))
            st.write("The largest number is:", largest_num)
        else:
            st.write("Please enter numeric values only.")
    
    footer_html = """
    <style>
    .footer {
        position: fixed;
        bottom: 50px;
        right: 0;
        padding: 5px;
        font-size: 14px;
        color: #888888;
    }
    </style>
    <div class="footer">Made by 22ds1000038</div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()