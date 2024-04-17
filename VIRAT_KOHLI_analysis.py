#!/usr/bin/env python
# coding: utf-8

# # Kohli's Analysis  in IPL

# In[36]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[144]:


print('''
      Meet VIRAT KOHLI, a cricketing legend whose journey from humble beginnings to global stardom
      is nothing short of inspiring.
      With exceptional talent and unwavering determination, Kohli has etched his name in the annals of cricket history. 
      Join us as we delve into the remarkable story of India's cricketing icon, Virat Kohli.''')
from PIL import Image
# Open the images
img1 = Image.open('2.png')
img2 = Image.open('vk5.jpg')
# Plotting
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
# Display the images
axes[0].imshow(img1)
axes[0].axis('off')
axes[1].imshow(img2)
axes[1].axis('off')
plt.tight_layout()
plt.show()

# In[168]:


data=pd.read_csv("deliveries.csv")
data.head(3)


# # Total Runs by Virat Kohli

# In[39]:


total_runs_by_kohli = data.groupby('batsman').get_group('V Kohli')['batsman_runs'].sum()

print("Total runs by V Kohli:", total_runs_by_kohli)


# In[40]:


# Grouping th data by team and batsman
team_runs_by_batsman = data.groupby(['match_id', 'batsman'])['batsman_runs'].sum()

# Filter the data for runs scored by V Kohli
kohli_runs_by_team = team_runs_by_batsman.loc[:, 'V Kohli']

