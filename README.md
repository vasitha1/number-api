# Number Classification API

This API classifies a number based on its mathematical properties and provides a fun fact.

## Endpoints

- `GET /api/classify-number?number=<integer>`

### Technology Stack:

    Programming Language/Framework: Django (Python)

### Deployment:

    Deployed with Render

### Setup instructions

    On your terminal, clone the repository using the command "git clone git@github.com:vasitha1/number-api.git" or "git clone https://github.com/vasitha1/number-api.git"

    Enter into the project by running the command "cd number_api

    Then run the project locally using the command "python manage.py runserver"

    If your project runs sucessfully, you can run the following: "http://127.0.0.1:8000/api/classify-number/?number=371" in your browser. Feel free to play arround by changing the last number 371


### Example Response:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
}
