import folium
from folium.plugins import MarkerCluster

def get_priority_color(score):
    if score > 0.8:
        return "red"
    elif score > 0.5:
        return "orange"
    else:
        return "green"

def generate_map(df):
    m = folium.Map(location=[27.709, 85.320], zoom_start=14)
    marker_cluster = MarkerCluster().add_to(m)

    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"{row['name']} ({row['infra_type']})",
            icon=folium.Icon(color=get_priority_color(row["priority_score"]))
        ).add_to(marker_cluster)

    return m
