import streamlit as st
import pandas as pd
import base64
import os
import datetime
from PIL import Image
from io import BytesIO
from streamlit_option_menu import option_menu

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="AMINA | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CUSTOM CSS ====================
def local_css():
    st.markdown("""
    <style>
    /* Main styling */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Custom containers */
    .card {
        padding: 2rem;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    /* Title styling */
    .title-text {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .subtitle-text {
        font-size: 1.5rem;
        color: #6c757d;
        margin-bottom: 2rem;
    }
    
    /* Section headers */
    .section-header {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 3rem 0 1.5rem 0;
        color: #ffffff;
        border-left: 5px solid #667eea;
        padding-left: 1rem;
    }
    
    /* Skill badges */
    .skill-badge {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        margin: 0.5rem;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .skill-badge-beginner {
        background: rgba(255, 193, 7, 0.2);
        border: 2px solid #ffc107;
        color: #ffc107;
    }
    
    .skill-badge-intermediate {
        background: rgba(0, 123, 255, 0.2);
        border: 2px solid #007bff;
        color: #007bff;
    }
    
    .skill-badge-advanced {
        background: rgba(40, 167, 69, 0.2);
        border: 2px solid #28a745;
        color: #28a745;
    }
    
    .skill-badge-expert {
        background: rgba(111, 66, 193, 0.2);
        border: 2px solid #6f42c1;
        color: #6f42c1;
    }
    
    .skill-badge:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Project cards */
    .project-card {
        padding: 1.5rem;
        border-radius: 10px;
        background: rgba(30, 30, 40, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        height: 100%;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        border-color: #667eea;
        transform: translateY(-3px);
    }
    
    /* Timeline */
    .timeline-item {
        padding: 1rem 1.5rem;
        border-left: 2px solid #667eea;
        margin: 1rem 0;
        position: relative;
    }
    
    .timeline-item:before {
        content: '';
        position: absolute;
        left: -7px;
        top: 20px;
        width: 12px;
        height: 12px;
        background: #667eea;
        border-radius: 50%;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Contact icons */
    .contact-icon {
        font-size: 2rem;
        transition: transform 0.3s ease;
    }
    
    .contact-icon:hover {
        transform: translateY(-3px);
    }
    
    </style>
    """, unsafe_allow_html=True)

local_css()

# ==================== HELPER FUNCTIONS ====================
def display_image(image_path, width=300):
    """Display image with placeholder fallback"""
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            img.thumbnail((width, width))
            img_bytes = BytesIO()
            img.save(img_bytes, format='PNG')
            st.image(img_bytes, width=width)
        except Exception as e:
            st.error(f"Error loading image: {e}")
            create_placeholder(width)
    else:
        create_placeholder(width)

def create_placeholder(width=300):
    """Create a profile placeholder"""
    st.markdown(f'<div style="width: {width}px; height: {width}px; background: linear-gradient(45deg, #667eea, #764ba2); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto;"><span style="font-size: {width//3}px; color: white;">JD</span></div>', unsafe_allow_html=True)

def create_download_link(file_path, link_text):
    """Create a download link for files"""
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            file_content = file.read()
        b64 = base64.b64encode(file_content).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{os.path.basename(file_path)}" style="background: linear-gradient(45deg, #667eea, #764ba2); padding: 0.8rem 2rem; border-radius: 5px; color: white; text-decoration: none; display: inline-block; margin-top: 1rem;">{link_text}</a>'
        return href
    return ""

# ==================== NAVIGATION MENU ====================
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Skills", "Projects", "Experience", "Contact"],
        icons=["house", "person", "tools", "code-slash", "briefcase", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "rgba(0,0,0,0)"},
            "icon": {"color": "white", "font-size": "20px"}, 
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "rgba(100, 126, 234, 0.1)",
            },
            "nav-link-selected": {"background-color": "#667eea"},
        }
    )

