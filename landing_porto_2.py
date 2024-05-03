# Importing required libraries
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Other libraries
import warnings
warnings.filterwarnings("ignore")

# Customizing with 'ggplot' style
plt.style.use('ggplot')


# Loading dataset
df = pd.read_csv('global_mortality_clean.csv')

# Set page title and layout
st.set_page_config(page_title="Global Mortality Analysis: A Focus on Indonesia's Landscape", layout="centered")

# Title and author
st.title("Understanding Global Mortality Trends of 30 years data: A Focus on Indonesia's Landscape")
st.caption("By Harish Muhammad")

# Global Mortality Illustration
image = Image.open("global_mortality_illustration.png")
st.image(image, caption="Global Mortality Illustration", width=700)

# Background
st.subheader("Background")
st.write("""
Understanding global mortality trends is crucial for evidence-based decision-making, prioritizing healthcare needs, 
allocating resources effectively, and overall potentially improving public health outcomes. This analysis delves into 
mortality data from 1990 to 2019, exploring global patterns and Indonesia's unique situation.
""")

# Exploring Global Mortality Trends
st.subheader("Global Mortality Overview")
st.write("""
The global mortality dataset of 30 years data (from 1990-2019) and 204 countries offers a comprehensive view of worldwide 
mortality patterns. 
""")
st.markdown("* Global mortality rates have steadily risen, exceeding 54 million deaths in 2019.")


# Data preparation
df0 = df[["Year", "Total mortality"]].groupby("Year").sum().reset_index().sort_values(by="Year")

# Function to format numbers in millions
def million_formatter(x, pos):
    return "%.1f M" % (x / 1e6)  

# Create Seaborn line plot
plt.figure(figsize=(10, 6))  # Adjust figure size
sns.lineplot(x="Year", y="Total mortality", data=df0, marker="o", color="red")
plt.title("Global Mortality Trend (1990-2019)")
plt.xlabel("Year")
plt.ylabel("Total mortality (Millions of lives)")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Apply formatter to y-axis
plt.gca().yaxis.set_major_formatter(million_formatter)

# Display the plot
st.pyplot(plt)



# ======== The 5 top countries with highest mortality causes

st.markdown("* Analysis reveals that China, India, the United States, Russia, and Indonesia are among the top contributors to total mortality.")

# All country mortality during 30 years
# Creating pivot table based on country and total mortality
sum_mortality_30 = pd.pivot_table(data=df[['Country', 'Total mortality']],
                                   index=['Country'],
                                   values='Total mortality',
                                   aggfunc='sum'
).reset_index()


# Sorting and ranking the top 5 countries with the highest mortality
top_5_countries_mortality = sum_mortality_30.sort_values(by='Total mortality', ascending=False).head(5)


# Define million_formatter function
def million_formatter(x, pos):
    return "%.1f M" % (x / 1e6)  # Format to display in millions with 1 decimal place

# Define annotate_bars function
def annotate_bars(ax):
    for bar in ax.patches:
        x, y = bar.get_xy()
        ax.text(
            x + bar.get_width(), y + bar.get_height()/2, f'{bar.get_width() / 1e6:.1f} M ',
            va='center', ha='right', color='white'
        )
    return ax

# Setting the width and height of figure
fig, ax = plt.subplots(figsize=(10,6))

# Creating horizontal bar charts
sns.barplot(x='Total mortality', y='Country', data=top_5_countries_mortality, zorder=2)

# Adding title and labels
plt.title('The top 5 countries with the highest total mortality from 1990 to 2019')
plt.xlabel('Total Mortality (Millions of lives)')
plt.ylabel('')  # No ylabel for better presentation


# Apply million_formatter to x-axis
plt.gca().xaxis.set_major_formatter(million_formatter)

# Annotate bars with labels representing millions
annotate_bars(ax)

# Displaying bar charts
st.pyplot(plt)

# Global mortality

#Displaying table
#sum_mortality_30.sort_values(by='Total mortality', ascending=False)

