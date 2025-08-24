
# Client Churning Predictor

This project was made as an exercise on deployment of Data science applications.
You can download the data for the project at <https://www.kaggle.com/datasets/surajbhandari527/ecommerce-churn-data-for-churn-prediction-models?resource=download>.

You also can find the working application showing how the model works at <https://client-churning-predictor.onrender.com/>.

Or alternatively you can use our second application made using streamlit at <https://client-churning-predictor-trkxdunqjtmcsktfjtagby.streamlit.app/>

## Initial Setup in Codespaces (Recommended)

No manual setup is required, as **Codespaces is automatically configured** with the predefined files created by the academy for you. Just follow these steps:

1. **Wait for the environment to configure automatically**.
   - All necessary packages and the database will install themselves.
   - The automatically created `username` and `db_name` are in the **`.env`** file at the root of the project.
2. **Once Codespaces is ready, you can start working immediately**.

## Local Setup

### **Prerequisites**

Make sure you have Python 3.11+ installed on your machine. You will also need pip to install the Python packages.

### **Installation**

Clone the project repository to your local machine.

Navigate to the project directory and install the required Python packages:

```bash
pip install -r requirements-dev.txt
```

### **Environment Variables**

Create a .env file in the root directory of the project to store your environment variables, such as your database connection string:

```makefile
FLASK_ENV="postgresql://<USER>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>"

#example
DATABASE_URL="postgresql://my_user:my_password@localhost:5432/my_database"
```

## Running the Application

To run the application, execute th app.py script from wherever you want:

```bash
python src/app.py
```

## Working with Data

You can place your raw datasets in the data/raw directory, intermediate datasets in data/interim, and processed datasets ready for analysis in data/processed.

To process data, you can modify the app.py script to include your data processing steps, using pandas for data manipulation and analysis.

You shouldn't worry too much about manipulating data though since this project implements a pipeline for data pre-processing.

## Contributors

This project structure was inspired by a template that was built as part of the [Data Science and Machine Learning Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning) by 4Geeks Academy by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Learn more about [4Geeks Academy BootCamp programs](https://4geeksacademy.com/us/programs) here.

Other templates and resources like this can be found on the school's GitHub page.
