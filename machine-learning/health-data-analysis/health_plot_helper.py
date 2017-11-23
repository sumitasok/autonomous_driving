import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

AGE_GROUPS = ['< 18', '18 - 29', '30 - 49', '50 - 79', '> 70']

def ageGroup(age):
    if age == np.NaN:
        return np.NaN
    if age < 18:
        return '< 18'
    if 18 <= age < 30:
        return '18 - 30'
    if 30 <= age < 50:
        return '30 - 50'
    if 50 <= age < 70:
        return '50 - 70'
    if age > 70:
        return '> 70'

def diag_gender_bar_graph(data):
    '''
        https://matplotlib.org/examples/pylab_examples/bar_stacked.html
    '''
    _total = data['Gender'].count()
    totalGender = data[['Gender']].groupby('Gender')['Gender'].count()
    diagStatGender = data[['Gender', 'Diagnostics Status']].groupby(['Gender', 'Diagnostics Status'])['Gender'].count()

    N = 2
    ready = (diagStatGender['Male']['ready'], diagStatGender['Female']['ready'])
    total = (totalGender['Male'] - diagStatGender['Male']['ready'], totalGender['Female'] - diagStatGender['Female']['ready'])

    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, ready, width, color='#d62728')
    p2 = plt.bar(ind, total, width,
                 bottom=ready)

    plt.ylabel('Count')
    plt.title('Count by status and gender')
    plt.xticks(ind, ('Men', 'Women'))
    plt.yticks(np.arange(0, _total, 1000))
    plt.legend((p1[0], p2[0]), ('Participated', 'Total per gender'))

def bloodGroupDistrib(data):
    tab = pd.crosstab([data.Gender],
            [data['Blood Group']],
           margins=False)
    tab = tab.drop('nan', axis=1)
    # tab = tab.sort_values('+', ascending=False)
    return tab.style.background_gradient(cmap='summer_r')

def severityByAgeGroup(data, severity):
    return pd.crosstab([data.Gender, data.AgeGroup],
            [data[severity]],
           margins=True).style.background_gradient(cmap='summer_r').set_properties(**{'border-color': 'black'})

def severityByBloodGroup(data, severity):
    return pd.crosstab([data.Gender, data['Blood Group']],
            [data[severity]],
           margins=True).style.background_gradient(cmap='summer_r').set_properties(**{'border-color': 'black'})

def severityByAgeBarGraph(data, severity, ax = None):
    '''
    https://stackoverflow.com/questions/43544694/using-pandas-crosstab-with-seaborn-stacked-barplots
    '''
    ct = pd.crosstab(data.AgeGroup, data[severity])
    stacked = ct.stack().reset_index().rename(columns={0:'value'})
    print(stacked)
    if ax == None:
        return sns.barplot(x=stacked.AgeGroup, y=stacked.value, hue=stacked[severity])
    else:
        return sns.barplot(x=stacked.AgeGroup, y=stacked.value, hue=stacked[severity], ax = ax)

def severityByAgeAndGenderBarGraph(data, severity, ax = None):
    '''
    https://stackoverflow.com/questions/43544694/using-pandas-crosstab-with-seaborn-stacked-barplots
    '''
    ct = pd.crosstab([data.AgeGroup, data.Gender], data[severity], )
    stacked = ct.stack().reset_index().rename(columns={0:'value'})
    print(stacked)
    if ax == None:
        return sns.barplot(x=stacked.AgeGroup, y=stacked.value, hue=stacked[severity]).set_title("AgeGroup by Gender")
    else:
        return sns.barplot(x=stacked.AgeGroup, y=stacked.value, hue=stacked[severity], ax = ax).set_title("AgeGroup by Gender")

def severityCrossTab(data, severities):
    return pd.crosstab([data.Gender, data.AgeGroup],
            severities,
           margins=True).style.background_gradient(cmap='summer_r').set_properties(**{'border-color': 'black'})