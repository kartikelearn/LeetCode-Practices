import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # counts = person.groupby('email').size()
    # result = counts[counts > 1]

    # return result.reset_index()[['email']].rename(
    #     columns={'email': 'Email'}
    # )
# Gonna try using inbuilt functions
    return person[person.duplicated('email')][['email']].drop_duplicates().rename(columns={'email':'Email'})