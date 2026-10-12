import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df=pd.read_csv("students_record.csv")
# print(df.shape)

first_three_rows=df.head(3)
first_three_rows_flipped=first_three_rows.T
# print(first_three_rows)
# print(first_three_rows_flipped)

#see what columns exist, and what you are predicting

column_names=df.columns.tolist()
# print(column_names)
target_values=df["placed"].unique()
# print(target_values)

#check for duplicates values

duplicate_count=df.duplicated().sum()
# print(duplicate_count)

#check a column data
cgpa_dtype=df["cgpa"].dtype 
# print(cgpa_dtype)
# print(df.info())

#to check how many diff values a category column has

branch_variety=df["branch"].nunique()
# print(branch_variety)

#sanity check every numeric column range
#describe() computes -> mean, max, count etc

summary_stats=df.describe()
summary_stats_flipped=summary_stats.T
# print(summary_stats_flipped)


#remove the duplicates
df=df.drop_duplicates()
# print(df.shape)


#fix cgpa column


cgpa_text=df["cgpa"]
cgpa_with_dots=cgpa_text.str.replace(",",".")
cgpa_with_numbers=cgpa_with_dots.astype(float)
df["cgpa"]=cgpa_with_numbers

# print(df["cgpa"].dtype)

#map abbrevations to one consistent name

canonical_branch_names={
    "cse":"cse",
    "computer science":"cse",
    "c.s.e":"cse",
    "CSE":"cse",
    "C.S.E":"cse",
    "Cse":"cse",
    "it":"it",
    "i.t.":"it",
    "information technology":"it",
    "ece":"ece",
    "electronics":"ece",
    "eee":"eee",
    "electrical":"eee",
    "mech":"mech",
    "mechanical":"mech",
    "civil":"civil"
}

def get_canonical_branch(branch_name):
    branch_name = branch_name.strip().lower()  # Only added line
    if branch_name in canonical_branch_names:
        return canonical_branch_names[branch_name]
    return branch_name

df["branch"]=df["branch"].map(get_canonical_branch)

branch_counts=df["branch"].value_counts()
# print(branch_counts)


#turn imposible values into missing values
df.loc[df["attendance_percent"]>100,"attendance_percent"]=np.nan
df.loc[df["cgpa"]>10,"cgpa"]=np.nan
df.loc[df["salary_expectation"]>5000000,"salary_expectation"]=np.nan
df.loc[df["coding_problems_solved"]>1000,"coding_problems_solved"]=np.nan
# print("outlier cleanup done")

#lets see how  much data is missing

missing_per_column=df.isna().sum()
# print(missing_per_column)

#lets fill missing values
#handle numeric ones

numeric_columns_with_gaps=[
    "attendance_percent",
    "communication_skill",
    "tech_events_attended",
    "salary_expectation",
    "cgpa",
    "coding_problems_solved"
]

for column_name in numeric_columns_with_gaps:
    column_median=df[column_name].median()
    df[column_name]=df[column_name].fillna(column_median)
# print("Numeric values filled")

#categrical values
df["city"]=df["city"].fillna("Unknown")

remaining_missing=df.isna().sum()
total_missing=remaining_missing.sum()
# print(total_missing)

#check the target class balance
placement_counts=df["placed"].value_counts()
# print(placement_counts)



placement_proportions=df["placed"].value_counts(normalize=True)
placement_percentages=placement_proportions*100
placement_percentages_rounded=placement_percentages.round(1)
# print(placement_percentages_rounded)


#lets compare feature average between the outcomes  

grouped_by_placement=df.groupby("placed")
selected_columns=grouped_by_placement[["cgpa","attendance_percent","coding_problems_solved"]]
group_averages_rounded=selected_columns.mean().round(2)
# print(group_averages_rounded)

#compare placement rate across a category

internship_vs_placement_rounded=pd.crosstab(df["internship"],df["placed"], normalize="index").round(2)
print(internship_vs_placement_rounded)

#drop columns that can not help our Model

column_to_drop=["student_id","name","registration_date"]
model_df=df.drop(columns=column_to_drop)


#turn categorical column into numbers
categorical_columns=["gender","branch","city","internship","has_backlog"]
model_df=pd.get_dummies(model_df,columns=categorical_columns,drop_first=True)
# print(model_df)


#separate features(X) from the target (Y)

target_map={"No":0,"Yes":1}

Y=model_df["placed"].map(target_map)
X=model_df.drop(columns=["placed"])
# print(Y.shape)
# print(X.shape)


#split into a training set and a testing set

X_train, X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2, random_state=42, stratify=Y)


# print(X_train.shape)
# print(X_test.shape)

#scaling
#model train
#test
#deploy - fast api, flask

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)

X_test_scaled=scaler.transform(X_test)

print("Scalling completed")

model=LogisticRegression()

model.fit(X_train_scaled,Y_train)

y_pred=model.predict(X_test_scaled)
# print("This is prediction")
# print(y_pred)
# print("This is  reality")
# print(Y_test)

accuracy=accuracy_score(Y_test,y_pred)
print(accuracy)



gender = input("Gender (Male/Female): ").strip().title()

branch = input(
    "Branch (cse/it/ece/eee/mech/civil): "
).strip().lower()

city = input("City: ").strip().title()

cgpa = float(input("CGPA: "))

attendance = float(
    input("Attendance percentage: ")
)

technical_skills = int(
    input("Technical skills rating: ")
)

projects_completed = int(
    input("Projects completed: ")
)

coding_problems = int(
    input("Coding problems solved: ")
)

communication_skill = float(
    input("Communication skill rating: ")
)

internship = input(
    "Internship (Yes/No): "
).strip().title()

has_backlog = input(
    "Has backlog (Yes/No): "
).strip().title()

tech_events = float(
    input("Tech events attended: ")
)

salary_expectation = float(
    input("Salary expectation: ")
)


new_student = {
    "gender": gender,
    "branch": branch,
    "city": city,
    "cgpa": cgpa,
    "attendance_percent": attendance,
    "technical_skills": technical_skills,
    "projects_completed": projects_completed,
    "coding_problems_solved": coding_problems,
    "communication_skill": communication_skill,
    "internship": internship,
    "has_backlog": has_backlog,
    "tech_events_attended": tech_events,
    "salary_expectation": salary_expectation,
}

new_student_df = pd.DataFrame([new_student])
# print(new_student_df.head())

new_student_encoded=pd.get_dummies(
    new_student_df,
    columns=categorical_columns,
)

new_student_encoded=new_student_encoded.reindex(
    columns=X.columns,
    fill_value=0
)

new_student_scaled=scaler.transform(
    new_student_encoded
)

prediction=model.predict(new_student_scaled)
print("Prediction : ",prediction[0])