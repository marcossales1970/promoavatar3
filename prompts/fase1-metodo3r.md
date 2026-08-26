# Fase de texto — Método 3R

Gere um roteiro por alvo listado abaixo, e nenhum outro:

{{publicos}}

Cada alvo termina em `-alc`, `-aut` ou `-pro`. O sufixo define a função:

- `-alc`: alcance, 25–40 s, identificação ou quebra de mito, sem venda;
- `-aut`: autoridade, 35–60 s, ensina uma distinção concreta;
- `-pro`: promocional, 30–45 s, apresenta a avaliação e chama para conversar.

Assunto fornecido pelo usuário:

<assunto>
{{input}}
</assunto>

Referência: {{ref}}

Antes de escrever, leia `docs/editorial-metodo3r.md`. Ele é a fonte editorial
local e vence qualquer gatilho, fecho, marca ou CTA herdado do INEMA.club que
apareça nos dados do alvo. Não use IA, trilha, curso, Nei, Tiza ou inema.club.

## Contrato factual

Use somente fatos do assunto e do editorial. Se faltar um fato necessário, não
preencha com plausibilidade. Troque o ângulo ou declare a lacuna no resumo.

O Método 3R significa Respirar, Reeducar, Restaurar. Cássia Saito é
profissional da saúde e do movimento, especialista em Yoga e Breathwork. O
serviço central é avaliação respiratória
individual, presencial ou on-line. Quando indicado, podem ser propostas
práticas individualizadas de consciência e reeducação respiratória.

A abordagem é complementar. Não substitui avaliação, diagnóstico ou tratamento
médico. Não diagnostique pela fala e não prometa cura ou resultado.

## Passo zero

Registre em `resumo-estrategico.md`:

1. essência fiel do assunto em 2–4 frases;
2. uma tese central específica;
3. um motivo prático para assistir, sem urgência inventada;
4. um elemento demonstrável na tela;
5. fatos usados e fatos deliberadamente não inferidos;
6. riscos de saúde, estereótipo ou promessa encontrados na revisão.

Se não houver tese e elemento demonstrável, termine com `ERRO:` e não fabrique
roteiros.

## Oficina de gancho

Escreva cinco primeiras frases por alvo, descarte quatro e registre a linha
`Ganchos descartados:`. O escolhido deve abrir uma lacuna que a segunda frase
precise completar. Prefira sinais observáveis e mitos concretos. Evite “você
merece”, “transforme sua vida”, medo, culpa e pergunta genérica.

## Regras da fala

1. Uma ideia principal por vídeo.
2. Falar como Cássia: calma, concreta, educativa e responsável.
3. Não presumir rotina, maternidade, profissão ou estado emocional pela palavra
   “mulheres”.
4. Não usar “respire fundo” como solução universal.
5. Não prescrever retenção, contagem ou exercício intenso em conteúdo genérico.
6. Um sinal isolado nunca vira diagnóstico.
7. Jargão só entra se for explicado em linguagem comum.
8. O nome Método 3R precisa cumprir função; não é slogan decorativo.
9. Não repetir a mesma arquitetura nos três tipos.
10. A primeira frase é fala, não título; deve soar natural em voz alta.
11. Logo depois do gancho, incluir exatamente: “Eu sou Cássia Saito,
    profissional da saúde e do movimento, especialista em Yoga e Breathwork.”
    A identificação deve estar dentro de `## FALA EXATA` em todos os roteiros.

### Alcance

Reconhecimento ou quebra de mito. Pode convidar a pessoa a observar um hábito
sem tentar corrigi-lo. CTA de comentar, compartilhar ou acompanhar. Não citar
WhatsApp, avaliação paga ou agendamento.

### Autoridade

Ensinar uma distinção verificável: as quatro dimensões da respiração, diferença
entre observar e corrigir, ou uma etapa da avaliação. Pode propor auto-observação
leve, sem técnica terapêutica. CTA de salvar, seguir ou observar.

### Promocional

Dor ou dúvida concreta → por que receita genérica não basta → avaliação
individual → benefício educativo limitado → convite. CTA único:
“Converse com a Cássia pelo WhatsApp e solicite informações sobre a avaliação.”

## Bloco de execução obrigatória — Agnes + HeyGen

Cada roteiro deve sair pronto para execução, sem interpretação manual posterior.
A fala, a timeline, os visuais, as sobreposições e o CTA devem descrever o mesmo
vídeo, sem contradições.

### Identificação

Preencha ID estável, tipo, público, objetivo, estágio do funil, duração, formato
e CTA. Use TOFU para `-alc`, MOFU para `-aut` e BOFU para `-pro`. As plataformas
são Instagram Reels e YouTube. O avatar mestre da HeyGen é 16:9: ele serve
diretamente ao YouTube e é reenquadrado pelo compositor para o reel 9:16. Nunca
grave texto essencial nas bordas do avatar.

### HeyGen

Reutilize `avatar_id`, `voice_id` e template reais somente quando estiverem
configurados no repositório para aquele alvo. **Não inventar IDs.** Quando algum
valor não existir, escreva `CONFIG_REQUIRED` e, logo depois da ficha, registre:
"Preencher com o ID real configurado no projeto."

A linguagem é `pt-BR`; `aspect_ratio` da HeyGen é `16:9`; a voz deve ser serena, próxima, profissional e sem
teatralização. Não invente `speed` se o valor não estiver configurado. O texto
de `## FALA EXATA` é o único texto enviado ao avatar: não coloque instruções,
títulos ou observações dentro dele.

### Timeline

