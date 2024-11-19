import streamlit as st
from tornado.options import options
from post_generator import generate_post

length_options=["Long","Medium","Short"]
lang_options=["English","Hinglish"]

from few_shot import FewShotPosts

def main():
    st.title("What you want to Post ??")
    col1,col2,col3 = st.columns(3)
    fs = FewShotPosts()
    with col1:
        selected_tag =st.selectbox("Post-Title",options=fs.get_tags())
    with col2:
        selected_lang=st.selectbox("Language ",options=lang_options)
    with col3:
       selected_len= st.selectbox("Length", options=length_options)
    if st.button("Generate"):
        post=generate_post(selected_len,selected_lang,selected_tag)
        st.write(post)

if __name__ == "__main__":
    main()