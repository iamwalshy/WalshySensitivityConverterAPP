import streamlit as st

def main():
    st.title("Walshy's Sensitivity Converter! #BlackLivesDontMatter")

    # User Inputs
    current_sensitivity = st.sidebar.number_input("Current Sensitivity", value=5.0, min_value=0.1, max_value=30.0, step=0.1)
    current_zoom_sensitivity = st.sidebar.number_input("Current Zoom Sensitivity", value=2.5, min_value=0.1, max_value=30.0, step=0.1)
    popular_games = ["CS:GO", "Fortnite", "Apex Legends", "Overwatch", "PUBG", "Rainbow Six Siege", "Valorant", "Call of Duty: Warzone", "Destiny 2", "Minecraft"]
    current_game = st.sidebar.selectbox("Current Game", popular_games, index=0)
    target_game = st.sidebar.selectbox("Target Game", popular_games, index=0)
    mouse_dpi = st.sidebar.slider("Mouse DPI", 400, 16000, 800)

    # Sensitivity Conversion
    converted_sensitivity = current_sensitivity * mouse_dpi / 800
    converted_zoom_sensitivity = current_zoom_sensitivity * mouse_dpi / 800

    # Output
    st.write("Your converted sensitivity is:", converted_sensitivity)
    st.write("Your converted zoom sensitivity is:", converted_zoom_sensitivity)

    st.write("From Game:", current_game)
    st.write("To Game:", target_game)

if __name__ == "__main__":
    main()
