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
    if len(instance) > 0:
        name_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {name_file} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
