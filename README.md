# Disaster Recovery AI Project

An AI-driven approach to disaster recovery and critical infrastructure planning, specifically analyzing data like the 2015 Nepal earthquake. This project uses geographical data analysis, graph networks, and artificial intelligence to assist in emergency response and recovery planning.

## Overview

Following a major disaster, recovering critical infrastructure (roads, buildings, hospitals) requires prioritizing resources effectively. This project builds dependency graphs of urban network infrastructure (e.g., Kathmandu roads) and uses AI to generate step-by-step, empathetic recovery narratives and priority maps.

## Features

- **Interactive Map Visualization:** A Streamlit-based user interface using Folium to visualize damaged infrastructure and priority zones on a map.
- **AI-Powered Recovery Planning:** Integrates with the Groq API (via OpenAI's Python client) to generate professional and data-driven recovery plans based on dynamically calculated priority scores.
- **Infrastructure Dependency Graphs:** Explores complex networks using geospatial data (`.shp`, `.graphml`, and `.geojson`) to determine critical paths and dependencies.
- **Metro Route Optimizer:** A C++ based sub-project built with Qt for calculating and visualizing optimal transit routes.
- **Rich Data Analysis:** Deep-dive exploratory data analysis (EDA) and network building available in Jupyter Notebooks (`project.ipynb`, `infra.ipynb`).

## Tech Stack

- **Python:** Data processing and machine learning pipelines.
- **Streamlit & Folium:** For the interactive web frontend and map visualization.
- **Pandas & GeoPandas / NetworkX / OSMnx:** For geospatial data wrangling and graph construction.
- **Groq API:** Fast LLM inference for generating recovery narratives.
- **C++ & Qt:** For the standalone Metro Route Optimizer module.

## Setup and Installation

### Prerequisites
- Python 3.10+
- [Git](https://git-scm.com/)
- (Optional) C++/Qt environment if you wish to run the Metro Route Optimizer.

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/gunottam/disaster-recovery.git
cd disaster-recovery
\`\`\`

### 2. Environment Setup (Python UI)
It is recommended to use a virtual environment.
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
\`\`\`

Install the UI dependencies:
\`\`\`bash
# Assuming within the project/ui directory
cd project/ui
pip install -r requirements.txt
\`\`\`

### 3. API Key Configuration
The Streamlit application uses the Groq API for generating response plans. 
1. Copy the example environment file:
   \`\`\`bash
   cp .env.example .env
   \`\`\`
2. Open \`.env\` and add your Groq API key:
   \`\`\`
   GROQ_API_KEY=your_actual_api_key_here
   \`\`\`

## Usage

To start the disaster recovery dashboard:

\`\`\`bash
cd project/ui
streamlit run app.py
\`\`\`

Navigate to `http://localhost:8501` in your browser to view the interactive dashboard.
