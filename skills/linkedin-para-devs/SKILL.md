---
name: linkedin-para-devs
description: Melhora o LinkedIn de desenvolvedores de ponta a ponta, com base em fatos. Junta evidências (repositórios no GitHub, documentos), diagnostica o perfil e escreve o plano campo a campo (título/headline, Sobre/About, experiências, projetos, competências/skills, destaques/featured, perfil em inglês). Aplica pelo navegador, se o usuário aprovar. Monta o plano de rede com SSI (Social Selling Index), textos prontos de convite, validação/endorsement e recomendação, ideias de post técnico e uma lista curada de recrutadores. Use sempre que o usuário falar de LinkedIn, perfil profissional, headline, About, experiências, recrutadores ou tech recruiters, Open to Work, networking, convites, conexões, SSI, validações, recomendações, posts técnicos ou marca pessoal (personal branding). Use também quando ele quiser procurar emprego ou vaga como dev, se recolocar ou ser achado por recrutadores, mesmo sem citar o LinkedIn. Não escreve CV nem faz candidaturas.
---

# LinkedIn para devs

Este é um processo completo para um desenvolvedor melhorar o LinkedIn com base em fatos. Ele cobre evidências, diagnóstico, plano do perfil, aplicação opcional pelo navegador, plano de rede e de vagas, textos prontos, ideias de post e recrutadores. Tudo vira arquivo Markdown, que o usuário guarda e segue no dia a dia.

Os caminhos `references/...` e `scripts/...` desta página ficam no diretório base desta skill, não no diretório de trabalho.

## Como trabalhar

- **Você prepara, o usuário envia.** Convites, mensagens, posts, pedidos de recomendação e o "Open to work" falam em nome dele. Deixe tudo pronto para colar. Quem clica em enviar é ele, porque é o nome dele que vai junto. Se ele pedir que você envie convites pelo navegador, envie só os da lista e com o texto que ele aprovou, um a um (`references/aplicar-no-navegador.md`, seção "Enviar convites (só com lista e texto aprovados)").
- **Nenhum número sem fonte.** Cada métrica aponta para um commit, um arquivo, um documento ou uma resposta do usuário. Número inventado cai na primeira entrevista e mancha o resto do perfil. Sem fonte, pergunte ou deixe fora.
- **Não infle.** Bolsa não é emprego. Contribuição pequena é descrita como pequena. Em projeto de terceiros, diga exatamente a parte do usuário (só o front, pair programming, validação etc.).
- **Exija a evidência mínima.** Para cada experiência: cargo, datas e vínculo confirmados pelo usuário, mais pelo menos 1 entrega descrita por ele. Sem isso, entregue um esqueleto marcado como rascunho, com [colchetes] e _a confirmar_ nos buracos, e a lista de perguntas. Texto escrito sem fato sai genérico ou errado.
- **Dê um ganho rápido.** Se o pedido for vago ("melhora meu LinkedIn"), a 1ª resposta traz as perguntas da fase 0 **e** um rascunho de título com o que o usuário já disse, marcado como provisório. Ele vê o rumo antes de responder tudo. Se ele não disse nem cargo nem stack, mostre a fórmula ao lado do título da Ana, a persona fictícia de `references/perfil-campo-a-campo.md` (seção "Exemplo curto (inventado)"), e diga as 3 respostas que destravam o título dele: cargo-alvo, stack e alvo.
- **Conte caracteres com o script, não de cabeça.** O diretório de trabalho não é a pasta da skill, então caminho relativo falha. Use o caminho absoluto: `python3 <diretório base desta skill>/scripts/contar.py`. Ele recebe um arquivo ou o texto pela entrada padrão e usa `len()` do Python, em que a quebra de linha conta 1. Passe o limite com `--limite`; os nomeados são `titulo` (220), `sobre` (2600), `convite` (200), `mensagem` (500, teto desta skill para mensagem direta: validação, recomendação e pós-aceite), `posicao` (2000) e `projeto` (2000). Acima do limite, o formulário corta o texto ou não deixa salvar, e texto cortado passa impressão de descuido. Contagem feita com [colchetes] é provisória: refaça depois de preencher.
- **Siga a ordem, mas deixe o usuário pular.** Se ele quer só o título, faça só o título, com uma fase 1 curta. Se quer só recrutadores, vá direto à fase 6.
- **Escreva no idioma do usuário.** Os arquivos saem em português se a conversa for em português. O perfil no segundo idioma entra na fase 3.
- **Mostre e espere.** Ao fim das fases 2, 3 e 6, mostre o resultado e espere o OK antes de seguir. Cada fase usa a anterior como base. Se o Diagnóstico não tem nada em Errado, siga para a fase 3 e mostre os dois juntos, com um OK só.

