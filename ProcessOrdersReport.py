import pandas as pd
from tkinter import filedialog
import tkinter as tk
from tkinter import *

root = Tk()

root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

activity_report = pd.read_csv(root.filename)

# Get the unique values of the "company" column
companies = activity_report["company"].unique()

columns_to_select = ['order number',
                    'status',
                    'order value',
                    'Ship Address Name',
                    'Ship Address 1',
                    'Ship Address 2',
                    'Ship Address City',
                    'Ship Address Country',
                    'Ship Address Phone',
                    'Ship Address Postal Code',
                    'Ship Address Postal State',
                    'Received Date',
                    'Ship Date',
                    'Carrier',
                    'Tracking Number Label',
                    'Carrier Service',
                    'Dimensions',
                    'Delivered',
                    'Customer Purchase Order',
                    'Country Process',
                    'Reason',
                    'Personalization',
                    'Mexican Warehouse Departure Date',
                    'USA Warehouse Arrival Date',
                    'Warehouse Delivery to Carrier Date',
                    'Boxes Quantity',
                    'Label Created Date',
                    'Description',
                    'Ship Address Company',
                    'Requested Quantity (�)',
                    'Picked Quantity (�)'
                    'Validated Quantity (�)']

# Function to filter and save the data
def filter_and_save():
    selected_company = dropdown_var.get()
    if selected_company in companies:
        activity_report_cleaned = activity_report[activity_report["company"] == selected_company]
        save_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV files', '*.csv')])
        if save_path:
            activity_report_cleaned.filter(items=columns_to_select).to_csv(save_path, index=False)
            status_label.config(text="Data filtered and saved successfully.")
        else:
            status_label.config(text="File not saved.")
    else:
        status_label.config(text="Invalid selection from dropdown.")

# Create the dropdown and label
dropdown_var = tk.StringVar(root)
dropdown_var.set(companies[0])
dropdown = tk.OptionMenu(root, dropdown_var, *companies)
dropdown.pack(pady=10)

# Create the "Filter and Save" button
filter_button = tk.Button(root, text="Filter and Save", command=filter_and_save)
filter_button.pack(pady=10)

# Create a label to display the status message
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Exit button
Button(root, text="Salir de aplicación", command=root.destroy).pack()

root.mainloop()
