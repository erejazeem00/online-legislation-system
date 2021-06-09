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
        st.info("http://www.na.gov.pk/uploads/documents/1462252100_756.pdf")
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
        st.info("http://www.pakistani.org/pakistan/legislation/1860/actXLVof1860.html")



elif choice == "Login":
        st.subheader("Login Section")
        image = Image.open('crime1.png')
        st.image(image, width=700)
        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        if st.checkbox("Login"):
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
                
                st.write("---------------------------------------------------------------------------------------------")

                if st.checkbox("Find a Lawyer"):
                   st.success("We will find you a LAWYER!")
                   image = Image.open('law.jpg')
                   st.image(image, width=700)
                   st.write("Select City and get to know about Pakistani Lawyers and Law Firms:")

                   options = ["-", "Lahore", "Karachi", "Islamabad", "Peshawar", "Rawalpindi"]
                   choice = st.selectbox("City", options)

                   if choice == "Lahore":
                       st.subheader("1. Bajwa Law Chamber")
                       st.write("Address: Bajwa Law Chamber, Court Street, 26 Lower Mall, St Nagar, Lahore, Punjab 54000")
                       st.info("Phone No: +923334882726")
                       st.write("Mian Owais Ilyas Advocate is one of the best family lawyers of the High Court of Pakistan Lahore. Expertise in custody of children, international divorce, court marriage, online marriage, khula, international khola, foreign marriage with Pakistani citizen. He handles all kinds of family matters in Pakistan.")
                       st.write("******************************************************************************************")

                       st.subheader("2. Nazia Law Associates")
                       st.write("Address: LG28, Saddiq Trade Center, Gulberg, Lahore 54000, Pakistan")
                       st.info("Phone No: +923334882726")
                       st.write("Lahore-based A.A. Nazia Law Associates has additional offices in other cities. Practices include family law – court marriage, divorce and dissolution, wife and child care, guardianship and succession certificates, custody of children, international abduction, and adoption.")
                       st.write("*******************************************************************************************")

                       st.subheader("3. Rana Ijaz & Partners")
                       st.write("Address: RA Tower, 7-A Turner Road, Lahore 54000, Pakistan")
                       st.info("Phone No: +923334882726")
                       st.write("Rana Law Chambers also famous as Rana Ijaz & Partners, provides consulting and litigation services in a wide range of fields, including foreign investment, company law, contracts, banking law, white collar crime, intellectual property and international trade and commerce law.")
                       st.write("********************************************************************************************")

                       st.subheader("4. Zafar Associates – LLP")
                       st.write("Address: 8-G Mushtaq Ahmed Gurmani Rd, Block G Gulberg 2, Lahore, Punjab 54600")
                       st.info("Phone No: +923334882726")
                       st.write("Zafar & Associates – LLP, founded in 1975, is one of the world’s largest specialized global companies providing extensive legal services to a wide range of domestic and international clients in the areas covered by Success Pages.")
                       st.write("********************************************************************************************")

                       st.subheader("5. Haseeb Baig Associates")
                       st.write("Address: PMA Trade Centre, 3rd Floor, Office 301, Ferozpur Road, Lahore 54500 Pakistan")
                       st.info("Phone No: +923334882726")
                       st.write("Haseeb Baig Associates has been established as a general practice law firm. The firm is highly valued for its ADR, corporate and commercial law practices and provides solution-oriented legal services to a large number of clients, including national and international public organizations.")
                       st.write("**********************************************************************************************")


                   elif choice == "Karachi":
                       st.subheader("1. A. Nawaz Osmani Law Associates")
                       st.write("Address: Suite # 17, 7th Floor, Office Towers, Rimpa Plaza,")
                       st.write("M A Jinnah Road,")
                       st.write("Karachi 75300- Pakistan")
                       st.info("Phone+92 321 2770225")
                       st.write("*********************************************************************************************")

                       st.subheader("2.Liaquat Merchant Associates (LMA) Barristers, Advocates & Corporate Legal Consultants")
                       st.write("Address: Building No. 4-C, 9th Zamzama Commercial Lane, Phase V, DHA")
                       st.write("Karachi 75500- Pakistan")
                       st.info("Phone+92 21 35835101")
                       st.write("*********************************************************************************************")

                       st.subheader("3.Zain Sheikh & Associates")
                       st.write("Address: 64/1, 23rd Street")
                       st.write("Khayaban-e-Badban, D.H.A. Phase 5: Karachi-Pakistan")
                       st.info("Phone+92 2-135-853-010 or +92 2-135-244-259")
                       st.write("*********************************************************************************************")

                       st.subheader("4. Ali & Associates")
                       st.write("Address: 23-A Block 6, P.E.C.H.S., Shahrah-e-Faisal")
                       st.write("First Floor, Shaheen Towers: Karachi 75400- Pakistan")
                       st.info("Phone+92 2-134-534-580")
                       st.write("*********************************************************************************************")

                       st.subheader("5. Ahmed Ali Dewan & Co")
                       st.write("Address: Abdullah Haroon Road")
                       st.write("Suite # 9, 1st Floor, Fareed Chamber: Karachi 74400- Pakistan")
                       st.info("Phone+92 021-35620898")
                       st.write("*********************************************************************************************")


                   elif choice == "Islamabad":
                       st.subheader("1. Alvi Law Associates")
                       st.write("Address: 21-Fatima Jinnah block,F-8, Markaz Islamabad")
                       st.write("Park Towers, F-10 Islamabad: Pakistan")
                       st.info("Phone+92 300 5334502")
                       st.write("***************************************************************************************")

                       st.subheader("2.AQLAAL Advocates")
                       st.write("Address:G-8 Markaz, 19, Second Floor Executive Complex")
                       st.write("Islamabad 44000: Pakistan")
                       st.info("Phone+92 51 8438140-2")
                       st.write("****************************************************************************************")

                       st.subheader("3. Legal Oracles")
                       st.write("Address:207, Millennium Heights, F-11, Markaz")
                       st.write("Islamabad 9251: Pakistan")
                       st.write("Phone+92-51-2224803")
                       st.write("****************************************************************************************")

                       st.subheader("4. Nishtar & Zafar Corporate Counsels")
                       st.write("Address:Ground Floor, State Life Building #7, Blue Area F-6/4")
                       st.write("Islamabad 44000:Pakistan")
                       st.info("Phone+92 332 820 4444")
                       st.write("****************************************************************************************")

                       st.subheader("5. Septentrio Global Consulting")
                       st.write("Address:32-A, Street 38, F-10/4, Nazim ud Din Road")
                       st.write("Islamabad 44000- Pakistan")
                       st.info("Phone+92 302 5077 777")
                       st.write("*******************************************************************************************")

                   elif choice == "Peshawar":
                       st.subheader("1. Kakakhel Law Associates")
                       st.write("Peshawar, Pakistan")
                       st.write("Full Service International Law Firm in Pakistan")
                       st.info("Phone +92 91 5250412")
                       st.write("-------------------------------------------------------------------------------------------")

                       st.subheader("2.Valid Consultants")
                       st.write("Peshawar, Pakistan")
                       st.write("Immigration, Visas and Work Permit Law Firm in Peshawar, Pakistan")
                       st.info("Phone +92 345 9009633")
                       st.write("------------------------------------------------------------------------------------------")

                   elif choice == "Rawalpindi":
                       st.subheader("1. Salman & Associates")
                       st.write("Rawalpindi, Pakistan")
                       st.write("Aviation, Defense, Engineering & Energy Lawyer in Pakistan")
                       st.info("Phone +92 51 5707211")
                       st.write("-----------------------------------------------------------------------------------------")

                       st.subheader("2.Corporate Debt Collections Services Pvt Ltd.")
                       st.write("Rawalpindi, Pakistan")
                       st.write("Debt Collection, Legal Consultants, Skip Tracing, Asset Tracing")
                       st.info("Phone +92 51 5157389")
                       st.write("-----------------------------------------------------------------------------------------")

                       st.subheader("3.Afzal & Afzal")
                       st.write("Rawalpindi, Pakistan")
                       st.write("Corporate Litigation Law Firm in Rawalpindi, Pakistan")
                       st.info("Phone +92 51 5566297")
                       st.write("------------------------------------------------------------------------------------------")

                       st.subheader("4.Naqvi Law Associates")
                       st.write("Rawalpindi, Pakistan")
                       st.write("Criminal, Civil, Family, Corporate Law Office In Islamabad and Rawalpindi")
                       st.info("Phone +923 (051) 5567517")
                       st.write("-----------------------------------------------------------------------------------------")

                       st.subheader("5. Aziz Law Associates")
                       st.write("Rawalpindi, Pakistan")
                       st.write("Legal Services to Businesses and Individuals in Rawalpindi, Pakistan")
                       st.info("Phone +92 30 28162835")
                       st.write("-----------------------------------------------------------------------------------------")


                

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
                
                if st.checkbox("Find a Lawyer"):
                   st.success("We will find you a LAWYER!")
                   image = Image.open('law.jpg')
                   st.image(image, width=700)
                   st.write("Select City and get to know about Pakistani Lawyers and Law Firms:")

                   options = ["-", "Lahore", "Karachi", "Islamabad", "Peshawar", "Rawalpindi"]
                   choice = st.selectbox("City", options)

                   if choice == "Lahore":
                       st.subheader("1. Bajwa Law Chamber")
                       st.write("Address: Bajwa Law Chamber, Court Street, 26 Lower Mall, St Nagar, Lahore, Punjab 54000")
                       st.info("Phone No: +923334882726")
                       st.write("Mian Owais Ilyas Advocate is one of the best family lawyers of the High Court of Pakistan Lahore. Expertise in custody of children, international divorce, court marriage, online marriage, khula, international khola, foreign marriage with Pakistani citizen. He handles all kinds of family matters in Pakistan.")
                       st.write("******************************************************************************************")

                       st.subheader("2. Nazia Law Associates")
                       st.write("Address: LG28, Saddiq Trade Center, Gulberg, Lahore 54000, Pakistan")
                       st.info("Phone No: +923334882726")
                       st.write("Lahore-based A.A. Nazia Law Associates has additional offices in other cities. Practices include family law – court marriage, divorce and dissolution, wife and child care, guardianship and succession certificates, custody of children, international abduction, and adoption.")
                       st.write("*******************************************************************************************")

                       st.subheader("3. Rana Ijaz & Partners")
                       st.write("Address: RA Tower, 7-A Turner Road, Lahore 54000, Pakistan")
                       st.info("Phone No: +923334882726")
                       st.write("Rana Law Chambers also famous as Rana Ijaz & Partners, provides consulting and litigation services in a wide range of fields, including foreign investment, company law, contracts, banking law, white collar crime, intellectual property and international trade and commerce law.")
                       st.write("********************************************************************************************")

                       st.subheader("4. Zafar Associates – LLP")
                       st.write("Address: 8-G Mushtaq Ahmed Gurmani Rd, Block G Gulberg 2, Lahore, Punjab 54600")
                       st.info("Phone No: +923334882726")
                       st.write("Zafar & Associates – LLP, founded in 1975, is one of the world’s largest specialized global companies providing extensive legal services to a wide range of domestic and international clients in the areas covered by Success Pages.")
                       st.write("********************************************************************************************")

                       st.subheader("5. Haseeb Baig Associates")
                       st.write("Address: PMA Trade Centre, 3rd Floor, Office 301, Ferozpur Road, Lahore 54500 Pakistan")
                       st.info("Phone No: +923334882726")
                       st.write("Haseeb Baig Associates has been established as a general practice law firm. The firm is highly valued for its ADR, corporate and commercial law practices and provides solution-oriented legal services to a large number of clients, including national and international public organizations.")
                       st.write("**********************************************************************************************")


                   elif choice == "Karachi":
                       st.subheader("1. A. Nawaz Osmani Law Associates")
                       st.write("Address: Suite # 17, 7th Floor, Office Towers, Rimpa Plaza,")
                       st.write("M A Jinnah Road,")
                       st.write("Karachi 75300- Pakistan")
                       st.info("Phone+92 321 2770225")
                       st.write("*********************************************************************************************")

                       st.subheader("2.Liaquat Merchant Associates (LMA) Barristers, Advocates & Corporate Legal Consultants")
                       st.write("Address: Building No. 4-C, 9th Zamzama Commercial Lane, Phase V, DHA")
                       st.write("Karachi 75500- Pakistan")
                       st.info("Phone+92 21 35835101")
                       st.write("*********************************************************************************************")

                       st.subheader("3.Zain Sheikh & Associates")
                       st.write("Address: 64/1, 23rd Street")
                       st.write("Khayaban-e-Badban, D.H.A. Phase 5: Karachi-Pakistan")
                       st.info("Phone+92 2-135-853-010 or +92 2-135-244-259")
                       st.write("*********************************************************************************************")

                       st.subheader("4. Ali & Associates")
                       st.write("Address: 23-A Block 6, P.E.C.H.S., Shahrah-e-Faisal")
                       st.write("First Floor, Shaheen Towers: Karachi 75400- Pakistan")
                       st.info("Phone+92 2-134-534-580")
                       st.write("*********************************************************************************************")

                       st.subheader("5. Ahmed Ali Dewan & Co")
                       st.write("Address: Abdullah Haroon Road")
                       st.write("Suite # 9, 1st Floor, Fareed Chamber: Karachi 74400- Pakistan")
                       st.info("Phone+92 021-35620898")
                       st.write("*********************************************************************************************")


                   elif choice == "Islamabad":
                       st.subheader("1. Alvi Law Associates")
                       st.write("Address: 21-Fatima Jinnah block,F-8, Markaz Islamabad")
                       st.write("Park Towers, F-10 Islamabad: Pakistan")
                       st.info("Phone+92 300 5334502")
                       st.write("***************************************************************************************")

                       st.subheader("2.AQLAAL Advocates")
                       st.write("Address:G-8 Markaz, 19, Second Floor Executive Complex")
                       st.write("Islamabad 44000: Pakistan")
                       st.info("Phone+92 51 8438140-2")
                       st.write("****************************************************************************************")

                       st.subheader("3. Legal Oracles")
                       st.write("Address:207, Millennium Heights, F-11, Markaz")
                       st.write("Islamabad 9251: Pakistan")
                       st.write("Phone+92-51-2224803")
                       st.write("****************************************************************************************")

                       st.subheader("4. Nishtar & Zafar Corporate Counsels")
                       st.write("Address:Ground Floor, State Life Building #7, Blue Area F-6/4")
                       st.write("Islamabad 44000:Pakistan")
                       st.info("Phone+92 332 820 4444")
                       st.write("****************************************************************************************")

                       st.subheader("5. Septentrio Global Consulting")
                       st.write("Address:32-A, Street 38, F-10/4, Nazim ud Din Road")
                       st.write("Islamabad 44000- Pakistan")
                       st.info("Phone+92 302 5077 777")
                       st.write("*******************************************************************************************")

                   elif choice == "Peshawar":
                       st.subheader("1. Kakakhel Law Associates")
                       st.write("Peshawar, Pakistan")
                       st.write("Full Service International Law Firm in Pakistan")
                       st.info("Phone +92 91 5250412")
                       st.write("-------------------------------------------------------------------------------------------")

                       st.subheader("2.Valid Consultants")
                       st.write("Peshawar, Pakistan")
                       st.write("Immigration, Visas and Work Permit Law Firm in Peshawar, Pakistan")
                       st.info("Phone +92 345 9009633")
                       st.write("------------------------------------------------------------------------------------------")

                   elif choice == "Rawalpindi":
                       st.subheader("1. Salman & Associates")
                       st.write("Rawalpindi, Pakistan")
                       st.write("Aviation, Defense, Engineering & Energy Lawyer in Pakistan")
                       st.info("Phone +92 51 5707211")
                       st.write("-----------------------------------------------------------------------------------------")

                       st.subheader("2.Corporate Debt Collections Services Pvt Ltd.")
                       st.write("Rawalpindi, Pakistan")
                       st.write("Debt Collection, Legal Consultants, Skip Tracing, Asset Tracing")
                       st.info("Phone +92 51 5157389")
                       st.write("-----------------------------------------------------------------------------------------")

                       st.subheader("3.Afzal & Afzal")
                       st.write("Rawalpindi, Pakistan")
                       st.write("Corporate Litigation Law Firm in Rawalpindi, Pakistan")
                       st.info("Phone +92 51 5566297")
                       st.write("------------------------------------------------------------------------------------------")

                       st.subheader("4.Naqvi Law Associates")
                       st.write("Rawalpindi, Pakistan")
                       st.write("Criminal, Civil, Family, Corporate Law Office In Islamabad and Rawalpindi")
                       st.info("Phone +923 (051) 5567517")
                       st.write("-----------------------------------------------------------------------------------------")

                       st.subheader("5. Aziz Law Associates")
                       st.write("Rawalpindi, Pakistan")
                       st.write("Legal Services to Businesses and Individuals in Rawalpindi, Pakistan")
                       st.info("Phone +92 30 28162835")
                       st.write("-----------------------------------------------------------------------------------------")


        else:
            st.error('The username or password you have entered is invalid.')
            st.success("Account created successfully!")
            st.info("Go to Login Menu to login")

    if __name__ == '__main__':
        main()
