def exists_word(word, instance):
    final_list = list()
    for item in instance.queue:
        occurrences_info = []
        new_object = {
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": occurrences_info,
            }
        for i, row in enumerate(item["linhas_do_arquivo"]):
            if word in row.lower():
                occurrences_info.append({"linha": i + 1})
        if len(occurrences_info):
            final_list.append(new_object)
    return final_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