## Visão geral

| Fase | Objetivo | Entrega | Leia antes |
|---|---|---|---|
| 0. Combinar | perfil atual, situação, alvo, prazo, tempo e o que é privado | seção "Contexto" no `linkedin.md` | nada |
| 1. Evidências | fatos com fonte | fichas de evidência | `references/evidencias.md` |
| 2. Diagnóstico | o que está errado, fraco ou vazio | "Diagnóstico" e "Resumo do que muda", no topo do `linkedin.md` | `references/aplicar-no-navegador.md`, só se for ler pelo navegador |
| 3. Plano do perfil | textos prontos, campo a campo | `linkedin.md` | `references/perfil-campo-a-campo.md` |
| 4. Aplicar (opcional) | editar o perfil item a item | "Status da aplicação" no `linkedin.md` | `references/aplicar-no-navegador.md` |
| 5. Rede e SSI | plano semanal, textos, posts e funil de vagas | `rede-linkedin.md` | `references/rede-e-ssi.md` e `references/textos-modelo.md` |
| 6. Recrutadores | lista curada para convidar | `recrutadores.md` | `references/recrutadores.md` e `scripts/extrair_busca.js` |
| 7. Checklist | o que fazer em cada dia | `checklist.md` | `references/rede-e-ssi.md`, seção "Modelo do `checklist.md`" |

Salve os arquivos onde o usuário escolher, de preferência num repositório privado. O `recrutadores.md` tem dados de terceiros, e o `linkedin.md` costuma ter contexto que não é público.

## Fase 0: Combinar

**Objetivo:** alinhar o essencial antes de escrever qualquer coisa.

Pergunte tudo numa mensagem só. Cada rodada a mais atrasa o trabalho e cansa o usuário. As fases seguintes usam estas respostas e não perguntam de novo sobre estes pontos.
- **Perfil atual:** o PDF (no perfil, Mais > Salvar como PDF) ou o texto colado. É a base do diagnóstico.
- **Situação hoje:** está empregado? Onde? Pode citar o empregador e postar sobre ele? Post sobre o trabalho atual pede o OK da chefia antes; na busca discreta, o próprio pedido denuncia, e os posts ficam em temas de fora do empregador.
- **Busca discreta?** Se for, o "Open to work" fica visível só para recrutadores, o título não leva "aberto a", o Sobre usa uma frase neutra, o compartilhamento com a rede fica desligado e os pedidos de validação e recomendação vão só para quem não está na empresa atual. Assim o empregador não descobre pelo perfil.
- **Alvo:** Brasil ou exterior, e o idioma principal do perfil. O inglês vale o esforço se ele busca vaga remota internacional.
- **Prazo e objetivo:** uma data e o que ele quer até lá. Se for vaga, qual: área, senioridade, CLT ou PJ, remoto ou presencial (e em que região). No exterior: contractor (PJ) ou EOR, fuso aceitável e se mudaria de país. O plano de rede é montado semana a semana até o prazo.
- **Vagas-alvo:** 3 a 5 vagas que ele quer (o link ou o texto). O título e o Sobre usam as palavras delas.
- **GitHub e links:** o usuário do GitHub e os links dos projetos no ar. Para quem é júnior, a prova está aí.
- **Tempo real por dia:** o plano cabe no tempo que ele tem, não no ideal.
- **O que é privado:** projetos que não podem aparecer, nomes de clientes, números confidenciais.
- **Onde salvar** os arquivos.
- **Navegador** (só se a sessão tem uma ferramenta de navegador): se o LinkedIn está logado e se ele quer que você aplique as edições ou prefere colar sozinho.

**Entrega:** as respostas, numa seção "Contexto" no fim do `linkedin.md`.

Um projeto que o usuário pede para tirar fica fora de todo canal: perfil, posts, mensagens e exemplos.

## Fase 1: Evidências

**Objetivo:** ter fatos com fonte antes de escrever o primeiro texto. Texto sem evidência vira adjetivo. Com evidência, vira entrega.

