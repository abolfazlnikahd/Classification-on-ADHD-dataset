import pandas as pd
from imblearn.over_sampling import SMOTE

def resampling():
    # بارگذاری داده‌ها
    data = pd.read_excel('Lastـchange.xlsx')

    # جدا کردن ویژگی‌ها و برچسب‌ها
    X = data.drop('diagnosed_code', axis=1)
    y = data['diagnosed_code']


    # ایجاد نمونه‌های جدید با استفاده از SMOTE
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)

    return X_resampled, y_resampled
