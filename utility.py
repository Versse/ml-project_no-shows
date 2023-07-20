import pandas as pd

#data_path = '/home/tegbe/2023 dev projects/well-test/ml-project_no-shows/data_set/KaggleV2-May-2016 (1).csv'

def get_data(data_path):
    no_shows_df = pd.read_csv(data_path)
    return no_shows_df


def features_selection_v1(df):
    #selected features 
    input_columns = ['Gender', 'Age', 'Scholarship', 'Hipertension', 'Diabetes', 'Alcoholism', 'Handcap', 'SMS_received']
    output_column = ['No-show']

    X = df[input_columns]  
    y = df[output_column]
    return X, y