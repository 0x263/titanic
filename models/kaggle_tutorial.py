'''
VARIABLE DESCRIPTIONS:
survival        Survival
                (0 = No; 1 = Yes)
pclass          Passenger Class
                (1 = 1st; 2 = 2nd; 3 = 3rd)
name            Name
sex             Sex
age             Age
sibsp           Number of Siblings/Spouses Aboard
parch           Number of Parents/Children Aboard
ticket          Ticket Number
fare            Passenger Fare
cabin           Cabin
embarked        Port of Embarkation
                (C = Cherbourg; Q = Queenstown; S = Southampton)

SPECIAL NOTES:
Pclass is a proxy for socio-economic status (SES)
 1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower

Age is in Years; Fractional if Age less than One (1)
 If the Age is Estimated, it is in the form xx.5

With respect to the family relation variables (i.e. sibsp and parch)
some relations were ignored.  The following are the definitions used
for sibsp and parch.

Sibling:  Brother, Sister, Stepbrother, or Stepsister of Passenger Aboard Titanic
Spouse:   Husband or Wife of Passenger Aboard Titanic (Mistresses and Fiances Ignored)
Parent:   Mother or Father of Passenger Aboard Titanic
Child:    Son, Daughter, Stepson, or Stepdaughter of Passenger Aboard Titanic

Other family relatives excluded from this study include cousins,
nephews/nieces, aunts/uncles, and in-laws.  Some children travelled
only with a nanny, therefore parch=0 for them.  As well, some
travelled with very close friends or neighbors in a village, however,
the definitions do not support such relations.
'''

import csv as csv
import numpy as np
import pandas as pd
import matplotlib as plt

training_file_object = csv.reader(open('../data/train.csv'))
test_file_object = csv.reader(open('../data/test.csv'))

training_header = next(training_file_object)
training_data = list(training_file_object)

test_header = next(test_file_object)
test_data = list(test_file_object)

training_data = np.array(training_data)

number_passengers = np.size(training_data[0::, 1].astype(np.float))
number_survived = np.sum(training_data[0::, 1].astype(np.float))
proportion_survivors = number_survived / number_passengers

df = pd.read_csv("../data/train.csv", header=0)

# Map Gender to 1 (male) or 0 (female)
df['Gender'] = df['Sex'].map({'female': 0, 'male': 1}).astype(int)

median_ages = np.zeros((2, 3))

df['AgeFill'] = df.Age

for i in range(2):
    for j in range(3):
        median_ages[i, j] = df[(df['Gender'] == i) & (
            df['Pclass'] == j + 1)]['Age'].dropna().median()

for i in range(2):
    for j in range(3):
        df.loc[(df.Age.isnull()) & (df.Gender == i) & (
            df.Pclass == j + 1), 'AgeFill'] = median_ages[i, j]

df['AgeIsNull'] = pd.isnull(df.Age).astype(int)
df['FamilySize'] = df.Parch + df.SibSp
df['Age*Class'] = df.AgeFill * df.Pclass