# Plotting
plt.figure(figsize=(32, 7))
kohli_runs_by_team.plot(kind='bar', color='skyblue', linewidth=2)  
plt.title('Runs scored by Virat Kohli in each match')
plt.xlabel('match_id')
plt.ylabel('batsman_runs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# # Total sixes by Virat Kohli

# In[43]:


# Grouing the data by batsman
kohli_data = data.groupby('batsman').get_group('V Kohli')

# Counting the number of sixes which scored by V Kohli
total_no_of_sixes_by_kohli = (kohli_data['batsman_runs'] == 6).sum()
#displaying
print("Total sixes  by V Kohli:", total_no_of_sixes_by_kohli)



# # Total four by virat kohli

# In[44]:


# Grouping the data by batsman
kohli_data = data.groupby('batsman').get_group('V Kohli')

# Counting the number of FOUR which scored by V Kohli
total_no_of_FOUR_by_kohli = (kohli_data['batsman_runs'] == 4).sum()
#displaying
print("Total FOUR  by V Kohli:", total_no_of_FOUR_by_kohli)


# In[129]:


# Grouping the data by 'batsman'
kohli_data = data.groupby('batsman').get_group('V Kohli')

# Counting  the number of sixes and fours scored by V Kohli
sixes = (kohli_data['batsman_runs'] == 6).sum()
fours = (kohli_data['batsman_runs'] == 4).sum()
# Data for the pie chart
labels = ['Sixes', 'Fours']
sizes = [sixes, fours]
colors = ['blue', 'red']
# Plotting the pie chart
plt.figure(figsize=(8, 3))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Sixes and Fours by Virat Kohli')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[48]:


# Count the number of sixes scored by each batsman
sixes_by_batsman = data[data['batsman_runs'] == 6]['batsman'].value_counts()

# Get the top 5 batsmen
top_six_hitters = sixes_by_batsman.head(5)

# Print the top 5 batsmen
print("Top 5 players who hit the most sixes:")
print(top_six_hitters)


# In[132]:


# Count the number of sixes scored by each batsman
sixes_by_batsman = data[data['batsman_runs'] == 6]['batsman'].value_counts()

# Get the top 5 batsmen
top_six_hitters = sixes_by_batsman.head(5)

# Plotting the no of sixes hit by the top 5 batsmen using a pie chart
plt.figure(figsize=(5, 5))
plt.pie(top_six_hitters, labels=top_six_hitters.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 5 players with most sixes')
plt.axis('equal')  
plt.show()





# In[130]:


#  Virat Kohli's entries
vk = data[data['batsman'] == 'V Kohli']

# counting of each type of run scored by Virat Kohli
one_runs = vk[vk['batsman_runs'] == 1]['batsman'].count()
two_runs = vk[vk['batsman_runs'] == 2]['batsman'].count()
three_runs = vk[vk['batsman_runs'] == 3]['batsman'].count()
four_runs = vk[vk['batsman_runs'] == 4]['batsman'].count()
six_runs = vk[vk['batsman_runs'] == 6]['batsman'].count()

# Ploting the runs scored by Virat Kohli using an area plot
plt.figure(figsize=(8, 5))

# Creating lists x and y axis
runs_labels = ['1 Run', '2 Runs', '3 Runs', '4 Runs', '6 Runs']
runs_values = [one_runs, two_runs, three_runs, four_runs, six_runs]

# Plot the area plot
plt.stackplot(runs_labels, runs_values, colors=['orange'])
plt.xlabel('Runs')
plt.ylabel('Frequency')
plt.title("Virat Kohli's Runs Distribution")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



# In[133]:


#  Virat Kohli's entries
vk = data[data['batsman'] == 'V Kohli']

# Calculate runs scored by Virat Kohli
runs_scored = vk['batsman_runs'].sum()

# Calculate balls faced by Virat Kohli
balls_faced = len(vk)

# Calculate strike rate
strike_rate = (runs_scored / balls_faced) * 100

print("Virat Kohli's batting strike rate:", strike_rate)


# # Virat Kohli runs distribution in each over

# In[134]:


# Filter data for Virat Kohli's entries
vk = data[data['batsman'] == 'V Kohli']

# Calculate runs scored by Virat Kohli in each over
runs_in_each_over = vk.groupby(['over'])['batsman_runs'].sum()

# Plot the runs scored by Virat Kohli in each over using a pie chart
plt.figure(figsize=(8, 8))
plt.pie(runs_in_each_over, labels=runs_in_each_over.index, autopct='%1.1f%%', startangle=140)
plt.title("Virat Kohli's Runs Distribution by Over")
plt.axis('equal') 
plt.show()



# # #Wickets 

# In[135]:


# finding where virat kohli loses their wickets
vk_outs = data[(data['player_dismissed'] == 'V Kohli') & (data['dismissal_kind'] != 'run out')]

# Counting of each bowler who take Virat Kohli's wicket
bowlers = vk_outs['bowler'].value_counts()

# all bowlers who took wickets
print("Bowlers who have taken Virat Kohli's wicket:")
print(bowlers)


# In[158]:


# checking Virat Kohli's wickets
vk_wickets = data[data['batsman'] == 'V Kohli']

# Filter the specified wickets kinds
specified_wickets = ['caught', 'bowled', 'run out', 'lbw', 'stumped', 'caught and bowled']
filtered_wickets = vk_wickets[vk_wickets['dismissal_kind'].isin(specified_wickets)]

# Group by wickets kind and count occurrences
wickets_counts = filtered_wickets['dismissal_kind'].value_counts()

# using color palette
colors = plt.cm.tab10.colors
# Plotting
plt.figure(figsize=(8, 6))
plt.pie(wickets_counts, labels=wickets_counts.index, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops=dict(width=0.3))
plt.title('Wickets Kinds of Virat Kohli')
plt.axis('equal')  
plt.show()


# In[137]:


# Grouping the data by match ID and batting team,and total run by each team
total_runs_by_team = deliveries_data.groupby(['match_id', 'batting_team'])['total_runs'].sum().reset_index()

print(total_runs_by_team)


# In[138]:


# Read the deliveries CSV file into a DataFrame
deliveries_data = pd.read_csv('deliveries.csv')

# Grouping the data by batting team and total runs by each team
total_runs_by_team = deliveries_data.groupby('batting_team')['total_runs'].sum()

# Reverse the order of teams 
total_runs_by_team = total_runs_by_team[::-1]

# set colors for each team
team_colors = {
    'Chennai Super Kings': 'yellow',
    'Delhi Capitals': 'purple',
    'Kings XI Punjab': 'red',
    'Kolkata Knight Riders': 'black',
    'Mumbai Indians': 'blue',
    'Rajasthan Royals': 'pink',
    'Royal Challengers Bangalore': 'orange',
    'Sunrisers Hyderabad': 'teal',
}

#  horizontal bar plot 
plt.figure(figsize=(10, 6))
total_runs_by_team.plot(kind='barh', color=[team_colors.get(team, 'gray') for team in total_runs_by_team.index])
plt.title('Total Runs Scored by Each Team')
plt.xlabel('Total Runs')
plt.ylabel('Team')
plt.grid(axis='x', linestyle='--', alpha=0.7)  
plt.gca().invert_yaxis() 
plt.show()


----------VIRAT KOHLI's journey in cricket exemplifies dedication and excellence, 
inspiring fans worldwide. His remarkable achievements and leadership make him a true icon of the sport. 
Kohli's legacy will continue to inspire future generations of cricketers for years to come.------------------------
