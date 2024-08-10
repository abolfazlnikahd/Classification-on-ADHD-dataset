# cleaning data

import pandas as pd
#import matplotlib as mtp
import numpy as np
from sklearn.preprocessing import LabelEncoder




# drop the useless columns


# find adhd
def adhd_rows(dr) -> None:
    dr['if_yes_please_list_these_difficulties_and_or_symptoms'] = dr['if_yes_please_list_these_difficulties_and_or_symptoms'].apply(lambda x: 'adhd' if 'adhd' in str(x) else 'no')
    dr['if_you_have_been_diagnosed_formally_or_informally_please_list_the_diagnosis_diagnoses'] = dr['if_you_have_been_diagnosed_formally_or_informally_please_list_the_diagnosis_diagnoses'].apply(lambda x: 'adhd' if 'adhd' in str(x) else 'no')

# cleaning data
def cleaning(dr) -> None:
    dr.loc[dr['have_you_ever_been_diagnosed_with_a_mental_illness']=='no',['if_you_have_been_diagnosed_formally_or_informally_please_list_the_diagnosis_diagnoses']] = 'no'
    dr.loc[dr['have_you_ever_used_prescribed_psychiatric_medication_for_a_mental_illness_or_symptoms_of_one'] == 'not applicable', ['have_you_ever_used_prescribed_psychiatric_medication_for_a_mental_illness_or_symptoms_of_one']] = 'no'
    dr.loc[dr['are_you_currently_using_prescribed_psychiatric_medication_for_a_mental_illness_or_symptoms_of_one'] == 'not applicable', ['are_you_currently_using_prescribed_psychiatric_medication_for_a_mental_illness_or_symptoms_of_one']] = 'no'
    dr.loc[dr['have_you_ever_been_to_therapy_or_counselling_for_a_mental_illness_or_symptoms_of_one'] == 'not applicable', ['have_you_ever_been_to_therapy_or_counselling_for_a_mental_illness_or_symptoms_of_one']] = 'no'
    dr.loc[dr['are_you_currently_in_therapy_or_counselling_for_a_mental_illness_or_symptoms_of_one'] == 'not applicable', ['are_you_currently_in_therapy_or_counselling_for_a_mental_illness_or_symptoms_of_one']] = 'no'


# encoding columns
def encoding(dr) -> None:
    label = LabelEncoder()


    # test
    dr['mental_health_difficulties_experience_code'] = label.fit_transform(dr['have_you_ever_experienced_any_mental_health_difficulties_or_symptoms_before_starting_university_e_g_in_primary_or_high_school'])
    dr['sex_code'] = label.fit_transform(dr['sex'])
    dr['diagnosed_with_a_mental_illness_code'] = label.fit_transform(dr['have_you_ever_been_diagnosed_with_a_mental_illness'])
    dr['diagnosed_code'] = label.fit_transform(dr['if_you_have_been_diagnosed_formally_or_informally_please_list_the_diagnosis_diagnoses'])
    dr['used_prescribed_code'] = label.fit_transform(dr['have_you_ever_used_prescribed_psychiatric_medication_for_a_mental_illness_or_symptoms_of_one'])
    dr['using_prescribed_code'] = label.fit_transform(dr['are_you_currently_using_prescribed_psychiatric_medication_for_a_mental_illness_or_symptoms_of_one'])
    dr['been_to_therapy_code'] = label.transform(dr['have_you_ever_been_to_therapy_or_counselling_for_a_mental_illness_or_symptoms_of_one'])
    dr['currently_in_therapy_code'] = label.fit_transform(dr['are_you_currently_in_therapy_or_counselling_for_a_mental_illness_or_symptoms_of_one'])
    dr['nbt_completed_code'] = label.fit_transform(dr['nbt_completed'])

    # targets
    dr['difficulties_code'] = label.fit_transform(dr['if_yes_please_list_these_difficulties_and_or_symptoms'])

