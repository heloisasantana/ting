import sys
from .file_management import txt_importer


def process(path_file, instance):
    for item in instance.queue:
        if item["nome_do_arquivo"] == path_file:
            return None
    new_object = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    instance.enqueue(new_object)
    sys.stdout.write(str(new_object))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
