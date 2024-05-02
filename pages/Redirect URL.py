import os
import streamlit as st
from datetime import datetime

def save_data_to_file(data, file_name):
    file_path = f"redirect_{file_name}.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w"):
            pass
    with open(file_path, "a") as file:
        file.write(data + "\n")


def clear_data(file_name):
    file_path = f"redirect_{file_name}.txt"
    if os.path.exists(file_path):
        os.remove(file_path)
        st.success("Data cleared successfully!")
    else:
        st.warning("No data to clear.")

def main():
    st.title("Redirect permanent URL")

    # Date picker to select file
    selected_date = st.date_input("Select Date", datetime.today())
    file_name = selected_date.strftime("%Y-%m-%d")

    name = st.text_input("Enter old URL:")
    address = st.text_input("Enter new URL:")

    if st.button("Add"):
        data = f'Redirect permanent "{name}" "{address}"'
        save_data_to_file(data, file_name)
        st.success("Data added successfully!")

    # if st.button("Clear Data"):
    #     clear_data(file_name)

    st.header("Saved Data:")

    with open(f"redirect_{file_name}.txt", "r") as file:
        saved_data = file.readlines()
    for line in saved_data:
        st.write(line.strip())

    # Download button outside the if statement
    with open(f"redirect_{file_name}.txt", "r") as file:
        data = file.readlines()
    data = "".join(data)
    st.download_button(
        label="Download Data",
        data=data,
        file_name=f"redirect_{file_name}.txt",
        mime="text/plain"
    )

if __name__ == "__main__":
    main()