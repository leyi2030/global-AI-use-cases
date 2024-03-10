from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read data from Excel with filters
data = pd.read_excel('Global AI use cases in FS.xlsx', sheet_name='Credentials', 
                     usecols=['Area', 'FS Function', 'Solution Name (Max 5 words)', 
                              'Short Description', 'File Link', 'Data/AI Implementation', 'Cred Quality'],
                     dtype={'File Link': str})
data = data[(data['Data/AI Implementation'] == 'Y') & 
            (data['Cred Quality'].isin(['2-Credential Only', '3-Useful Content', '4-Quantified Benefit']))]

# Rename columns
data.rename(columns={'Area': 'Area', 'FS Function': 'Function', 
                     'Solution Name (Max 5 words)': 'Capabilities', 
                     'Short Description': 'Description', 
                     'File Link': 'Link'}, inplace=True)

# Organize data into a nested structure
areas_functions = data.groupby(['Area', 'Function'])

@app.route('/')
def index():
    areas = list(set(data['Area']))
    return render_template('index.html', areas=areas)

@app.route('/area/<area_name>')
def area(area_name):
    functions = list(set(data[data['Area'] == area_name]['Function']))
    return render_template('area.html', area_name=area_name, functions=functions)

@app.route('/function/<function_name>')
def function(function_name):
    projects = data[data['Function'] == function_name].to_dict(orient='records')
    return render_template('function.html', function_name=function_name, projects=projects)

if __name__ == '__main__':
    app.run(debug=True)

