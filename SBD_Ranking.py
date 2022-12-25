import flask
import openpyxl
from flask import request
from flask import app
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/calculate_percentiles', methods=['POST'])
def calculate_percentiles():
    # Get the user's input for squat, bench, deadlift, total, dots, sex, and weight class
    user_squat = int(request.form['squat'])
    user_bench = int(request.form['bench'])
    user_deadlift = int(request.form['deadlift'])
    user_total = int(request.form['total'])
    user_dots = int(request.form['dots'])
    user_sex = request.form['sex']
    user_wc = int(request.form['wc'])

    # Open the Excel workbook in read-only mode
    workbook = openpyxl.load_workbook('/Users/alexmammen/Documents/Projects/PowerliftingRanks/LifterSorting/IPF_Updated.xlsx', read_only=True)
    # Get the sheet with the lift data
    sheet = workbook['Sheet1']
    # Initialize variables to store the number of people with a higher lift than the user
    squat_higher = 0
    bench_higher = 0
    deadlift_higher = 0
    total_higher = 0
    dots_higher = 0
    # Initialize variables to store the total number of people in the same age and sex group as the user
    wc_sex_group_size = 0
    # Iterate over the rows in the sheet
    for row in sheet.rows:
    # Skip the first row (the header row)
        if row[0].row == 1:
            continue
        # Round the weight class in the current row down to the nearest whole number
        wc = row[5].value
        # Check the user's weight class and sex against the weight class and sex in the current row
        if user_wc == wc and user_sex == row[1].value:
            wc_sex_group_size += 1
        # Compare the user's lifts to the lifts in the current row
        if row[6] is not None and row[6].value is not None and user_squat > row[6].value:
            squat_higher += 1
        if row[7] is not None and row[7].value is not None and user_bench > row[7].value:
            bench_higher += 1
        if row[8] is not None and row[8].value is not None and user_deadlift > row[8].value:
            deadlift_higher += 1
        if row[9] is not None and row[9].value is not None and user_total > row[9].value:
            total_higher += 1
        if row[10] is not None and row[10].value is not None and user_dots > row[10].value:
            dots_higher += 1
        # Calculate the percentile for each lift
        squat_percentile = ((squat_higher / wc_sex_group_size)) * 100
        bench_percentile = ((bench_higher / wc_sex_group_size)) * 100
        deadlift_percentile = ((deadlift_higher / wc_sex_group_size)) * 100
        total_percentile = ((total_higher / wc_sex_group_size)) * 100
        dots_percentile = ((dots_higher / wc_sex_group_size)) * 100

        #Return the user's percentiles as a JSON object
        return jsonify({
        'squat_percentile': squat_percentile,
        'bench_percentile': bench_percentile,
        'deadlift_percentile': deadlift_percentile,
        'total_percentile': total_percentile,
        'dots_percentile': dots_percentile
        })

        ##Run the app
        if name == 'main':
            app.run()