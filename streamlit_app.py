import streamlit as st

st.set_page_config(page_title="Demo App", layout="centered")
st.title("تجربة تطبيق Streamlit - واجهة عرض مشروع")
st.write("واجهة تجريبية تُظهر كيف سيبدو المشروع في معرض الأعمال.")
user_input = st.text_input("اكتب استفسارًا:", "")
if st.button("إرسال"):
    # محاكاة رد ذكي
    st.markdown("**رد النظام (تجريبي):** هذا رد مُولّد لغرض العرض فقط. استبدل هذا الجزء بموصل OpenAI/LLM الحقيقي.")
