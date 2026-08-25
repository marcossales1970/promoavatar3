"""Cercas editoriais enquanto o Método 3R ainda não é um domínio plugado."""
import json
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]


def ler(caminho: str) -> str:
    return (RAIZ / caminho).read_text(encoding="utf-8")


def test_prompt_tem_identidade_cta_e_cerca_de_saude():
    prompt = ler("prompts/fase1-metodo3r.md")
    normalizado = " ".join(prompt.casefold().split())

    assert "Respirar, Reeducar, Restaurar" in prompt
    assert "Cássia Saito" in prompt
    assert "Converse com a Cássia pelo WhatsApp" in prompt
    assert "Não diagnostique" in prompt
    assert "não substitui avaliação, diagnóstico ou tratamento médico" in normalizado


def test_prompt_exige_contrato_executavel_agnes_e_heygen():
    prompt = ler("prompts/fase1-metodo3r.md")

    for secao in (
        "# VIDEO SPEC", "## HEYGEN", "## FALA EXATA", "## TIMELINE",
        "## VISUAL INTENTS", "## CTA", "## HEALTH COMPLIANCE", "## VALIDATION",
    ):
        assert secao in prompt
    assert "CONFIG_REQUIRED" in prompt
    assert "Não inventar IDs" in prompt
    assert "ready_for_agnes:" in prompt
    assert "ready_for_heygen:" in prompt
    assert "prompt_instagram:" in prompt
    assert "prompt_youtube:" in prompt
    assert "30–80" in prompt


def test_prompt_recusa_o_editorial_inema_em_vez_de_usa_lo():
    prompt = ler("prompts/fase1-metodo3r.md")
    ocorrencias = [linha for linha in prompt.splitlines() if "inema.club" in linha]

    assert ocorrencias == [
        "apareça nos dados do alvo. Não use IA, trilha, curso, Nei, Tiza ou inema.club."
    ]


def test_variante_nao_esta_liberada_no_fluxo_com_avatar_e_cta_antigos():
    fluxo = json.loads(ler("flow.json"))
    variantes = fluxo["fases"][0].get("variantes", {})

    assert "metodo3r" not in variantes
