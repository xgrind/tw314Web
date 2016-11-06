from cups import require

from django.shortcuts import render
from service import UsuarioService
from service import EmpresaService
from form.UsuarioForm import UsuarioForm
from django.views.decorators.http import require_POST, require_GET


def template(request):
    if request.method == "POST":
        cadastra(request)
    form = UsuarioForm()
    estabelecimentos = listar_empresa(request)
    if request.method == "GET":
        admins = lista_por_empresa_perfil(request)
        # estabelecimentos = busca_por_cnpj(request)
        return render(request, 'home/suporte/suporte_cadastro_admin.html',
                      {'form': form, 'admins': admins, 'estabelecimentos': estabelecimentos})

    return render(request, 'home/suporte/suporte_cadastro_admin.html', {'form': form, 'estabelecimentos': estabelecimentos})


@require_POST
def cadastra(usuario):
    UsuarioService.suporte_cadastra(usuario.POST)


def lista_por_empresa_perfil(request):
    empresa = str(1)
    perfil = 2
    return UsuarioService.lista_por_empresa_perfil(empresa, perfil)


def busca_por_cnpj(request):
    cnpj = request.POST.cnpj
    return EmpresaService.busca_por_cnpj(cnpj)


def listar_empresa(request):
    return EmpresaService.lista()


def params(form, servicos, ramos):
    return {'form': form, 'servicos': servicos, 'ramos': ramos}

