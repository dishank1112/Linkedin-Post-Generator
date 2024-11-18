import json

import pandas as pd


class FewShotPosts:
    def __init__(self,filepath="data/process_data.json"):
        self.df = None
        self.Unique_tags=None
        self.load_posts(filepath)

    def load_posts(self,file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df=pd.json_normalize(posts)
            self.df["length"] = self.df["line_cnt"].apply(self.categorize_len)
            all_tags=self.df['tags'].apply(lambda x:x).sum()
            self.unique_tags = set(list(all_tags))

    def categorize_len(self,line_cnt):
        if line_cnt<5:
            return "Short"
        if 5<= line_cnt < 10:
            return "Medium"
        if line_cnt >= 10:
            return "Long"

    def get_tags(self):
        return self.unique_tags

    def get_filtered_posts(self, length, language, p):
        df_filtered = self.df[
            (self.df['language'] == language) &
            (self.df['length'] == length) &
            (self.df['tags'].apply(lambda tags: p in tags))
            ]
        return df_filtered.to_dict(orient="records")

if __name__ == "__main__":
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("Long","English","Leadership")
    print(posts)