**Leia `references/evidencias.md` agora.** Ela traz os comandos e o formato das fichas. Em resumo:
- **Repositórios:** `gh repo list` do usuário e das organizações e clone parcial. Depois, `git log --author` com todas as identidades dele, inclusive as variações com erro de digitação. Daí saem o período, a stack e o que ele fez de fato. Se houver repositório do empregador, pergunte antes se a política da empresa deixa clonar na máquina pessoal.
- **Sem repositório acessível** (código privado, comum em sênior): a ficha sai do relato do usuário e de documentos. A referência traz as perguntas.
- **Documentos:** certificados, diplomas e publicações. Confira o DOI, as páginas e os autores numa fonte pública, como Crossref e ORCID.
- **Perguntas ao usuário:** o papel em cada projeto e os números de impacto (usuários, pagantes, pedidos por dia). Só ele sabe isso. Na mesma rodada, para a fase 5: quem já topou recomendar e quem pode validar o quê.

**Entrega:** fichas de evidência, no formato da referência. Cada número que for para o perfil aponta para uma delas.

## Fase 2: Diagnóstico

**Objetivo:** saber o que mudar e em que ordem.

Leia o perfil atual: título, Sobre, experiências, formação, competências, destaques, seções vazias e posts recentes. Use as fontes nesta ordem:
1. **O PDF ou o texto colado** que veio na fase 0.
2. **Com navegador, as páginas `/in/<vanity>/details/<secao>/`** (por exemplo `experience`, `projects`, `skills`). A página principal do perfil às vezes não renderiza as seções de baixo.
3. **A API interna (voyager)**, só como alternativa e depois de avisar o usuário. Ela usa o token de sessão dele: nunca mostre, grave nem registre esse token. Os detalhes estão em `references/aplicar-no-navegador.md`.

Classifique cada ponto em três listas:
- **Errado:** datas, vínculos, cargos e nomes trocados. Corrija primeiro, porque um dado errado tira a confiança no resto.
- **Fraco:** texto genérico, sem entrega e sem resultado.
- **Vazio:** seções que ajudariam e não existem, como projetos, destaques, perfil em inglês e competências.

Cruze com as evidências. Tudo que a evidência mostra e o perfil não mostra é oportunidade.

**Entrega:** a seção "Diagnóstico", com as três listas, e o "Resumo do que muda", tirado delas, no topo do `linkedin.md`. Mostre ao usuário antes de seguir.

## Fase 3: Plano do perfil

**Objetivo:** ter todo o texto do perfil pronto para colar, na ordem em que vai ser aplicado.

**Leia `references/perfil-campo-a-campo.md` antes de escrever.** Ela traz o modelo de cada seção e os limites de caracteres.

**Entrega:** o `linkedin.md`, nesta ordem:
1. **Correções urgentes:** os dados errados.
2. **Título e Sobre:** título de até 220 caracteres e Sobre de até 2.600. O gancho, de até cerca de 200 caracteres, abre o Sobre: é o que aparece antes do "ver mais".
3. **Experiências, campo a campo:** cargo, tipo de emprego, datas, local e modalidade. Na descrição, use verbo + o quê + resultado com fonte. Indique até 5 competências por item.
4. **Seções novas:**
   - projetos, publicações e certificados que pesam;
   - prêmios, voluntariado, organizações e formação;
   - competências: as 5 principais fixadas, alinhadas ao título, e até cerca de 30 em ordem de prioridade, cada uma com a evidência;
   - destaques: 3 ou 4, e o 1º é o produto que se pode clicar.
5. **Perfil no segundo idioma:** headline, About e as experiências principais. Use o idioma principal combinado na fase 0. Se o alvo é o exterior, escreva o inglês junto com o português, seção a seção, e não por último: é ele que o recrutador de fora lê.
6. **Rede e visibilidade:** um resumo, com recomendações, Open to work, posts e calendário. O detalhe fica no `rede-linkedin.md`.

**Júnior ou 1º emprego:** Projetos e Destaques viram a etapa 3, e as Experiências passam para a 4, porque a prova está nos projetos (ver a seção "Júnior ou primeiro emprego" da referência).

Logo abaixo do cabeçalho, antes do "Diagnóstico", abra a seção "Status da aplicação", que a fase 4 vai atualizar. É a posição do modelo em `references/perfil-campo-a-campo.md` (seção "Modelo do `linkedin.md`"), porque é o que o usuário lê primeiro quando volta ao arquivo. Cada texto fica num bloco de código, com a contagem ao lado, por exemplo "(204/220)".