Divida a fala em segmentos sem alterar nenhuma palavra. Calcule os tempos pela
quantidade real de palavras e por uma velocidade natural de português falado;
não distribua tempos arbitrariamente. O fim do último segmento deve coincidir
com a duração total estimada. Cada segmento deve apontar para exatamente uma
imagem Agnes.

Headline tem no máximo duas linhas; overlay, no máximo uma frase curta. Não
exiba mais de 7–9 palavras simultaneamente e não copie literalmente a fala.
Priorize leitura em celular.

### Intenção visual e adaptação Agnes

Escreva a intenção uma vez em inglês, em prosa descritiva FLUX, com 30–80
palavras e na ordem sujeito → cenário → detalhes → iluminação → atmosfera.
Defina sujeito, ação observável, ambiente, enquadramento, fonte, qualidade,
direção e temperatura da luz e estética editorial. Não use boosters vazios como
`masterpiece`, `8k`, `ultra detailed` ou equivalentes. Preserve em
`continuity_notes` personagem, roupa, paleta e iluminação quando houver
continuidade entre imagens.

Para cada intenção, escreva duas adaptações em inglês, sem mudar o conteúdo:

- `prompt_instagram`: composição para a faixa visual do reel 9:16, com assunto
  principal centralizado e seguro para o recorte definido pelo template;
- `prompt_youtube`: composição 16:9, 1920×1088, usando a largura narrativa sem
  deslocar o assunto essencial para as bordas.

O renderizador, e não o modelo de texto, decide os pixels finais. A Agnes recebe
a adaptação do canal e o adaptador normaliza o resultado sem esticar.

Imagens devem ser anatomicamente plausíveis, adultas e não sensacionalistas.
Não representar diagnóstico, cura, pulmão “sujo/limpo”, aura ou energia mágica.
Todo `negative_prompt` deve proibir ao menos texto, marca-d'água, sofrimento
dramático, ambiente hospitalar desnecessário e símbolos espirituais.
Como a rota de imagem não possui campo negativo independente neste projeto, o
adaptador incorpora essas restrições ao prompt como `Avoid:`.

### CTA e saúde

O CTA deve coincidir com o sufixo: não comercial em ALC, leve em AUT e conversão
para o WhatsApp em PRO. A frase falada do CTA precisa aparecer também, sem
divergência, no fim de `## FALA EXATA` e no último segmento da timeline.

Em `## HEALTH COMPLIANCE`, todos os campos devem ser `false`. Se o roteiro
contiver diagnóstico, resultado garantido, cura, causalidade sem evidência,
substituição de cuidado médico ou medo como argumento, corrija-o antes de
entregar. Bloqueie expressões como “você respira errado”, “isso causa sua
ansiedade”, “cure”, “elimine”, “desbloqueie” e “resultado garantido”.

## Formato de saída obrigatório

Cada `<alvo>.md` deve conter exatamente esta estrutura e todos os campos:

```text
# VIDEO SPEC

ID:
TIPO:
PÚBLICO:
OBJETIVO:
ESTÁGIO:
DURAÇÃO:
PLATAFORMAS: Instagram Reels; YouTube
FORMATOS: Instagram 9:16; YouTube 16:9
CTA:

## HEYGEN

avatar:
voice:
language: pt-BR
voice_style: sereno, próximo, profissional, sem teatralização
speed:
template:
aspect_ratio: 16:9
background:
caption_style:

## FALA EXATA

<texto exato enviado ao HeyGen>

## TIMELINE

### SEGMENTO 1
start:
end:
duration:
fala:
visual_agnes: IMAGE 1
headline:
overlay_text:
transition:

### SEGMENTO 2
...

## VISUAL INTENTS

### IMAGE 1
segment: 1
duration:
aspect_ratio_instagram: template_defined
aspect_ratio_youtube: 16:9
prompt_en:
prompt_instagram:
prompt_youtube:
negative_prompt:
continuity_notes:

### IMAGE 2
...

## CTA

spoken:
onscreen:
button_or_caption:
destination:

## HEALTH COMPLIANCE

diagnostic_claims: false
guaranteed_results: false
disease_cure_claims: false
causal_claims_without_evidence: false
medical_replacement_claims: false
fear_based_copy: false

## VALIDATION

speech_duration_matches_timeline:
all_segments_have_visual:
all_visuals_have_prompt:
all_segments_have_headline_or_overlay:
cta_matches_funnel_stage:
health_rules_passed:
ready_for_agnes:
ready_for_heygen:
```

Todos os itens de `## VALIDATION` devem ser `true`. Se qualquer item seria
`false`, corrija o roteiro antes de gravar o arquivo. `ready_for_heygen` só pode
ser `true` quando avatar, voz e template forem reais; se houver
`CONFIG_REQUIRED`, mantenha esse item `false` e declare a lacuna no resumo. Essa
é a única exceção permitida à regra de corrigir antes de entregar, pois IDs
nunca podem ser inventados.

## Saída

Grave em `{{pasta}}/<alvo>.md` e o resumo em
`{{pasta}}/resumo-estrategico.md`.

Faça `git add` dos arquivos gerados e um único commit no repositório onde
`{{pasta}}` fica, com autor `inematds <inematds@gmail.com>` e mensagem curta
descrevendo o assunto. Não faça push.

Ao terminar, grave em `{{saida}}` um resumo curto, com um alvo por linha e o
caminho do respectivo arquivo. A fala completa permanece nos arquivos Markdown.
A última linha da resposta deve ser exatamente:

```text
RESULT: {{saida}}
```

Em caso de bloqueio factual:

```text
ERRO: <motivo curto>
```
