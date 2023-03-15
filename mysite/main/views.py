from django.shortcuts import render

# Create your views here.

def calculator(request):
    number1 = request.POST.get('number1')
    number2 = request.POST.get('number2')
    if not number1 or not number2:
        return render(request, 'main/calculator.html', context={'error_message': 'Please enter valid values for number1 and number2.'})
    result = []
    for i in range(int(number2), int(number1) + 1):
        if i % int(number2) == 0:
            result.append(i)
    return render(request, 'main/calculator.html', context={'res':result})
    