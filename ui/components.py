import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium


def inject_custom_css():
    """
    Inject professional white-blue clean theme CSS styling into Streamlit.
    """
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* App Background */
        .stApp {
            background-color: #F8FAFC;
        }

        /* Main Container Padding */
        .main .block-container {
            padding-top: 1.8rem;
            padding-bottom: 2.5rem;
            max-width: 1200px;
        }

        /* Custom Header Styling */
        .header-box {
            background: linear-gradient(135deg, #0F4C81 0%, #1E88E5 100%);
            padding: 2rem;
            border-radius: 12px;
            color: white;
            box-shadow: 0 4px 20px rgba(15, 76, 129, 0.15);
            margin-bottom: 2rem;
        }

        .header-title {
            font-size: 1.85rem;
            font-weight: 700;
            margin: 0;
            color: #FFFFFF;
            line-height: 1.3;
        }

        .header-subtitle {
            font-size: 0.95rem;
            color: #E3F2FD;
            margin-top: 0.5rem;
            font-weight: 400;
        }

        /* Card Container */
        .custom-card {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
            margin-bottom: 1.5rem;
        }

        /* Recommendation Highlight Card */
        .rec-card {
            background: linear-gradient(145deg, #FFFFFF 0%, #F0F7FF 100%);
            border: 2px solid #2196F3;
            border-radius: 14px;
            padding: 1.6rem;
            box-shadow: 0 4px 15px rgba(33, 150, 243, 0.12);
            margin-bottom: 1.5rem;
        }

        .rec-badge {
            display: inline-block;
            background-color: #2196F3;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.8rem;
        }

        .rec-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #0F4C81;
            margin-bottom: 1rem;
        }

        /* Metric Box Styling */
        .metric-container {
            background: #FFFFFF;
            border-left: 4px solid #1E88E5;
            border-radius: 8px;
            padding: 1rem 1.2rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.04);
            text-align: center;
        }

        .metric-label {
            font-size: 0.8rem;
            color: #64748B;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .metric-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: #0F172A;
            margin-top: 0.2rem;
        }

        /* Custom Button */
        div.stButton > button {
            background: linear-gradient(135deg, #1E88E5 0%, #0D47A1 100%);
            color: white !important;
            font-weight: 600 !important;
            font-size: 1.05rem !important;
            padding: 0.65rem 1.5rem !important;
            border-radius: 8px !important;
            border: none !important;
            box-shadow: 0 4px 12px rgba(13, 71, 161, 0.25) !important;
            transition: all 0.2s ease-in-out !important;
            width: 100%;
        }

        div.stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(13, 71, 161, 0.35) !important;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #0F172A;
            color: #F8FAFC;
        }

        [data-testid="stSidebar"] * {
            color: #E2E8F0;
        }

        .sidebar-status-box {
            background-color: #1E293B;
            border: 1px solid #334155;
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1rem;
        }

        .status-item {
            display: flex;
            align-items: center;
            font-size: 0.85rem;
            margin-bottom: 0.6rem;
        }

        .status-dot-green {
            height: 10px;
            width: 10px;
            background-color: #10B981;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }

        .status-dot-red {
            height: 10px;
            width: 10px;
            background-color: #EF4444;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }

        /* Footer */
        .footer-container {
            text-align: center;
            padding: 1.5rem;
            color: #64748B;
            font-size: 0.85rem;
            border-top: 1px solid #E2E8F0;
            margin-top: 3rem;
        }

        .footer-badge {
            background-color: #E2E8F0;
            color: #334155;
            padding: 3px 8px;
            border-radius: 4px;
            font-weight: 500;
            font-size: 0.78rem;
            margin: 0 3px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header():
    """
    Render main header section.
    """
    st.markdown(
        """
        <div class="header-box">
            <div class="header-title">Scalable Multimodal Transportation Recommendation System</div>
            <div class="header-subtitle">
                Powered by Hadoop, Apache Spark, NetworkX, Dijkstra Algorithm, and Random Forest ML
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(status_info):
    """
    Render sidebar with team info and system status indicators.
    """
    with st.sidebar:
        st.markdown("<h2 style='color:#FFFFFF; font-size:1.3rem; font-weight:700;'>Navigation & Info</h2>", unsafe_allow_html=True)
        st.markdown("---")

        st.markdown("<h4 style='color:#94A3B8; font-size:0.85rem; text-transform:uppercase;'>Project Details</h4>", unsafe_allow_html=True)
        st.markdown("**Title:** Multimodal Transport Recommender")

        team_name = st.text_input("Team Name", value="Big Data & ML Innovators", key="team_name_input")

        st.markdown("<h4 style='color:#94A3B8; font-size:0.85rem; text-transform:uppercase; margin-top:1.5rem;'>System Status</h4>", unsafe_allow_html=True)

        if status_info["system_ok"]:
            sys_status_html = '<span class="status-dot-green"></span> <strong>System Operational</strong>'
        else:
            sys_status_html = '<span class="status-dot-red"></span> <strong>System Error</strong>'

        if status_info["model_loaded"]:
            model_status_html = '<span class="status-dot-green"></span> Model Loaded: <code>random_forest.pkl</code>'
        else:
            model_status_html = '<span class="status-dot-red"></span> Model Missing'

        if status_info["graph_loaded"]:
            nodes_count = status_info.get("graph_nodes", 0)
            graph_status_html = f'<span class="status-dot-green"></span> Graph Loaded: <code>road_graph.pkl</code> ({nodes_count:,} nodes)'
        else:
            graph_status_html = '<span class="status-dot-red"></span> Graph Missing'

        st.markdown(
            f"""
            <div class="sidebar-status-box">
                <div class="status-item">{sys_status_html}</div>
                <div class="status-item">{model_status_html}</div>
                <div class="status-item">{graph_status_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")
        st.markdown(f"<p style='font-size:0.8rem; color:#64748B; text-align:center;'>{team_name} &copy; 2026</p>", unsafe_allow_html=True)


def render_metric_cards(best_route):
    """
    Render 4 top metric cards: Distance, Time, Cost, Carbon.
    """
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="metric-container" style="border-left-color: #1E88E5;">
                <div class="metric-label">Distance</div>
                <div class="metric-value">{best_route['distance_km']:.2f} <span style="font-size:0.9rem; font-weight:normal; color:#64748B;">km</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-container" style="border-left-color: #00ACC1;">
                <div class="metric-label">Travel Time</div>
                <div class="metric-value">{best_route['travel_time_hr']:.2f} <span style="font-size:0.9rem; font-weight:normal; color:#64748B;">hr</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-container" style="border-left-color: #43A047;">
                <div class="metric-label">Travel Cost</div>
                <div class="metric-value">${best_route['travel_cost']:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="metric-container" style="border-left-color: #FB8C00;">
                <div class="metric-label">Carbon Emission</div>
                <div class="metric-value">{best_route['carbon_emission']:.2f} <span style="font-size:0.9rem; font-weight:normal; color:#64748B;">kg</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_recommended_route_card(best_route, source_name, dest_name):
    """
    Display winning recommended route card with all required attributes.
    """
    score_pct = best_route.get("score_pct", round(best_route["score"] * 100, 2))

    st.markdown(
        f"""
        <div class="rec-card">
            <div class="rec-badge">Recommended Option</div>
            <div class="rec-title">Optimal Mode: {best_route['mode']} ({source_name} &rarr; {dest_name})</div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin-top: 1rem;">
                <div>
                    <span style="color:#64748B; font-size:0.82rem; font-weight:600;">MODE</span><br/>
                    <strong style="color:#0F172A; font-size:1.1rem;">{best_route['mode']}</strong>
                </div>
                <div>
                    <span style="color:#64748B; font-size:0.82rem; font-weight:600;">DISTANCE</span><br/>
                    <strong style="color:#0F172A; font-size:1.1rem;">{best_route['distance_km']:.2f} km</strong>
                </div>
                <div>
                    <span style="color:#64748B; font-size:0.82rem; font-weight:600;">TRAVEL TIME</span><br/>
                    <strong style="color:#0F172A; font-size:1.1rem;">{best_route['travel_time_hr']:.2f} hrs</strong>
                </div>
                <div>
                    <span style="color:#64748B; font-size:0.82rem; font-weight:600;">TRAVEL COST</span><br/>
                    <strong style="color:#0F172A; font-size:1.1rem;">${best_route['travel_cost']:.2f}</strong>
                </div>
                <div>
                    <span style="color:#64748B; font-size:0.82rem; font-weight:600;">CARBON EMISSION</span><br/>
                    <strong style="color:#0F172A; font-size:1.1rem;">{best_route['carbon_emission']:.2f} kg</strong>
                </div>
                <div>
                    <span style="color:#64748B; font-size:0.82rem; font-weight:600;">TRANSFERS</span><br/>
                    <strong style="color:#0F172A; font-size:1.1rem;">{best_route['transfers']}</strong>
                </div>
                <div>
                    <span style="color:#64748B; font-size:0.82rem; font-weight:600;">RECOMMENDATION SCORE</span><br/>
                    <strong style="color:#10B981; font-size:1.15rem;">{score_pct:.2f}%</strong>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_candidate_table(candidates, recommended_mode):
    """
    Render table of Candidate Routes with recommended route highlighted in green.
    """
    df = pd.DataFrame(candidates)

    # Rename columns as requested
    df_display = pd.DataFrame({
        "Mode": df["mode"],
        "Distance (km)": df["distance_km"],
        "Travel Time (hr)": df["travel_time_hr"],
        "Travel Cost ($)": df["travel_cost"],
        "Carbon Emission (kg)": df["carbon_emission"],
        "Transfers": df["transfers"],
        "Score (%)": df["score_pct"],
    })

    def highlight_recommended(row):
        if row["Mode"] == recommended_mode:
            return ["background-color: #E8F5E9; color: #1B5E20; font-weight: bold;"] * len(row)
        return [""] * len(row)

    styled_df = df_display.style.apply(highlight_recommended, axis=1).format({
        "Distance (km)": "{:.2f}",
        "Travel Time (hr)": "{:.2f}",
        "Travel Cost ($)": "${:.2f}",
        "Carbon Emission (kg)": "{:.2f}",
        "Score (%)": "{:.2f}%",
    })

    st.markdown("<h3 style='font-size:1.2rem; color:#0F4C81; margin-top:1.5rem; font-weight:700;'>Candidate Routes</h3>", unsafe_allow_html=True)
    st.dataframe(styled_df, use_container_width=True)

    return df_display


def render_folium_map(src_geo, dst_geo, route_coords):
    """
    Render interactive Folium map with source marker, destination marker, and route polyline.
    """
    st.markdown("<h3 style='font-size:1.2rem; color:#0F4C81; margin-top:1.5rem; font-weight:700;'>Route Map Visualization</h3>", unsafe_allow_html=True)

    src_lat, src_lon = src_geo["latitude"], src_geo["longitude"]
    dst_lat, dst_lon = dst_geo["latitude"], dst_geo["longitude"]

    center_lat = (src_lat + dst_lat) / 2.0
    center_lon = (src_lon + dst_lon) / 2.0

    m = folium.Map(location=[center_lat, center_lon], zoom_start=11, tiles="OpenStreetMap")

    # Source Marker (Green)
    folium.Marker(
        location=[src_lat, src_lon],
        popup=f"Source: {src_geo['place']}",
        tooltip=f"Source: {src_geo['place']}",
        icon=folium.Icon(color="green", icon="play", prefix="fa"),
    ).add_to(m)

    # Destination Marker (Red)
    folium.Marker(
        location=[dst_lat, dst_lon],
        popup=f"Destination: {dst_geo['place']}",
        tooltip=f"Destination: {dst_geo['place']}",
        icon=folium.Icon(color="red", icon="stop", prefix="fa"),
    ).add_to(m)

    # Polyline
    if route_coords and len(route_coords) > 1:
        folium.PolyLine(
            locations=route_coords,
            color="#1E88E5",
            weight=5,
            opacity=0.8,
            tooltip="Dijkstra Shortest Path",
        ).add_to(m)
    else:
        # Straight-line polyline connection fallback
        folium.PolyLine(
            locations=[[src_lat, src_lon], [dst_lat, dst_lon]],
            color="#1E88E5",
            weight=4,
            opacity=0.7,
            dash_array="5, 10",
        ).add_to(m)

    st_folium(m, width=None, height=420, use_container_width=True)


def render_download_section(df_display):
    """
    Provide CSV download button for candidate recommendation data.
    """
    csv_data = df_display.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Recommendation as CSV",
        data=csv_data,
        file_name="multimodal_route_recommendation.csv",
        mime="text/csv",
        use_container_width=True,
    )


def render_footer():
    """
    Render modern footer with tech stack credentials.
    """
    st.markdown(
        """
        <div class="footer-container">
            Built using
            <span class="footer-badge">Python</span>
            <span class="footer-badge">Hadoop</span>
            <span class="footer-badge">Apache Spark</span>
            <span class="footer-badge">NetworkX</span>
            <span class="footer-badge">Dijkstra Algorithm</span>
            <span class="footer-badge">Random Forest</span>
            <span class="footer-badge">OpenStreetMap</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
