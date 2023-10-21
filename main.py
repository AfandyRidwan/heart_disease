import numpy as np 
import pickle 
import random 
import streamlit as st
import sklearn

# load model 
model = pickle.load(open('MLPModel.pkl', 'rb'))

# Define function for predict from input field
def Prediction(data):
    # change the data to numpy array
    data = np.asarray(data)
    
    # reshape the array
    data_re = data.reshape(1,-1)
    
    # make prediction
    predicts = model.predict(data_re)
    
    # return value based on predict
    return 'The Person is Heart Disease' if predicts[0] == 1 else 'The Person is not Heart Disease'

def main():
    # Title 
    st.title('Heart Disease Prediction')
    
    with st.sidebar:
        
        # define variable for select
        genders = {1: 'Laki - Laki', 2: 'Perempuan'}
        chestP = {0: 'Angina', 1: 'Tidak Stabil', 2: 'Tidak Stabil yang Parah', 3: 'Tidak Terkait dengan masalah jantung'}
        res = {0: 'Normal', 1: 'Kelainan gelombang ST-T', 2: 'Hipertrofi Ventrikel Kiri'}
        ex = {0: 'Tidak', 1: 'Ya'}
        t = {1: 'Normal', 2: 'Defek tetap pada Thalassemia', 3: 'Defek yang dapat dipulihkan pada Thalassemia'}
        f = {0: '< 120 mg/dl', 1: '> 120 mg/dl'}
        
        
        # define function for format the select that only return number
        def g(option):
            return genders[option]

        def cP(option):
            return chestP[option]

        def re(option):
            return res[option]
        
        def exa(option):
            return ex[option]
        
        def th(option):
            return t[option]
        
        def fb(option):
            return f[option]
        
        
        # input field
        sex = st.selectbox("Pilih Jenis Kelamin", options=list(genders.keys()), format_func=g)
        age = st.slider("Usia", 29, 77)
        cp  = st.selectbox("Type Nyeri Dada", options=list(chestP.keys()), format_func=cP)
        exang = st.selectbox("Nyeri Dada disebabkan Olahraga", options=list(ex.keys()), format_func=exa)
        restecg = st.selectbox("Resting Electrocardiographic", options=list(res.keys()), format_func=re)
        fbs = st.selectbox("Fasting blood sugar", options=list(f.keys()), format_func=fb)
        thal = st.selectbox("Tes Thalium", options=list(t.keys()), format_func=th)
        ca = st.slider("Jumlah pembuluh darah Utama", 0,3)
        
        
        # declare variable for store the result
        diagnosis = ''
        
        if st.button('Generate Result'):
            diagnosis = Prediction([sex,cp,age, restecg, exang, fbs, thal, ca])
    
    # show the prediction
    st.success(diagnosis)
    

if __name__=='__main__':
    main()
