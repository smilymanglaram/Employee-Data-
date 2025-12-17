import streamlit as st
import sqlite3
import pandas as pd

conn=sqlite3.connect("emp.db",check_same_thread=False)

cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS employee
(id integer,name text,sal integer)""")
conn.commit()

menu=["INSERT","VIEW"]
choice=st.sidebar.selectbox("MENU",menu)
if choice=="INSERT":
    id=st.number_input("ID")
    name=st.text_input("NAME")
    sal=st.number_input("SALARY")
    if st.button("SAVE"):
        cursor.execute("""INSERT INTO employee(id,name,sal)
        VALUES(?,?,?)""",(id,name,sal))
        conn.commit()
        st.success("EMPLOYEE ADDED SUCCESSFULLY")

elif choice == "VIEW":
    st.subheader("View Employee Details")
    df = pd.read_sql("SELECT * FROM employee",conn)
    st.dataframe(df)
        
