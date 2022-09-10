import streamlit as st


# title
st.title("My favorites")

# caption by your name
st.caption("Wawiwu")

# 3 columns that display your favorite songs from youtube
colu1, colu2, colu3 = st.columns(3)

with colu1:
    st.write("My first favorite song")
    st.video("https://youtu.be/XqZsoesa55w")

with colu2:
    st.write("My second favorite song")
    st.video("https://youtu.be/79DijItQXMM")
    
with colu3:
    st.write("My third favorite song")
    st.video("https://youtu.be/gIOyB9ZXn8s")




# 3 columns that display your photo of favorite foods.
col1, col2, col3 = st.columns(3)

with col1:
    st.write("My first favorite food")
    st.image("http://steves-kitchen.com/wp-content/uploads/2016/07/Nasi-Lemak-08.jpg")

with col2:
    st.write("My second favorite food")
    st.image("https://asset-a.grid.id/crop/0x0:0x0/700x465/photo/2019/01/25/3555489530.jpg")
    
with col3:
    st.write("My third favorite food")
    st.image("https://2.bp.blogspot.com/-JMTQDGT5SVs/WLjlFxt2-0I/AAAAAAAAGKM/KRhDR-6l9J0dTYEUCQIPGodIXlGVkl3KACLcB/s1600/AfiqHalid%2B-%2BPak%2BPutra%2B2.JPG")



# balloon or snowflake
st.balloons()


