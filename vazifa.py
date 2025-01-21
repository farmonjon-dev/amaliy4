import pandas as pd
import numpy as np
import gzip

# Ma'lumotlarim
data = {
    'Ism': ['Ali', 'Diyorbek', 'Olim', 'Shahzod', 'Zaynab'],
    'Yosh': [21, 20, 22, 20, 23],
    'Qabul_sanasi': ['2021-09-01', '2022-02-15', '2021-05-10', '2022-01-20', '2021-08-25']
}

group_df = pd.DataFrame(data)

# -------------------------
# Siqish 
with gzip.open('guruh.csv.gz', 'wt', encoding='utf-8') as f:
    group_df.to_csv(f, index=False)

print("Guruh ro'yxati siqilib saqlandi.")

# ----------------------------------
# Siqilgan faylni ochish
with gzip.open('guruh.csv.gz', 'rt', encoding='utf-8') as f:
    group_df_loaded = pd.read_csv(f)

print("Siqilgan guruh ro'yxati ochildi:")
print(group_df_loaded)
