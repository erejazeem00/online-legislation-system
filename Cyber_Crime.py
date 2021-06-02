import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
    #col1, mid, col2 = st.beta_columns([1, 1, 2])
    #with col1:
        #st.image('crime.png', width=700)
    #with col2:
        #st.write('Cyber crime refers to criminal activity where computer or a network is the source, tool, target, or any site of a crime. Although cyber crime are much more properly restricted to describing criminal activity in which computer or network is part of crime that is necessary.')

    image = Image.open('crime.png')
    st.image(image, width=700)
    st.write('Cyber crime refers to criminal activity where computer or a network is the source, tool, target, or any site of a crime. Although cyber crime are much more properly restricted to describing criminal activity in which computer or network is part of crime that is necessary.')

    options = ["-","Cyber Stalking", "Cyber Terrorism", "Spamming", "Spoofing", "Electronic Forgery",
               "Electronic Fraud", "Unauthorized access to information system or data",
               "Unauthorized copying or transmission of data", "Interference with information system or data",
               "Unauthorized access to critical infrastructure information system or data",
               "Unauthorized copying of data", "Interference with critical infrastructure information system or data",
               "Glorification of an offence and hate speech", "Making, obtaining, or supplying device for use in offence",
               "Unauthorized use of identity information", "Unauthorized issuance of SIM cards","Tampering of communication equipment",
               "Unauthorized interception", "Offences against dignity of natural person","Offences against modesty of a natural person and minor",
               "Child Pornography"]
    choice = st.selectbox("Select Crime", options)


    if choice == "Cyber Stalking":

        st.subheader("The Punishment for Cyber Stalking is jail - 5 years and fine 10 million rupees")
        st.text("")
        st.text("Cyber Stalking is the use of the Internet or other electronic means to stalk or harass an")
        st.text("individual, group, or organization. It may include false accusations, defamation, slander")
        st.text(" and libel.")

    elif choice == "Cyber Terrorism":

        st.subheader("The Punishment for Cyber Terrorism is jail - 14 years and fine fifty million rupees")
        st.text("")
        st.text("Cyber Terrorism is the use of the Internet to conduct violent acts that result in, or ")
        st.text("threaten, loss of life or significant bodily harm, in order to achieve political or  ")
        st.text("ideological gains through threat or intimidation.")

    elif choice == "Spamming":

        st.subheader("The Punishment for Spamming is jail - 3 months and fine one million rupees")
        st.text("")
        st.text("Spam is a crime against all users of the Internet since it wastes both the storage ")
        st.text("and network capacities of ISPs, as well as often simply being offensive.")

    elif choice == "Spoofing":

        st.subheader("The Punishment for Spoofing is jail - 3 years and fine five hundred thousand rupees ")
        st.text("")
        st.text("Spoofing is the act of disguising a communication from an unknown source as being ")
        st.text(" from a known, trusted source. Spoofing can apply to emails, phone calls, and websites,")
        st.text(" or can be more  technical, such as a computer spoofing an IP address, Address Resolution  ")
        st.text("Protocol (ARP), or Domain Name System (DNS) server.")



    elif choice == "Electronic Forgery":

        st.subheader("The Punishment for Electronic Forgery is jail - 7 years and fine 5 million rupees")
        st.text("")
        st.text("Electronic forgery means the creation or use of an “electronic signature” of that of ")
        st.text("another natural person without authorization or ratification, and with the intent to")
        st.text(" deceive.")

    elif choice == "Electronic Fraud":

        st.subheader("The Punishment for Electronic Fraud is jail - 2 years and fine ten million rupees ")
        st.text("")
        st.text("Electronic fraud is a type of cybercrime fraud or deception which makes use of the ")
        st.text("Internet and could involve hiding of information or providing incorrect information ")
        st.text("for the purpose of tricking victims out of money, property, and inheritance")

    elif choice == "Unauthorized access to information system or data":

        st.subheader("The Punishment for this crime is jail- 3 months and fine fifty thousand rupees ")
        st.text("")
        st.text("")

    elif choice == "Unauthorized copying or transmission of data":

        st.subheader("The Punishment for this crime is jail -  6 months and fine one hundred thousand rupees ")
        st.text("")
        st.text("")

    elif choice == "Interference with information system or data":

        st.subheader("The Punishment for this crime is jail - 2 years and fine five hundred thousand rupees")
        st.text("")
        st.text("")

    elif choice == "Unauthorized access to critical infrastructure information system or data":

        st.subheader("The Punishment for this crime is jail - 3 years and fine one million")
        st.text("")
        st.text("")

    elif choice == "Unauthorized copying of data":

        st.subheader("The Punishment for this crime is jail - 5 years and fine five million rupees")
        st.text("")
        st.text("")

    elif choice == "Interference with critical infrastructure information system or data":

        st.subheader("The Punishment for this crime is jail - 7 years and fine ten million rupees")
        st.text("")
        st.text("")

    elif choice == "Glorification of an offence and hate speech":

        st.subheader("The Punishment for this crime is jail - 5 years and fine ten million rupees")
        st.text("")
        st.text("")

    elif choice == "Making, obtaining, or supplying device for use in offence":

        st.subheader("The Punishment for this crime is jail - 6 months and fine fifty thousand rupees ")
        st.text("")
        st.text("")

    elif choice == "Unauthorized use of identity information":

        st.subheader("The Punishment for this crime is jail- 3 years and fine 5 million rupees ")
        st.text("")
        st.text("")

    elif choice == "Unauthorized issuance of SIM cards":

        st.subheader("The Punishment for this crime is jail -  3 years and fine five hundred thousand rupees ")
        st.text("")
        st.text("")

    elif choice == "Tampering of communication equipment":

        st.subheader("The Punishment for this crime is jail - 3 years and fine one million rupees")
        st.text("")
        st.text("")

    elif choice == "Unauthorized interception":

        st.subheader("The Punishment for this crime is jail - 2 years and fine five hundred thousand rupees")
        st.text("")
        st.text("")

    elif choice == "Offences against dignity of natural person":

        st.subheader("The Punishment for this crime is jail- 3 years and fine five hundred thousand rupees ")
        st.text("")
        st.text("")

    elif choice == "Offences against modesty of a natural person and minor":

        st.subheader("The Punishment for this crime is jail -  7 years and fine 5 million rupees")
        st.text("")
        st.text("")



    elif choice == "Child Pornography":

        st.subheader("The Punishment for Child Pornography is jail - 7 years and fine 5 million rupees")
        st.text("")
        st.text("")

    elif choice == "":

        st.subheader("")
        st.text("")
        st.text("")

    elif choice == "":

        st.subheader("")
        st.text("")
        st.text("")

