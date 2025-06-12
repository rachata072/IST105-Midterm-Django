from django.shortcuts import render
from .forms import CalculatorForm

def calculate_view(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            input1 = form.cleaned_data['input1']
            input2 = form.cleaned_data['input2']
            operation = form.cleaned_data['operation']
            
            # Perform the selected operation
            if operation == 'add':
                result = input1 + input2
                operation_symbol = '+'
            elif operation == 'sub':
                result = input1 - input2
                operation_symbol = '-'
            elif operation == 'mul':
                result = input1 * input2
                operation_symbol = '×'
            elif operation == 'div':
                if input2 == 0:
                    return render(request, 'calculator/result.html', {
                        'error': 'Error: Division by zero',
                        'form': form,
                        'input1': input1,
                        'input2': input2,
                        'operation': '/',
                        'raw_result': None,
                        'final_result': None
                    })
                result = input1 / input2
                operation_symbol = '÷'
            
            # Apply extra logic
            raw_result = result
            if result > 100:
                result *= 2
            elif result < 0:
                result += 50
            
            return render(request, 'calculator/result.html', {
                'input1': input1,
                'input2': input2,
                'operation': operation_symbol,
                'raw_result': raw_result,
                'final_result': result,
                'form': form
            })
    else:
        form = CalculatorForm()
    
    return render(request, 'calculator/math_form.html', {'form': form})
