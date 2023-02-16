import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

# pip install streamlit - for framework
# pip install streamlit-lottie for gifs
# pip install requests - requests library
# pip install pillow - for images
# find more emojis here https://www.webfx.com/tools/emoji-cheat-sheet/
# animation files from lottiefiles.com
# get forms from formsubmit.co
# pip install pipreqs for deployment

#run the app "python -m streamlit run app.py"


st.set_page_config(page_title="My Webpage", page_icon=":blue_heart:", layout="wide")


# request animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#function to get css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")


# load assets
lottie_coding = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_tfb3estd.json"
)  # gif
first_img = Image.open("images/first_img1.jpeg")
second_img = Image.open("images/second_img.jpeg")

# header section
with st.container():
    st.subheader("Hi, I am Olumide :wave:")
    st.title("A web developer from Nigeria")
    st.write(
        "I am passionate about using graphics software and python for making businesses more effective"
    )
    st.write("[learn more >](https://new-syte.netlify.app/)")

# about me
with st.container():
    st.write("---")  # makes lines
    left_column, right_column = st.columns(2)  # making two columns
    with left_column:  # content of the left column
        st.header("What I do :rocket:")
        st.write("##")
        st.write(
            """My name is Olumide Adewole.
                 I am a Front-End Designer and a graphics designer I have had 4 years of experience making websites with HTML, CSS and JAVASCRIPT and made graphics with PHOTOSHOP, AFTER EFFECTS, ILLUSTRATOR, FIGMA and CANVA.
                 I deliver projects quickly and all projects meet your aesthetic needs. I currently work as a Health Informatics Intern at Maryland Global Initiatives Corporation.
                 I look forward to working with you.
                 Love, M :heart:"""
        )
        st.write("[Follow my Instagram >](https://instagram.com/mide.6x)")

    with right_column:
        st_lottie(lottie_coding, height=450, key="Coding")

# projects

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    # insert image
    with image_column:
        st.image(first_img)
    with text_column:
        st.subheader("Therapy Website")
        st.write(
            """I made this therapy website using HTML, CSS and JavaScript.
        colors and effects make our website more fun and that is what I took note of in the development of this website.
        I also made it as minimalistic as possible."""
        )
        st.write("[See Demo...](https://wallforworries.netlify.app/)")
with st.container():
    text_column, image_column = st.columns((2, 1))
    with text_column:
        st.subheader("Another Portfolio Page")
        st.write(
            """I made another portfolio website using HTML, CSS and JavaScript.
        colors and effects makes this website look really good and I had fun doing this.
        I made it as colorful as possible so as to capture peoples fancy."""
        )
        st.write("[See Demo...](https://new-syte.netlify.app/)")
    with image_column:
        st.image(second_img)

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documentation: https://formsubmit.co/ remember to change the email address
    contact_form = """
    <form action="https://formsubmit.co/adewoleolumide05@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>"""

    #adding the contact form to out app.
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
