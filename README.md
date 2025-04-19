## Book Recommendation System

### Data Description   
We've three dataset -  
• Book data – (ISBN, Book-Title, Book-Author, Year-Of-Publication, Publisher, Image-URL-S, Image-URL-M, Image-URL-L)  
• Users data - (User-ID, Location, Age)  
• Ratings data - (User-ID, ISBN, Book-Rating)   

Dataset link: https://www.kaggle.com/datasets/saurabhbagchi/books-dataset

### How to Run the Application

1. **Setup Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Application**
   ```bash
   python3 app.py
   ```

4. **Access the Application**
   - Open your web browser and go to: http://127.0.0.1:8080
   - The application will be running in debug mode

### Features
- View top 50 popular books
- Get personalized book recommendations
- Search for books and get similar recommendations
- Modern and responsive UI

### Summary of Project

- As the first step, we performed data preparation (i.e data cleaning and feature engineering) and EDA part.   

- After data preparation, build a recommendation system based on popularity (i.e ratings). These recommendations are usually given to every user irrespective of personal characterization. Merged book_data dataset and ratings, considering ISBNs that were explicitly rated for this recommendation system. We have listed all the top 50 books with the highest average rating but we have only selected those books whose no ratings are more than 250.

- The third step is to do Collaborative Filtering - Memory based approach was our first trial on train and test dataset which uses the memory of previous user's interactions to compute user's similarities based on items they've interacted with (i.e user-based approach) or compute items similarities based on the users that have interacted with them (i.e item-based approach). Our approach here is that we will only select users who have rated more than 200 books and we will only select books that are rated by more than 50 users to get more accurate results for the model and avoid outliners. Then we apply cosine similarity to make item similarity need to take the transpose of a matrix. This matrix would help in managing the train-test matrix. After all views predictions based on similarity, we find recommendation on it based on score. 

- The last step is to create a function recommend which will take the book name as input from the user and it will return 4 similar books with the author.

Reference images:
<img width="1437" alt="Screenshot 2025-04-19 at 12 55 40 PM" src="https://github.com/user-attachments/assets/af2c8520-1bfe-4e6d-bb65-d48c9583f4c3" />

<img width="1440" alt="Screenshot 2025-04-19 at 12 56 05 PM" src="https://github.com/user-attachments/assets/6af18a69-7824-431c-bd10-0489d53cc0c4" />

<img width="1435" alt="Screenshot 2025-04-19 at 12 57 10 PM" src="https://github.com/user-attachments/assets/2ca3cf32-aa26-4577-be6e-96bf6c69361f" />



