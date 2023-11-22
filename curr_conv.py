import streamlit as st
from PIL import Image

img  = Image.open("dollars.jpg")
st.sidebar.image(img.resize((200,300)))

curr = ["Naira","Pounds","Dollars","Euros","Yen","Cedis"]
conv = [1, 1023, 816, 890, 114, 68]

def convert(num,inital,final):
    ini_id = curr.index(inital)
    fin_id = curr.index(final)

    value1 = conv[ini_id]
    value2 = conv[fin_id]

    result = num * value1 / value2

    return round(result,2)

num = st.number_input("How much are you converting")
inital = st.selectbox("Amount Currency",curr)
final = st.selectbox("Conversion Currency",curr)

amount = convert(num,inital,final)

if st.button("Convert"):
    st.write(amount)