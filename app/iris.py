import streamlit as st
import joblib 

st.title("IRIS 品種預測")
knn = joblib.load("knn_model.joblib")
svm = joblib.load("svm_model.joblib")
rf = joblib.load("rf_model.joblib")

# 左側選單
clf = st.sidebar.selectbox("### 請選擇分類氣: ",("SVM","KNN","RandomForset"))
if clf=="SVM":
    model = svm
elif clf=="KNN":
    model = knn
else:
    model = rf

# 產生預測用的資料
s1 = st.slider("花萼的長: ",3.0,8.0,5.8)
s2 = st.slider("花萼的寬: ",2.0,5.0,3.8)
s3 = st.slider("花辦的長: ",1.0,7.0,4.8)
s4 = st.slider("花辦的寬: ",0.1,2.6,1.8)
