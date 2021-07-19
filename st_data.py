import os
import json
import pandas as pd

BASE_DIR = 'data'

#effect_id.json
def load_effect_id_data():
    FILE_NAME = BASE_DIR + '/effect_id.json'
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, encoding='utf-8') as f:
        return json.load(f)

#rev_effect_id.csv
def load_rev_effect_id_data():
    FILE_NAME = BASE_DIR + '/rev_effect_id.csv'
    if not os.path.exists(FILE_NAME):
        return []
    return pd.read_csv(FILE_NAME)

#EXscore.csv
def load_exscore_data():
    FILE_NAME = BASE_DIR + '/EXscore.csv'
    if not os.path.exists(FILE_NAME):
        return []
    return pd.read_csv(FILE_NAME)

def save_exscore_data(save_data):
    FILE_NAME = BASE_DIR + '/EXscore.csv'
    save_data.to_csv(FILE_NAME, index=False)

#user_data.json
def load_user_data():
    FILE_NAME = BASE_DIR + '/user_data.json'
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, encoding='utf-8') as f:
        return json.load(f)

def save_user_data(save_data):
    FILE_NAME = BASE_DIR + '/user_data.json'
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(save_data, f, ensure_ascii=False, indent=4)