# image1 = Image.open("2_top_5_countries_with_highest_mortality.png")
# st.image(image1, caption="Top 5 Countries with Highest Mortality (1990-2019)", width=650)

# ======== 5 Top global mortality causes

st.markdown("""
* **Non-communicable diseases, such as cardiovascular or heart diseases, cancers, chronic lung conditions, chest 
infections and newborn health issues**, dominate global mortality.
* These diseases pose significant public health and economic burdens, highlighting the need for targeted interventions and prevention strategies.
""")

# Data preparation of top 5 causes
cause_death_df = df.iloc[:, 2:-1].sum().to_frame()
cause_death_df.rename(columns={0: "mortality"}, inplace=True)
cause_death_df = cause_death_df.rename_axis('causes')
cause_death_df = cause_death_df.sort_values(by='mortality', ascending=False)

# Sorting the top 5 causes with the highest mortality
top_5_causes = cause_death_df.head(5)

# Resetting index of top_5_causes DataFrame
top_5_causes.reset_index(inplace=True)

# Define million_formatter function
def million_formatter(x, pos):
    return "%.1f M" % (x / 1e6)  # Format to display in millions with 1 decimal place

# Define annotate_bars function
def annotate_bars(ax):
    for bar in ax.patches:
        x, y = bar.get_xy()
        ax.text(
            x + bar.get_width(), y + bar.get_height()/2, f'{bar.get_width() / 1e6:.1f} M ',
            va='center', ha='right', color='white'
        )
    return ax

# Setting the width and height of figure
fig, ax = plt.subplots(figsize=(10, 6))

# Creating horizontal bar charts
sns.barplot(x='mortality', y='causes', data=top_5_causes, zorder=2)

# Adding title and labels
plt.title('The top 5 causes of global mortality from 1990 to 2019')
plt.xlabel('Total Mortality (Millions of lives)')
plt.ylabel('')  # No ylabel for better presentation

# Apply million_formatter to x-axis
plt.gca().xaxis.set_major_formatter(million_formatter)

# Annotate bars with labels representing millions
annotate_bars(ax)

# Displaying bar charts
st.pyplot(plt)

# image2 = Image.open("3_top_5_causes_global_mortality.png")
# st.image(image2, caption="Top 5 Causes of Global Mortality (1990-2019)", width=650)

# Indonesia's Position
st.subheader("Understanding Key Causes of Mortality in Indonesia")
st.write("""
**Ranked fifth in global mortality**, Indonesia plays a significant role. However, its leading causes differ from the 
global picture.
""")
# Mortality of Indonesia
# Filtering mortality cause data only for the country of Indonesia
df_indonesia = df[df['Country'] == 'Indonesia']

# Mortality trend in Indonesia within 30 years of data
df_indo_mortality_trend = df_indonesia[["Year", "Total mortality"]].groupby("Year").sum().reset_index()


# Using function to define a format of million
def million_formatter(x, pos):
    return "%.1f M" % (x / 1e6)  # Adjusted to format in millions

# Create Seaborn line plot
plt.figure(figsize=(10, 6))
a = sns.lineplot(data=df_indo_mortality_trend, x='Year', y='Total mortality', color='orange', marker="o")

# Customize the plot with seaborn functions
a.yaxis.set_major_formatter(million_formatter)  # Applying the formatter to y-axis

# Customize the plot
plt.xlabel('Year')
plt.ylabel("Total Mortality (Millions of lives)")
plt.title('Mortality trend in Indonesia from 1990 to 2019')

# Show the plot
st.pyplot(plt)

st.write("""
* While non-communicable diseases like cardiovascular diseases and cancers are present, **communicable diseases such 
as tuberculosis and diarrheal diseases** play a more significant role in Indonesia.
""")

# Calculating the accumulated total mortality of Indonesia from each cause
idn_cause_death_df = df_indonesia.iloc[:,2:-1].sum().to_frame().reset_index()
idn_cause_death_df.rename(columns={"index": "causes", 0:"mortality"}, inplace=True)
idn_cause_death_df = idn_cause_death_df.sort_values(by='mortality',ascending=False)

