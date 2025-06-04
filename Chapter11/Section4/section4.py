import streamlit as st


if "interaction_count" not in st.session_state:
    st.session_state.interaction_count = 0

def count_interaction():
    st.session_state.interaction_count += 1


st.text_input("Enter your name", key="name", on_change=count_interaction)
st.slider("Pick a number", 0, 10, key="number", on_change=count_interaction)
st.radio("Choose an option", ["A", "B", "C"], key="choice", on_change=count_interaction)
st.button("Click me", on_click=count_interaction)

st.markdown("### 🔢 Total interactions:")
st.write(st.session_state.interaction_count)
