import streamlit as st
import os
from utils.data_loader import load_project_metadata


def show_projects():
    """Display the projects page with all ML projects."""
    st.title("Machine Learning Projects")
    st.write(
        "Explore my portfolio of machine learning projects, from deep learning to computer vision applications."
    )

    # Load project metadata
    projects = load_project_metadata()

    # Display projects in a grid layout
    for i in range(0, len(projects), 2):
        cols = st.columns(2)

        # First project in row
        with cols[0]:
            if i < len(projects):
                project_key = list(projects.keys())[i]
                project = projects[project_key]

                # Check if image exists
                image_path = project.get("image", "")
                if os.path.exists(image_path):
                    st.image(image_path, use_column_width=True)
                else:
                    # Display colored box as placeholder
                    st.markdown(
                        f"""
                    <div style="background-color: #4CAF50; height: 200px; 
                    display: flex; justify-content: center; align-items: center; color: white;">
                    <h3>{project['title']}</h3>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

                st.subheader(project["title"])
                st.write(project["description"])

                # Technologies used
                st.write("**Technologies:** " + ", ".join(project["technologies"]))
                st.write("**Date:** " + project["date"])

                # View details button
                if st.button("View Details", key=f"view_{project_key}"):
                    st.session_state["selected_project"] = project_key
                    # Use rerun to refresh page
                    st.rerun()

        # Second project in row (same logic as first)
        with cols[1]:
            if i + 1 < len(projects):
                project_key = list(projects.keys())[i + 1]
                project = projects[project_key]

                # Check if image exists
                image_path = project.get("image", "")
                if os.path.exists(image_path):
                    st.image(image_path, use_column_width=True)
                else:
                    # Display colored box as placeholder
                    st.markdown(
                        f"""
                    <div style="background-color: #2196F3; height: 200px; 
                    display: flex; justify-content: center; align-items: center; color: white;">
                    <h3>{project['title']}</h3>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

                st.subheader(project["title"])
                st.write(project["description"])

                # Technologies used
                st.write("**Technologies:** " + ", ".join(project["technologies"]))
                st.write("**Date:** " + project["date"])

                # View details button
                if st.button("View Details", key=f"view_{project_key}"):
                    st.session_state["selected_project"] = project_key
                    # Use rerun to refresh page
                    st.rerun()

    # Add a horizontal separator
    st.markdown("---")

    # Call to action
    st.subheader("Want to see more?")
    st.write("Check out my GitHub for additional projects and contributions.")

    # GitHub button
    if st.button("Visit GitHub"):
        st.markdown(
            "[Visit GitHub](https://github.com/poshraj24)", unsafe_allow_html=True
        )
