import streamlit as st
import pandas as pd
import numpy as np
from openai import OpenAI


client = OpenAI(api_key=st.secrets['open_key'])

symptoms = 'I have a headache and I feel sick, my stomach hurts and I have thrown up multiple times'
flow = False

st.header("Deepmind Analysis")

st.markdown("###")

Insights = "Hello"

with st.form("my_form"):
  description = st.text_area('Introduce the company details')

  uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
  
  submitted = st.form_submit_button("Submit")
  if submitted:
    flow = True

if flow:
  completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
          {"role": "system", "content": "You are a worldwide renounce marketer, you can manage the best marketing campaigns and understand client needs when a user gives you a company description and data to interpret."},
          {"role": "user", "content": f"Write a marketing report with the next structure [Relation between the Company product and the new category found][A marketing strategy for LinkedIn, Instagram, Twitter, and TikTok, based in the insights gained][Microinfluencers er social media network that can help the company]  Company Description: {description}  Insights Gained: {Insights}"}
        ]
      )

  output = completion.choices[0].message.content

  st.info(output)

  

  st.info(output)
