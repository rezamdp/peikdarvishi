import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
from dbfile import *
import sqlite3



#------------------------------------------------page setting-----------------------------------------------------  

page_tittle = "سامانه ارزیابی عملکرد"
page_icon = "📊"

st.set_page_config(page_title=page_tittle , page_icon=page_icon , layout="wide")

#------------------------------------------------css file reader-----------------------------------------------------  

with open("./style.css") as f :
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html=True)
    st.markdown(f'<style>[data-testid=stSidebarUserContent]{f.read()}</style>' , unsafe_allow_html=True)
    
    
#------------------------------------------------sidebar-----------------------------------------------------  

with st.sidebar:
    menutitle="منوکاربری"
    page=[" خانه ","ثبت درخواست " , "گزارشات" ,"تنظیمات"]
    
    selected = option_menu(menutitle,page, 
        icons=['house', 'gear',"gear" ,"gear" ], menu_icon="cast", default_index=0 , styles={
            "nav-link": {"font-size": "14px", "text-align": "right", "margin":"0px","font-family":"estedad"},
            "nav-link-selected": {"font-size": "14px","font-family":"estedad"},
            "menu-title" : {"font-size": "16px","font-family":"estedad","text-align": "right"},
            "icon": {"text-align":"right"},
            "container":{"direction":"rtl"}
        })

#------------------------------------------------body-----------------------------------------------------    

#------------------------------------------------page 1-----------------------------------------------------  

if selected ==  " خانه " : 
    st.header("خانه")
    st.markdown("------")

#------------------------------------------------page 2-----------------------------------------------------      

elif selected == "ثبت درخواست " :
    col1 , col2 = st.columns(2)
    with col1 :
        date = str(st.date_input(" تاریخ ثبت درخواست"))
    with col2 :
            list_db_emp = show_emp()
            list_emp = []
            for i in list_db_emp:
                list_emp.append(i[0])
                
                
            emp_select = st.selectbox("نام درخواست دهنده" , options=list_emp)
            
    col3 , col4 , col5 ,col6= st.columns(4)
    with col3 :
            name_cust = str(st.text_input("نام مشتری"))
    with col4 :
        city = str(st.text_input ("مقصد"))
    with col5 :
        pay = str(st.radio("هزینه پیک" ,["مشتری" , "ماه رویان"],key="pay"))
    with col6 :
        peik = str(st.text_input("مبلغ پیک"))
    name_deli = str(st.text_input("نام راکب"))
    bigak_num = st.text_input("شماره بیجک")
    
    col7 , col8 = st.columns([1,7])
    with col7 :
        peik = str(st.radio("برگشت پیک" ,["ندارد" , "دارد"],key="peik"))
        if peik == "دارد" :
            with col8 :
                back_list = ["برگ عدم فاکتور" , "مهر و چک" , "رسید تحویل کالا" , "خرید کالا" , "جواب نامه" , "گارانتی"]
                elat = str(st.selectbox("علت برگشت را  بیان کنید" , options=back_list))      
                          
    if st.button("clicked") :
        if peik == "دارد" :     
            d = {'تاریخ': date, 'نام درخواست دهنده':emp_select,"نام مشتری":name_cust,"مقصد":city , "هزینه پیک":pay,
                        "برگشت پیک" : peik , "علت برگشت را  بیان کنید" :elat}
            df = pd.DataFrame(data=d , index=[0])
            reg(b=date,c=emp_select ,d=name_cust, e=city , f=pay ,g=peik ,h=elat , i=peik , j=name_deli, k=bigak_num)
        else :    
            d = {'تاریخ': date, 'نام درخواست دهنده':emp_select,"نام مشتری":name_cust,"مقصد":city , "هزینه پیک":pay,
                        "برگشت پیک" : peik}
            df = pd.DataFrame(data=d , index=[0])
            reg(b=date,c=emp_select ,d=name_cust, e=city , f=pay ,g=peik ,h=" " , i=peik , j=name_deli, k=bigak_num)
        
        st.write(df)                      





#------------------------------------------------page 3-----------------------------------------------------                      

elif selected ==  "گزارشات" : 
    menutitle_setting_page=""
    pages_of_setting =[" گزارش کلی"," گزارش بر اساس کارمند"]
    selected_setting_menu = option_menu(menutitle_setting_page,pages_of_setting, 
        icons=['house', 'gear'], menu_icon="cast", default_index=0 , styles={
            "nav-link": {"font-size": "14px", "text-align": "right", "margin":"0px","font-family":"estedad"},
            "nav-link-selected": {"font-size": "14px","font-family":"estedad"},
            "menu-title" : {"font-size": "16px","font-family":"estedad","text-align": "right"},
            "icon": {"text-align":"right"},
            "container":{"direction":"rtl"}
        },orientation="horizontal")
    
    if selected_setting_menu == " گزارش کلی":
        if st.button("کلیک کنید") :
            
            df1 = pd.DataFrame(show())
            
            st.write(df1)
            










##------------------------------------------------page 4-----------------------------------------------------     
    
elif selected == "تنظیمات" :
    menutitle_setting_page=""
    pages_of_setting =[" تنظیمات کارمندان ","تنظیمات راکب "]
    selected_setting_menu = option_menu(menutitle_setting_page,pages_of_setting, 
        icons=['house', 'gear'], menu_icon="cast", default_index=0 , styles={
            "nav-link": {"font-size": "14px", "text-align": "right", "margin":"0px","font-family":"estedad"},
            "nav-link-selected": {"font-size": "14px","font-family":"estedad"},
            "menu-title" : {"font-size": "16px","font-family":"estedad","text-align": "right"},
            "icon": {"text-align":"right"},
            "container":{"direction":"rtl"}
        },orientation="horizontal")
    
    if selected_setting_menu == " تنظیمات کارمندان ":
        def add():
            with st.form(key="add_emp") :
                col9 , col10 , col11= st.columns(3)
                with col9 :
                    CodeM = st.text_input("کد ملی کارشناس")
                
                with col10 :
                    Name = st.text_input("نام کارشناس")
                    
                with col11 :
                    Lname = st.text_input("فامیلی کارشناس")
                Phone = st.text_input("تلفن کارشناس")
                col16 , col17 = st.columns(2)
                with col16 : 
                    User = st.text_input("یوزر کارشناس")
                with col17 :
                    passw =st.text_input("رمز کارشناس", type="password")
                
        
                submit = st.form_submit_button('ذخیره')
            
            if submit :
                st.success(" با موفقیت ذخیره شد")

            
                if CodeM != "" and Name != "" and Lname != "" and Phone != "" and User != "" and passw != "":
                    add_emp(CodeM , Name , Lname , Phone , User , passw)
            
        add()
        
        
        col18 , col19 = st.columns(2)
        def search_emps () :
            with st.form(key="remove_emp") :
                global CodeM_Searching
                CodeM_Searching = st.text_input("کد ملی را وارد کنید")
                
                submit = st.form_submit_button (label="جستجو")  
                submit2 = st.form_submit_button(label="حذف کردن")
                        
                if submit :
                    st.warning("نام کاربری جستجو شده شما")
                    a = Search_emp(CodeM_Searching)
                    if CodeM_Searching in a :        
                            #df = pd.DataFrame(a,)
                        st.warning(f"نام کارمند {a[0][1]}" , f"نام خانوادگی کارمند {a[0][2]}")
                    else :
                        st.warning("این کارمند وجود ندارد")
                if submit2 :
                        remove_emp_db(CodeM_Searching)
        search_emps()


