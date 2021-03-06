from pip._vendor import requests

from form.EmpresaServicoForm import EmpresaServicoForm
# TODO MASTER: MUDAR AS ROTAS DE REQUEST DO


def cadastra(request, rel_emp_svc):
    form = EmpresaServicoForm(rel_emp_svc)

    if form.is_valid():
        status_ativacao = form.cleaned_data['status_ativacao']
        servico = form.cleaned_data['servico']

        data = monta_json(status_ativacao, request.session["user"]["empresa"]["id"], servico)

        try:
            form = requests.post('http://localhost:3000/servicos_empresa', json=data)
        except requests.exceptions.ConnectionError:  # verificar se funciona
            form = "Erro ao tentar conectar com WebService"
    else:
        form = "Campos de Empresa nao preenchidos corretamente"
    return form


def atualiza(rel_novo, rel, pk):

    form = EmpresaServicoForm(rel_novo)

    if form.is_valid():
        status_ativacao = rel['status_ativacao']
        servico = form.cleaned_data['servico']

        data = monta_json(status_ativacao, servico)

        try:
            form = requests.put('http://localhost:3000/rel/' + pk, json=data)

        except requests.exceptions.ConnectionError:  # verificar se funciona
            form = "<h3>Erro ao tentar conectar com WebService</h3>"
    else:
        form = "<h3>Campos de Empresa nao preenchidos corretamente</h3>"

    return form


def lista(empresa):
    rel_emp_svc = requests.get('http://localhost:3000/servicos_empresa/' + str(empresa)).json()
    return rel_emp_svc


def monta_json(status_ativacao, empresa, servico):
    data = {'status_ativacao': status_ativacao, 'empresaId': empresa, 'servicoId': servico}
    return data
