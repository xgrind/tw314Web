from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from service.ServicoService import servico_por_id
from service.TicketService import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

template_name = 'home/funcionario/funcionario_principal.html'


def template(request):
    guiche = request.session["guiche"]
    servico = servico_por_id(request.session["servico"])
    fila = mostrar_fila(1, request.session["servico"])
    pegar_codigo = chamar_ticket(1, request.session["servico"])
    senha = mostrar_ticket(1, request.session["servico"])

    return render(request, template_name, params(guiche, servico, fila, senha, pegar_codigo))


def chamar_proximo(request, pk):
    mudar_status_ticket(pk)
    return HttpResponseRedirect(reverse('funcionario_principal'))


def params(guiche, servico, fila, senha, pegar_codigo):
    return {"guiche": guiche, "servico": servico, 'fila': fila, 'senha': senha, 'pegar_codigo': pegar_codigo}
