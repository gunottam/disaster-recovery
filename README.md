# 🌍 AI-Driven Disaster Recovery & Infrastructure Planning

An advanced analytical and interactive platform designed to assess infrastructure damage, analyze critical network dependencies, and generate AI-powered recovery plans. This project utilizes geospatial data (specifically analyzing the devastating 2015 Nepal earthquake) to demonstrate how artificial intelligence and graph theory can assist emergency response teams in prioritizing rebuilding efforts.

---

## ✨ Key Features

- 🗺️ **Geospatial Network Analysis:** Leverages `OSMnx`, `NetworkX`, and `GeoPandas` to map out city infrastructure, forming dependency graphs of roads and critical buildings.
- 🚨 **Damage Assessment & Prioritization:** Dynamically calculates recovery priority scores based on damage severity, structural importance, and network centrality.
- 🤖 **AI Recovery Narratives:** Integrates with **Groq's LLM API** to automatically generate empathetic, professional, and actionable step-by-step rebuilding plans for policymakers and rescue teams.
- 🚇 **Metro Route Optimizer:** A standalone C++ and Qt-based application for calculating optimal transit and evacuation routes during crisis recovery.
- 📊 **Interactive Web Dashboard:** A `Streamlit` interface integrating `Folium` maps to visualize damaged zones, critical networks, and prioritized recovery paths in real-time.

---

## 📂 Repository Structure

The workspace is organized into several key components:

```text
📦 disaster-recovery
├── 📂 project/
│   ├── 📂 ui/                       # Streamlit web application & Groq AI integration
│   ├── 📂 Metro-Route-Optimizer/    # C++ / Qt module for specialized route planning
│   ├── 📂 lib/                      # Frontend libraries (Tom-Select, Vis.js)
│   ├── 📓 project.ipynb             # Core data science, EDA, and model training
│   ├── 📓 infra.ipynb               # Infrastructure graph building notebook
│   └── 🗃️ *Geospatial Data*         # Shapefiles (.shp), graphml, proxy maps (ignored via .gitignore if large)
├── 📄 disaster_recovery_arch.pdf    # System architecture diagram
├── 📄 PROJECT PROPOSAL.pdf          # Initial project proposal and research outline
├── 📄 report.pdf                    # Comprehensive project documentation
└── 📄 README.md                     # You are here!
```

---

## 🛠️ Tech Stack

**Data Science & AI:**
- Python 3.10+
- Pandas / GeoPandas
- OSMnx / NetworkX (Graph Theory & Dependency mapping)
- Groq API (LLM Inference using the OpenAI Python Client)

**Web Dashboard / UI:**
- Streamlit
- Folium / Streamlit-Folium

**Systems & Route Optimization:**
- C++
- Qt Framework

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/gunottam/disaster-recovery.git
cd disaster-recovery
```

### 2. Dashboard / AI Setup (Python)

It is highly recommended to use a virtual environment to manage dependencies:

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Navigate to the UI directory
cd project/ui

# Install the required Python packages
pip install -r requirements.txt
```

### 3. API Key Configuration

The disaster recovery narrative generation uses the **Groq API**. You must supply your API key to use this feature:

1. Create a `.env` file in the `project/ui/` directory:
   ```bash
   cp .env.example .env
   ```
2. Open the `.env` file and insert your Groq API key:
   ```env
   GROQ_API_KEY=gsk_your_actual_groq_api_key_here
   ```

### 4. Running the Dashboard

```bash
# Ensure you are inside the project/ui directory and venv is active
streamlit run app.py
```
*The app will automatically open in your default browser at `http://localhost:8501`.*

---

## 🚇 Metro Route Optimizer (C++)
For the C++ routing application:
1. Ensure you have **Qt Creator** or the **Qt Framework** installed on your system.
2. Open `project/Metro-Route-Optimizer/MetroProject.pro` in Qt Creator.
3. Build and Run the project via the IDE to launch the desktop application.
