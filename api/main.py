from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

api = Flask(__name__)
CORS(api,  supports_credentials=True) 

EXPORT_PATH="/mnt/dump/code/data-cleaning/public/"



# Iterate through columns and create plots dynamically
# for column in df.columns:
#     plt.figure()  # Create a new figure for each plot

#     if pd.api.types.is_numeric_dtype(df[column]):
#         # Create a scatter plot for numeric columns
#         scatter_matrix(df[[column]], alpha=0.8, figsize=(5, 5), diagonal='hist')
#     else:
#         # Create a bar plot for categorical columns
#         df[column].value_counts().plot(kind='bar', title=f'{column} Distribution')

#     # Save the plot as an image file
#     plt.savefig(f'{column}_plot.png')


@api.route('/images', methods=['POST','OPTIONS'])
def get_images_before_cleaning():
    if request.method == 'OPTIONS':
        response = jsonify(success=True)
        return response
    params = request.json
    uri = params.get('file')
    fileName = uri.split('/')[-1].split('.')[0]
    imageNames = []
    df = pd.read_csv(uri)
    # Iterate through columns and create plots dynamically
    for column in df.columns:
        plt.figure()  # Create a new figure for each plot

        if pd.api.types.is_numeric_dtype(df[column]):
            # Create a scatter plot for numeric columns
            scatter_matrix(df[[column]], alpha=0.8, figsize=(5, 5), diagonal='hist')
        else:
            # Create a bar plot for categorical columns
            df[column].value_counts().plot(kind='bar', title=f'{column} Distribution')

        # Save the plot as an image file
        imageName = '{}_{}_plot.png'.format(fileName, column)
        imageNames.append(imageName)
        plt.savefig('{}{}_{}_plot.png'.format(EXPORT_PATH,fileName, column))
        plt.close()
    response = jsonify({"imageNames": imageNames})

    return response

@api.route('/aimages', methods=['POST','OPTIONS'])
def get_images_after_cleaning():
    if request.method == 'OPTIONS':
        response = jsonify(success=True)
        return response
    params = request.json
    uri = params.get('file')
    fileName = uri.split('/')[-1].split('.')[0]
    imageNames = []
    df = pd.read_csv(uri)
    # Iterate through columns and create plots dynamically
    for column in df.columns:
        plt.figure()  # Create a new figure for each plot

        if pd.api.types.is_numeric_dtype(df[column]):
            # Create a scatter plot for numeric columns
            scatter_matrix(df[[column]], alpha=0.8, figsize=(5, 5), diagonal='hist')
        else:
            # Create a bar plot for categorical columns
            df[column].value_counts().plot(kind='bar', title=f'{column} Distribution')

        # Save the plot as an image file
        imageName = 'a{}_{}_plot.png'.format(fileName, column)
        imageNames.append(imageName)
        plt.savefig('{}{}'.format(EXPORT_PATH,imageName))
        plt.close()
    response = jsonify({"imageNames": imageNames})

    return response


@api.route('/', methods=['OPTIONS'])
def options():
    response = jsonify(success=True)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


if __name__ == '__main__':
    api.run()