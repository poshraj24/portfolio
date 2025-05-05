import streamlit as st


def show_contact():
    """Display contact page with form."""
    st.title("Contact Me")
    st.write(
        "Feel free to reach out to me for collaborations, job opportunities, or just to connect!"
    )

    # Contact information
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Contact Information")
        st.markdown("**Email:** dahal.poshraj24@gmail.com")
        st.markdown("**Phone:** +49 17610815381")
        st.markdown("**Location:** Erlangen, Germany")

        # Social links
        st.subheader("Connect with me")

        # Using icons in markdown
        st.markdown(
            """
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/poshrajdahal)
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/poshraj24)
        """
        )

    with col2:
        st.subheader("Send me a message")

        # Contact form
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=150)

            # Submit button
            submitted = st.form_submit_button("Send Message")

            if submitted:
                if name and email and message:
                    # In a real application, you would send an email here
                    # For this demo, we'll just show a success message
                    st.success("Thank you for your message! I'll get back to you soon.")

                    # Display the submitted information (for demo purposes)
                    st.write("Submitted information:")
                    st.write(f"Name: {name}")
                    st.write(f"Email: {email}")
                    st.write(f"Subject: {subject}")
                    st.write(f"Message: {message}")
                else:
                    st.error(
                        "Please fill in all required fields: Name, Email, and Message."
                    )

    # Additional information
    st.markdown("---")
    st.subheader("Availability")
    st.write(
        "I'm currently available for freelance work, project collaborations, and job opportunities related to machine learning and data science."
    )

    # FAQ section
    with st.expander("Frequently Asked Questions"):
        st.markdown(
            """
        **Q: Are you available for remote work?**  
        A: Yes, I'm open to remote opportunities worldwide.
        
        **Q: What are your primary areas of expertise?**  
        A: My core expertise is in machine learning, deep learning, computer vision, and natural language processing.
        
        **Q: Do you provide consulting services?**  
        A: Yes, I offer consulting services for machine learning projects and data science implementations.
        """
        )
