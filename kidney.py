import pickle
import streamlit as st
import pyautogui
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(bp,sg,al,bgr,bu,sc,hemo,rc,htn,dm,appet,ane):  
    # Pre-processing user input    
    if htn == "No":
        htn = 0
    else:
        htn = 1
 
    if dm == "No":
        dm = 0
    else:
        dm = 1
 
    if appet == "Good":
        appet = 0
    else:
        appet = 1  
    
    if ane == "No":
        ane = 0
    else:
        ane = 1 
 
    # Making predictions 
    prediction = classifier.predict( [[bp,sg,al,bgr,bu,sc,hemo,rc,htn,dm,appet,ane]])
    if prediction == 0:
        pred = 'You donot have CKD disease'
    else:
        pred = 'You have CKD disease, Consult Doctor Immediately'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Chronic Kidney Disease Prediction Using Machine Learning App</h1> 
    </div>     """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    bp = st.number_input("Blood Pressure")
    sg = st.number_input("Specific Gravity", format="%.3f") 
    al = st.number_input("Albumin")
    bgr = st.number_input("Blood Glucose Random")
    bu = st.number_input("Blood Urea")
    sc = st.number_input("Serum Creatinine")
    hemo = st.number_input("Hemoglobin")
    rc = st.number_input("Red Blood Cell Count")
    htn = st.selectbox('Hypertension',("Yes","No"))
    dm = st.selectbox('Diabetes Mellitus',("Yes","No")) 
    appet = st.selectbox('Appetite',("Good","Poor"))
    ane = st.selectbox('Anemia',("Yes","No"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(bp,sg,al,bgr,bu,sc,hemo,rc,htn,dm,appet,ane) 
        st.success('Result: {}'.format(result))
        
    if st.button("Reset"):
        pyautogui.hotkey("ctrl","F5")     
     
if __name__=='__main__': 
    main()