# ==================== HOME PAGE ====================
if selected == "Home":
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown('<h1 class="title-text">Amina A</h1>', unsafe_allow_html=True)
        st.markdown('<h2 class="subtitle-text">python and ML intern,data scientist intern,data analyst intern</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <p style="font-size: 1.2rem; line-height: 1.8;">
            a passionate intern fascinated in Machine learning 
            scalable machine learning solutions and web applications. 
            Specialized in Python, TensorFlow, and Data visualizations.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        cv_link = create_download_link("AMINA_UPDATED_RESUME.pdf", "📄 Download CV")
        if cv_link:
            st.markdown(cv_link, unsafe_allow_html=True)
        else:
            st.markdown('<div style="margin-top: 2rem;"><a href="#contact" style="background: linear-gradient(45deg, #667eea, #764ba2); padding: 0.8rem 2rem; border-radius: 5px; color: white; text-decoration: none; margin-right: 1rem; display: inline-block;">Get in Touch</a><a href="#projects" style="border: 2px solid #667eea; padding: 0.8rem 2rem; border-radius: 5px; color: #667eea; text-decoration: none; display: inline-block;">View Projects</a></div>', unsafe_allow_html=True)
    
    with col2:
        display_image("image1p.jpeg", width=300)

# ==================== ABOUT PAGE ====================
elif selected == "About":
    st.markdown('<h1 class="section-header">About Me</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # About content - using separate markdown calls
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3>My Journey</h3>', unsafe_allow_html=True)
        st.markdown('<p>I\'m a passionate intern fascinated in Machine learning. With a Bachelor\'s in Computer Science from Dhanalakshmi srinivasan engineering college, I\'ve experience with leading real time prjects and internships to deliver innovative solutions.</p>', unsafe_allow_html=True)
        st.markdown('<h3>Philosophy</h3>', unsafe_allow_html=True)
        st.markdown('<p>I believe in writing clean, efficient code and building solutions that make a real impact. My approach combines technical excellence with user-centric design thinking.</p>', unsafe_allow_html=True)
        st.markdown('<h3>Education</h3>', unsafe_allow_html=True)
        st.markdown('<div class="timeline-item"><h4>Dhanalakshmi srinivasan engineering college</h4><p><strong>B.E. Computer Science and engineering</strong> | 2022-2026</p><p>Specialization in Machine Learning & Data analysis</p></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Quick stats
        st.markdown("""
        <div class="card">
            <h3>Quick Stats</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 1rem;">
                <div style="text-align: center;">
                    <h2 style="color: #667eea; margin: 0;">Fresher</h2>
                    <p>Years Experience</p>
                </div>
                <div style="text-align: center;">
                    <h2 style="color: #667eea; margin: 0;">5+</h2>
                    <p>Projects Completed</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Interests
        st.markdown("""
        <div class="card">
            <h3>Interests</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem;">
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.5rem 1rem; border-radius: 20px;">AI Research</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.5rem 1rem; border-radius: 20px;">ML presentations</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.5rem 1rem; border-radius: 20px;">Avid reader</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.5rem 1rem; border-radius: 20px;">Cooking</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.5rem 1rem; border-radius: 20px;">tutoring</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==================== SKILLS PAGE ====================
elif selected == "Skills":
    st.markdown('<h1 class="section-header">Technical Skills</h1>', unsafe_allow_html=True)
    
    st.markdown("### 🚀 Programming Languages")
    languages = [("Python", "advanced"),  ("SQL", "intermediate"), ("Java", "intermediate"), ("ML", "intermediate"), ("Data visualization", "intermediate")]
    badges_html = "".join([f'<span class="skill-badge skill-badge-{level}">{lang}</span>' for lang, level in languages])
    st.markdown(f'<div class="card"><div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">{badges_html}</div></div>', unsafe_allow_html=True)
    
    st.markdown("### ⚡ Frameworks & Libraries")
    frameworks = [("TensorFlow", "intermediate"), ("PyTorch", "intermediate"), ("svm", "advanced"), ("matplotlib", "intermediate"), ("Streamlit", "advanced"),('CNN', 'intermediate'),('ViTS','intermediate')]
    
    col1, col2 = st.columns(2)
    with col1:
        frameworks_html1 = "".join([f'<span class="skill-badge skill-badge-{level}">{fw}</span>' for fw, level in frameworks[:3]])
        st.markdown(f'<div class="card"><div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">{frameworks_html1}</div></div>', unsafe_allow_html=True)
    
    with col2:
        frameworks_html2 = "".join([f'<span class="skill-badge skill-badge-{level}">{fw}</span>' for fw, level in frameworks[3:]])
        st.markdown(f'<div class="card"><div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">{frameworks_html2}</div></div>', unsafe_allow_html=True)
    
    st.markdown("### 🛠️ Tools & Platforms")
    tools = [("VS Code", "advanced"), ("Jupyter notebook", "intermediate"), ("Git", "advanced"), ("MySQL",  "intermediate")]
    
    cols = st.columns(4)
    for i, (tool, level) in enumerate(tools):
        with cols[i]:
            st.markdown(f'<div style="text-align: center; padding: 1rem; background: rgba(100, 126, 234, 0.1); border-radius: 10px; margin: 0.5rem 0;"><div style="font-size: 2rem;"></div><div style="font-weight: 600; margin-top: 0.5rem;">{tool}</div><div style="margin-top: 0.5rem;"><span class="skill-badge skill-badge-{level}" style="padding: 0.2rem 0.8rem; font-size: 0.8rem;">{level.title()}</span></div></div>', unsafe_allow_html=True)

# ==================== PROJECTS PAGE ====================
elif selected == "Projects":
    st.markdown('<h1 class="section-header">Featured Projects</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>Real time captioning system</h3>
            <p>live captioning with help of google API </p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">Python</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">pytorch</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">whisper</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3> real time Oil spill detection using ml </h3>
            <p>Highlighting the oil the oill spilled area from SAR images.</p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">SVM</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">Scikit-Learn</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">Streamlit</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>Brain cancer detection using CNN and VIT</h3>
            <p>Trained with image labels,CNN covers the global features and ViTS covers the local features</p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">convolutional neural network</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">Vision Transformers</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">SVM classifier</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3>plant disease prediction</h3>
            <p>identifying disease undeer tuned working .</p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">Gradient boosting</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">cnn</span>
                <span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">SVM</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==================== EXPERIENCE PAGE ====================
elif selected == "Experience":
    st.markdown('<h1 class="section-header">Professional Experience</h1>', unsafe_allow_html=True)
    
    experiences = [
        {
            "title": "ML intern",
            "company": "fantasy solution",
            "period": "2025",
            "description": ["Learnt ML pipelines serving ", "Reduced inference time by 40%", "tuned the performance"]
        },
        {
            "title": "ML enginner intern",
            "company": "Code Alpha",
            "period": "2025",
            "description": ["involved multiple tasks or volume based completion", "Credit-scoring", "heart disease prediction"]
        },
        
    ]
    
    for exp in experiences:
        exp_html = f'<div class="card"><div style="display: flex; justify-content: space-between; align-items: start;"><div><h3 style="margin: 0;">{exp["title"]}</h3><h4 style="color: #667eea; margin: 0.5rem 0;">{exp["company"]}</h4></div><span style="background: rgba(100, 126, 234, 0.2); padding: 0.3rem 1rem; border-radius: 15px;">{exp["period"]}</span></div><ul style="margin-top: 1rem;">{"".join([f"<li>{item}</li>" for item in exp["description"]])}</ul></div>'
        st.markdown(exp_html, unsafe_allow_html=True)

# ==================== CONTACT PAGE - COMPLETELY FIXED ====================
elif selected == "Contact":
    st.markdown('<h1 class="section-header">Get in Touch</h1>', unsafe_allow_html=True)
    # Contact Summary Table
    st.markdown("### 📋 Contact Summary")
    contact_summary = pd.DataFrame({
        'Method': ['Email', 'Phone', 'LinkedIn', 'Github', 'Response Time'],
        'Details': ['aminashajanbee@gmail.com', '9597592877', 'https://www.linkedin.com/in/amina1610', 'https://github.com/aminashajan', 'Within 24 hours']
      })
    st.dataframe(contact_summary, use_container_width=True, hide_index=True)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown('<div style="text-align: center; color: #6c757d; padding: 2rem 0;"><p>© 2025 Amina/16. All rights reserved.</p><p style="font-size: 0.9rem;">Built with ❤️ using Streamlit & Python</p></div>', unsafe_allow_html=True)