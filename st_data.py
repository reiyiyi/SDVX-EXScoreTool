import os
import json
import pandas as pd
import boto3

#本番
#--------------------------------------------------------------------------------
BASE_DIR = 'data/'
MIRROR_DIR = 'mirror/'
#BASE_DIR = 'test_data/'

s3 = boto3.resource('s3',
                aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
                region_name=os.environ["REGION_NAME"])
bucket = s3.Bucket('sdvx-exscoretool')
#--------------------------------------------------------------------------------

'''#ローカル
#--------------------------------------------------------------------------------
BASE_DIR = 'local_data/'
MIRROR_DIR = 'local_data/'
#BASE_DIR = 'test_data/'

s3 = boto3.resource('s3')
bucket = s3.Bucket('sdvx-exscoretool')
#--------------------------------------------------------------------------------'''

#effect_id.json
def load_effect_id_data():
    FILE_NAME = 'effect_id.json'
    bucket.download_file(BASE_DIR + FILE_NAME, FILE_NAME)
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, encoding='utf-8') as f:
        return json.load(f)

#rev_effect_id.csv
def load_rev_effect_id_data():
    FILE_NAME = 'rev_effect_id.csv'
    bucket.download_file(BASE_DIR + FILE_NAME, FILE_NAME)
    if not os.path.exists(FILE_NAME):
        return []
    return pd.read_csv(FILE_NAME)

#EXscore.csv
def load_exscore_data():
    FILE_NAME = 'EXscore.csv'
    bucket.download_file(BASE_DIR + FILE_NAME, FILE_NAME)
    if not os.path.exists(FILE_NAME):
        return []
    return pd.read_csv(FILE_NAME)

def save_exscore_data(save_data):
    FILE_NAME = 'EXscore.csv'
    save_data.to_csv(FILE_NAME, index=False)
    bucket.upload_file(FILE_NAME, BASE_DIR + FILE_NAME)
    bucket.upload_file(FILE_NAME, MIRROR_DIR + FILE_NAME)

#old_EXscore.csv
def load_old_exscore_data():
    FILE_NAME = 'old_EXscore.csv'
    bucket.download_file(BASE_DIR + FILE_NAME, FILE_NAME)
    if not os.path.exists(FILE_NAME):
        return []
    return pd.read_csv(FILE_NAME)

def save_old_exscore_data(save_data):
    FILE_NAME = 'old_EXscore.csv'
    save_data.to_csv(FILE_NAME, index=False)
    bucket.upload_file(FILE_NAME, BASE_DIR + FILE_NAME)
    bucket.upload_file(FILE_NAME, MIRROR_DIR + FILE_NAME)

#user_data.json
def load_user_data():
    FILE_NAME = 'user_data.json'
    bucket.download_file(BASE_DIR + FILE_NAME, FILE_NAME)
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, encoding='utf-8') as f:
        return json.load(f)

def save_user_data(save_data):
    FILE_NAME = 'user_data.json'
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(save_data, f, ensure_ascii=False, indent=4)
    bucket.upload_file(FILE_NAME, BASE_DIR + FILE_NAME)
    bucket.upload_file(FILE_NAME, MIRROR_DIR + FILE_NAME)

#strengths.csv
def load_strengths_data():
    FILE_NAME = 'strengths.csv'
    bucket.download_file(BASE_DIR + FILE_NAME, FILE_NAME)
    if not os.path.exists(FILE_NAME):
        return []
    return pd.read_csv(FILE_NAME)

def save_strengths_data(save_data):
    FILE_NAME = 'strengths.csv'
    save_data.to_csv(FILE_NAME, index=False)
    bucket.upload_file(FILE_NAME, BASE_DIR + FILE_NAME)
    bucket.upload_file(FILE_NAME, MIRROR_DIR + FILE_NAME)

#ranking.csv
def load_ranking_data():
    FILE_NAME = 'ranking.csv'
    bucket.download_file(BASE_DIR + FILE_NAME, FILE_NAME)
    if not os.path.exists(FILE_NAME):
        return []
    return pd.read_csv(FILE_NAME)

def save_ranking_data(save_data):
    FILE_NAME = 'ranking.csv'
    save_data.to_csv(FILE_NAME, index=False)
    bucket.upload_file(FILE_NAME, BASE_DIR + FILE_NAME)
    bucket.upload_file(FILE_NAME, MIRROR_DIR + FILE_NAME)

#resister_error_data.json
def load_resister_error_data():
    FILE_NAME = 'resister_error_data.json'
    bucket.download_file(BASE_DIR + FILE_NAME, FILE_NAME)
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, encoding='utf-8') as f:
        return json.load(f)

def save_resister_error_data(save_data):
    FILE_NAME = 'resister_error_data.json'
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(save_data, f, ensure_ascii=False, indent=4)
    bucket.upload_file(FILE_NAME, BASE_DIR + FILE_NAME)
    bucket.upload_file(FILE_NAME, MIRROR_DIR + FILE_NAME)