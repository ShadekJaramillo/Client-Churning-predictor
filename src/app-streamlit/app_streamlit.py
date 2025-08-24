import streamlit as st
from pickle import load
from pathlib import Path
from pandas import DataFrame

@st.cache_resource
def load_model():
    model_path = Path(__file__).parent.parent.parent/'models'/'AdaBoost_learning_rate_1.5_n_estimators_300_random_state_42.sav'
    with open(str(model_path),'rb') as f:
        return load(f)

model = load_model()

def prediction_from_dict(value_dict:dict):
    data = DataFrame([value_dict])
    prediction = model.predict(data)
    if prediction==1:
        return 'The client is likely to churn'
    else:
        return 'The client is likely not churning'

st.title('Client Churning Prediction')
st.markdown(
    """
This is a tool to identify customers who are at risk of "churning" — ceasing their relationship with an e-commerce company.
    """
)
st.sidebar.title('Introduce the values')

values = {
    'Age': st.sidebar.number_input('Age', step=1),
    'Gender': st.sidebar.selectbox('Gender',['Male','Female','Other']),
    'Tenure': st.sidebar.number_input('Months Using The App',step=1),
    'PreferredLoginDevice': st.sidebar.selectbox('Preferred Login Device',['Mobile', 'Desktop']),
    'CityTier': st.sidebar.selectbox('City Tier',[1,2,3]),
    'WarehouseToHome': st.sidebar.number_input('Warehouse To Home Distance (km)'),
    'HoursSpentOnApp': st.sidebar.number_input('Hours Spent On App', step=1),
    'NumberOfDevicesRegistered': st.sidebar.number_input('Number Of Devices Registered'),
    'SatisfactionScore': st.sidebar.selectbox('Satisfaction Score', range(1,6)),
    'NumberOfAddress': st.sidebar.number_input('Number Of Addresses', step=1),
    'Complain': st.sidebar.selectbox('Has Complained?',['yes','no']) == 'yes',
    'OrderCount': st.sidebar.number_input('Order Count',step=1),
    'DaySinceLastOrder': st.sidebar.number_input('Days Since Last Order',step=1),
    'CashbackAmount': st.sidebar.number_input('Cashback Amount (USD)', step=0.01)
}

if st.sidebar.button('Make prediction'):
    st.markdown(f'## **{prediction_from_dict(values)}**')


if __name__ == '__main__':
    pass
