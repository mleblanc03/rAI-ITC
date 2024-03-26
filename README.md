# rhombusAI - Assessment

ITC (Intelligent Types Converter) is a web application designed to automatically infer the types of datasets from xlsx and csv files.

## Features

- **Authentication**: Basic authentication is implemented on the website. API authentication is currently not activated (TODO).
- **Types Converter**: Located in the `src` directory, the Types Converter is a Python class instantiated by the file path given by the Django Model `UploadedFile` instance. It provides a fast schema by analyzing a subset of the data. The schema is saved in the model on the first call. For heavier operations, conversion can be requested as needed (TODO: Implement chunking, etc.).
- **File Upload**: File uploads are managed via the `file_upload` view and the `Fileform` (TODO: Manage this operation in the React part).
- **Logging and Error Management**: Improve the logging system and error management (TODO).
- **Testing**: Implement unit and integration tests (TODO).

## Frontend

The frontend is built with React and consists of two pages:

- **Dashboard**: A main dashboard similar to the home of the Django application.
- **Analysis**: A detailed view of each file where the schema and data samples can be viewed before and after conversion. (TODO: Improve user interaction, allow users to choose their own default values for replacing incorrect ones, enable file download, allow file search by name, and file deletion).

## Backend

The backend is built with Django.

## Running the Application

To run the application, follow these steps:

1. Ensure you have Python version 3.11.8 installed.
2. Install the required Python packages with `pip install -r requirements.txt`.
3. Install the required Node.js packages with `npm install`.
4. Start the Django server with `python manage.py runserver`.
5. Start the React application with `npm start`.

(TODO: Create a Dockerfile and Docker image for hosting the application)