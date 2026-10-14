# It would be written like this..
# import pandas as pd
# person_table=pd.DataFrame(columns=["personId","lastName","firstName"],index=["1","2"])
# address_table=pd.DataFrame(columns=["addressId","personId","city","state"],index=["1","2"])
# result_table=pd.merge(person_table,address_table,on="personId",how="left")
# return result_table[["firstName","lastName","city","state"]]

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person, address, on="personId", how="left")

    return result[["firstName", "lastName", "city", "state"]]
    