import streamlit as st
import pandas as pd
from PIL import Image
import hashlib

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# DB Management
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()


# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT username FROM userstable')
    data = c.fetchall()
    return data


#def view_user_record():
    #c.execute('SELECT DISTINCT username FROM userstable')
    #data = c.fetchall()
    #return data


def main():
    """Simple Login App"""

menu = ["Home", "Login", "SignUp", "Admin"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
        st.title("""WELCOME TO ONLINE LEGISLATION SYSTEM
               """)
        st.text("")

        image = Image.open('img.jpg')
        st.image(image)

        st.text("")

        st.text("Online Legislation System is a project in which I have focused on bringing an outcome of")
        st.text(" punishments to the crimes that includes almost all sort of crimes including the digital ")
        st.text(" crimes in accordance to the Pakistan’s Law. The main purpose of keeping the name of my  ")
        st.text(" project as Online Legislation System is that Legislation is a law or a set of laws that ")
        st.text(" have been passed by the Parliament. And my project mainly focuses on telling the exact  ")
        st.text(" punishments and sanctions according to the Pakistan's law. It is a simple project that ")
        st.text(" simply provides with the output which will be the punishments of crimes that the user ")
        st.text(" will select.")
        st.text("Punishments are according to PECA i.e; Pakistan Electronic Crime Act, 2016 for Cyber Crime")
        st.text("and Pakistan Penal Code for Violent Crimes.")
        st.text("------------------------------------------------------------------------------------------")
        st.header("PECA - Pakistan Electronic Crime Act, 2016.")
        image = Image.open("peca.jpg")
        st.image(image)
        st.text("In 2016, the National Assembly enacted the Prevention of Electronic Crimes Act (“PECA”) to")
        st.text("provide comprehensive legal framework to define many kinds of electronic crimes, mechanisms")
        st.text("for investigation, prosecution and adjudication in relation to electronic crimes.")
        st.text("http://www.na.gov.pk/uploads/documents/1462252100_756.pdf")
        st.text("-------------------------------------------------------------------------------------------")
        st.header("Pakistan Penal Code.")
        image = Image.open("ppc.jpg")
        st.image(image, width=700)
        st.text("Pakistan Penal Code abbreviated as PPC, is a penal code for all offences charged in Pakistan.")
        st.text("It was originally prepared by Lord Macaulay with a great consultation in 1860 on the behalf of")
        st.text("the Government of India as Indian Penal Code. After the independence(1947), Pakistan inherited")
        st.text("the same code and subsequently after several amendments by different governments, in Pakistan ")
        st.text("it is now a mixture of Islamic and English Law. Presently, the Pakistan Penal Code is still in")
        st.text("effect and can be amended by the Senate of Pakistan")
        st.text("http://www.pakistani.org/pakistan/legislation/1860/actXLVof1860.html")



elif choice == "Login":
        st.subheader("Login Section")
        # image = Image.open('crime1.png')
        # st.image(image, width=700)
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:

                st.success("Logged In as {}".format(username))

                import Cyber_Crime
                import statistics
                import v_crime
                import streamlit as st

                PAGES = {

                     "Crime Statistics": statistics,
                     "Cyber Crimes": Cyber_Crime,
                     "Violent Crimes": v_crime

                 }
                st.title('Navigation')
                selection = st.radio("Go to", list(PAGES.keys()))
                page = PAGES[selection]
                page.app()

            else:
                st.warning("Incorrect Username/Password")

elif choice == "SignUp":
        st.title("Register yourself")
        st.text(" ")
        st.subheader("Registration Page")
        st.text(" ")
        st.subheader("CREATE NEW ACCOUNT")
        #
        #           # menu1 = ["User", "Admin"]
        #           # choice1 = st.selectbox("Menu", menu1)
        #
        #           if choice1 == "User":
        new_user1 = st.text_input("Username")
        new_password1 = st.text_input("Password", type='password')
        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user1, make_hashes(new_password1))
            st.success("Account created successfully!")
            st.info("Go to Login Menu to login")

elif choice == "Admin":
    st.subheader("Welcome")

    def authenticate(username, password):
        return username == "admin123" and password == "admin456"

    username = st.text_input('Admin_Name')
    password = st.text_input("password", type='password')
    if st.checkbox("Login"):
        if authenticate(username, password):
            st.success('You are Successfully Login as Admin !')
            task = st.selectbox("Task", ["Select option", "Profiles"])
            if task == "Profiles":
                st.subheader("Users Profiles")
                #user_result = view_user_record()
                user_result = view_all_users()
                clean_db = pd.DataFrame(user_result,
                                        columns=["Username"])
                st.dataframe(clean_db)

                import Cyber_Crime
                import statistics
                import v_crime


                PAGES = {

                    "Crime Statistics": statistics,
                    "Cyber Crimes": Cyber_Crime,
                    "Violent Crimes": v_crime

                }
                st.title('Navigation')
                selection = st.radio("Go to", list(PAGES.keys()))
                page = PAGES[selection]
                page.app()

        else:
            st.error('The username or password you have entered is invalid.')
            st.success("Account created successfully!")
            st.info("Go to Login Menu to login")

    if __name__ == '__main__':
        main()
