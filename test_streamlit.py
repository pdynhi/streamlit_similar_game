import streamlit as st
import requests
from pprint import pformat

# Streamlit application title
st.title("Game Similarity Finder")

# Input box for the game description
game_description = st.text_area(
    "Enter the game description:",
    placeholder="Describe the game you want to find similar games for...",
)

# Button to trigger the API call
if st.button("Find Similar Games"):
    if game_description.strip():
        ENDPOINT = "http://localhost:7001/steam_database/games/search/"

        # API request
        response = requests.post(
            ENDPOINT,
            json={"game_descriptions": [game_description]}
        )

        # Check if the API call was successful
        if response.status_code == 200:
            games = response.json()[0]
            st.subheader("Result:")
            
            # Loop through the top 5 games and display their details
            for rank, game in enumerate(games, start=1):
                st.write(f"### Top {rank} similar game:")
                st.write(f"**Name:** {game['name']}")
                st.write(f"**Score:** {game['score']:.6f}")
                st.write(f"**Steam ID:** {game['steam_id']}")
                st.write(f"**Steam URL:** [Link]({game['steam_url']})")
                st.write(f"**Description:** {game['description']}")
                st.write(f"**Tags:** {', '.join(game['tags'])}")
                st.write("---")
        else:
            st.error("Error: " + response.json().get("message", "Unknown error occurred."))
    else:
        st.warning("Please enter a game description.")

#streamlit run test_streamlit.py
