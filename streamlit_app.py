import streamlit as st
import random


DATA_LOC = 'data/ideas.txt'

# Load data
def load_data():
    with open(DATA_LOC,'r') as f:
        ideas = list(f)
    ideas = [i.split('\n')[0] for i in ideas]
    return ideas

# Your list of song ideas
ideas = load_data()

# Streamlit app
def main():
    # Rainbow-colored title
    # st.markdown("""
    #     <div style="text-align: center; margin: 0; padding: 0;">
    #         <span style="font-size: 40px; color: red;">S</span>
    #         <span style="font-size: 40px; color: orange;">o</span>
    #         <span style="font-size: 40px; color: yellow;">n</span>
    #         <span style="font-size: 40px; color: green;">g</span>
    #         <span style="font-size: 40px; color: blue;">&nbsp;</span>
    #         <span style="font-size: 40px; color: blue;">I</span>
    #         <span style="font-size: 40px; color: indigo;">d</span>
    #         <span style="font-size: 40px; color: violet;">e</span>
    #         <span style="font-size: 40px; color: red;">a</span>
    #         <span style="font-size: 40px; color: orange;">&nbsp;</span>
    #         <span style="font-size: 40px; color: yellow;">G</span>
    #         <span style="font-size: 40px; color: green;">e</span>
    #         <span style="font-size: 40px; color: blue;">n</span>
    #         <span style="font-size: 40px; color: indigo;">e</span>
    #         <span style="font-size: 40px; color: violet;">r</span>
    #         <span style="font-size: 40px; color: red;">a</span>
    #         <span style="font-size: 40px; color: orange;">t</span>
    #         <span style="font-size: 40px; color: yellow;">o</span>
    #         <span style="font-size: 40px; color: green;">r</span>
    #     </div>
    #     """, unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; margin: 0; padding: 0;">
            <span style="font-size: 40px; color: MediumSlateBlue;">Song</span>
            <span style="font-size: 40px; color: blue;">&nbsp;</span>
            <span style="font-size: 40px; color: MediumPurple;">Idea</span>
            <span style="font-size: 40px; color: yellow;">&nbsp;</span>
            <span style="font-size: 40px; color: MediumOrchid;">Generator</span>
        </div>
        """, unsafe_allow_html=True)

    # Display other text with fixed size and centered alignment
    st.markdown("""
        <p style="text-align: center; font-size: 22px; margin: 0; padding: 0;">
            A simple app to help generate song lyrics ideas
        </p>
        """, unsafe_allow_html=True)

    st.markdown("""
        <p style="text-align: center; font-size: 12px; margin: 0; padding: 0;">
             
        </p>
        """, unsafe_allow_html=True)

    # Initialize session state if not already initialized
    if 'generated_idea' not in st.session_state:
        st.session_state.generated_idea = None
    if 'button_label' not in st.session_state:
        st.session_state.button_label = "Generate Idea"

    # Create a full-width row and center the button
    col1, col2, col3 = st.columns([2.05, 2, 1])
    with col2:
        # Create button and handle its state
        if st.button(st.session_state.button_label):
            # Generate a random idea
            st.session_state.generated_idea = random.choice(ideas)
            # Update button label to "Re-generate Idea"
            st.session_state.button_label = "Re-generate Idea"
            # Trigger rerun to update the button label and display the new idea
            st.rerun()
    
    # Display the generated idea if available
    if st.session_state.generated_idea:

        # Display generated idea with fixed font size and centered alignment
        st.markdown(f"""
        <p style="text-align: center; font-size: 18px; margin: 0; padding: 0; font-style: italic;">
            {st.session_state.generated_idea}
        </p>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
