# Personalized Parent Onboarding System with Blog Storage

## Objective

Develop a backend system for a personalized onboarding experience for parents. The system should collect essential details about the parent and their child, and based on the child's age, provide a personalized home feed consisting of a mix of blogs and vlogs. The home feed should be customizable based on the child's age group, gender, and the parent's type (e.g., first-time parent, experienced parent). Additionally, the system should store and manage blog content efficiently.

## Setup Instructions

Follow these steps to set up the project locally:

1. Clone the repository:
   git clone https://github.com/my_repository

2. Create and activate a virtual environment:
    python3 -m venv venv
    source venv/bin/activate
3. Install all requirements:
    pip install -r requirements.txt
4. Apply all migrations
    pip install -r requirements.txt
5. Start the Django development server:
    python manage.py runserver


## Models

### Parent Model

- **Description:** Represents a parent.
- **Fields:**
  - `name` (CharField): Name of the parent.
  - `email` (EmailField): Email address of the parent.
  - `parent_type` (CharField): Type of the parent.

### Child Model

- **Description:** Represents a child.
- **Fields:**
  - `parent` (ForeignKey): Reference to the parent.
  - `name` (CharField): Name of the child.
  - `age_group` (CharField): Age group of the child.
  - `gender` (CharField): Gender of the child.

### Blog Model

- **Description:** Represents a blog post.
- **Fields:**
  - `title` (CharField): Title of the blog.
  - `content` (TextField): Content of the blog.
  - `age_group` (CharField): Age group targeted by the blog.
  - `gender` (CharField): Gender targeted by the blog.
  - `parent_type` (CharField): Parent type targeted by the blog.
  - `link` (URLField): Link to the blog.
  - `snippet` (TextField): Snippet of the blog content.
  - `preview_image` (URLField): URL of the preview image.
  - `description` (TextField): Description of the blog.
  - `type` (CharField): Type of the blog (e.g., blog or vlog).


## API Endpoints

### Parent API

- **GET /api/parents/**
  - Description: Retrieve a list of parents.
  - Parameters: None
  - Responses:
    - 200 OK: Successfully retrieved the list of parents.
    - 404 Not Found: No parents found.

- **POST /api/parents/**
  - Description: Create a new parent.
  - Parameters:
    - name (string): Name of the parent.
    - email (string): Email address of the parent.
    - parent_type (string): Type of the parent.
  - Responses:
    - 201 Created: Parent created successfully.
    - 400 Bad Request: Invalid request data.

### Blog API

- **GET /api/blogs/**
  - Description: Retrieve a list of blogs.
  - Parameters: None
  - Responses:
    - 200 OK: Successfully retrieved the list of blogs.
    - 404 Not Found: No blogs found.

- **POST /api/blogs/**
  - Description: Create a new blog.
  - Parameters:
    - title (string): Title of the blog.
    - content (string): Content of the blog.
    - age_group (string): Age group targeted by the blog.
    - gender (string): Gender targeted by the blog.
    - parent_type (string): Parent type targeted by the blog.
    - link (string): Link to the blog.
    - snippet (string): Snippet of the blog content.
    - preview_image (string): URL of the preview image.
    - description (string): Description of the blog.
    - type (string): Type of the blog (e.g., blog or vlog).
  - Responses:
    - 201 Created: Blog created successfully.
    - 400 Bad Request: Invalid request data.

### Home Feed API

- **GET /api/home-feed/**
  - Description: Generates a personalized home feed for each user based on the child's age and gender.
  - Parameters:
    - age_group (string, optional): Age group of the child (default: infant).
    - gender (string, optional): Gender of the child (default: male).
  - Responses:
    - 200 OK: A list of blogs and vlogs relevant to the child's age group and gender.

### Custom Home Feed API

- **GET /api/custom-home-feed/**
  - Description: Generate a custom home feed based on age group, gender, and parent type.
  - Parameters:
    - age_group (string, required): Age group of the child.
    - gender (string, required): Gender of the child.
    - parent_type (string, required): Type of the parent.
  - Responses:
    - 200 OK: Successfully generated the custom home feed.
    - 404 Not Found: No data found for the given parameters.

## Testing Instructions

To run the tests, execute the provided test script.

### Additional Testing Information

The provided `tests.py` script contains the following test cases:
Run the command - python manage.py test

- `test_generate_home_feed`: Tests the generation of a home feed based on age group, gender, and parent type.
