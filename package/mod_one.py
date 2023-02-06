import pandas as pd
import re

def change_name_column():
    pass

def change_value(data: pd.DataFrame ,
                condition: list | dict, 
                value: dict | list | str | re.RegexFlag = None, 
                regex: bool=False,
                inplace: bool=False
                ) -> pd.DataFrame:
    """Change the value

    Args:
    ---------
        * data (DataFrame): Data from DataFrame
        * condition (List or Dict): List or Dict of conditions: \n
            Example of Dict: {"condition": "New Value"}. If is a dictionary, don't pass a value argument \n
            Example of List: ["condition", "condition", ...]. If is a List, is necessary to pass a value argument
        * value (scalar, dict, list, str, regex, default None): _description_. Defaults to None.
        * regex (bool, optional): _description_. Defaults to False.

    Returns:
    ---------
        DataFrame: return a filter DataFrame with the conditions
    """
    if type(condition) == type({}):
        return data.replace(to_replace = condition, regex = regex, inplace = inplace)

    return data.replace(to_replace=condition, value=value, regex=regex, inplace = inplace)

if __name__ =='__main__':
    print("This is a module")