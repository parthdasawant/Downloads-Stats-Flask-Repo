from datetime import datetime
from flask import Flask, Response,jsonify
from google.cloud import storage


app = Flask(__name__)

# EDIT SECTION: Enter appropriate values
bucket_name = "BUCKET_NAME" # Enter Bucket Name here
start_date_str = "2023-08" # Enter published date of app in YYYY-MM here 
app_name = "com.example.app" # Enter your app package name
client = storage.Client.from_service_account_json('KEY_FILE_NAME') # Enter key file name here

lastDate = "" 


# For genearating all month-year pair since published date of the app  
def generate_month_year_pairs(start_date_str):
    start_date = datetime.strptime(start_date_str, '%Y-%m')
    current_date = datetime.now()
    
    month_year_pairs = []
    
    while start_date <= current_date:
        month_year_pairs.append((start_date.month, start_date.year))
        if start_date.month == 12:
            start_date = start_date.replace(year=start_date.year + 1, month=1)
        else:
            start_date = start_date.replace(month=start_date.month + 1)
    return month_year_pairs

# Can be customize as per your need
def generate_svg_badge(text):
    height = 20
    font_size = 14
    width = 240
    svg = f'''
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}">
        <rect width="100%" height="100%" fill="#007BFF" />
        <a xlink:href="#" download="badge.svg">
            <rect width="16" height="16" x="2" y="2" fill="#FFFFFF" />
            <text x="10" y="{(height / 2)+1}" fill="#007BFF" font-size="16" text-anchor="middle" alignment-baseline="middle" style="cursor: pointer;">⬇</text>
        </a>
        <text x="130" y="{height / 2}" fill="#FFFFFF" font-size="{font_size}" font-family="Roboto, sans-serif" text-anchor="middle" alignment-baseline="middle">{text}</text>
    </svg>
    '''
    return svg

# This helper function is used for fetching the reports
def helper():
    try:
        totalDownload = 0
        month_year_pairs = generate_month_year_pairs(start_date_str)
        
        for month, year in month_year_pairs:
            file_name = f'installs_{app_name}_{year}{month:02}_overview.csv'
            file_path = f'stats/installs/{file_name}'
            bucket = client.get_bucket(bucket_name)
            blob =  bucket.blob(file_path)
            with blob.open("r", encoding='utf-16le') as f:
                passFirstLine = True
                for line in f:
                    if passFirstLine:
                        passFirstLine = False
                        continue
                    lineList = line.split(',')
                    totalDownload += int(lineList[-3])
                    lastDate = lineList[0]
        return totalDownload, lastDate
    
    except Exception as e:
        return str(e)
 
  
# For GitHub readme file Badge
@app.route('/')
def get_app_stats_file():
    try:
        totalDownload, lastDate = helper()
        text =  f'{totalDownload} downloads till {lastDate}'
        svg =  generate_svg_badge(text)
        return Response(svg, content_type='image/svg+xml')
    
    except Exception as e:
        return str(e)


# API for downloads with date of updation
@app.route('/json') 
def get_app_stats_file_json():
    try:
        totalDownload, lastDate = helper()
        return jsonify({'download': totalDownload, 'date': lastDate})
    
    except Exception as e:
        return str(e)
