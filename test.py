import streamlit as st

st.header('Aplikasi penjumlahan bilangan numerik', divider='rainbow')

angka_pertama = st.number_input('masukan angka pertama')
st.write('the first number is',angka_pertama)

angka_kedua = st.number_input ('Masukkan angka kedua')
st.write('the second number is',angka_kedua)
angka_ketiga = st.number_input ('Masukan angka ketiga')
st.write('the second number is',angka_ketiga)
operasi_matematika = angka_pertama * angka_kedua + angka_ketiga 
st.write(f"angka pertama {angka_pertama} x angka kedua {angka_kedua} + {angka_ketiga} = {operasi_matematika}")