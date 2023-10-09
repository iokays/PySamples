#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


titanic = pd.read_csv('./exercise_data/train.csv')
print(titanic.head())
print(titanic.set_index('PassengerId').head())

males = (titanic['Sex'] == 'male').sum()
females = (titanic['Sex'] == 'female').sum()

proportions = [males, females]

plt.pie(
    proportions,
    labels=['Males', 'Females'],

    # with no shadows
    shadow=False,
    # with colors
    colors=['blue', 'red'],
    # with one slide exploded out
    explode=(0.15, 0),

    # with the start angle at 90%
    startangle=90,

    # with the percent listed as a fraction
    autopct='%1.1f%%'
)


# View the plot drop above
plt.axis('equal')

# Set labels
plt.title("Sex Proportion")

# View the plot
plt.tight_layout()
plt.show()



# 运行以下代码
# sort the values from the top to the least value and slice the first 5 items
df = titanic.Fare.sort_values(ascending = False)

# create bins interval using numpy
binsVal = np.arange(0,600,10)

# create the plot
plt.hist(df, bins = binsVal)

# Set the title and labels
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare Payed Histrogram')

# show the plot
plt.show()












