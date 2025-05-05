import streamlit as st
import plotly.express as px
import pandas as pd


def show_skills():
    """Display skills and experience page."""
    st.title("Skills & Experience")
    st.write(
        "An overview of my technical skills, professional experience, and educational background."
    )

    # Create sections
    tab1, tab2, tab3 = st.tabs(
        ["Technical Skills", "Professional Experience", "Education"]
    )

    with tab1:
        st.subheader("Technical Skills")

        # Create skills data based on your resume
        skills_data = {
            "Category": [
                "Programming",
                "Programming",
                "Programming",
                "Programming",
                "Tools & Frameworks",
                "Tools & Frameworks",
                "Tools & Frameworks",
                "Tools & Frameworks",
                "Tools & Frameworks",
                "Data Engineering",
                "Data Engineering",
                "Visualization",
                "Visualization",
                "Visualization",
                "Visualization",
            ],
            "Skill": [
                "Python",
                "Flutter",
                "HTML/CSS",
                "SQL",
                "PyTorch",
                "TensorFlow",
                "Pandas",
                "OpenCV",
                "Git",
                "Jayvee",
                "ETL pipelines",
                "Matplotlib",
                "Microstrategy",
                "Tableau",
                "RapidMiner",
            ],
            "Proficiency": [95, 85, 80, 90, 92, 88, 90, 85, 88, 80, 82, 90, 85, 80, 78],
        }

        df = pd.DataFrame(skills_data)

        # Create visualization
        fig = px.bar(
            df,
            x="Skill",
            y="Proficiency",
            color="Category",
            color_discrete_sequence=px.colors.qualitative.Set2,
            title="Technical Skills Assessment",
            labels={"Proficiency": "Expertise Level (%)"},
        )

        fig.update_layout(xaxis_title="", yaxis_range=[0, 100], height=600)

        st.plotly_chart(fig, use_container_width=True)

        # Languages section
        st.subheader("Languages")

        language_data = {
            "Language": ["German", "English", "Nepali"],
            "Level": ["B1", "Fluent", "Native"],
            "Proficiency": [60, 90, 100],
        }

        lang_df = pd.DataFrame(language_data)

        # Create language bar chart
        lang_fig = px.bar(
            lang_df,
            x="Language",
            y="Proficiency",
            text="Level",
            color="Language",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            title="Language Proficiency",
        )

        lang_fig.update_layout(
            xaxis_title="", yaxis_title="Proficiency Level (%)", yaxis_range=[0, 100]
        )

        st.plotly_chart(lang_fig, use_container_width=True)

    with tab2:
        st.subheader("Professional Experience")

        # Experience from resume
        experience = [
            {
                "title": "Vendor Data Analyst",
                "company": "Cotiviti Technologies",
                "location": "Kathmandu, Nepal",
                "period": "May 2021 - April 2023",
                "description": "Led healthcare data quality control initiatives reducing error rates by 15%",
                "technologies": "SQL, Bitbucket, Confluence, Microstrategy, Jira, Git, Advanced Excel",
            },
            {
                "title": "IT Support Analyst",
                "company": "Eternal Light Secondary School",
                "location": "Kathmandu, Nepal",
                "period": "May 2020 - March 2021",
                "description": "Implemented network infrastructure supporting 500+ students during pandemic",
                "technologies": "Cisco networking, Python automation, system administration",
            },
            {
                "title": "Project Manager-Intern",
                "company": "10 Orbits Pvt Ltd",
                "location": "Lalitpur, Nepal",
                "period": "November 2019 to February 2020",
                "description": "Conducted thorough documentation processes for contracts and solicitation proposals; streamlined administrative tools that provided valuable insights, contributing to the successful onboarding of 4 new ERP systems within tight deadlines.",
                "technologies": "Jira, Odoo, Slack, Git",
            },
        ]

        # Display experience with timeline
        for idx, exp in enumerate(experience):
            col1, col2 = st.columns([1, 3])

            with col1:
                st.markdown(f"**{exp['period']}**")
                st.markdown(f"*{exp['location']}*")

            with col2:
                st.markdown(f"### {exp['title']}")
                st.markdown(f"**{exp['company']}**")
                st.markdown(exp["description"])
                st.markdown(f"**Technologies used:** {exp['technologies']}")

            # Add separator between experiences
            if idx < len(experience) - 1:
                st.markdown("---")

    with tab3:
        st.subheader("Education")

        # Education from resume
        education = [
            {
                "degree": "MSc. Data Science",
                "institution": "FAU Erlangen-Nuremberg",
                "location": "Erlangen, Germany",
                "period": "April 2023 - Present",
                "courses": "Deep Learning, Artificial Intelligence, Business Intelligence, Machine Learning, Statistics, Bioinformatics, Data Mining, Image Processing",
            },
            {
                "degree": "BSc. Computer Science and Information Technology",
                "institution": "Tribhuvan University",
                "location": "Kathmandu, Nepal",
                "period": "December 2015 - December 2019",
                "courses": "Probability and Statistics, Artificial Intelligence, Neural Networks, Java Programming, Simulation and Modeling, Software Engineering, Data Warehousing",
            },
        ]

        # Display education
        for idx, edu in enumerate(education):
            col1, col2 = st.columns([1, 3])

            with col1:
                st.markdown(f"**{edu['period']}**")
                st.markdown(f"*{edu['location']}*")

            with col2:
                st.markdown(f"### {edu['degree']}")
                st.markdown(f"**{edu['institution']}**")
                st.markdown("**Relevant Coursework:**")
                st.markdown(edu["courses"])

            # Add separator between education entries
            if idx < len(education) - 1:
                st.markdown("---")
