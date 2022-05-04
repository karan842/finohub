import streamlit as st
import pickle

#Customize page icon and title
st.set_page_config(page_title='FinoHub® | Loan Eligibility Calculator', page_icon='media/FinoHub.png')

# loading the model
model = pickle.load(open('ML model/log_reg.pkl', 'rb'))

def run():
    st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
    st.title("FINOHUB®")
    st.markdown("#### Welcome to FinoHub®, it is a loan eligibility prediction system which is driven by AI. Just submit your personal details below and check your loan eligibility in one click.")
    st.warning("WARNING! Do not share your Debit/Credit card number, CVV and OTP to any fraud message or call. We are not requesting this types of information.")
    # Video intro
    vide_file = open('media/finohub.mp4','rb')
    video_bytes = vide_file.read()
    st.video(video_bytes)
    

    ## Account No
    account_no = st.text_input('Account Number')

    ## Full Name
    fn = st.text_input('Full Name')

    # hide footer and menu bar in streamlit
    st.markdown(""" <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)

    ## For gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## For Marital Status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    ## No of dependets
    dep_display = ('No','One','Two','More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])

    ## For edu
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    ## For emp status
    emp_display = ('Job','Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

    ## For Property status
    prop_display = ('Rural','Semi-Urban','Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area",prop_options, format_func=lambda x: prop_display[x])

    ## For Credit Score
    cred_display = ('Between 300 to 500','Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score",cred_options, format_func=lambda x: cred_display[x])

    ## Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income(in $)",value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income(in $)",value=0)

    ## Loan AMount
    loan_amt = st.number_input("Loan Amount(in thousands($))",value=0)

    ## loan duration
    dur_display = ['2 Months','6 Months','8 Months','1 Year','16 Months']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.warning(
                "Hello, " + fn +" ||  "
                "Account number: "+account_no 
            )
            st.error('Sorry, YOU WILL NOT GET LOAN FROM THE BANK :(')
            
        else:
            st.warning(
                "Hello: " + fn +" || "
                "Account number: "+account_no 
            )
            st.success('Congratulations!! YOUR ARE ELIGIBLE FOR A LOAN FROM THE BANK🎉.')
            

run()

