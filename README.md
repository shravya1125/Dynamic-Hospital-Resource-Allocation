# 🏥 Dynamic Resource Allocation Framework for Hospital Management Using Risk-Aware Scheduling


## 🚀 Project Overview

This project simulates a real-time hospital triage system using core Operating System concepts like dynamic scheduling, interrupt handling, and safe resource allocation—combined with machine learning for patient risk prediction.

In emergency situations like pandemics, where resources such as ICU beds, ventilators, and doctors are limited, manual allocation can be slow and unsafe. Our system predicts the risk level of each patient using a trained ML model and dynamically allocates resources using an interrupt-aware rule-based allocator.


## 🧠 Key Features

- 🧬 **Machine Learning Risk Prediction** (Decision Tree Classifier)
- ⚙️ **Interrupt-driven Resource Allocation**
- 🔄 **Safe state resource management**
- 🌐 **Flask RESTful APIs** (`/predict`, `/allocate`, `/dashboard`)
- 📊 **Interactive Dashboard** with Chart.js bar/pie visualizations
- 🛠️ **Modular Flask structure** with clear separation of model, allocator, routes, and frontend


## 📁 Project Structure

OS/

├── app.py # Flask entry point

├── core/

│ ├── model.py # ML model logic

│ ├── resource_manager.py # Resource allocation logic

│ └── routes.py # Flask API routes

├── dataset/

│ └── labeled_patient_data.csv # Synthetic training data

├── templates/

│ ├── index.html # Patient input form

│ ├── dash.html # Dashboard with charts

│ └── result.html # Prediction result page

├── static/

│ └── dash.css # Styling for dashboard

└── README.md


## 🧪 How It Works

1. A user submits patient data through the frontend (age, BP, heart rate, comorbidity score).
2. The backend predicts the **risk level (0 or 1)** using a trained ML model.
3. The allocator checks available ICU resources and safely allocates them based on **priority (risk)**.
4. In case of an emergency, **interrupt handling** preempts lower-priority patients.
5. The dashboard updates charts in real-time to reflect system state.


## 🔧 Tech Stack

- **Python 3.11**
- **Flask** (API development)
- **scikit-learn** (ML model)
- **HTML5 + CSS3 + Chart.js** (Frontend)
- **Postman** (API Testing)
- **Jinja2** (Flask Templating)


## 💡 Future Scope

- 🔄 **Advanced Scheduling Algorithms**: Incorporate algorithms like Round Robin or Priority Scheduling for multi-patient queue simulation.
- 🧠 **Enhanced ML Model**: Upgrade to ensemble models (e.g., Random Forest, XGBoost) or deep learning to improve prediction accuracy.
- 📈 **Historical Analytics**: Add time-series data storage and visual trends to observe ICU usage over time.
- 🌍 **Real Hospital Integration**: Connect to real-time hospital data using APIs from IoT devices or hospital databases.
- 🧪 **Load Simulation Testing**: Simulate thousands of requests using tools like JMeter to analyze system performance under load.
- 🔐 **Security Layer**: Add login systems and role-based access (admin vs. staff) for data privacy and control.
- 📊 **More Charts and Analytics**: Introduce line graphs, risk progression plots, and patient recovery tracking.
- 🧑‍⚕️ **Doctor Feedback System**: Add optional manual override inputs for doctors in edge cases.

## 📦 Installation & Setup

1. **Clone the repository**

   git clone https://github.com/your-username/OS-Hospital-Resource-Allocation.git
   cd OS-Hospital-Resource-Allocation
   
2. **Install dependencies**

   pip install -r requirements.txt

3. **Run the Flask App**

   python app.py

4. **View the Dashboard**
   Open your browser and go to:
   👉 [http://127.0.0.1:5000/dashboard](http://127.0.0.1:5000/dashboard)

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes
4. Push to the branch (`git push origin feature-name`)
5. Create a pull request

