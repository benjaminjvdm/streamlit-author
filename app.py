st.subheader("About the Author")

    image_url = "https://github.com/benjaminjvdm/streamlit-author/blob/main/Untitled%20design(1)(1).png?raw=true"
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image = response.content
        st.image(image, caption="Moon Benjee (문벤지)", use_container_width=True)
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading image: {e}")

    st.markdown(
        """
        This app was Built with ❤️ by **Benjee(문벤지)**. 
        You can connect with me on: [LinkedIn](https://www.linkedin.com/in/benjaminjvdm/)
        """
    )
