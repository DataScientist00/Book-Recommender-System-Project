# Book Recommender System

A machine learning project to recommend books based on user preferences using collaborative filtering. This project features an interactive web interface built with **Streamlit**.

## Watch the Demo 📺
[![YouTube Video](https://img.shields.io/badge/YouTube-Watch%20Video-red?logo=youtube&logoColor=white&style=for-the-badge)](https://youtu.be/uHKaGtwkFWE)

---

![Image](https://github.com/user-attachments/assets/ba0f197f-392a-49ac-b377-d3393c9a0f00)

## 🎯 Project Overview
The goal of this project is to recommend books to users based on their reading preferences and ratings. The system utilizes:
- **Collaborative Filtering**: Suggests books based on user-item interactions.
- **K-Nearest Neighbors (KNN)**: Finds books similar to the user's chosen book.
- **Streamlit Web Application**: Provides an interactive interface for users to get book recommendations.

---

## 🚀 How to Run the Project

### 1. **Clone the Repository**
```bash
git clone https://github.com/DataScientist00/Book-Recommender-System.git
cd Book-Recommender-System
```

### 2. **Install Required Dependencies**
Create a Python virtual environment and install the dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. **Run the Streamlit App**
Start the Streamlit app to use the book recommender system:
```bash
streamlit run app.py
```
The application will be available at `http://localhost:8501`. You can select a book, and the system will recommend similar books along with their covers.

---

## 🧑‍💻 Technologies Used
- **Languages**: Python
- **Libraries**:
  - **Machine Learning**: Scikit-learn (KNN-based recommendation system)
  - **Data Handling**: Pandas, NumPy
  - **Web Framework**: Streamlit
  - **Serialization**: Pickle (for saving trained models)
- **Tools**: Jupyter Notebook (for development and exploration)

---

## 🧠 Model Overview

### **K-Nearest Neighbors (KNN) Model**
   - **Input**: Book name
   - **Processing**: Finds the nearest neighbors using collaborative filtering
   - **Output**: List of recommended books with their cover images

---

## 📊 Dataset
The system is trained on a dataset containing:
- **Books.csv**: Contains book details such as title, author, and image URLs.
- **Ratings.csv**: Contains user ratings for books.
- **Users.csv**: Contains user demographic details.

---

## 🖼 Screenshots

Here’s how the Streamlit app looks:

![Image](https://github.com/user-attachments/assets/92bae149-b624-4d2b-a1b7-7a7209ad11a8)

*Example: Select a book and get recommendations.*

---

## 🛠 Future Work
- Improve recommendation accuracy by implementing matrix factorization techniques like SVD.
- Add content-based filtering using book metadata such as genre and author.
- Deploy the model using cloud services like AWS or Google Cloud.

---

## 🤝 Contributing
Contributions are always welcome! If you'd like to contribute:
1. Fork the repository
2. Create a branch for your changes
3. Submit a pull request

---

## 📞 Contact
For any questions or feedback, reach out to:
- **Email**: nikzmishra@gmail.com
- **YouTube**: [Channel](https://www.youtube.com/@DataScienceSensei/videos)

---

**⭐ If you found this project helpful, please give it a star! ⭐**

