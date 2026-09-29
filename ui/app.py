import streamlit as st
import os
import sys

# Ensure relative imports resolve correctly
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from ui.utils import check_system_status, calculate_route_recommendation
from ui.components import (
    inject_custom_css,
    render_header,
    render_sidebar,
    render_metric_cards,
    render_recommended_route_card,
    render_candidate_table,
    render_folium_map,
    render_download_section,
    render_footer,
)

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Multimodal Transport Recommendation System",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject Custom White-Blue Theme CSS
inject_custom_css()

# System status for Sidebar
status_info = check_system_status()

# Render Sidebar
render_sidebar(status_info)

# Render Main Header
render_header()

# Main Search Form Container
with st.container():
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size:1.15rem; color:#0F4C81; margin-bottom:1rem; font-weight:700;'>Route Parameters</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.2, 1.2, 1])

    with col1:
        source_city = st.text_input(
            "Source City",
            value="Guatemala City",
            placeholder="e.g. Guatemala City",
            help="Enter origin city or address",
        )

    with col2:
        dest_city = st.text_input(
            "Destination City",
            value="Antigua Guatemala",
            placeholder="e.g. Antigua Guatemala",
            help="Enter destination city or address",
        )

    with col3:
        preference = st.selectbox(
            "Preference",
            options=["Fastest", "Cheapest", "Eco Friendly", "Balanced"],
            index=3,
            help="Select routing optimization criteria",
        )

    recommend_clicked = st.button("🚀 Recommend Route", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Store results in session state to persist upon re-renders
if "recommendation_result" not in st.session_state:
    st.session_state["recommendation_result"] = None

if recommend_clicked:
    if not source_city.strip() or not dest_city.strip():
        st.error("Please enter both Source City and Destination City.")
    else:
        with st.spinner("Analyzing road graph, evaluating Dijkstra path, and scoring candidate modes..."):
            result = calculate_route_recommendation(source_city.strip(), dest_city.strip(), preference)
            st.session_state["recommendation_result"] = result

# Render Results section if available
res = st.session_state.get("recommendation_result")

if res:
    if "error" in res:
        st.error(res["error"])
    elif res.get("success"):
        best_route = res["best_route"]

        st.markdown("---")
        st.markdown("<h2 style='font-size:1.4rem; color:#0F4C81; font-weight:700; margin-bottom:1rem;'>Recommendation Analysis</h2>", unsafe_allow_html=True)

        # 1. Top Metric Cards
        render_metric_cards(best_route)

        # 2. Recommended Route Highlight Card
        render_recommended_route_card(best_route, res["src_geo"]["place"], res["dst_geo"]["place"])

        # 3. Interactive Folium Map
        render_folium_map(res["src_geo"], res["dst_geo"], res["route_coords"])

        # 4. Candidate Routes Table (Highlighting Recommended in Green)
        df_display = render_candidate_table(res["candidates"], best_route["mode"])

        # 5. Download Section
        st.markdown("<br/>", unsafe_allow_html=True)
        render_download_section(df_display)

# Render Footer
render_footer()
