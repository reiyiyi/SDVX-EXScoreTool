import st_data

strengths_data = st_data.load_strengths_data()
ranking_data = st_data.load_ranking_data()
exscore_data = st_data.load_exscore_data()

column_list = list(exscore_data.columns)

for i in range(exscore_data.shape[0]):
    strengths_data.loc[i] = 999
    ranking_data.loc[i] = -1
    sort_data = list(exscore_data.loc[i])
    play_num = 0
    for j in range(exscore_data.shape[1]):
        if sort_data[j] > 0:
            play_num += 1
        sort_data[j] = {
            "ユーザーID":column_list[j],
            "EXスコア":sort_data[j]
        }
    sort_data.sort(reverse=True, key=lambda x: x["EXスコア"])

    for j in range(play_num - 1, -1, -1):
        ranking_data.loc[i, sort_data[j]["ユーザーID"]] = j + 1
        if j == play_num - 1:
            strengths_data.loc[i, sort_data[j]["ユーザーID"]] = 100.0
            continue
        if sort_data[j]["EXスコア"] == sort_data[j + 1]["EXスコア"]:
            strengths_data.loc[i, sort_data[j]["ユーザーID"]] = strengths_data.loc[i, sort_data[j + 1]["ユーザーID"]]
        else:
            strengths_data.loc[i, sort_data[j]["ユーザーID"]] = (j + 1) / play_num * 100

st_data.save_strengths_data(strengths_data)
st_data.save_ranking_data(ranking_data)