def main():
    # collecting data
    dr = pd.read_excel("ADHD.xlsx")

    # drop the useless columns
    drop_list = ["specify", "home_language", "aas_change", 'nbt_did_math', 'nbt_year',
                 'if_you_have_ever_experienced_difficulties_and_or_symptoms_of_a_mental_illness_how_old_were_you_when_this_started',

                 'was_this_diagnosis_made_before_or_after_you_left_high_school',
                 'if_you_have_been_diagnosed_with_a_mental_illness_at_what_age_was_this',

                 'bdi1_item_1', 'bdi1_item_2', 'bdi1_item_3', 'bdi1_item_4', 'bdi1_item_5', 'bdi1_item_6',
                 'bdi1_item_7',
                 'bdi1_item_8', 'bdi1_item_9', 'bdi1_item_10', 'bdi1_item_11', 'bdi1_item_12', 'bdi1_item_13',
                 'bdi1_item_14',
                 'bdi1_item_15', 'bdi1_item_16', 'bdi1_item_17', 'bdi1_item_18', 'bdi1_item_19', 'bdi1_item_20',
                 'bdi1_item_21',

                 'audit1_item_1', 'audit1_item_2', 'audit1_item_3', 'audit1_item_4', 'audit1_item_5',
                 'audit1_item_6', 'audit1_item_7', 'audit1_item_8', 'audit1_item_9',

                 'aas1_item_1', 'aas1_item_2', 'aas1_item_3', 'aas1_item_4',
                 'aas1_item_5', 'aas1_item_6', 'aas1_item_7', 'aas1_item_8', 'aas1_item_9',

                 'asrs1_item_1', 'asrs1_item_2', 'asrs1_item_3', 'asrs1_item_4',
                 'asrs1_item_5', 'asrs1_item_6', 'asrs1_item_7', 'asrs1_item_8',
                 'asrs1_item_9', 'asrs1_item_10', 'asrs1_item_11', 'asrs1_item_12',
                 'asrs1_item_13', 'asrs1_item_14', 'asrs1_item_15', 'asrs1_item_16',
                 'asrs1_item_17', 'asrs1_item_18',

                 'bai1_item_1', 'bai1_item_2', 'bai1_item_3', 'bai1_item_4', 'bai1_item_5', 'bai1_item_6',
                 'bai1_item_7',
                 'bai1_item_8', 'bai1_item_9', 'bai1_item_10', 'bai1_item_11', 'bai1_item_12', 'bai1_item_13',
                 'bai1_item_14',
                 'bai1_item_15', 'bai1_item_16', 'bai1_item_17', 'bai1_item_18', 'bai1_item_19', 'bai1_item_20',
                 'bai1_item_21',
                 ]

    dr.drop(drop_list, axis=1, inplace=True)
    dr.drop([505], axis=0, inplace=True)

    adhd_rows(dr)
    cleaning(dr)
    encoding(dr)

    # drop *****
    drop_list= ['age',
                'sex',
                'have_you_ever_experienced_any_mental_health_difficulties_or_symptoms_before_starting_university_e_g_in_primary_or_high_school',
                'if_yes_please_list_these_difficulties_and_or_symptoms',
        'nbt_completed',
        'have_you_ever_been_diagnosed_with_a_mental_illness',
        'if_you_have_been_diagnosed_formally_or_informally_please_list_the_diagnosis_diagnoses',

        'have_you_ever_used_prescribed_psychiatric_medication_for_a_mental_illness_or_symptoms_of_one',
        'are_you_currently_using_prescribed_psychiatric_medication_for_a_mental_illness_or_symptoms_of_one',

        'have_you_ever_been_to_therapy_or_counselling_for_a_mental_illness_or_symptoms_of_one',
        'are_you_currently_in_therapy_or_counselling_for_a_mental_illness_or_symptoms_of_one',]
    dr.drop(drop_list, axis=1, inplace=True)
    return  dr

if __name__ == "__main__":

    df = main()
    df = pd.DataFrame(df)
    df.to_excel("Lastـchange.xlsx", index=False)

