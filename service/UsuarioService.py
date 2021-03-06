from persistence import UsuarioPersistence


def administrador_cadastra(request, usuario):
    return UsuarioPersistence.administrador_cadastra(request, usuario)


def suporte_cadastra(usuario):
    return UsuarioPersistence.suporte_cadastra(usuario)


def suporte_atualiza(request, usuario, pk):
    return UsuarioPersistence.suporte_atualiza(request, usuario, pk)


def administrador_atualiza(request, usuario, pk):
    return UsuarioPersistence.administrador_atualiza(request, usuario, pk)


def adiciona_senha(request, pk):
    return UsuarioPersistence.adiciona_senha(request, pk)


def lista_por_empresa_perfil(empresa, perfil):
    return UsuarioPersistence.lista_por_empresa_perfil(empresa, perfil)


def lista_por_perfil(perfil):
    return UsuarioPersistence.lista_por_perfil(perfil)


def usuario_por_id(pk):
    return UsuarioPersistence.usuario_por_id(pk)


def usuario_por_email(email):
    return UsuarioPersistence.usuario_por_email(email)


def loga(request, login):
    return UsuarioPersistence.loga(request, login)
