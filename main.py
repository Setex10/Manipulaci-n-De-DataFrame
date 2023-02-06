import pandas as pd
import numpy as np
import re
from package.mod_one import change_value

path = "C:\\Users\\pedro\\Documents\\Programación\\Curso\\Platzi\\ManipulaciónTransformaciónDatosPandaMumPy\\project_new\\amazon.csv"
data = pd.read_csv(path)

#Inecessary data
data = data.drop([
    "img_link", "product_link", "about_product", 
    "review_title", "review_content", "user_name", 
    "review_id", "user_id"
    ], axis=1)

#Only data I used
data_important = data[
    ["product_name", "actual_price", "discount_percentage",
    "discounted_price", "rating_count", "category"]
    ]

data_important.loc[:, ["actual_price", 
    "discount_percentage", 
    "discounted_price", 
    "rating_count"]] = change_value(
    data_important.loc[:, ["actual_price", 
        "discount_percentage", 
        "discounted_price", 
        "rating_count"] ],
    condition = [r"^₹", r",", r"%$"],
    value = "",
    regex = True
    ).astype(float)



data_important.loc[ : , "category"] = change_value(
    data_important.loc[ : , "category"],
    condition = {
        r"^Computers&Accessories.*": "Computer",
        r"^Electronics.*": "Electronics",
        r"^OfficeProducts.*": "Office",
        r"^Home&Kitchen.*": "Home&Kitchen",
        r"^HomeImprovement.*": "HomeImprovement",
        r"^Health&PersonalCare.*": "Health&PersonalCare",
        r"^MusicalInstruments.*": "MusicalInstruments",
        r"^Toys&Games.*": "Toys&Games",
        r"^Car&Motorbike.*" : "Car&Motorbike"
    },
    regex = True
)
#Mas caros
more_price = data_important.sort_values("actual_price", ascending=False)
print(more_price)

#Group by category and ordered by total price
group_total_price = data_important.groupby("category")["actual_price"].sum().sort_values(ascending=False)
print(group_total_price)

#Group by category and ordered by discount_percentage
group_discount_percentage = data_important.groupby("category")[
    "discount_percentage"
    ].agg(["count", "max", "sum"]).sort_values(by="sum", ascending=False)
print(group_discount_percentage)
