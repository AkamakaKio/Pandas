# Implementation of an expense tracker with data analysis using Pandas
# Users can add expenses, categorize spending, and perform data analysis on expenses

import pandas as pd

expenses = pd.DataFrame(columns=['Category', 'Amount'])

def add_expense(category, amount):
    global expenses
    expenses = expenses.append({'Category': category, 'Amount': amount}, ignore_index=True)

def view_summary():
    summary = expenses.groupby('Category')['Amount'].sum()
    return summary.to_dict()

# Example usage:
add_expense('Food', 50)
add_expense('Transportation', 30)
add_expense('Food', 20)
print(view_summary())
