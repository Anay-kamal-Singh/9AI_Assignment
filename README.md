# Setup and Installation

# Clone the Repository

git clone <repository_url>
cd <repository_name>

# Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate   # Activate virtual environment (for Unix/Mac)

# Install Dependencies

pip install -r requirements.txt

# Configure MongoDB
Update the MongoDB connection settings in app/db.py according to your MongoDB server configuration.

# Run the FastAPI Application

uvicorn app.main:app --reload

# API Documentation
* Endpoints

Create Blog Post: POST /posts/

Request Body: JSON representing the new blog post.

Get Blog Post: GET /posts/{post_id}

Path Parameter: post_id - ID of the blog post.

Create Comment: POST /posts/{post_id}/comments/

Path Parameter: post_id - ID of the blog post.

Request Body: JSON representing the new comment.

Like Blog Post: POST /posts/{post_id}/like/

Path Parameter: post_id - ID of the blog post.

# Data Models
Post:
{
  "id": "string",
  "title": "string",
  "content": "string",
  "likes": "integer"
}

Comment:
{
  "id": "string",
  "post_id": "string",
  "content": "string"
}