Deixe fora o que é sensível: segredos, IPs, nomes de clientes internos e detalhes de segurança que alguém poderia explorar. O perfil e os posts falam de padrão e decisão, não de configuração.

Peça ao usuário para revisar. O plano aprovado é o contrato da fase 4.

## Fase 4: Aplicar (opcional)

**Objetivo:** levar o plano aprovado para o perfil, sem efeito colateral.

Só faça esta fase se o usuário pedir e houver uma ferramenta de navegador. **Leia `references/aplicar-no-navegador.md` inteira antes do primeiro clique.** A interface tem armadilhas que já causaram duplicatas e competências erradas.

**Antes de começar:**
- O login é do usuário. Se a sessão cair, peça para ele entrar.
- Combine o escopo de forma explícita, por exemplo "aplique as etapas 1 a 5". Qualquer coisa fora dele, pergunte antes.

**Durante a aplicação:**
- Desligue o "compartilhar com a rede" em todas as edições, a menos que o usuário peça. Sem isso, cada salvamento vira uma notificação para os contatos.
- Recuse as ofertas do LinkedIn: compartilhar, pedir recomendação e assinar o Premium.
- Confira antes de criar um item e de novo depois de salvar, pela página `/details/<secao>/` ou, depois de avisar o usuário, pela API interna. A tela principal do perfil não é confiável.
- No autocompletar, liste as opções e escolha a que bate exatamente.
- Confira os valores antes de salvar.
- Exclua só com pedido explícito, item a item. Se você criar uma duplicata, registre o erro e pergunte o que fazer.
- Pare e devolva o controle ao usuário diante de captcha, verificação de segurança, pedido de senha ou termos para aceitar.

**Entrega:** a seção "Status da aplicação" atualizada, com três listas:
- o que foi aplicado, com a data;
- o que ficou com o usuário;
- os seus erros e o que ele precisa desfazer.

Se houver memória disponível, salve as armadilhas novas que encontrar. A interface muda, e a próxima sessão agradece.

## Fase 5: Rede e SSI

**Objetivo:** transformar o perfil novo em alcance e, se o objetivo for vaga, em conversas e entrevistas até o prazo.

A skill cuida da presença no LinkedIn e do funil básico de vagas. Ela não escreve CV nem faz candidaturas: isso fica com o usuário.

**Leia `references/rede-e-ssi.md`** (SSI, plano, rotina, limites e posts) **e `references/textos-modelo.md`** (textos prontos). Use o prazo, o alvo e o tempo por dia da fase 0.

**Entrega:** o `rede-linkedin.md`, com:
- **Linha de base:** conexões, validações, recomendações e as métricas do `/dashboard/` (impressões, seguidores, visualizações do perfil e aparições em buscas). Sem navegador, peça ao usuário esses números no 1º dia. Inclua o SSI, se a conta ainda mostrar. Se não mostrar, meça o progresso pelas métricas; estimar os 4 pilares é opcional quando o objetivo é vaga.
- **Plano semana a semana até o prazo:** metas acumuladas, com as premissas escritas como premissas. A partir da 2ª semana, troque cada premissa pelo dado real.
- **Funil de vagas, se o objetivo for vaga:** alertas de vaga, candidaturas, conversas com recrutador e entrevistas, cada um com meta semanal, mais as preferências de vaga do "Open to work". Conexão sem conversa não vira entrevista.
- **Rotina diária** de 20 a 30 minutos, ou de 30 a 40 com o bloco de vagas, quando houver funil.
- **Limites da conta gratuita.** O LinkedIn não publica números, então trate cada um como estimativa. A cota de notas aparece ao clicar em "Adicionar nota": em out/2026 eram 3 por mês, e isso pode mudar.
- **Textos prontos, com contagem:** validação, recomendação, convites de até 200 caracteres e mensagem depois do aceite.
- **Ideias de post técnico tiradas dos projetos reais.** Cada uma traz o gancho, o problema, a solução, o aprendizado, o formato, a semana, a pergunta final, as hashtags, a fonte de cada número e os cuidados.

Convide primeiro quem já interagiu com o usuário. Essas pessoas aceitam mais, e convites ignorados demais trazem restrições. A ordem completa está na referência.

