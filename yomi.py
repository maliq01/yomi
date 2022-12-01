import requests as requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu


from datetime import datetime
import calendar

# setting up page variables
page_title = "yomi exquisite"
page_icon = Image.open("image/yomi_logo.png")
layout = "wide"
currency = "ksh"

# --------setting up page config----------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)


# loading lottie files
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ----------setting up css----------------

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("style/style.css")

# ---------------loading assets--------------
logo = Image.open("image/yomi.png")
lipstick = Image.open("image/lipstickk.png")
lipstick_product = Image.open("image/ponds (5).jpg")
ponds_1 = Image.open("image/ponds (4).jpg")
mascarra = Image.open("image/images (1).jpg")
mascarra_1 = Image.open("image/images (2).jpg")
mascarra_2 = Image.open("image/images (3).jpg")
mascarra_3 = Image.open("image/images (4).jpg")
ponds_2 = Image.open("image/ponds (2).jpg")
ponds_3 = Image.open("image/ponds (3).jpg")
diamond_pond = Image.open("image/diapond.png")
home_lottie = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_j6nmheu0.json")
product_lottie = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jpsfxfin.json")
service_lottie = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_vchruvd5.json")


# ----------setting up option menu--------
selected = option_menu(
    menu_title=None,
    options=["Home", "Shop products", "Book services"],
    icons=["house-fill", "shop-window", "truck"],
    orientation="horizontal",

)


# -------setting up date and time----------

years = datetime.today().year
months = list(calendar.month_name[1:])


# setting up logo and web header

if selected == "Home":
    with st.container():
        logo_column, title_column, lottie_column = st.columns((1, 2, 1))
        with logo_column:
            st.image(logo)
            st.image(lipstick)
        with title_column:
            st.header("Yomi Exquisite")
            st.subheader("we not only make you look good. We make you feel good")
            st.write("""We are a one stop shop for all your beauty and cosmetic products.
                        Taking care of yourself is essential for your well-being.
                        It’s important to choose the right beauty products for your face, body and hair to achieve the results you’re looking for. 
                        From skin care products that leave your face hydrated and wrinkle-free, hair care products for gorgeous locks, to specially curated bath & body products for the entire family.
                        you can find all beauty products you need at Yomi Exquisite.
                        """)
            st.write("[learn more >](https://getbootstrap.com/)")
        with lottie_column:
            st_lottie(home_lottie, height=300, key="home_lottie")
            st.image(diamond_pond)


    "---"
    with st.container():
        text_column, lottie_column = st.columns((2, 1))
        with text_column:
            st.subheader("about our products:")
            st.write("""we offer top quality from verified suppliers at a really competitive price.
            Delivery of our products is free within the Nairobi Cbd area.
            we ship both nationally and internationally, prices vary with the location of delivery. 
            """)
        with lottie_column:
            st_lottie(product_lottie, height=200, key="product_lottie")
        col1, col2, col3, col4 = st.columns((1, 1, 1, 1))
        col1.image(lipstick_product)
        col2.image(ponds_1)
        col3.image(ponds_2)
        col4.image(ponds_3)
        "---"
        col5, col6, col7, col8 = st.columns((1, 1, 1, 1))
        col5.image(mascarra)
        col6.image(mascarra_1)
        col7.image(mascarra_2)
        col8.image(mascarra_3)
    "---"
    with st.container():
        lottie_column1, text_column1 = st.columns((1, 2))
        with lottie_column1:
            st_lottie(service_lottie, height=300, key="service_lottie")
        with text_column1:
            st.subheader(" about our services:")
            st.write("""we offer make up services for weddings, movies, baby showers and all corporate events.
            contact us to get yourself a complete make over and make your events and yourself glamorous and shine as you
            make your memorable moment shine.
            
            """)

    with st.container():
        st.write("---")
        st.subheader("contact us or make an order")
        st.write("##")
        contact_form = """
         <form action="https://formsubmit.co/wanjikumwaura98@gmail.com" method="POST">
         <input type = "hidden" name ="captcha" value ="false">
         <input type="text" name="name" placeholder= "your name" required>
         <input type="email" name="email" placeholder = "your email" required>
         <textarea name= "message" placeholder = "your message" required></textarea>
         <button type="submit">Send</button>
         </form>
    """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html = True)
        with right_column:
            st.empty()

    # ---------products-----------
if selected == "Shop products":
    image_column, price_column = st.columns(2)
    with image_column:
        st.image("image/yomi.png")
    with price_column:
        st.subheader("price 2000")
if selected == "Book services":
    image2_column, text2_column = st.columns((1, 2))
    st.subheader("Our services include:")
    st.write("""make up appliance for events such as baby showers, weddings,
    graduations and bridal showers.
    we also do movies and tv makeup to ensure you look glamorous on set.
    """)







