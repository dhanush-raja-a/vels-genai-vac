import streamlit as st
import os

# ==========================================
# 📘 TEACHING GUIDE FOR INSTRUCTOR
# ==========================================
# How to use this file:
# 1. Start the app: Run `streamlit run main.py` in your terminal.
# 2. Section 1 (Base UI) is already visible. Explain it to the students.
# 3. As you teach each concept, UNCOMMENT the corresponding block.
# 4. Save the file (Ctrl+S) and click 'Always Rerun' in Streamlit to see live changes.
#
# TIP: To uncomment a block in VS Code, highlight the lines and press (Cmd + /) or (Ctrl + /).
# ==========================================

# --- STEP 1: PAGE CONFIG & BASE UI ---
# This part is visible as soon as you run the app!
st.set_page_config(page_title="GenAI Blog Builder", page_icon="📝", layout="wide")

# Sidebar for settings
with st.sidebar:
    st.title("⚙️ AI Settings")
    persona = st.selectbox("Select AI Persona", ["Professional Writer", "Creative Storyteller", "Technical Expert"])
    st.info("This persona will change how the AI writes your blog!")

# Main Title & Hero Section
st.title("🤖 AI Blog Outline Generator")
st.markdown("### *Turning your ideas into structured blog posts using LangChain & Groq*")
st.divider()

user_topic = st.text_input("Enter a blog topic (e.g., 'Future of AI in Education')", placeholder="Type something...")

# ==========================================
# 🛑 STOP HERE AND TEACH STEP 1
# ==========================================

# --- STEP 2: LOAD API & INITIALIZE LLM ---
# Uncomment the following lines when you teach about Environment Variables and Models!

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load the .env file
load_dotenv()

# Initialize our connection to the AI (Groq)
try:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        temperature=0.7,
        api_key=os.getenv("GROQ_API_KEY")
    )
    st.sidebar.success("✅ AI Model Connected")
except Exception as e:
    st.sidebar.error("❌ API Key Missing or Invalid")


# ==========================================
# 🛑 STOP HERE AND TEACH STEP 2
# ==========================================

# --- STEP 3: CREATE PROMPT TEMPLATE ---
# Uncomment these lines to teach about Prompt Engineering!

from langchain.prompts import PromptTemplate

blog_template = PromptTemplate.from_template(
    """You are a {persona}. 
    Create a detailed, engaging blog outline for the topic: {topic}.
    
    Requirements:
    1. Include a catchy title recommendation.
    2. List 5 main chapters/sections.
    3. Add 3 bullet points of what to cover in each chapter.
    """
)


# ==========================================
# 🛑 STOP HERE AND TEACH STEP 3
# ==========================================

# --- STEP 4: TRIGGER LOGIC & INVOCATION ---
# Uncomment these lines to teach about how to trigger the AI!

if st.button("Generate My Outline", type="primary"):
    if user_topic:
        with st.spinner("AI is thinking..."):
            # 1. Format the template with our inputs
            formatted_prompt = blog_template.format(persona=persona, topic=user_topic)
            
            # 2. Invoke the LLM
            response = llm.invoke(formatted_prompt)
            
            # 3. Store the result in session state (so it stays on screen)
            st.session_state.blog_output = response.content
    else:
        st.warning("Please enter a topic first!")


# ==========================================
# 🛑 STOP HERE AND TEACH STEP 4
# ==========================================

# --- STEP 5: PREMIUM OUTPUT DISPLAY ---
# Uncomment these lines to show how to dress up the results!

if 'blog_output' in st.session_state:
    st.success("✨ Your Blog Outline is Ready!")
    
    # Using Streamlit "Containers" to make it look premium
    with st.container(border=True):
        st.markdown(st.session_state.blog_output)
        
    # Bonus: Add a download button for the outline!
    st.download_button(
        label="📥 Download Outline as Text",
        data=st.session_state.blog_output,
        file_name="blog_outline.txt",
        mime="text/plain"
    )
