from datetime import datetime

class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade="média"):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.criado_em = datetime.now()
        self.concluida = False

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "criado_em": self.criado_em.isoformat(),
            "concluida": self.concluida
        }

class Usuario:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password