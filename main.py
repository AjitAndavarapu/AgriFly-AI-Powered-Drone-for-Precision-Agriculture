import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Orchard Management"])

#Main Page
if(app_mode=="Home"):
    # st.header("SIH-2024")
    #image_path = "home_page.jpeg"
    #st.image(image_path,use_column_width=True)
    st.markdown("""
    # Apple Orchard Management System

Welcome to the Apple Orchard Management System! 🍏🚀

Our mission is to revolutionize orchard management through advanced technology. With our integrated system of drones and a robotic cart, we aim to enhance the health and productivity of your apple orchards.

## How It Works
1. **Data Collection**: Our drones capture real-time images of your apple trees, monitoring health, moisture levels, and temperature variations.
2. **Disease Detection**: Using machine learning algorithms, the system analyzes the images to identify potential diseases like apple black rot and scab.
3. **Robotic Cart Monitoring**: The robotic cart collects vital ground-level data, sprays pesticides precisely where needed, and tracks a designed path to gather soil information.
4. **Real-Time Insights**: Farmers receive updates via a mobile app, including soil vitals, disease predictions, and control recommendations.

## Why Choose Us?
- **Accuracy**: Our cutting-edge technology ensures precise detection and analysis.
- **User-Friendly**: A simple interface for an intuitive experience.
- **Efficiency**: Fast results enable quick decision-making to protect your crops.

## Get Started
Click on the "Dashboard" in the sidebar to explore the features and enhance your orchard management with our system!

## About Us
Learn more about our project, our team, and our goals on the "About" page. Together, let’s cultivate healthier and more productive apple orchards!
    """)

#About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purpose.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)

                """)

#Prediction Page
elif(app_mode=="Orchard Management"):
    st.header("Upload an Image for Disease Prediction")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=2,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        #st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))





# import streamlit as st
# import pandas as pd
# import numpy as np
# import tensorflow as tf

# data = {
#     'Tree_ID': [f'Tree_{i}' for i in range(1, 21)],
#     'Health_Status': np.random.choice(['Healthy', 'Diseased'], 20, p=[0.8, 0.2]),
#     'Moisture_Level': np.random.uniform(20, 100, 20).round(2),
#     'Temperature': np.random.uniform(15, 30, 20).round(2),
#     'Nutrient_Level': np.random.uniform(0, 100, 20).round(2),
# }

# #Tensorflow Model Prediction
# def model_prediction(test_image):
#     model = tf.keras.models.load_model("trained_plant_disease_model.keras")
#     image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
#     input_arr = tf.keras.preprocessing.image.img_to_array(image)
#     input_arr = np.array([input_arr]) #convert single image to batch
#     predictions = model.predict(input_arr)
#     return np.argmax(predictions) #return index of max element

# orchard_df = pd.DataFrame(data)

# # Streamlit app
# st.title("Apple Orchard Management Dashboard")

# # Overview Section
# st.header("Overview")
# st.write("This dashboard provides insights into the health of your apple orchard.")

# # Displaying Health Status
# st.subheader("Health Status of Trees")
# health_counts = orchard_df['Health_Status'].value_counts()
# st.bar_chart(health_counts)

# # Displaying Real-Time Data
# st.subheader("Real-Time Data")
# st.write("Moisture Levels, Temperature, and Nutrient Levels:")
# st.dataframe(orchard_df)

# # Disease Alerts
# st.subheader("Disease Alerts")
# diseased_trees = orchard_df[orchard_df['Health_Status'] == 'Diseased']
# if not diseased_trees.empty:
#     st.warning(f"Diseased Trees Detected: {len(diseased_trees)}")
#     st.dataframe(diseased_trees[['Tree_ID', 'Health_Status']])

# # Yield Predictions (Dummy)
# st.subheader("Yield Predictions")
# predicted_yield = np.random.uniform(100, 300)
# st.write(f"Predicted Yield: {predicted_yield:.2f} tons")

# # Upload Image Section
# st.subheader("Upload Image for Disease Recognition")
# uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# if uploaded_file is not None:
#     st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
#     st.write("Processing the image...")
#     if(st.button("Predict")):
#         #st.snow()
#         st.write("Our Prediction")
#         result_index = model_prediction(uploaded_file)
#         #Reading Labels
#         class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy']
#         st.success("Model is Predicting it's a {}".format(class_name[result_index]))


# #YT link - https://youtu.be/RrupuszF1Mk?si=7aaw_hmdskoxFScf