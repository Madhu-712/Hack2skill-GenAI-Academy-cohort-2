import streamlit as st
import streamlit.components.v1 as components

# Set up a wide, modern layout for a professional dashboard look
st.set_page_config(page_title="BigQuery Legal Data Agent", layout="wide", page_icon="💼")

# Title and Subtitle
st.title("💼 Legal Contract Data Agent")
st.markdown("Interact directly with **your_legal_dataset** using natural language via Vertex AI BigQuery Data Agents.")

st.markdown("---")

# Create two columns: Left for information/metrics, Right for the actual Chat Agent
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Current Dataset Scope")
    st.info("""
    **Connected Tables:**
    * `clauses` (Uploaded successfully)
    * `contracts`
    * `legal_terms`
    * `summaries`
    """)
    
    st.markdown("### 💡 Example Prompts to Try:")
    st.write("👉 *'Summarize the primary clauses in the latest contract.'*")
    st.write("👉 *'Are there any conflicting legal terms in our clauses table?'*")
    st.write("👉 *'Give me a breakdown of contract summaries by date.'*")

with col2:
    st.subheader("💬 Chat with your BigQuery Agent")
    
    # Your Looker Studio conversation link
    AGENT_URL = "https://lookerstudio.google.com/conversation?agent=projects/notebooklm-491108/locations/us/dataAgents/agent_c03cf192-61ec-4859-a042-4bd22d531bc5"
    
    # Embed the Looker Studio Conversation UI directly into the Streamlit App
    components.iframe(AGENT_URL, height=650, scrolling=True)

st.markdown("---")
st.caption("Built with Streamlit • Powered by Google Cloud Vertex AI & BigQuery Data Agents")