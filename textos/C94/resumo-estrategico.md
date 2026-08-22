# C#94 — resumo estratégico (variante viral)

## ESSÊNCIA (o que o assunto afirma, fielmente, antes de qualquer opinião)

O INEMA.club é apresentado como uma plataforma gratuita, **sem cadastro**, para
aprender IA de forma **prática** — não "ouvir falar de IA", mas aprender a
criar, automatizar, construir e usar IA no mundo real. A mensagem institucional
do assunto é: democratizar o acesso à IA prática, sem barreira, sem promessa
milagrosa, para quem quer aprender a fazer coisas reais. O posicionamento
central que o texto propõe: "INEMA.club não vende IA. Ensina você a usar IA." E
a frase de campanha mais forte do próprio assunto: "O mundo está aprendendo IA.
Você pode começar agora. Grátis. Sem cadastro."

O que este conteúdo NÃO é: não é uma promessa de emprego ou renda garantida;
não é "curso completo definitivo"; não é uma crítica a quem vende curso pago
(o assunto não ataca concorrência, só afirma um caminho gratuito que existe);
não é conteúdo institucional de "sobre nós" — é convite direto a agir agora.

## Assunto (resumo)

Reposicionamento de mensagem do INEMA.club: a promessa não é "compre algo", é
"venha aprender aqui, de graça, sem cadastro, sem enrolação". Núcleo: acesso
livre ao conhecimento necessário para não ficar para trás na era da IA.

## Tese central

"Você não precisa comprar curso nem se cadastrar em lugar nenhum para aprender
IA de verdade — o acesso livre já existe, só falta você usar."

## Motivo para assistir agora

Todo mundo fala de IA; poucos ensinam de graça e na prática. Quem só ouve
falar (ou só assiste vídeo sobre o assunto) fica para trás de quem já está
fazendo. Não há elemento de urgência temporal no assunto — a relevância é
prática, não um relógio.

## Elemento demonstrável

A cena de entrar num lugar de aprendizado SEM formulário de cadastro, sem
pedir cartão, sem senha — e já estar dentro do conteúdo. Usada como PROVA nas
sobreposições da maioria dos roteiros.

## Decisão de variante: por que a marca não aparece na fala

A regra da variante viral proíbe "inema.club", curso e marca na FALA em
qualquer um dos três tipos — inclusive o `-pro`, que aqui também é de alcance
puro. Isso criava tensão com um assunto que É sobre o INEMA.club. A saída:
cada roteiro ataca o COMPORTAMENTO por trás da mensagem — a barreira artificial
entre "aprender IA de verdade" e "só ouvir falar de IA", ou o hábito de esperar
comprar algo pra começar — sem nomear a marca. O clipe de encerramento com a
marca (3s, injetado pelo pipeline) é quem fecha a associação; o roteiro não
precisa fazer esse trabalho.

## Como os três tipos se diferenciam, por público

Em todos os 12 públicos, o padrão seguido foi:
- **-alc**: formato de alcance puro (afirmação provocativa, pergunta incômoda,
  mito vs realidade, etc.), gancho emocional forte, engajamento de escolha
  binária ou marcação — vídeo pensado pra quem nunca ouviu falar da marca.
- **-aut**: ensina algo concreto e demonstrável sobre a barreira entre "ouvir
  falar" e "fazer" — autoridade demonstrada, não declarada; fecha com um
  princípio repetível.
- **-pro**: liga a dor específica do público a um primeiro passo nomeado e
  concreto de hoje, sem produto — CTA de compromisso público predominante.

Cada arquivo registra no topo (`Tipo:`, `Formato escolhido:`, ganchos
descartados e a emoção-gatilho vencedora) a decisão específica daquele vídeo.

## Riscos de repetição / pontos de atenção para revisão humana

- **Convergência de PROVA**: como o elemento demonstrável (tela sem cadastro)
  é o mesmo para os 33 vídeos, há risco real de vários usarem a mesma imagem
  de "formulário vazio" ou "tela sem senha" — checar diversidade visual entre
  públicos antes de aprovar, não só dentro do mesmo público.
- **Tentação de prometer emprego/renda**: mais forte nos públicos
  `recolocacao`, `40mais`, `60mais`, `jovens` — os agentes foram instruídos a
  evitar, mas é o ponto onde a variante mais tende a escorregar. Reler a FALA
  desses públicos com atenção redobrada.
- **Testemunho inventado**: a regra de "pessoa concreta, não depoimento" foi
  reforçada em todos os prompts, mas especialmente em `familia` (risco de citar
  fala do filho como se fosse real) e `educadores`/`empreendedores` (risco de
  "caso que um aluno/cliente me contou").
- **Geração distribuída em 12 agentes paralelos**: cada um só viu o próprio
  público, não os demais — não houve verificação cruzada de que os ganchos de
  diferentes públicos não soem repetitivos entre si (ex.: dois públicos usando
  a mesma estrutura de "escolha binária 1 ou 2" com frase quase idêntica).
  Vale uma leitura rápida em sequência antes de aprovar o lote inteiro.
- **IMAGENS**: os 33 arquivos têm `headline` e `hook` em todos os segmentos
  (checado automaticamente), mas o conteúdo visual em si (clichês proibidos,
  qualidade da provocação da IMAGEM 1) não foi auditado por segmento — revisão
  humana no portão antes de renderizar continua sendo o filtro real.

## Públicos e alvos (36 arquivos, 12 públicos × 3 tipos)

40mais, 60mais, criadores, educadores, empreendedores, familia, jovens,
mulheres, pessoacomum, profissionais, recolocacao, tecnicos — cada um com
`-alc`, `-aut`, `-pro` em `textos/C94/<alvo>.md`.
