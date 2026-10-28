import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs["prev1"] = logs["num"].shift(1)
    logs["prev2"] = logs["num"].shift(2)

    consecutive_data= logs[(logs["num"] == logs["prev1"]) & (logs["num"] == logs["prev2"])]
    return consecutive_data[["num"]].drop_duplicates().rename(columns={"num": "ConsecutiveNums"})