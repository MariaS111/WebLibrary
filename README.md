# WebLibrary

## Set Up

The first thing to do is to clone the repository:

```
git clone https://github.com/Marias111/WebLibrary.git
cd WebLibrary

```

Create a virtual environment to install dependencies in and activate it:
```
python -m venv myenv
myenv\Scripts\activate

pip install pipenv
pipenv install 

```

Then enter command:

```
python Library/manage.py runserver

```
And navigate to http://127.0.0.1:8000/

### Using Docker

The project can also be set up using Docker. Use the provided Dockerfile to build and run the application in a Docker container.

```
docker build -t library_app . 
docker run -p 8000:8000 library_app

```

After running these commands, you can access the application at http://127.0.0.1:8000/.

## Functionality

- **User Registration/Login/Logout**
  - Users can create accounts, log in, and log out of the system.

- **View a List of Books**
  - Users can see a list of all books of the system.

- **View Detailed Book Information**
  - Users can view detailed information about a specific book.

- **Search for Books by Title or Author**
  - Users can search for books using titles or author names.

- **Ability to Add, Edit, and Delete Books**
  - Admins or authorized users can add new books, edit existing ones, and remove books from the system.

- **Leave Comments on Books (For Authenticated Users But not for Admins)**
  - Authenticated users can leave comments on books.

- **View a List of Authors**
  - Users can see a list of all authors of the system.

- **View Detailed Author Information**
  - Users can view detailed information about a specific author.
    
- **Ability to Add Authors**
  - Admins or authorized users can add new authors to the system.
    
- **Pagination for Books and Authors Lists**
  - Implementing pagination for books and authors lists, allowing for easier navigation and a better user experience.

- **Leave Rating for Books (For Authenticated Users But not for Admins)**
  - Allowing users to rate books, providing an extra layer of interaction and feedback for the system.

## Testing

Automated tests can be run using this command in the root directory:

```
$ pytest Library/

```
