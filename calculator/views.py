from django.shortcuts import render
from .forms import CalculatorForm

def calculate_view(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operation = form.cleaned_data['operation']
            
            raw_result = None
            result = None
            error_message = None

            if operation == 'add':
                raw_result = num1 + num2
            elif operation == 'subtract':
                raw_result = num1 - num2
            elif operation == 'multiply':
                raw_result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    error_message = 'Error: Division by zero'
                else:
                    raw_result = num1 / num2
            
            if not error_message:
                result = raw_result
                # Apply extra logic
                if result > 100:
                    result *= 2
                elif result < 0:
                    result += 50
            
            operation_symbols = {
                'add': '+',
                'subtract': '-',
                'multiply': '×',
                'divide': '÷'
            }

            context = {
                'num1': num1,
                'num2': num2,
                'operation_symbol': operation_symbols.get(operation, ''),
                'raw_result': raw_result,
                'final_result': result,
                'error': error_message,
            }
            
            return render(request, 'calculator/result.html', context)
    else:
        form = CalculatorForm()
    
    return render(request, 'calculator/math_form.html', {'form': form}) 