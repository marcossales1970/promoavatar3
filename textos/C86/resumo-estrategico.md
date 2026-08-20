# C#86 — Resumo estratégico

## 0. Essência do conteúdo

O assunto pedido foi: "quero ensinar as pessoas a fazer projetos". Interpretado
dentro do inema.club, isso é uma proposta de FORMAÇÃO PRÁTICA em IA: não ensinar
a usar mais uma ferramenta, mas ensinar a CONSTRUIR algo real do início ao fim —
um app, uma automação, um sistema simples — usando IA como meio, não como fim.
Fala para qualquer pessoa disposta a sair do "testar prompt" e chegar numa
primeira versão funcional em poucos dias. Não é um curso de programação
tradicional, não promete emprego garantido, não é sobre uma ferramenta
específica.

## Tese central (a mesma para os 36 vídeos)

"Aprender a FAZER PROJETOS com IA — não só usar ferramentas — é o que separa
quem fica obsoleto de quem vira mais valioso."

## Motivo para assistir agora

A maioria das pessoas só testa ferramentas soltas (pergunta pro chatbot, copia,
esquece) e nunca constrói nada que funcione até o fim. Esse é o gargalo real —
não é falta de acesso à IA, é falta do hábito de terminar um projeto.

## Elemento demonstrável

A tela de um projeto sendo construído passo a passo: um app, uma automação ou
um sistema simples nascendo em etapas visíveis (problema → fluxo → primeira
versão rodando). Cada roteiro adapta esse elemento ao contexto do público
(plano de aula para educadores, atendimento para empreendedores, pipeline/agente
para técnicos, portfólio para recolocação, etc.).

## Como os 3 tipos se diferenciam, por público

Em todos os 12 públicos, o padrão se repetiu de forma consistente:

- **-alc**: aponta o ERRO comum (testar ferramenta ≠ construir projeto) sem
  citar a marca, sem ensinar o "como", termina em convite a comentar/compartilhar.
  Nenhum -alc tem CTA comercial.
- **-aut**: ENSINA o método/mecânica de fato (passos concretos até a primeira
  versão funcional), demonstra autoridade sem declará-la, fecha num princípio
  repetível, CTA de salvar/seguir — sem venda direta.
- **-pro**: segue dor específica → consequência → solução NOMEADA → benefício →
  CTA único e comercial para "a trilha de IA do seu perfil no inema.club", com
  a promessa calibrada (5 dias, primeira versão funcional — nunca "sistema
  completo" nem promessa de emprego/renda garantida).

Detalhe por público (gancho de cada tipo):

- **40mais**: alc "erro que custa a vaga, não é idade" · aut "diferença entre
  usar e construir com IA" · pro "colega mais novo entrega projeto pronto".
- **60mais**: alc "problema não é a idade" · aut "duas coisas decidem se você
  aprende rápido depois dos 60" · pro "aposentadoria não vai esperar você
  aprender sozinho".
- **criadores**: alc "erro não é qual ferramenta" · aut "automação de conteúdo
  tem uma ordem, a maioria inverte" · pro "o que esgota não é postar todo dia".
- **educadores**: alc "seu aluno já usa IA melhor que você" · aut "o erro não é
  usar IA, é usar solta" · pro "sua noite de domingo virou plantão de correção".
- **empreendedores**: alc "testa ferramenta atrás de ferramenta, nada sai do
  lugar" · aut "todo projeto de IA que funciona passa pelas mesmas 3 etapas" ·
  pro "a fatura da agência chega todo mês, o projeto ainda não".
- **familia**: alc "nenhuma escola faz essa pergunta pro seu filho" · aut
  "duas formas de ensinar seu filho sobre IA" · pro "existe um jeito de blindar
  o futuro dele".
- **jovens**: alc "erro que quase todo jovem comete com IA" · aut "ideia boa
  sozinha não vira renda, vira projeto quando alguém termina" · pro "toda vaga
  de primeiro emprego pede experiência que ninguém dá chance de ter".
- **mulheres**: alc "testar ferramenta não é a mesma coisa que saber usar IA" ·
  aut "um projeto com IA quebra em 3 partes, você só treina uma" · pro "entre
  trabalho, casa e tudo mais, sobra pouco tempo".
- **pessoacomum**: alc "a maioria usa IA do jeito mais fraco possível" · aut
  "tem uma habilidade que ninguém te ensinou: terminar um projeto" · pro "cinco
  dias separam você do seu primeiro projeto de verdade".
- **profissionais**: alc "testar ferramenta de IA não é saber trabalhar com
  IA" · aut "sinal simples pra saber se você só usa ou sabe construir com IA" ·
  pro "você vê a IA avançando e sente que sua cadeira pode ficar menor".
- **recolocacao**: alc "erro que quase todo mundo comete procurando emprego" ·
  aut "diferença entre saber usar uma ferramenta e saber construir com ela" ·
  pro "atualiza o currículo, manda pra mais uma vaga, resposta não vem".
- **tecnicos**: alc "erro que quase todo técnico comete com IA" · aut "isso
  aqui não é mais um tutorial de prompt" · pro "ninguém contrata quem só sabe
  testar ferramenta".

## Riscos de repetição / pontos para revisão humana

- **Padrão de abertura repetido entre públicos** ("tem um erro que...", "erro
  não é..."): dentro de CADA público os 3 tipos não se repetem (checado), mas
  vários `-alc` de públicos diferentes usam a mesma família de gancho ("erro
  comum"). Isso é aceitável porque o formato foi escolhido de forma
  independente por 12 agentes em paralelo — vale revisar se, publicados juntos,
  soam repetitivos entre si e variar 3-4 deles manualmente antes de gravar.
- **CTA genérico**: todos os `-pro` usam o CTA-safe "a trilha de IA do seu
  perfil no inema.club" (nenhum nome de curso específico do catálogo foi citado,
  por segurança — nenhum agente tinha certeza de qual curso do catálogo casava
  melhor com "projetos"). Se houver uma trilha específica de projetos práticos
  no catálogo, considerar substituir manualmente antes de gerar os avatares.
- **Público `familia`**: os roteiros falam para o pai/mãe sobre formar o filho
  — conferir se a cena do filho em 2ª pessoa/hipótese soa natural e não como
  depoimento (regra 15 do CLAUDE.md), já que é o público mais sensível a esse
  risco.
- **Público `recolocacao`**: dor é urgente de verdade (falta de renda); checar
  que nenhum `-pro` deslizou para promessa de emprego/renda (proibido).
- Cada um dos 36 arquivos tem sua própria linha `Ganchos descartados:` com o
  porquê das 4 opções descartadas na oficina de gancho — útil para quem revisar
  querer um ângulo diferente do já escolhido.

## Geração

36 arquivos gerados em paralelo (12 agentes, um por público, 3 alvos cada).
Nenhum vídeo foi gerado — esta fase termina nos textos; avatar e reel dependem
de revisão humana (`/aprovar C86`).