Não publique na semana em que o perfil está sendo arrumado. Quem chega pelo post deve encontrar o perfil pronto. Depois, reserve um dia fixo da semana para os posts.

## Fase 6: Recrutadores

**Objetivo:** montar uma lista curta de recrutadores (ou tech leads) para convidar com critério.

**Leia `references/recrutadores.md`** e use o `scripts/extrair_busca.js` na página de resultados.

**Como fazer:**
- Use a busca de pessoas do LinkedIn no navegador, **só lendo**. Não convide ninguém.
- Comece pelo 2º grau, que aceita mais.
- Pare em cerca de 8 buscas, para não gastar o limite mensal de busca da conta gratuita.
- O extrator acumula os resultados entre as páginas. Limpe o que ele guardou ao terminar. Se a sessão cair antes, limpe no começo da próxima.
- Sem navegador, passe ao usuário os recortes de busca e peça para ele colar os resultados.

**Curadoria:**
- Tire quem não é recrutador.
- **Prioridade A** (região do usuário, vagas remotas ou no exterior, setores dele, quem está contratando): convite com nota enquanto houver cota (3 por mês em out/2026). O resto da A vai sem nota, e o texto segue como 1ª mensagem depois do aceite.
- **Prioridade B:** convite sem nota, ou seguir primeiro.

**Entrega:** o `recrutadores.md`, no formato da referência. A lista inclui os excluídos e as próximas buscas.

Guarde só dados profissionais e públicos, num arquivo privado. Não cruze com outras fontes. É uma lista de contatos, não um dossiê.

## Fase 7: Checklist e acompanhamento

**Objetivo:** dizer o que fazer em cada dia. O plano semanal diz o quê; o checklist diz o que fazer hoje. É o arquivo que a pessoa abre todo dia, então ele precisa ser curto e concreto.

**Leia `references/rede-e-ssi.md`, seção "Modelo do `checklist.md`".**

**Entrega:** o `checklist.md`, com os próximos 10 a 14 dias, dia a dia, em itens `- [ ]`. Inclua:
- a rotina diária, que se repete;
- a planilha de sexta, com as colunas definidas (as do funil, se houver);
- as tarefas únicas: anotar a linha de base no 1º dia, pedir as recomendações, publicar os posts e aplicar o que ficou com o usuário na fase 4.

Cada item aponta para o texto pronto no `rede-linkedin.md` ou para a pessoa no `recrutadores.md`.

**Quando o usuário voltar:**
- marque o que foi feito;
- troque as premissas pelos números reais, como a taxa de aceite;
- gere o checklist do período seguinte.

No meio do prazo, faça uma revisão do plano. No fim, compare com a linha de base, reestime o SSI (se ele foi estimado) e diga o que funcionou.

## Limites e segurança

- **Login e senha:** são do usuário. Nunca digite senha nem resolva captcha. Peça para ele fazer.
- **Token de sessão:** nunca mostre, grave nem registre. Use só dentro da chamada que precisa dele.
- **Edição do perfil:** só com escopo aprovado, item a item, conferindo antes e depois.
- **Exclusão:** só com pedido explícito, item a item.
- **Automação:** nada em massa. Convite ou mensagem em lote arrisca restrição da conta, e os termos do LinkedIn proíbem bots.
- **Termos e declarações formais:** aceitar termos e declarar algo em nome do usuário cabe a ele.
- **Dados de terceiros:** só profissionais e públicos, em arquivo privado, sem cruzar fontes.
- **Honestidade:** registre seus erros no plano e liste o que o usuário precisa desfazer.

## Erros comuns que esta skill evita

- **Número sem fonte**, ou premissa (convites por semana, aceite) tratada como fato.
- **Papel inflado:** bolsa vira emprego, participação vira "liderei".
- **Contagem de cabeça:** o texto passa do limite e é cortado ou recusado.
- **Convite frio antes do perfil pronto:** quem recebe olha o perfil. Até o título e o Sobre novos estarem no ar, convide só conhecidos.
- **Notas gastas cedo:** a cota é pequena. Guarde para recrutadores e tech leads; sem nota, mande o texto como 1ª mensagem depois do aceite.
- **Post com dado sensível**, ou sobre o trabalho atual sem o OK da chefia (na busca discreta, nem peça: poste sobre temas de fora do empregador).
- Armadilhas de navegador (duplicatas, autocompletar, foco): ver `references/aplicar-no-navegador.md`.
