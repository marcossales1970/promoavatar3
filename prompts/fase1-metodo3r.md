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

O Método 3R significa Respirar, Reeducar, Restaurar. Cássia Saito é professora
de Yoga especialista em respiração. O serviço central é avaliação respiratória
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

## Imagens e sobreposições

Depois da fala, escreva `### SOBREPOSIÇÕES`, com ATENÇÃO, RETENÇÃO, PROVA,
ENGAJAMENTO e CTA. Depois escreva `## IMAGENS`, uma imagem por segmento:

```text
IMAGEM <N> — "<início exato do segmento>" [função]
headline: <até duas linhas curtas>
hook: <frase curta; {uma palavra-chave}>
<prompt visual em inglês, sem texto dentro da imagem>
```

Imagens devem ser anatomicamente plausíveis, adultas e não sensacionalistas.
Não representar diagnóstico, cura, pulmão “sujo/limpo”, aura ou energia mágica.

Finalize cada arquivo com `## ESTRUTURA`, registrando tese, função, prova, CTA,
gancho escolhido e mudança esperada na compreensão da pessoa.

## Saída

Grave em `{{pasta}}/<alvo>.md` e o resumo em
`{{pasta}}/resumo-estrategico.md`. A última linha da resposta deve ser:

```text
RESULT: {{pasta}}
```

Em caso de bloqueio factual:

```text
ERRO: <motivo curto>
```

