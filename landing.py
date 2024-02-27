# Importing Streamlit and PIL libraries
import streamlit as st
from PIL import Image

# Set page title and layout
st.set_page_config(page_title="Global Mortality Analysis: A Focus on Indonesia's Landscape", layout="centered")

# Title and author
st.title("Understanding Global Mortality Trends: A Focus on Indonesia's Landscape")
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
# Adding image Global Mortality Trend
image = Image.open("global_mortality_trend.png")
st.image(image, caption="Global Mortality Trend from 1990 to 2019", width=630)    

st.markdown("* Analysis reveals that China, India, the United States, Russia, and Indonesia are among the top contributors to total mortality.")
image1 = Image.open("2_top_5_countries_with_highest_mortality.png")
st.image(image1, caption="Top 5 Countries with Highest Mortality (1990-2019)", width=650)

st.markdown("""
* **Non-communicable diseases, such as cardiovascular or heart diseases, cancers, chronic lung conditions, chest 
infections and newborn health issues**, dominate global mortality.
* These diseases pose significant public health and economic burdens, highlighting the need for targeted interventions and prevention strategies.
""")
image2 = Image.open("3_top_5_causes_global_mortality.png")
st.image(image2, caption="Top 5 Causes of Global Mortality (1990-2019)", width=650)

# Indonesia's Position
st.subheader("Understanding Key Causes of Mortality in Indonesia")
st.write("""
**Ranked fifth in global mortality**, Indonesia plays a significant role. However, its leading causes differ from the 
global picture.
* While non-communicable diseases like cardiovascular diseases and cancers are present, **communicable diseases such 
as tuberculosis and diarrheal diseases** play a more significant role in Indonesia.
""")
# Image
image = Image.open("4_top_5_mortality_cause_indonesia.png")
st.image(image, caption="Top 5 Causes of Mortality in Indonesia (1990-2019)", width=650)

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
