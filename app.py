from flask import *
import numpy as np
import joblib as joblib
from difflib import get_close_matches

popular_df = joblib.load(open('popular.pkl', 'rb'))
pt = joblib.load(open('pt.pkl', 'rb'))
books = joblib.load(open('books.pkl', 'rb'))
similarity_scores = joblib.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books',methods=['post'])
def recommend():
    try:
        user_input = request.form.get('user_input')
        
        # Convert user input to title case for better matching
        user_input = user_input.title()
        
        # If exact match not found, find similar titles
        if user_input not in pt.index:
            available_titles = list(pt.index)
            close_matches = get_close_matches(user_input, available_titles, n=5, cutoff=0.5)
            
            if close_matches:
                return render_template('recommend.html', 
                                    error=f"Book not found. Did you mean one of these?",
                                    suggestions=close_matches)
            else:
                return render_template('recommend.html', 
                                    error=f"Book '{user_input}' not found in our database.")

        # Get the index of the book
        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)

        return render_template('recommend.html', data=data)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return render_template('recommend.html', 
                             error="An error occurred while processing your request. Please try again.")


if __name__ == '__main__':
    app.run(debug=True)
