# import streamlit as st
# from pdf_agent_backend import retrival_qn_chain, get_response

# st.title("PDF Chatbot with RAG")

# uploaded_file = st.file_uploader('Upload a PDF file', type=['pdf'])

# if uploaded_file is not None:
#     file_path = 'RAG_AGENT_PROJECT/' + uploaded_file.name

#     with open(file_path, 'wb') as f:
#         f.write(uploaded_file.getbuffer())
#     st.success("save file")
    
#     chain = retrival_qn_chain(file_path)

#     user_question = st.text_input("Enter Your Question:", placeholder="Ask anything about the PDF...")

#     if user_question:
#         with st.spinner("Getting Response..."):
#             answer= get_response(user_question, chain)
#             st.markdown("### Answer:")
#             st.write(answer)


# if not uploaded_file:
#     st.info("Please upload a PDF file to start interacting with the chatbot.")











import streamlit as st
from pdf_agent_backend import retrival_qn_chain, get_response

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="PDF Chatbot with RAG", layout="wide")
st.title("📄 PDF Chatbot with RAG")

# ---------- SESSION STATE ----------
if "chain" not in st.session_state:
    st.session_state.chain = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "processing_done" not in st.session_state:
    st.session_state.processing_done = False

# ---------- FILE UPLOAD ----------
uploaded_file = st.file_uploader("📤 Upload a PDF file", type=["pdf"])

if uploaded_file is not None and not st.session_state.processing_done:
    file_path = f"RAG_AGENT_PROJECT/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ PDF uploaded successfully")

    # ---------- PROCESSING PDF ----------
    with st.spinner("⏳ Processing PDF... Please wait 1–2 minutes"):
        st.session_state.chain = retrival_qn_chain(file_path)

    st.session_state.processing_done = True
    st.success("🚀 PDF processing completed! You can now ask questions.")

# ---------- CHAT SECTION ----------
if st.session_state.processing_done:

    st.markdown("---")
    st.subheader("💬 Ask Questions")

    user_question = st.text_input(
        "Type your question",
        placeholder="Ask anything about the uploaded PDF...",
        key="user_input"
    )

    if user_question:
        with st.spinner("🤖 Thinking..."):
            answer = get_response(user_question, st.session_state.chain)

        # Save chat
        st.session_state.chat_history.append({
            "question": user_question,
            "answer": answer
        })

        # Clear input
        st.rerun()

    # ---------- DISPLAY CHAT HISTORY ----------
    st.markdown("## 📜 Chat History")

    for chat in reversed(st.session_state.chat_history):
        st.markdown(
            f"""
            <div style="background-color:#e8f0fe;padding:12px;border-radius:10px;margin-bottom:8px">
                <b>🧑 You:</b><br>{chat['question']}
            </div>
            <div style="background-color:#f1f3f4;padding:12px;border-radius:10px;margin-bottom:20px">
                <b>🤖 Bot:</b><br>{chat['answer']}
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------- INFO ----------
if not uploaded_file:
    st.info("⬆️ Upload a PDF to start chatting")
