import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn

# Load the model
with open('etcl_model.pkl', 'rb') as file:
    etcl_model = pickle.load(file)

# Function to preprocess input data
def preprocess_input(inp):
    inp_arr = np.asarray(inp)
    inp_arr_reshaped = inp_arr.reshape(1, -1)
    return inp_arr_reshaped


# Function to make prediction
def predict_diabetes(features):
    # Make prediction
    inp_arr_reshaped = preprocess_input(features)
    prediction = etcl_model.predict(inp_arr_reshaped)
    return prediction

# Function to provide recommendations
def get_recommendations(features):
    recommendations = []

    if features['HighBP'] == 1:
        recommendations.append("Control blood pressure through medication, diet, and exercise.")
    else:
        recommendations.append("Maintain a healthy lifestyle to prevent high blood pressure.")

    if features['HighChol'] == 1:
        recommendations.append("Lower cholesterol levels through a healthy diet and medication if necessary.")
    else:
        recommendations.append("Consume a diet low in saturated fats and cholesterol to prevent high cholesterol.")

    if features['BMI'] >= 30:
        recommendations.append("Achieve a healthy weight through diet and exercise to reduce diabetes risk.")
    else:
        recommendations.append("Maintain a healthy weight to reduce the risk of developing diabetes.")

    if features['Smoker'] == 1:
        recommendations.append("Quit smoking to lower the risk of developing diabetes and other health issues.")
    else:
        recommendations.append("Avoid smoking to reduce the risk of diabetes and improve overall health.")

    if features['Stroke'] == 1:
        recommendations.append("Follow doctor's recommendations for stroke management and prevention.")
    else:
        recommendations.append("Maintain a healthy lifestyle to reduce the risk of stroke.")

    if features['HeartDiseaseorAttack'] == 1:
        recommendations.append("Manage heart disease or heart attack risk factors with medical treatment and lifestyle changes.")
    else:
        recommendations.append("Take preventive measures to reduce the risk of heart disease or heart attack.")

    if features['PhysActivity'] == 1:
        recommendations.append("Stay physically active to maintain overall health and reduce diabetes risk.")
    else:
        recommendations.append("Incorporate regular physical activity into your routine to prevent diabetes.")

    if features['Fruits'] == 0 or features['Veggies'] == 0:
        recommendations.append("Increase consumption of fruits and vegetables to improve overall health and reduce diabetes risk.")
    else:
        recommendations.append("Continue consuming fruits and vegetables as part of a healthy diet.")

    if features['NoDocbcCost'] == 1:
        recommendations.append("Seek affordable healthcare options to address medical needs and prevent complications.")
    else:
        recommendations.append("Ensure access to regular healthcare to monitor and manage health conditions.")

    if features['DiffWalk'] == 1:
        recommendations.append("Consult with a healthcare professional to address mobility issues and maintain physical activity.")
    else:
        recommendations.append("Stay physically active and seek medical advice for any mobility concerns.")

    return recommendations

# Streamlit interface
def main():
    st.title('Diabetes Classification System')

    # Input fields
    st.subheader('Enter Patient Information:')
    features = {}
    features['HighBP'] = st.selectbox('High Blood Pressure:', ['No', 'Yes'])
    features['HighChol'] = st.selectbox('High Cholesterol:', ['No', 'Yes'])
    features['BMI'] = st.number_input('Body Mass Index:')
    features['Smoker'] = st.selectbox('Ever smoked at least 100 cigarettes:', ['No', 'Yes'])
    features['Stroke'] = st.selectbox('Ever had a stroke:', ['No', 'Yes'])
    features['HeartDiseaseorAttack'] = st.selectbox('Ever had coronary heart disease or myocardial infarction:', ['No', 'Yes'])
    features['PhysActivity'] = st.selectbox('Engaged in physical activity past 30 days (not including job):', ['No', 'Yes'])
    features['Fruits'] = st.selectbox('Consumed fruits 1 or more times per day:', ['No', 'Yes'])
    features['Veggies'] = st.selectbox('Consumed vegetables 1 or more times per day:', ['No', 'Yes'])
    features['NoDocbcCost'] = st.selectbox('Needed to see a doctor but could not because of cost in past 12 months:', ['No', 'Yes'])
    features['GenHlth'] = st.slider('General health (scale 1-5):', 1, 5, 3)
    features['MentHlth'] = st.slider('Days of poor mental health in past 30 days (scale 1-30):', 1, 30, 15)
    features['PhysHlth'] = st.slider('Physical illness or injury days in past 30 days (scale 1-30):', 1, 30, 15)
    features['DiffWalk'] = st.selectbox('Serious difficulty walking or climbing stairs:', ['No', 'Yes'])
    features['Sex'] = st.selectbox('Sex:', ['Female', 'Male'])
    features['Age'] = st.slider('Age (13-level category):', 1, 13, 6)
    features['Education'] = st.slider('Education level (scale 1-6):', 1, 6, 3)
    features['Income'] = st.slider('Income scale (scale 1-8):', 1, 8, 4)

    # Convert categorical variables to numerical
    features['HighBP'] = 1 if features['HighBP'] == 'Yes' else 0
    features['HighChol'] = 1 if features['HighChol'] == 'Yes' else 0
    features['Smoker'] = 1 if features['Smoker'] == 'Yes' else 0
    features['Stroke'] = 1 if features['Stroke'] == 'Yes' else 0
    features['HeartDiseaseorAttack'] = 1 if features['HeartDiseaseorAttack'] == 'Yes' else 0
    features['PhysActivity'] = 1 if features['PhysActivity'] == 'Yes' else 0
    features['Fruits'] = 1 if features['Fruits'] == 'Yes' else 0
    features['Veggies'] = 1 if features['Veggies'] == 'Yes' else 0
    features['NoDocbcCost'] = 1 if features['NoDocbcCost'] == 'Yes' else 0
    features['DiffWalk'] = 1 if features['DiffWalk'] == 'Yes' else 0
    features['Sex'] = 1 if features['Sex'] == 'Male' else 0

    # Predict
    if st.button('Predict'):
        prediction = predict_diabetes(list(features.values()))
        recommendations = get_recommendations(features)
        show_prediction(prediction, recommendations)


def show_prediction(prediction, recommendations):
    if prediction == 1:
        st.markdown("<h2 style='text-align: center; font-weight: bold;'>Patient Suffering From Diabetes</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align: center; font-weight: bold;'>No Diabetes</h2>", unsafe_allow_html=True)

    if recommendations:
        st.subheader("Recommendations:")
        for recommendation in recommendations:
            st.info(recommendation)

    st.button('back', main)

if __name__ == '__main__':
    main()
