from dns.resolver import resolve, NoAnswer


def resolve_record(record_name, record_type):
    if record_name is None:
        raise ValueError("Missing record name!")
    print(f"Performing {record_type} resolution on: {record_name}")
    answers = resolve(record_name, record_type)
    return answers


def resolve_a(params):
    try:
        record_name = params.get("record", None)
        answer = resolve_record(record_name, "A")
        return [record.address for record in answer]
    except NoAnswer as no_answer_exception:
        print(no_answer_exception)
        return []
    

def resolve_cname(params):
    try:
        record_name = params.get("record", None)
        answer = resolve_record(record_name, "CNAME")
        return [record.address for record in answer]
    except NoAnswer as no_answer_exception:
        print(no_answer_exception)
        return []
