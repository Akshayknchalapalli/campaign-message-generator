import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def preprocess_data(df):
    train_data , test_data = train_test_split(df, test_size=0.2, random_state=42)
    return train_data, test_data
