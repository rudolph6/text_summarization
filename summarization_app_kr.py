import streamlit as st
import summarization_lib_kr as glib

st.set_page_config(layout="wide", page_title="문서 요약")
st.title("문서 요약")

return_intermediate_steps = st.checkbox("중간 단계 반환", value=True)
summarize_button = st.button("요약", type="primary")

if summarize_button:
    st.subheader("통합 요약")

    with st.spinner("Running..."):
        response_content = glib.get_summary(return_intermediate_steps=return_intermediate_steps)


    if return_intermediate_steps:

        st.write(response_content["output_text"])

    else:
        st.write(response_content["output_text"])

