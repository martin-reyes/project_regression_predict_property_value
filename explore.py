import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_target_heatmap(df):
    plt.figure(figsize=(2,3))
    plt.title('Feature Correlations to Property Value', fontsize=10, pad=10)

    ax = sns.heatmap(df.corr()['property_value'].sort_values(ascending=False).to_frame().iloc[1:,:],
                     linewidths=.5, annot=True, cmap='RdYlGn', vmin=-1, vmax=1, square=True,
                    yticklabels=['SqFt', 'Bathrooms','Bedrooms','Age (years)'],
                    xticklabels=['Propety Value'])

    plt.tick_params(axis='both', which='both', bottom=False, left=False)

    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=6) 
    cbar.set_ticks([-1, -.5, 0, .5, 1])

    plt.show()

    
def plot_sqft_to_value(df):
    sns.lmplot(data=df, x='sqft', y='property_value', height=4,
               scatter_kws = {'s':.05},
               line_kws = {'linewidth':1, 'color':'#EE2222'})

    plt.title('More SqFt Leads to More Value', fontsize=9, pad=10)
    plt.xticks(ticks=np.arange(500, 5001, 500), fontsize=7)
    plt.xlabel('SqFt', fontsize=9)
    plt.yticks(ticks=np.arange(0, 1_500_001, 250_000),
               labels=['$ 0', '$ 250K', '$ 500K', '$ 750K', '$ 1M', '$ 1.25M', '$ 1.5M'],
               fontsize=7)
    plt.ylabel('Property\nValue', rotation=0, fontsize=9, labelpad=12)
    
    plt.show()

    
def plot_value_average_by_county(df, target, category):
    
    plt.figure(figsize=(4,3))
    
    target_label = ' '.join([word.capitalize() for word in target.split('_')])
    cat_label = ' '.join([word.capitalize() for word in category.split('_')])
    
    sns.barplot(data=df, x=category, y=target, errorbar=None,
            order=df.groupby(category)[target].mean().sort_values().index,
            palette=['#33CC33','#33BB33','#33AA33'])

    ax = plt.gca()
    for p in ax.patches:
        ax.annotate(f'$ {str(round(p.get_height(), -3))[:3]}K', 
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=8)

    plt.title(f'Average {target_label} by {cat_label}', fontsize=10, pad=10)

    plt.xlabel(cat_label, fontsize=8, labelpad=5)
    plt.xticks(fontsize=7)

    plt.ylabel('\n'.join([word.capitalize() for word in target.split('_')]),
               rotation=0, fontsize=8, labelpad=15)
    plt.yticks(ticks=np.arange(0, 600_001, 100_000),
               labels=['', '$ 100K', '$ 200K', '$ 300K', '$ 400K', '$ 500K', '$ 600K'],
               fontsize=7)

    plt.tick_params(axis='both', which='both', bottom=False, left=False)

    sns.despine()
    plt.show()
    
    
def plot_value_average_by_county(df, target, category):
    
    plt.figure(figsize=(4,3))
    
    target_label = ' '.join([word.capitalize() for word in target.split('_')])
    cat_label = ' '.join([word.capitalize() for word in category.split('_')])
    
    sns.barplot(data=df, x=category, y=target, errorbar=None,
            order=df.groupby(category)[target].mean().sort_values().index,
            color='#33AA33')

    ax = plt.gca()
    for p in ax.patches:
        ax.annotate(f'$ {str(round(p.get_height(), -3))[:3]}K', 
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=8)

    plt.title(f'Average {target_label} by {cat_label}', fontsize=10, pad=10)

    plt.xlabel(cat_label, fontsize=8, labelpad=5)
    plt.xticks(fontsize=7)

    plt.ylabel('\n'.join([word.capitalize() for word in target.split('_')]),
               rotation=0, fontsize=8, labelpad=15)
    plt.yticks(ticks=np.arange(0, 600_001, 100_000),
               labels=['', '$ 100K', '$ 200K', '$ 300K', '$ 400K', '$ 500K', '$ 600K'],
               fontsize=7)

    plt.tick_params(axis='both', which='both', bottom=False, left=False)

    sns.despine()
    plt.show()
    
    
def plot_value_average_by_bathrooms(df, target, category):
    
    plt.figure(figsize=(6,3))
    
    target_label = ' '.join([word.capitalize() for word in target.split('_')])
    cat_label = ' '.join([word.capitalize() for word in category.split('_')])
    
    sns.barplot(data=df, x=category, y=target, errorbar=None, color='#33AA33')

    ax = plt.gca()
    for p in ax.patches:
        ax.annotate(f'$ {str(round(p.get_height(), -3))[:3]}K', 
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=8)

    plt.title(f'Average {target_label} by {cat_label}', fontsize=10, pad=10)

    plt.xlabel(cat_label, fontsize=8, labelpad=5)
    plt.xticks(fontsize=7)

    plt.ylabel('\n'.join([word.capitalize() for word in target.split('_')]),
               rotation=0, fontsize=8, labelpad=15)
    plt.yticks(ticks=np.arange(0, 900_001, 100_000),
               labels=['', '$ 100K', '$ 200K', '$ 300K', '$ 400K', '$ 500K',
                       '$ 600K', '$ 700K', '$ 800K', '$ 900K'],
               fontsize=7)

    plt.tick_params(axis='both', which='both', bottom=False, left=False)

    sns.despine()
    plt.show()

    
def plot_value_average_by_bedrooms(df, target, category):
    
    plt.figure(figsize=(6,3))
    
    target_label = ' '.join([word.capitalize() for word in target.split('_')])
    cat_label = ' '.join([word.capitalize() for word in category.split('_')])
    
    sns.barplot(data=df, x=category, y=target, errorbar=None, color='#33AA33')

    ax = plt.gca()
    for p in ax.patches:
        ax.annotate(f'$ {str(round(p.get_height(), -3))[:3]}K', 
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=8)

    plt.title(f'Average {target_label} by {cat_label}', fontsize=10, pad=10)

    plt.xlabel(cat_label, fontsize=8, labelpad=5)
    plt.xticks(fontsize=7)

    plt.ylabel('\n'.join([word.capitalize() for word in target.split('_')]),
               rotation=0, fontsize=8, labelpad=15)
    plt.yticks(ticks=np.arange(0, 650_001, 100_000),
               labels=['', '$ 100K', '$ 200K', '$ 300K', '$ 400K', '$ 500K',
                       '$ 600K'],
               fontsize=7)

    plt.tick_params(axis='both', which='both', bottom=False, left=False)

    sns.despine()
    plt.show()