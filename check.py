import streamlit as stm
status=stm.radio("Select Gender:",['Male','Female'])
if status=='Male':
    stm.success('Male')
else:
    stm.success('Female')
hobby=stm.selectbox("Select Hobby:", ['Reading', 'Writing', 'Drawing'])
stm.write(f"Selected Hobby: {hobby}")
