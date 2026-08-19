# C#81 — resumo estratégico

## ESSÊNCIA (o que este conteúdo É)

O assunto propõe que, com modelos como GPT-5.6 e Opus 5 — bons o bastante em
instruction-following para sustentar comportamentos combinados de forma
consistente — comandos nomeados e específicos (`/truth`, `/gaps`, `/pushback`,
`/rank`, e famílias maiores como `/verify`, `/challenge`, `/decide`,
`/blueprint`, `/redteam`...) funcionam quase como uma linguagem de programação
para raciocínio com IA. O exemplo dado é: alguém pensando em criar uma
comunidade paga de médicos interessados em IA, e a sequência de comandos
fazendo o trabalho de checar a realidade, achar lacunas, atacar a própria
tese, comparar alternativas e recomendar. O texto explicitamente NÃO propõe
"100 prompts secretos" — propõe uma convenção clara, uma DSL de comandos, algo
que qualquer um pode adotar porque tem especificação por trás. Não fala de um
produto, não promete resultado financeiro, não é lista fechada.

## Assunto (fonte)

Texto argumentativo sobre criar uma "INEMA Command Language" — convenções de
prompt tipo comando (`/truth /gaps /pushback /rank`) que, encadeadas, guiam o
raciocínio da IA em etapas (realidade → lacunas → ataque à tese → comparação →
recomendação), indo além dos 5 comandos iniciais para famílias mais amplas.

## Tese central

"Pedido vago recebe resposta vaga; comando específico obriga a IA a fazer o
trabalho difícil que você evitaria sozinho."

## Motivo para assistir agora

Modelos atuais (GPT-5.6, Opus 5) seguem instrução bem o bastante para sustentar
esse comportamento de forma consistente — relevância prática confirmada no
assunto, sem data ou prazo fabricado.

## Elemento demonstrável

A sequência de comandos aplicada a uma decisão real dada no assunto — "quero
criar uma comunidade paga de médicos interessados em IA" — e o que cada
comando faz aparecer: o cheque de realidade, a lacuna que a pessoa não via, o
ataque à própria ideia, a comparação de alternativas, a recomendação final.

## Diferenciação por público (gancho / estrutura / CTA)

Os 36 arquivos estão em `textos/C81/<alvo>.md`. Cada público tem dor e gatilho
próprios (tabela da skill `inemaclub-textos`), e dentro de cada público os
três tipos variam:

- **-alc**: formato de alcance puro (afirmação provocativa, pergunta
  incômoda, mito x realidade, etc.) — não menciona nada de curso ou marca,
  ideia única, CTA de comentário/compartilhamento.
- **-aut**: ensina algo concreto e demonstrado, termina com princípio
  repetível, CTA de salvar/seguir/testar.
- **-pro**: dor → consequência de não agir → primeiro passo nomeado, sem
  produto, CTA de compromisso público — nesta variante viral, também sem
  marca (a regra do topo do assunto vence sobre o `fecho` padrão do alvo).

Todos os 36 aplicam a mesma tese central, adaptando gancho, cena da regra 15
(pessoa concreta) e exemplo à dor específica do público.

## Riscos e pontos que pedem revisão humana

- **Consistência de tom entre os 4 lotes gerados em paralelo** — cada grupo de
  9 arquivos (3 públicos × 3 tipos) foi escrito por um agente diferente com o
  mesmo briefing; vale conferir se o registro de voz não varia demais entre
  lotes antes de aprovar em série.
- **Ganchos de 9 palavras** — checar manualmente os 36 primeiros trechos de
  FALA quanto ao limite e à ausência de saudação/"você sabia".
- **Regra 15 (pessoa concreta, sem testemunho em 1ª pessoa)** — checar que
  nenhum roteiro deslizou para "outro dia eu vi um aluno..." como se fosse
  relato pessoal.
- **Prompts de IMAGEM 1 (capa)** — conferir se de fato fogem dos clichês
  proibidos (perfil com holograma, HUD, matrix, robô apertando mão, lâmpada)
  e se mostram consequência/tensão, não só o tema.
- **Engajamento único e nomeado na fala** — nos formatos de escolha binária,
  checar se as duas opções estão de fato literalmente nomeadas na FALA.
- **Repetição entre `-alc`/`-aut`/`-pro` do mesmo público** — checar
  amostralmente que gancho, estrutura e fecho não colidem.

Aprovação segue o portão humano padrão: `/aprovar C81`.
