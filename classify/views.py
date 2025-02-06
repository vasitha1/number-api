import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sympy import isprime  


@api_view(['GET'])
def classify_number(request):
    # Get the number that is parsed into the URL
    number = request.GET.get('number')

    # Returns a 404 if the number is not provided or of wrong format
    if number is None or not number.isdigit():
        return Response({"number": "alphabet",
                         "error": True       
                        }, status=400)

    #Finding number of digits for amstrong before changing number to an 
    digit_count = len(number)
    amstrong_sum = 0
    digit_sum = 0

    for digit in number:
        amstrong_sum += (int(digit)) ** digit_count
        digit_sum += int(digit)

    number = int(number)

    is_amstrong = True if amstrong_sum == number else False

    # Handling even/odd
    parity = "even" if number % 2 == 0 else "odd"

    # Handling the property variable to return
    if is_amstrong == True:
        var_property = ["armstrong", "odd"] if parity == "odd" else ["armstrong", "even"]
    else:
        var_property = ["odd"] if parity == "odd" else ["even"]

    # Handling prime
    is_prime = isprime(number)

    # Handling perfect numbers
    factor_sum = 1

    for i in range(1, number):
        if number % i == 0:
            factor_sum += 0

    is_perfect = True if factor_sum == number else False


    # Handling fun fact
    fun_fact_url = f"http://numbersapi.com/{number}"

    try:
        fun_fact = requests.get(fun_fact_url).text
    except requests.RequestException:
        fun_fact = "No fun fact available"

    return Response({
        "number": number,
        "prime_status": is_prime,
        "is_perfect": is_perfect,
        "properties": var_property,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    })
