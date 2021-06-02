import streamlit as st
from PIL import Image


def app():
    options = ["-","Punjab Crime Profile", "All Reported Crimes", "Prosecution", "Crimes Against Person",
               "Property Crimes", "Local & Special Laws Violations", "Miscellaneous", "Cyber Crime during Lockdown"]
    choice = st.selectbox("Select Crime", options)

    if choice == "Punjab Crime Profile":
       image1 = Image.open('1.png')
       st.image(image1)

    elif choice == "All Reported Crimes":
       image2 = Image.open('2.png')
       st.image(image2)

    elif choice == "Prosecution":
       image3 = Image.open('3.png')
       st.image(image3)


    elif choice == "Crimes Against Person":
       st.subheader("CRIMES AGAINST PERSON")

       image4 = Image.open('4.png')
       st.image(image4)
       image5 = Image.open('5.png')
       st.image(image5)
       image6 = Image.open('6.png')
       st.image(image6)
       image7 = Image.open('7.png')
       st.image(image7)
       image8 = Image.open('8.png')
       st.image(image8)
       image9 = Image.open('9.png')
       st.image(image9)
       image10 = Image.open('10.png')
       st.image(image10)

    elif choice == "Property Crimes":

       st.subheader("CRIMES AGAINST PROPERTY")

       image11 = Image.open('11.png')
       st.image(image11)
       image12 = Image.open('12.png')
       st.image(image12)
       image13 = Image.open('13.png')
       st.image(image13)
       image14 = Image.open('14.png')
       st.image(image14)
       image15 = Image.open('15.png')
       st.image(image15)
       image16 = Image.open('16.png')
       st.image(image16)
       image17 = Image.open('17.png')
       st.image(image17)
       image18 = Image.open('18.png')
       st.image(image18)


    elif choice == "Local & Special Laws Violations":
       st.subheader("Local & Special Laws Violations")

       image19 = Image.open('19.png')
       st.image(image19)

    elif choice == "Miscellaneous":
       st.subheader("Miscellaneous")

       image20 = Image.open('20.png')
       st.image(image20)

    elif choice == "Cyber Crime during Lockdown":
       st.subheader("Cybercrime peaked in Pakistan during the lockdown")

       image21 = Image.open('21.jpg')
       st.image(image21)
       image22 = Image.open('22.jpg')
       st.image(image22)

