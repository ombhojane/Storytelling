import streamlit as st
from storiesdata import stories, fantasy_quest_pages

# Set page layout to wide
st.set_page_config(layout="wide")

# Custom CSS to center the app UI
st.markdown(
    """
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .next-button {
        display: flex;
        justify-content: flex-end;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def homepage():
    st.title("Interactive Storytelling App")
    st.write("Select a story scenario to begin your adventure:")

    selected_story = st.selectbox("Choose a story scenario:", list(stories.keys()))

    start_button = st.button("Start Adventure")
    if start_button:
        st.session_state["section"] = "storytelling"
        st.session_state["selected_story"] = selected_story
        st.session_state["current_page"] = 0  # Reset the current page when starting a new adventure

def storytelling():
    st.subheader("Storytelling")
    selected_story = st.session_state["selected_story"]
    st.write(f"You have chosen the {selected_story} adventure!")

    # Replace the 'story_pages' list with the appropriate story scenarios from storiesdata.py
    if selected_story == "Fantasy Quest":
        story_pages = fantasy_quest_pages
    else:
        # Add more story scenarios here as needed...
        pass

    current_page = st.session_state.get("current_page", 0)
    if current_page < len(story_pages):
        st.image(story_pages[current_page]["image"], use_column_width=True, output_format="JPEG", caption=f"Image {current_page + 1}")

        st.write(story_pages[current_page]["text"])

        col1, col2 = st.columns([2, 1])
        if col1.button("Previous Paragraph") and current_page > 0:
            st.session_state["current_page"] = current_page - 1  # Move to the previous paragraph
        if col2.button("Next Paragraph", key="next_button") and current_page < len(story_pages) - 1:
            st.session_state["current_page"] = current_page + 1  # Move to the next paragraph

        if current_page == 0:
            st.write("You are at the beginning of the story.")
        elif current_page == len(story_pages) - 1:
            st.write("Congratulations! You have completed your adventure.")
            # Display the "Home" button to redirect back to the homepage
            if st.button("Home"):
                st.session_state["section"] = "homepage"
                st.session_state["current_page"] = 0  # Reset the current page when returning to homepage

    else:
        st.session_state["section"] = "homepage"


def main():
    if "section" not in st.session_state:
        st.session_state["section"] = "homepage"

    if st.session_state["section"] == "homepage":
        homepage()
    elif st.session_state["section"] == "storytelling":
        storytelling()

if __name__ == "__main__":
    main()
