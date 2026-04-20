import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import random
import openai
import os

client = openai.OpenAI(
    api_key=os.environ.get("GROQ_API_KEY", ""),
    base_url="https://api.groq.com/openai/v1"
)

def generate_groq_narrative(sorted_df):
    items = []
    for i, row in enumerate(sorted_df.itertuples(), 1):
        items.append(f"{i}. Type: {row.type}, ID: {row.id}, Score: {row.priority_score:.2f}")

    prompt = (
        "You are a earthquake disaster recovery expert. Based on the following critical infrastructure "
        "ranked by priority, generate a step-by-step, professional yet empathetic plan "
        "for recovery. Each step should explain *why* it's important. and focus on using the name of node\n\n"
        "Give me answer according to the list and generate a concise step by step recovery here is the Infrastructure List:\n" + "\n".join(items)
    )

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content


# ----------- 1. Generate Dummy Data (Cached) -----------
@st.cache_data
def generate_dummy_data(n=50):
    types = ['Hospital', 'School', 'Govt Office', 'Shop', 'Warehouse']
    base_lat, base_lon = 27.7172, 85.3240  # Kathmandu center
    data = []

    for i in range(n):
        lat = base_lat + random.uniform(-0.02, 0.02)
        lon = base_lon + random.uniform(-0.02, 0.02)
        infra_type = random.choice(types)
        damage = round(random.uniform(0.1, 1.0), 2)
        weight = {'Hospital': 1.0, 'School': 0.7, 'Govt Office': 0.8, 'Shop': 0.3, 'Warehouse': 0.5}[infra_type]
        score = round(damage * weight, 2)
        data.append({
            'id': f'Node {i+1}',
            'type': infra_type,
            'lat': lat,
            'lon': lon,
            'damage_score': damage,
            'importance_weight': weight,
            'priority_score': score
        })

    return pd.DataFrame(data)

df = generate_dummy_data()

# ----------- 2. Title & Selection -----------
st.title("Disaster Recovery Prioritization - Kathmandu")
st.subheader("Select Affected Infrastructure Nodes")

# ----------- 3. Map -----------
def render_map(data):
    m = folium.Map(location=[27.7172, 85.3240], zoom_start=13)
    for _, row in data.iterrows():
        color = 'green' if row.priority_score < 0.3 else 'orange' if row.priority_score < 0.6 else 'red'
        folium.Marker(
            [row.lat, row.lon],
            popup=f"{row['id']} ({row['type']}) - Priority: {row['priority_score']}",
            icon=folium.Icon(color=color)
        ).add_to(m)
    return m

folium_map = render_map(df)
st_data = st_folium(folium_map, width=700, height=500)

# ----------- 4. Multiselect Input -----------
affected = st.multiselect(
    "Select affected nodes by ID:",
    options=df['id'].tolist(),
    default=[]
)

# ----------- 5. Recovery Plan Display -----------

if affected:
    selected_df = df[df['id'].isin(affected)]
    sorted_df = selected_df.sort_values(by='priority_score', ascending=False)
    st.subheader("📋 AI-Generated Recovery Narrative")

    try:
        narrative = generate_groq_narrative(sorted_df)
        st.markdown(narrative)
    except Exception as e:
        st.error(f"Failed to generate recovery plan: {e}")

else:
    st.info("Select nodes from the list above to see recovery order.")

# ----------- 6. Chatbot Q&A Section -----------

st.subheader("💬 Ask the Disaster Recovery Chatbot")

user_question = st.text_input("Type your question here and press Enter:")
damage_summary = "\n".join(
    [f"{row.id}: {row.type} with priority score {row.priority_score:.2f}" for row in df.itertuples()]
)

if user_question:
    try:
        system_message = {
            "role": "system",
            "content": (
                "You are a disaster recovery expert chatbot. "
                "Use the following infrastructure damage and priority data to answer questions strictly "
                "related to recovery plans, damage impact, and prioritization."
                "if something goes out of your scope, say 'I don't know' or 'I cannot answer that'. "
            )
        }

        data_message = {
            "role": "assistant",
            "content": (
                f"The current affected infrastructure with priority scores is:\n{damage_summary}\n"
                "Answer user queries only based on this data."
            )
        }

        user_message = {"role": "user", "content": user_question}

        messages = [system_message, data_message, user_message]

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
            temperature=0.7,
        )

        answer = response.choices[0].message.content
        st.markdown(f"**Chatbot Answer:** {answer}")
    except Exception as e:
        st.error(f"Failed to get chatbot response: {e}")
else:
    st.info("Ask a question about the disaster recovery process.")