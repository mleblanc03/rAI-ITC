import pandas as pd
import numpy as np
from faker import Faker
import pandas as pd
import pandas as pd

# Generate the sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Birthdate': ['1/01/1990', '2/02/1991', '3/03/1992', '4/04/1993', '5/05/1994'],
    'Score': [90, 75, 85, 70, 'Not Available'],
    'Grade': ['A', 'B', 'A', 'B', '']
}

df = pd.DataFrame(data)
df.to_csv('data/sample_data.csv', index=False)


# Generate a DataFrame with mixed data types
data = {
    'Integers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Floats': [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10],
    'Booleans': [True, False, True, False, True, False, True, False, True, False],
    'Dates': pd.date_range('2023-01-01', periods=10),
    'Mixed_Int_Float': [1, 2.2, 3, 4.4, 5, 6.6, 7, 8.8, 9, 10.10],
    'Mixed_Date_String': ['2023-01-01', '2023-01-02', 'A string', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08 08:00:00', '2023-01-09', '2023-01-10'],
    'Strings': ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango'],
    'Categories': ['a', 'b', 'c', 'a', np.NaN, 'b', 'c', 'a', np.NaN, 'b'],
}

df = pd.DataFrame(data)

# Save the DataFrame to CSV and Excel files
df.to_csv('data/mixed_data_types.csv', index=False)
df.to_excel('data/mixed_data_types.xlsx', index=False)

fake = Faker()

# Define the number of rows in the dataset
num_rows = 100000
# Generate random data
data = {
    'Name': [fake.name() for _ in range(num_rows)],
    'Address': [fake.address() for _ in range(num_rows)],
    'Email': [fake.email() for _ in range(num_rows)],
    'Phone Number': [fake.phone_number() for _ in range(num_rows)],
    'Date of Birth': [fake.date_of_birth() for _ in range(num_rows)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to CSV and Excel files
df.to_csv('data/heavy_data.csv', index=False)
df.to_excel('data/heavy_data.xlsx', index=False)