# The top 5 causes of mortality in Indonesia within 30 years (1990-2019)

# Top 5 causes in Indonesia
# Ranking and sorting the top 5 cause with highest mortality
top_5_causes_idn = idn_cause_death_df.head(5)

# Define million_formatter function
def million_formatter(x, pos):
    return "%.1f M" % (x / 1e6)  # Format to display in millions with 1 decimal place

# Define annotate_bars function
def annotate_bars(ax):
    for bar in ax.patches:
        x, y = bar.get_xy()
        ax.text(
            x + bar.get_width(), y + bar.get_height()/2, f'{bar.get_width() / 1e6:.1f} M ',
            va='center', ha='right', color='white'
        )
    return ax

# Setting the width and height of figure
fig, ax = plt.subplots(figsize=(10,6))

# Creating horizontal bar charts
sns.barplot(x='mortality', y='causes', data=top_5_causes_idn, zorder=2)  # Set zorder for the bar plot

# Adding title and labels
plt.title('The top 5 causes of mortality in Indonesia from 1990 to 2019')
plt.xlabel('Total Mortality (Millions of lives)')
plt.ylabel('')  # No ylabel for better presentation

# Apply million_formatter to x-axis
plt.gca().xaxis.set_major_formatter(million_formatter)

# Annotate bars with labels representing millions
annotate_bars(ax)

# Displaying bar charts
st.pyplot(plt)


# Displaying table
#idn_cause_death_df.sort_values(by='mortality',ascending=False)


# # Image
# image = Image.open("4_top_5_mortality_cause_indonesia.png")
# st.image(image, caption="Top 5 Causes of Mortality in Indonesia (1990-2019)", width=650)

st.markdown("* This unique profile necessitates tailored approaches to address these prevalent challenges.")

# Implications for Indonesian Healthcare
st.subheader("Implications for Indonesian Healthcare")
st.write("""
Government representatives can leverage data for evidence-based policies and interventions targeting prevalent diseases. 
Prioritizing funding and strengthening healthcare infrastructure are crucial for improving population health.
""")

# Insights for the Healthcare Industry
st.subheader("Insights for the Healthcare Industry")
st.write("""
The pharmaceutical industry can contribute by innovating and collaborating on research, development, and provision of 
essential medications. Developing affordable treatments for prevalent diseases and supporting public health initiatives 
are key areas for involvement.
""")

# Conclusion & Call to Action (continued)
st.write("""
Understanding global mortality trends provides valuable insights for shaping Indonesia's healthcare landscape. By fostering 
collaboration between government, industry, and communities, we can work towards creating a healthier future for Indonesia.

**Call to Action:**

* **Individuals:** Practice healthy lifestyles, seek preventive healthcare, and advocate for improved healthcare access.
* **Governments:** Utilize data for evidence-based policymaking, prioritize funding for prevalent diseases, and strengthen healthcare infrastructure.
* **Healthcare Industry:** Invest in research and development of affordable treatments and collaborate with governments on public health initiatives.
* **Communities:** Raise awareness about health challenges and promote healthy behaviors within communities.

Together, we can make a significant impact on global mortality trends and build a healthier future for all.
""")

# References
st.subheader("References")
st.write("""
* Institute for Health Metrics and Evaluation (2014): [Link](https://www.healthdata.org/research-analysis/library/financing-global-health-2013-transition-age-austerity)
* IPSOS (2023): [Link](https://www.ipsos.com/sites/default/files/ct/news/documents/2023-07/ipsos-global-perceptions-of-healthcare-2023.pdf)
* Ministry of Health Indonesia (2023): [Link](https://sehatnegeriku.kemkes.go.id/baca/rilis-media/20230816/0643661/anggaran-kesehatan-2024-ditetapkan-sebesar-5-6-dari-apbn-naik-8-1-dibanding-2023/)
""")
