# rhombusAI - Intelligent Types Converter (ITC)

ITC is a web application designed to automatically infer and convert data types in datasets from XLSX and CSV files. It provides an interface for uploading files, viewing data schemas, and managing data conversions.

## Backend

- **Authentication**: Basic authentication for website access. (TODO: Implement API authentication.)
- **Types Converter**: The Python class `DataTypeConverter` located in the `src/data_type_converter` directory provides schemas and converts data from XLSX and CSV tables. The `types_converter` view `UploadedFileViewSet` manages the interaction between this class and the Django Rest API. 
- **File Upload**: Managed via the `file_upload` function view and the `Fileform`. (TODO: Move this operation to the React frontend.)
- **Logging and Error Management**: (TODO: Improve the logging system and error management.)
- **Testing**: (TODO: Implement unit and integration tests.)

## Frontend

Built with React, the frontend consists of two main pages:

- **Dashboard**: The main dashboard, similar to the home page of the Django application.
- **Analysis**: Provides a detailed view of each file, allowing users to view the schema and data samples before and after conversion. (TODO: Improve user interaction, enable file download, allow file search by name, file deletion, and allow users to choose their own default values for replacing incorrect ones.)

## Running the Application

Follow these steps to run the application:

1. Ensure Python version 3.11.8 is installed.
2. Inside the root repository, create a virtual environment: `python -m venv ENV`
3. Activate the virtual environment: `source ENV/bin/activate`
4. Install the required Python packages: `pip install -r requirements.txt`
5. Navigate to `rhombusAI/` and initialize the local database db.sqlit3: `python manage.py migrate`
6. Navigate to `rhombusAI/frontend` and install the required Node.js packages: `npm install`
7. Start the Django server in the `rhombusAI` directory: `python manage.py runserver`
8. Start the React application in `rhombusAI/frontend` with `npm start`
9. Generate test datasets from `rhombusAI/types_converter/src/tests/` using `python dataset_generation.py` 
10. Access the web application locally at [http://127.0.0.1:8000](http://127.0.0.1:8000) and upload the test files for experimentation.

(TODO: Create a Dockerfile and Docker image for hosting the application)