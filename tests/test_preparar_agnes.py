import importlib.util
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("preparar", RAIZ / "scripts" / "preparar.py")
preparar = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(preparar)


def test_le_visual_intents_por_canal_sem_quebrar_formato_legado(tmp_path):
    roteiro = tmp_path / "roteiro.md"
    roteiro.write_text(
        """## VISUAL INTENTS

### IMAGE 1
segment: 1
duration: 4s
aspect_ratio_instagram: template_defined
aspect_ratio_youtube: 16:9
prompt_en:
\"Editorial photograph of an adult noticing their breathing.\"
prompt_instagram:
\"Centered adult noticing their breathing, composed for a vertical reel top band.\"
prompt_youtube:
\"Adult noticing their breathing in a wide editorial room composition.\"
negative_prompt:
\"text, watermark, dramatic distress\"
continuity_notes:
\"Keep the same adult and soft daylight.\"

## CTA
spoken: observe sua respiração
""",
        encoding="utf-8",
    )

    imagens = preparar.ler_imagens(roteiro)

    assert len(imagens) == 1
    assert imagens[0]["n"] == 1
    assert imagens[0]["duration"] == "4s"
    assert imagens[0]["aspect_ratio"] == "template_defined"
    assert "Centered adult" in imagens[0]["prompt"]
    assert "Continuity: Keep the same adult and soft daylight." in imagens[0]["prompt"]
    assert "Avoid: text, watermark, dramatic distress." in imagens[0]["prompt"]
    assert imagens[0]["continuity_notes"] == "Keep the same adult and soft daylight."

    youtube = preparar.ler_imagens(roteiro, "youtube")
    assert youtube[0]["aspect_ratio"] == "16:9"
    assert "wide editorial room" in youtube[0]["prompt"]
