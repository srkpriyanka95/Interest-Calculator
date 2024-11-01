import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import numpy as np

# Title of the app
# st.title("Interest Calculator")
st.markdown(
    """
    <style>
    .title-box {
        border: 2px solid #4CAF50;  
        border-radius: 10px;       
        border: 1px solid #ccc;
        box-shadow: inset 4px 4px 10px rgb(150, 189, 242, 0.8);
        padding: 10px;             
        font-size: 24px;           
        color: #D67D00;
        text-align: center;         
        margin-left:50px;
        margin-right:50px;
        max-width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add the title inside the styled box
st.markdown('<div class="title-box"style="font-size:20px; "><b>Interest Calculator</b></div>', unsafe_allow_html=True)

st.write("")
st.write("")
# Input fields
principal = st.text_input("**கடன் தொகை**")
time = st.date_input("**கடன் வாங்கியா தேதி**")

# date_1 = datetime.strptime(time,"%Y/%m/%d").date()
date_1 = time
date_2 = datetime.today().date()

date_diff = relativedelta(date_2, date_1)
if principal:
    principal = int(principal)
# print(date_diff.years,month_diff,date_diff.days)
    net_interest = principal*0.02
    initial_principal = principal
    interest = principal*0.02
    year_diff = date_diff.years
    month_diff = date_diff.months
    if year_diff > 0:
        diff_display = f"{year_diff}&nbsp;&nbsp;ஆண்டு&nbsp;&nbsp;&nbsp;{month_diff}&nbsp;&nbsp;மாதம்&nbsp;&nbsp;&nbsp;&nbsp;{date_diff.days}&nbsp;&nbsp;நாள்"
    else:
        diff_display = f"{month_diff}&nbsp;&nbsp;மாதம்&nbsp;&nbsp;&nbsp;&nbsp;{date_diff.days}&nbsp;&nbsp;நாள்"
    
    if date_diff.days > 0:
            month_diff +=1 

    if year_diff > 1 or (year_diff == 1 and month_diff > 0):
        for i in range(1,year_diff+1):
            final_amount = principal + (interest*12)
            principal += interest*12
            interest = principal*0.02        
        final_amount +=  (interest*month_diff) 
        

    elif year_diff == 0 :
        final_amount = principal + (interest * month_diff)

    total_months = ((year_diff*12)+month_diff)
    net_interest_final = total_months*net_interest
    final_amount_with_net_Interst = round(np.ceil(net_interest_final+initial_principal))
    if total_months > 12:
        final_amount_with_compound_Interst = (round(np.ceil(final_amount)))
        total_net_interest = round(final_amount_with_net_Interst - initial_principal)
        total_compount_interst = round(final_amount_with_compound_Interst - initial_principal)
        # total_net_interest = round(final_amount_with_net_Interst/total_months)
        # total_compount_interst = round(final_amount_with_compound_Interst/total_months)
    # Calculate compound interest if all inputs are filled
st.write("")
st.write("")
col1, col2, col3 = st.columns([1, 1, 1])
button_clicked= 'no'
with col2 :
    if st.button("Calculate",use_container_width=True):
        button_clicked = 'Yes'
if button_clicked == 'Yes':
    
    if not principal:
        st.error("கடன் தொகையில் எண்ணை உள்ளிடவும்",icon="🚨")
    else:
        st.write('')
        st.markdown(
    f'''<p style='border: 2px solid black;
                border-radius: 20px; 
                padding:10px;
                margin-left:10px; margin-right:10px; 
                box-shadow: inset 2px 2px 6px rgba(71, 181, 218, 0.8);
                text-align: center; font-size:10px; color:blue;'><b>{diff_display}</b></p>''',
    unsafe_allow_html=True
    )
        if total_months > 12:
            
            st.write("")
            st.markdown(f'''
    <div style="display: flex; margin: 20px;">
        <div style="width: 200px; padding: 20px; background-color: #8FCCC4; border: 1px solid #ccc; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); margin-right: 20px; text-align: center; border-radius: 15px; display: flex; align-items: center; justify-content: center;">
            <p style="margin: 0; font-size: 15px;"><b>கூட்டு வட்டி</b></p>
        </div>
        <div style="flex-grow: 1; padding: 10px; background-color: #ffffff; border: 1px solid #ccc; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); border-radius: 15px; box-shadow: inset 2px 2px 6px rgba(71, 181, 218, 0.8);">
            <p style='text-align: left; font-size: 10px; color: black; margin: 0;'>
                <b>&nbsp;கூட்டு வட்டி&nbsp;&nbsp;:&nbsp;&nbsp;</b> <span style="color: red; font-size: 10px;"><b>{total_compount_interst}</b></span>
                <br>
                <b>&nbsp;மொத்தம்&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;</b> <span style="color: green; font-size: 10px;"><b>{final_amount_with_compound_Interst}</b></span>
            </p>
        </div>
    </div>
    <div style="display: flex; margin: 20px;">
        <div style="width: 200px; padding: 20px; background-color: #F2C096; border: 1px solid #ccc; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); margin-right: 20px; text-align: center; border-radius: 15px; display: flex; align-items: center; justify-content: center;">
            <p style="margin: 0; font-size: 15px;"><b>Net வட்டி</b></p>
        </div>
        <div style="flex-grow: 1; padding: 10px; background-color: #ffffff; border: 1px solid #ccc; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); border-radius: 15px; box-shadow: inset 2px 2px 6px rgba(204, 155, 114, 0.8);">
            <p style='text-align: left; font-size: 10px; color: black; margin: 0;'>
                <b>&nbsp;Net வட்டி&nbsp;&nbsp;:&nbsp;&nbsp;</b> <span style="color: red; font-size: 10px;"><b>{total_net_interest}</b></span>
                <br>
                <b>&nbsp;மொத்தம்&nbsp;&nbsp;:&nbsp;&nbsp;</b> <span style="color: green; font-size: 10px;"><b>{final_amount_with_net_Interst}</b></span>
            </p>
        </div>
    </div>
''', unsafe_allow_html=True)
            # st.write(f'கூட்டு வட்டி = {total_compount_interst}')
            # st.write(f'மொத்தம் = {final_amount_with_compound_Interst}')
            # st.write(f'Net வட்டி = {total_net_interest}')
            # st.write(f'மொத்தம்       =  {final_amount_with_net_Interst}')
        else:
            st.markdown(f'''
                <div style="display: flex; align-items: center;">
                    <div style="width: 100px; padding: 10px; background-color: #8FCCC4; border: 1px solid #ccc; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); margin-right: 20px; text-align: center; border-radius: 15px;">
                        <p style="font-size: 15px; margin: 0;"><b>Net வட்டி</b></p>
                    </div>
                    <div style="flex-grow: 1; padding: 10px; background-color: #ffffff; border: 1px solid #ccc; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); border-radius: 15px; box-shadow: inset 2px 2px 6px rgba(71, 181, 218, 0.8);">
                        <p style='text-align: left; font-size: 10px; color: black; margin: 0;'>
                            <b>&nbsp;Net வட்டி&nbsp;&nbsp;:&nbsp;&nbsp;</b> <span style="color: red; font-size: 10px;"><b>{round(net_interest_final)}</b></span>
                            <br>
                            <b>&nbsp;மொத்தம்&nbsp;&nbsp;:&nbsp;&nbsp;</b> <span style="color: green; font-size: 10px;"><b>{final_amount_with_net_Interst}</b></span>
                        </p>
                    </div>
                </div>
            ''', unsafe_allow_html=True)
            # st.write(f'Net வட்டி = {round(net_interest_final)}')
            # st.write(f'மொத்தம்       =  {final_amount_with_net_Interst}')
        
