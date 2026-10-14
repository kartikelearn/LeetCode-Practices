import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee=employee["salary"].drop_duplicates()
    employee=employee.sort_values(ascending=False)
    if len(employee)>=N & N>0:
        return pd.DataFrame({f"getNthHighestSalary({N})":[employee.iloc[N-1]]})
    else:
        return pd.DataFrame({f"getNthHighestSalary({N})":[None]})