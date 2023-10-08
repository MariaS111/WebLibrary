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

## Testing

Automated tests can be run using this command in the root directory:

```
$ pytest Library/

```
