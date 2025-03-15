st.subheader("About the Author")

    image_url = "https://avatars.githubusercontent.com/u/97449931?v=4"
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        image = response.content
        st.image(image, caption="Moon Benjee (문벤지)", use_container_width=True)
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading image: {e}")  # Use st.error for better visibility

    st.markdown(
        """
        This app was Built with ❤️ by **Benjee(문벤지)**. 
        You can connect with me on: [LinkedIn](https://www.linkedin.com/in/benjaminjvdm/)
        """
    )
