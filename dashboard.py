import streamlit as st
from password_generators import RandomPasswordGenerator, pinGenerator, MemorablePasswordGenerator

st.title(":zap: Password Generator")

option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))

if option == 'Pin Code':
    length = st.slider("Select the length of the pin code", 4, 32)
    generator = pinGenerator(length)

elif option == "Random Password":
    length = st.slider("select the length of the password", 8, 100)
    include_symbol = st.toggle("Include Symbols")
    include_number = st.toggle("Include Number")
    generator = RandomPasswordGenerator(length, include_number, include_symbol)

elif option == 'Memorable Password':
    num_of_words = st.slider("Select number of words", 2, 10)
    seperator = st.text_input("Separator", value='-')
    capitalization = st.toggle("Capitalization")

    generator = MemorablePasswordGenerator(num_of_words, seperator, capitalization)
password = generator.generate()
st.write(fr"Your password is: ```{password}``` ")