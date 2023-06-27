import streamlit as st
import functions

text_item = functions.get_item()


def add_item():
    new_item = st.session_state['new_item'] + '\n'
    text_item.append(new_item)
    functions.write_item(text_item)


st.title("My Project")
st.subheader("This is a text application")
st.write("This is a text application")

for index, item in enumerate(text_item):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        text_item.pop(index)
        functions.write_item(text_item)
        del st.session_state[item]
        st.experimental_rerun()


st.text_input(label="Enter item", placeholder="Enter a text",
              on_change=add_item, key="new_item", label_visibility='hidden')
