from django.shortcuts import render, redirect
from ortools.linear_solver import pywraplp
from django.http import JsonResponse
from .forms import ProdutoForm
from .models import Produto

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


def index(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = ProdutoForm()
            return render(request, 'index.html', {'form': form})
    else:
        form = ProdutoForm()
    return render(request, 'index.html', {'form': form})


def solverCalc(request):
    produtos = Produto.objects.all()
    # Cria o solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Variáveis de decisão
    x1 = solver.IntVar(5, solver.infinity(), 'x1')  # moletons
    x2 = solver.IntVar(10, solver.infinity(), 'x2')  # camisas oversized
    x3 = solver.IntVar(10, solver.infinity(), 'x3')  # camisas comuns

    # Restrições de orçamento
    solver.Add((116 * x1) + (60 * x2) + (60 * x3) <= 1800)

    # Restrições de capacidade de armazenamento
    solver.Add(x1 + x2 + x3 <= 100)

    # Restrições de tempo de produção
    solver.Add(2 * x1 + 1 * x2 + 0.5 * x3 <= 30)

    # Restrições de transporte
    transport_cost = solver.IntVar(0, solver.infinity(), 'transport_cost')
    solver.Add(transport_cost >= ((x1 + x2 + x3) + 49) / 50)

    # Restrições de demanda mínima
    solver.Add(x1 >= 5)
    solver.Add(x2 >= 10)
    solver.Add(x3 >= 10)

    # Restrições de capacidade dos vendedores
    solver.Add(x1 + x2 + x3 <= 3 * 20)

    # Função objetivo (maximizar o lucro)
    profit = solver.Objective()
    profit.SetCoefficient(x1, 140 - (116 if x1.solution_value() <= 10 else 110))
    profit.SetCoefficient(x2, 75 - (60 if x2.solution_value() <= 20 else 55))
    profit.SetCoefficient(x3, 70 - (60 if x3.solution_value() <= 20 else 55))
    profit.SetCoefficient(transport_cost, -100)
    profit.SetOffset(-2 * (x1.solution_value() + x2.solution_value() + x3.solution_value()))
    profit.SetMaximization()

    # Resolve o problema
    status = solver.Solve()

    results_dict = {
        'x1': x1.solution_value(),
        'x2': x2.solution_value(),
        'x3': x3.solution_value(),
        'profit': solver.Objective().Value(),
    }

    # Return the results as a JSON response
    return JsonResponse(results_dict)
