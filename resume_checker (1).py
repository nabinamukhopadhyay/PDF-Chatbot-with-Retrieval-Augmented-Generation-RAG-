import streamlit as st
from io import StringIO, BytesIO
import pdfplumber
from resume_main_logic import get_response


st.title("AI Resume Checker")
st.caption("Compare Resume and Job Description")



def render_resume_report(report):
    # Header
    st.subheader("📊 Resume Match Report")

    # Match Score (Big & Visual)
    score = report.get("match_score", 0)

    col1, col2 = st.columns([1, 3])
    with col1:
        st.metric(
            label="Match Score",
            value=f"{score} / 100"
        )

    with col2:
        st.progress(score / 100)

    st.divider()

    # Strengths
    st.markdown("### ✅ Strengths")
    strengths = report.get("strengths", [])
    if strengths:
        for s in strengths:
            st.success(s)
    else:
        st.info("No strong matches identified.")

    # Gaps
    st.markdown("### ⚠️ Gaps / Missing Areas")
    gaps = report.get("gaps", [])
    if gaps:
        for g in gaps:
            st.warning(g)
    else:
        st.success("No major gaps identified.")

    # Feedback
    st.markdown("### 🛠 Resume Improvement Suggestions")
    feedback = report.get("feedback", [])
    if feedback:
        for f in feedback:
            st.info(f)
    else:
        st.info("No improvement suggestions.")

    # Summary
    st.divider()
    st.markdown("### 📝 Overall Summary")
    st.write(report.get("summary", "No summary provided."))



upload_file = st.file_uploader('Upload Resume', type=['pdf'])



if upload_file:
    file_path = upload_file.name

    with open(file_path, 'wb') as f:
        f.write(upload_file.getbuffer())
    st.success("save file")


jd = st.text_area("Jod Description : ", placeholder="Enter Jd ..")

if st.button("Analyze"):
    with st.spinner("Anylyzing....."):
        if upload_file and jd:
            response = get_response(file_path, jd)
            render_resume_report(response)
        else:
            st.error("Please Upload file  and JD")




