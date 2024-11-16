import PySimpleGUI as sg
import pandas as pd
import os

# Function to get the CSV file name based on the grade
def get_csv_file(grade):
    if grade == 'Extra':
        return 'extra.csv'
    elif grade == 'Teachers':
        return 'teachers.csv'
    elif grade == 'Non-Academic':
        return 'nonacademic.csv'
    return f'grade{grade}.csv'

# Create CSV files for each grade and category if they don't exist
grades = list(range(1, 14)) + ['Teachers', 'Non-Academic', 'Extra']
for grade in grades:
    csv_file = get_csv_file(grade)
    if not os.path.exists(csv_file):
        df = pd.DataFrame(columns=['Member Name', 'Member ID', 'Date of Birth', 'Address', 'Contact', 'Grade'])
        df.to_csv(csv_file, index=False)

# Define the layout of the form
layout = [
    [sg.Text('Grade'), sg.Push(), sg.Combo([str(i) for i in range(1, 14)] + ['Teachers', 'Non-Academic', 'Extra'], key='Grade')],
    [sg.Text('Member Name'), sg.Push(), sg.InputText(key='Member Name')],
    [sg.Text('Member ID'), sg.Push(), sg.InputText(key='Member ID')],
    [sg.Text('Date of Birth'), sg.Push(), sg.InputText(key='Date of Birth')],
    [sg.Text('Address'), sg.Push(), sg.InputText(key='Address')],
    [sg.Text('Contact'), sg.Push(), sg.InputText(key='Contact')],
    [sg.Push(), sg.Button('Submit'), sg.Button('Delete'), sg.Button('Search'), sg.Push()],
    [sg.Output(size=(80, 10))]
]

# Create the window
window = sg.Window('Member Details Entry Form', layout)

def clear_input():
    for key in ['Grade', 'Member Name', 'Member ID', 'Date of Birth', 'Address', 'Contact']:
        windowkey

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    grade = values['Grade']
    if not grade:
        sg.popup('Please select a grade!')
        continue

    csv_file = get_csv_file(grade)

    if event == 'Submit':
        # Append data to the appropriate CSV file
        new_data = pd.DataFrame([values])
        new_data.to_csv(csv_file, mode='a', header=False, index=False)
        sg.popup('Data saved!')
        clear_input()

    if event == 'Delete':
        # Delete data from the appropriate CSV file
        df = pd.read_csv(csv_file)
        df = df[df['Member ID'] != values['Member ID']]
        df.to_csv(csv_file, index=False)
        sg.popup('Data deleted!')
        clear_input()

    if event == 'Search':
        # Search data in the appropriate CSV file
        df = pd.read_csv(csv_file)
        result = df[df['Member ID'] == values['Member ID']]
        if not result.empty:
            print(result)
        else:
            sg.popup('No data found!')

window.close()

