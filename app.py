import streamlit as st
import random

st.image(
    image="https://raw.githubusercontent.com/we-are-alluma/datavis-styleguide/master/mini_book/data-program-icon.png",
    width=80,
)

st.title("SANDI Retreat Sept '21")

with open("prompts.txt", "r") as file:
    prompts = file.readlines()


def print_prompt():
    return random.choice(prompts)


prompt = print_prompt()
st.header(prompt)
col1, col2, col3 = st.columns([1, 1, 1])
col2.button(
    "Click for a prompt",
    on_click=print_prompt,
)
