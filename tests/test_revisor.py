"""Regressoes do revisor autonomo do promoavatar3."""
import importlib.util
from pathlib import Path


def carregar_revisor():
    arquivo = Path(__file__).resolve().parents[1] / "scripts" / "revisor.py"
    spec = importlib.util.spec_from_file_location("revisor", arquivo)
    assert spec and spec.loader
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def test_motor_encontra_utilitarios_na_skill_versionada():
    revisor = carregar_revisor()

    for nome in ("verify-cut.py", "lint-timeline.py"):
        encontrado = Path(revisor.motor(nome))
        assert encontrado == revisor.SKILL_LOCAL / nome
        assert encontrado.is_file()
