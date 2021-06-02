import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
    #col1, mid, col2 = st.beta_columns([1, 1, 2])
    #with col1:
        #st.image('vcrime.jpg', width=350)
    #with col2:
        #st.write('A violent crime is when someone physically hurts or threatens to hurt someone, and also includes crimes where a weapon is used. The police will record a crime as violent if the offender clearly intended or intends to physically harm you, regardless of whether or not it results in a physical injury.')

    image = Image.open('vcrime.jpg')
    st.image(image, width=700)
    st.write(
        'A violent crime is when someone physically hurts or threatens to hurt someone, and also includes crimes where a weapon is used. The police will record a crime as violent if the offender clearly intended or intends to physically harm you, regardless of whether or not it results in a physical injury.')

    options = ["-", "Assault", "False Evidence", "Issuing or signing false certificate", "Robbery", "Kidnapping",
               "Vandalism", "Drug Possession", "Murder", "Rape", "Dacoity", "Burglary/Theft", "Motor Vehicle Theft",
               "Shoplifting", "Bribery", "Giving False Evidence", "Qatl-bis-sabab", "Qatl-e-khata"]
    choice = st.selectbox("Select Crime", options)




    if choice == "False Evidence":

        st.subheader("The Punishment for this crime is jail - 3 years and shall also be liable to fine. ")

    elif choice == "Issuing or signing false certificate":

        st.subheader("The Punishment for this crime is jail - 3 years and shall also be liable to fine.")

    elif choice == "Assault":

        st.subheader("The Punishment for Assault is jail - not less than one year and shall also be liable to fine. ")

    elif choice == "Robbery":

        st.subheader("The Punishment for Robbery is jail - up to 10 years and shall also be liable to fine.")

    elif choice == "Kidnapping":

        st.subheader("The Punishment for Kidnapping is jail - up to  7 years and shall also be liable to fine.")

    elif choice == "Vandalism":

        st.subheader("The Punishment for Vandalism is jail - up to 2 years and shall also be liable to fine.")

    elif choice == "Drug Possession":

        st.subheader("The Punishment for Drug Possession is jail - up to 1 years and shall also be liable to fine.")

    elif choice == "Murder":

        st.subheader("Death penalty is frequently imposed for murder. Death sentences for blasphemy and under the Zina Ordinance involving stoning to death have been imposed but not so far been carried out.")

    elif choice == "Rape":

        st.subheader("The Punishment for rape in Pakistan under the Pakistani laws is either death penalty or imprisonment of between ten and twenty-five years")

    elif choice == "Dacoity":

        st.subheader("Whoever commits dacoity shall be punished with imprisonment for life, or with rigorous imprisonment for a term which may extend to ten years, and shall also be liable to fine")

    elif choice == "Burglary/Theft":

        st.subheader("The Punishment for this Crime is jail - up to 3 years and shall also be liable to fine.")

    elif choice == "Motor Vehicle Theft":

        st.subheader("Whoever commits theft of a car or any other motor vehicle, including motor-cycle, scooter and Tractor shall be punished with imprisonment of either description for a term which may extend to seven years and with fine not exceeding the value of the stolen car or motor vehicle.")

    elif choice == "Shoplifting":

        st.subheader("The Punishment for Shoplifting is jail - up to 3 years and shall also be liable to fine.")

    elif choice == "Shoplifting":

        st.subheader("The Punishment for Shoplifting is jail - up to 3 years and shall also be liable to fine.")

    elif choice == "Bribery":

        st.subheader("The Punishment for Bribery is jail - 1 year and shall also be liable to fine.")

    elif choice == "Giving False Evidence":

        st.subheader("The Punishment for giving False Evidence is jail - 7 years and shall also be liable to fine.")

    elif choice == "Qatl-bis-sabab":

        st.subheader("Whoever commit Qatl bis-sabab shall be liable to diyat.")
        st.text("Whoever, without any intention, cause death of, or cause harm to, any person, does any unlawful ")
        st.text("act which becomes a cause for the death of another person, is said to commit qatl-bis-sabab.")
        st.subheader("Diyat")
        st.text("Diyat in Islamic law, is the financial compensation paid to the victim or heirs of a victim in the")
        st.text("cases of murder, bodily harm or property damage.")

    elif choice == "Qatl-e-khata":

        st.subheader("Whoever commits qatl-i-khata shall be liable to diyat")
        st.text("Whoever, without any intention to cause death of, or cause harm to, a person causes death of such")
        st.text("person, either by mistake of act or by mistake of fact, is said to commit qatl-i-khata.")
        st.subheader("Diyat")
        st.text("Diyat in Islamic law, is the financial compensation paid to the victim or heirs of a victim in the")
        st.text("cases of murder, bodily harm or property damage.")

