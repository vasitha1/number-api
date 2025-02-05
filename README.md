# Number Classification API

This API classifies a number based on its mathematical properties and provides a fun fact.

## Endpoints

- `GET /api/classify-number?number=<integer>`

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
