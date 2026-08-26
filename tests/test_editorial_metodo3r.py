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
    assert "Eu sou Cássia Saito,\n    profissional da saúde e do movimento, especialista em Yoga e Breathwork." in prompt
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


def test_variante_esta_liberada_com_cta_proprio():
    fluxo = json.loads(ler("flow.json"))
    variantes = fluxo["fases"][0].get("variantes", {})

    assert variantes["metodo3r"] == "prompts/fase1-metodo3r.md"
    assert fluxo["cta"]["metodo3r"] == "cta/cta-metodo3r-9x16.mp4"
    assert (RAIZ / fluxo["cta"]["metodo3r"]).is_file()


def test_prompt_obedece_contrato_de_saida_do_runtime():
    prompt = ler("prompts/fase1-metodo3r.md")

    assert "grave em `{{saida}}`" in prompt.casefold()
    assert "RESULT: {{saida}}" in prompt
    assert "RESULT: {{pasta}}" not in prompt
    assert "git add" in prompt
    assert "Não faça push" in prompt
