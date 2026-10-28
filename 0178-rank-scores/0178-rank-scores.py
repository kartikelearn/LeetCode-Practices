import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)
    # scores["rank"] = scores["rank"].astype(int)
    # return scores[["score", "rank"]].sort_values(by="score", ascending=False)
    scores = scores.drop("id", axis = 1).sort_values(by='score', ascending=False)
    return scores