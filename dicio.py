from typing import Mapping


dicio = {"nome": "Gabriel", "ano": 1993, "valor_logico": True}
print(dicio)

dicio["nome"] = "Ana"
print(dicio)

dicio.update({"ano": 1952})
print(dicio)

dicio.update({"estado": "PR"})
print(dicio)

dicio.pop("valor_logico")
print(dicio)

dicio.popitem()
print(dicio)

dict()
print(type(dict()))

dicio.