from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Medicamento
import json


def lista_medicamentos(request):  # Adicionando o argumento "request"
    medicamentos = Medicamento.objects.all()
    data = {
        'medicamentos': list(medicamentos.values())
    }
    return JsonResponse(data)


def adicionar_medicamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        horario = request.POST.get('horario')
        medicamento = Medicamento(nome=nome, quantidade=quantidade, horario=horario)
        medicamento.save()
        return JsonResponse({'message': 'Medicamento adicionado com sucesso!'})


def remover_medicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, pk=medicamento_id)
    medicamento.delete()
    return JsonResponse({'message': 'Medicamento removido com sucesso!'})


def atualizar_status_medicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, pk=medicamento_id)
    if request.method == 'PUT':
        # Ler os dados da solicitação PUT
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        tomado = body_data.get('tomado')

        # Atualizar o status do medicamento com base nos dados recebidos na solicitação
        medicamento.tomado = tomado
        medicamento.save()

        return JsonResponse({'message': 'Status do medicamento atualizado com sucesso!'})
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
