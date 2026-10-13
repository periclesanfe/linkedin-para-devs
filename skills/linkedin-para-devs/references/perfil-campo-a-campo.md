# Plano do perfil, campo a campo

O plano é um arquivo, `linkedin.md`, com todo o texto do perfil pronto para colar, na ordem em que vai ser aplicado. Cada item é uma caixa `- [ ]`, cada texto fica num bloco de código e cada bloco traz a contagem de caracteres.

Por que nesse formato: quem aplica (o usuário ou você, pelo navegador) segue de cima para baixo sem decidir nada na hora. A contagem evita o formulário que corta ou não salva. As caixas mostram o progresso entre uma sessão e outra.

## Sumário

1. Limites e contagem
2. Modelo do `linkedin.md`, com o Diagnóstico
3. Status da aplicação
4. Seção a seção: correções, título, Sobre, experiências, projetos, publicações, certificados, prêmios e afins, formação, competências, destaques, segundo idioma, rede
5. Regras de conteúdo
6. Júnior ou primeiro emprego
7. Busca discreta
8. Exemplo curto (inventado)

## 1. Limites e contagem

| Campo | Limite | `contar.py --limite` |
|---|---|---|
| Título (headline) | 220 | `titulo` |
| Sobre (About) | 2.600 | `sobre` |
| Descrição de experiência | cerca de 2.000 | `posicao` |
| Descrição de projeto | cerca de 2.000 | `projeto` |
| Descrição de publicação, prêmio, voluntariado, organização | cerca de 2.000 | `2000` |
| Formação: "Atividades e grupos" | 500 | `500` |
| Formação: "Descrição" | 1.000 | `1000` |
| Nota de convite (conta gratuita) | 200 | `convite` |
| Mensagem direta (validação, recomendação, depois do aceite) | 500 (teto desta skill; o do LinkedIn é maior) | `mensagem` |
| Competências por experiência ou projeto | 5 | — |
| Principais competências (fixadas no topo) | 5 | — |
| Competências no perfil | 100 | — |

Título, Sobre, nota de convite e os limites de competências foram vistos na interface em português em 2026. Os demais (os marcados "cerca de" e os da formação) são referência, não medição: confira no contador do formulário. O LinkedIn muda sem aviso. Se um campo recusar o texto, confie no contador do próprio formulário e corrija o plano.

Conte sempre com o script, nunca de cabeça. Use o caminho absoluto, `<diretório base desta skill>/scripts/contar.py`, porque o diretório de trabalho não é a pasta da skill:

```bash
python3 <diretório base desta skill>/scripts/contar.py --limite titulo <<'EOF'
Desenvolvedora Front-end · React · TypeScript | ...
EOF
python3 <diretório base desta skill>/scripts/contar.py --limite sobre sobre.txt
```

Como ele conta:
- Usa `len()` do Python: a quebra de linha vale 1 e a letra acentuada vale 1.
- Formulários web costumam contar em UTF-16 (o `.length` do JavaScript), em que um emoji vale 2. Por segurança, o script mostra as duas contagens e decide pela maior.
- A quebra de linha no fim do arquivo não conta.

Escreva no plano a contagem ao lado do texto, no formato "(196/220)". Num texto com muitas quebras de linha e perto do limite, deixe uma folga de pelo menos o número de quebras: há editores que contam cada quebra como 2.

O LinkedIn não renderiza Markdown. `**negrito**` e `# título` aparecem crus. Dentro dos blocos de texto, use só linhas, linhas em branco e o marcador "•".

## 2. Modelo do `linkedin.md`

Copie este esqueleto e preencha. Seções sem conteúdo saem, em vez de ficarem vazias.

````markdown
# LinkedIn: plano de atualização

Perfil: linkedin.com/in/<vanity> · preparado em <dd/mm/aaaa> · aplique na ordem das etapas.

## Status da aplicação (<dd/mm/aaaa>)

**Aplicado e conferido:** nada ainda.

**Para você fazer:**
- [ ] ...

**Erros meus e como desfazer:** nenhum.

## Diagnóstico (<dd/mm/aaaa>)

Lido de: <PDF do perfil | texto colado | páginas /details/>.

**Errado** (dado que a evidência desmente)
- <campo>: está "<atual>", a evidência mostra "<certo>". <!-- fonte: ... -->

**Fraco** (existe, mas não prova nada)
- <campo>: <o que falta: entrega, resultado, as palavras das vagas>.

**Vazio** (ajudaria e não existe)
- <seção>: <o que entra e de qual evidência sai>.

## Resumo do que muda

Sai do Diagnóstico: o Errado vira o item 1, o Fraco vira os itens 2 e 3, e o Vazio vira os itens 4 e 5.

1. Corrige o que está errado: ...
2. Troca o título e o Sobre por ...
3. Reescreve as N experiências com entregas concretas e competências por cargo.
4. Preenche as seções vazias: ...
5. Cria o perfil em inglês e organiza recomendações, Open to work e posts até <prazo>.

As contagens seguem o `len()` do Python, em que cada quebra de linha conta 1.

## 1. Correções urgentes
## 2. Título e Sobre
### 2.1 Título
### 2.2 Sobre
## 3. Experiências (campo a campo)
### 3.1 <Cargo> · <Empresa>
## 4. Seções novas
### 4.1 Projetos
### 4.2 Publicações
### 4.3 Licenças e certificados
### 4.4 Prêmios
### 4.5 Trabalho voluntário
### 4.6 Organizações
### 4.7 Formação
### 4.8 Competências
### 4.9 Destaques
## 5. Perfil em <segundo idioma>
## 6. Rede e visibilidade

## Contexto
Respostas da fase 0: prazo e objetivo, situação atual (empregado? pode citar o empregador e postar sobre ele?), busca discreta ou aberta, alvo (Brasil ou exterior), idioma principal, vagas-alvo, GitHub e links, tempo por dia e o que é privado.
````

O Diagnóstico é a entrega da fase 2. O Resumo não traz nada que não esteja nele. Assim o usuário vê o motivo de cada mudança antes de ler o texto novo, e nada entra no plano sem um problema que o justifique.

Com alvo no exterior, o texto em inglês fica logo abaixo do português, em cada item (ver "Perfil no segundo idioma"). A seção 5 do modelo fica só com o que é exclusivo do perfil em inglês.

## 3. Status da aplicação

Fica no topo, logo abaixo do cabeçalho, porque é o que o usuário lê quando volta ao arquivo. Atualize depois de cada item aplicado, com a data.

- **Aplicado e conferido:** só o que você conferiu depois de salvar, pela página de detalhes ou, como alternativa, pela API. A tela não basta, porque às vezes não renderiza as seções de baixo (ver `aplicar-no-navegador.md`).
- **Para você fazer:** exclusões, envios, publicações, anexos de arquivo e tudo que dependa de uma decisão dele. Cada item com o caminho exato ("Perfil > Competências > ...").
- **Erros meus e como desfazer:** duplicatas criadas, campo salvo errado, o que for. Escreva sem rodeio e diga o que ele precisa apagar. Esconder um erro custa mais caro quando ele aparece no perfil.

Marque no corpo do plano as caixas `- [x]` dos itens aplicados, para as duas partes contarem a mesma história.

## 4. Seção a seção

### 4.1 Correções urgentes

Dados errados vêm antes de tudo: datas, vínculo, cargo, nome de empresa, status de artigo ("submetido" que já saiu, ou o contrário) e afirmações do texto atual que nenhuma fonte sustenta. Dado errado é pior que dado fraco: o recrutador compara o perfil com o CV, e uma data que não bate põe tudo em dúvida.

Formato de cada item:

```markdown
- [ ] **<Experiência>, início:** jul/2024 vira **jun/2024**. <Por quê, em uma frase.>
```

Diga que os textos das etapas seguintes já trazem as correções. Se as etapas 2 e 3 forem demorar, a pessoa corrige estas primeiro, em poucos minutos.

### 4.2 Título (até 220)

Entregue um título principal e duas alternativas, cada uma com a contagem e o público ("para vagas remotas", "para recrutadores de fora").

Fórmulas que funcionam para dev:

1. **Padrão:** `<Cargo-alvo> · <3 a 5 tecnologias> | <prova: o que lidera ou entregou, com setor ou escala> | <diferencial>`
2. **Remoto:** a fórmula 1 terminando em `| Inglês <nível> · Aberto(a) a remoto`
3. **Exterior, tudo em inglês:** `<Role> | <stack> | <proof> | English <level> · Open to remote`
4. **Júnior sem emprego ou em transição:** `Desenvolvedor(a) <área> Júnior · <stack> | <projeto no ar ou estágio> | <formação ou bootcamp>`
5. **Júnior no 1º emprego:** `Desenvolvedor(a) <área> Júnior · <stack> | <entrega no emprego> + <produto no ar> | <formação>`

Regras, e o porquê:
- **Comece pelo cargo que o recrutador digita** ("Desenvolvedor Back-end", "Engenheira de Software"). A busca e o card de resultado mostram o começo do título. "Entusiasta" e "apaixonado por tecnologia" não são buscados.
- **Use as palavras das vagas.** Abra 3 a 5 vagas que o usuário quer e copie os termos de stack delas.
- **Prova vale mais que adjetivo.** "Lidero o back-end de pagamentos de um app com 2 milhões de usuários" diz mais que "dev dedicado". A prova também precisa de fonte.
- **No título, número sem data; a data fica no Sobre.** "SaaS com 30 clínicas" cabe no título; "30 clínicas em out/2026" vai no Sobre, com a fonte. A data gasta caracteres e envelhece o título. Quando o número mudar, atualize o título e o Sobre juntos.
- **Nível de inglês com fonte.** Nível CEFR (B2, C1) só com certificado ou teste. Sem eles, use a palavra do usuário (intermediário, avançado, fluente), que ele sustenta na entrevista.
- **Sigla de empresa pouco conhecida não diz nada** a quem está fora dela. Descreva o produto e a escala.
- **Separe com "·" e "|", sem emoji.** O emoji pode contar 2 caracteres e vira ruído no resultado de busca.
- **Não ponha "buscando oportunidade" no título.** Para isso existe o Open to work, que é decisão do usuário. "Aberto(a) a remoto" informa a modalidade e pode ficar, exceto na busca discreta (ver "Busca discreta").

### 4.3 Sobre (até 2.600)

Estrutura:

1. **Gancho, até cerca de 200 caracteres.** Só ele aparece antes do "ver mais". O corte é visual, e no celular cabe menos que no computador: os 200 são uma estimativa, então confira no celular. Linha 1: quem é a pessoa e o que ela faz bem, numa frase. Linha 2: a prova mais forte, com número e fonte.
2. **Prova:** o trabalho atual, com contexto (produto, escala, equipe) e 2 ou 3 bullets "•" com a entrega mais forte de cada contexto. Não copie os bullets da experiência: o Sobre conta a história e as decisões, e a experiência lista as entregas.
3. **Antes:** um parágrafo curto por experiência relevante ou produto próprio.
4. **Opcional:** pesquisa, open source, comunidade, ensino. Só se reforça o alvo.
5. **Foco atual:** uma linha "Stack: ..." com as tecnologias na ordem das vagas-alvo. Ela alimenta a busca.
6. **O que busca:** formação, idioma e modalidade ("Aberta a oportunidades remotas no Brasil e no exterior"). Na busca discreta, troque por uma frase neutra de foco (ver "Busca discreta").
7. **Contato:** o e-mail e os links que o usuário quiser públicos. Pergunte; não presuma.

Regras:
- Escreva em 1ª pessoa, com frases curtas.
- Não repita o título palavra por palavra. O Sobre expande e prova.
- Tire do texto atual tudo que não tem fonte, e liste isso na etapa 1.
- Se a pessoa está empregada, lembre que o empregador também lê. "Aberta a oportunidades" é decisão dela.
- Ao lado do bloco, diga quantos caracteres tem o gancho e o que ficou de fora de propósito.

### 4.4 Experiências (descrição até cerca de 2.000)

Um bloco por experiência, na ordem em que aparecem no perfil:

````markdown
### 3.1 <Cargo> · <Empresa>

- [ ] **Cargo:** <título oficial> (<termo de busca, se o oficial não diz o que a pessoa faz>)
- [ ] **Tipo de emprego:** <atual> vira **<novo>**
- [ ] **Empresa:** <página da empresa no LinkedIn, com logo>
- [ ] **Local:** <cidade, estado, país> · **Tipo de local:** No local | Híbrido | Remoto
- [ ] **Início/Fim:** <mmm/aaaa> – <mmm/aaaa | atual>
- [ ] **Competências (5):** A · B · C · D · E
- [ ] **Descrição (N/2.000):**
```text
<contexto em 1 parágrafo>

• <bullet>
• <bullet>
```

**Por que muda:** <uma a três frases>.
**Confirme antes de colar:** <o que depende de resposta do usuário>.
````

Os campos:
- **Cargo:** o oficial vem na frente. Se ele não diz o que a pessoa faz, acrescente o termo de busca entre parênteses: "Analista de Sistemas II (desenvolvimento back-end)". O LinkedIn troca o texto por um cargo padronizado se você aceitar a sugestão. Feche as sugestões e confira (ver `aplicar-no-navegador.md`).
- **Tipo de emprego:** o mais próximo do vínculo real. Bolsa não é emprego: o cargo diz "Bolsista de ..." e o tipo fica em branco. Estágio é Estágio. PJ por demanda é Freelance ou Autônomo. O campo é opcional, e em branco é melhor que errado.
- **Datas:** mês e ano, conferidos com contrato, bolsa ou git. Experiências ao mesmo tempo são normais.
- **Competências:** 5 por cargo, as que aquele cargo comprova, na ordem do alvo.
- **Descrição:** um parágrafo de contexto (o que é o produto, para quem, escala com fonte, tamanho da equipe), depois 3 a 5 bullets. Sem a linha "Stack:": as tecnologias vão no campo Competências.

**Bullets: verbo + entrega + resultado com fonte.**
- Verbos: implementei, migrei, troquei X por Y, automatizei, reduzi, lancei, corrigi, conduzi. "Liderei" só se liderou. Liderança técnica sem cargo de gestão se diz como é: "conduzo as decisões técnicas do time, sem gestão de pessoas".
- Tempo verbal: presente para o que continua, passado para o que terminou, mesmo dentro do cargo atual.
- O resultado é medido (tempo, volume, erro, custo, usuários) ou é uma consequência verificável ("sem downtime", "hoje em produção", "usado por 3 equipes").

| Fraco | Forte (números inventados) |
|---|---|
| Responsável pelo front-end e por melhorias de performance. | Reduzi o bundle inicial de 480 KB para 210 KB (gzip) com divisão por rota. |
| Trabalhei com testes automatizados. | Pus testes de ponta a ponta no CI, que bloqueiam o merge quando o fluxo de pagamento quebra. |
| Participei da migração para a nuvem. | Migrei 4 serviços de VM para contêiner, com deploy blue-green e rollback automático. |

No plano, cada bullet com número leva o comentário da fonte logo abaixo do bloco: `<!-- fonte: git owner/repo, 13/10/2026 -->`. Ele não vai para o LinkedIn.

### 4.5 Projetos (descrição até cerca de 2.000)

Faça depois das experiências, porque cada projeto se associa a uma experiência ou à formação.

**Entra:** produto próprio no ar, de preferência com usuários; open source que alguém usa; projeto de pesquisa com publicação; projeto relevante que nenhuma experiência cobre.

**Polui:** exercício de curso, clone de tutorial, lista de tarefas, fork sem commit, e o projeto do empregador que já está descrito na experiência (duplicar dilui).

````markdown
#### <Nome>
- [ ] **Nome:** <Nome>: <o que faz, em uma frase>
- [ ] **Datas:** <mmm/aaaa> – <mmm/aaaa | "Estou trabalhando neste projeto">
- [ ] **Associado a:** <experiência ou formação | nenhum> · **Link:** <url que abre>
- [ ] **Competências (5):** A · B · C · D · E
- [ ] **Descrição (N/2.000):**
```text
<o que é e para quem, com número e data>

<o que o usuário fez, em bullets; em projeto de terceiros, a parte exata dele>
```
````

### 4.6 Publicações

Só o que foi publicado (ver `evidencias.md`, seção "Publicações"). Da mais recente para a mais antiga.

- **Título:** exato, como no artigo.
- **Publicação/editora:** nome dos anais ou da revista, edição, páginas e editora.
- **Data:** a que a fonte traz. Se só traz o ano, use o ano.
- **URL:** o DOI, se ele resolve; senão, a página dos anais, com a nota de trocar depois.
- **Autores:** na ordem do artigo. Coautores com perfil podem ser marcados.
- **Descrição:** 1 ou 2 frases sobre o trabalho e o papel do usuário ("1º autor", "apresentei no evento").

### 4.7 Licenças e certificados

Uma seção com dezenas de cursos de 2 horas esconde as credenciais que pesam e passa a imagem de iniciante.

**Entra:** certificação de mercado (nuvem, Kubernetes, segurança e afins); proficiência de idioma com nota ou nível; curso longo, de instituição reconhecida, ligado ao alvo. Sempre com a URL ou o código da credencial, se existir.

**Polui:** dezenas de cursos curtos de plataforma; cursos introdutórios de algo que a experiência já prova; participação em evento; declaração de atividade.

No plano, liste o que não entra numa subseção "Não cadastre aqui", com o motivo de cada item. Se o usuário quiser manter muitos cursos, sugira no máximo um item agrupado. Participações e declarações vão para a seção certa: voluntariado, organizações ou posts.

### 4.8 Prêmios, voluntariado e organizações

- **Prêmios:** hackathon, ideathon, olimpíada, bolsa por mérito. Diga o que foi premiado e entre quantos, se houver fonte.
- **Trabalho voluntário:** organizar evento, monitoria, mentoria, comunidade. Diga o papel.
- **Organizações:** centro acadêmico, grupo de pesquisa, comunidade técnica. Diga o cargo e o período.

### 4.9 Formação

- **"Atividades e grupos" (até 500):** iniciação científica, monitoria, centro acadêmico, grupos.
- **"Descrição" (até 1.000):** TCC (tema e resultado, se houver fonte), ênfase, previsão de conclusão.
- Curso em andamento: ponha a previsão de término nas datas.

### 4.10 Competências

- **As 5 principais, fixadas no topo** (aparecem na seção Sobre). Elas batem com o título. Se o título diz React e Node.js, elas também dizem.
- **Até cerca de 30 cadastradas, em ordem de prioridade**, cada uma com a evidência entre parênteses no plano: `NestJS (API do projeto X; projeto Y)`. Depois das 30, uma linha de reservas.
- **Sem evidência, não entra.** Competência que o usuário só estudou não é competência de perfil.
- **Ligue cada competência às experiências e aos projetos que a comprovam.** O formulário tem caixas para isso.
- **Use o nome exato do autocompletar.** O LinkedIn tem um catálogo, e o nome dele pode ser outro. Exemplos vistos na interface em português: "React.js", "Node.js", "Integração e entrega contínuas (CI/CD)". "LGPD" só sugere RGPD, então use "Privacidade dos dados". "Single Sign-On" sugere um produto específico, então use "Logon único (SSO)". Às vezes a 1ª sugestão é um produto homônimo, que nada tem a ver com a tecnologia. No plano, escreva "use o nome que o LinkedIn sugerir" e, na aplicação, confira a opção (ver `aplicar-no-navegador.md`).
- **Duplicatas e quase-iguais** já cadastradas (erro de digitação, singular e plural): liste para o usuário. Excluir é decisão dele.

### 4.11 Destaques (Featured)

De 3 a 4 itens, nesta lógica:
1. **O produto que se pode clicar:** site, app na loja, demo. O recrutador consegue testar na hora.
2. **O post de maior alcance**, se for técnico. O número de impressões vem das estatísticas do próprio post.
3. **Artigo com DOI** ou **repositório com bom README**.
4. **Opcional:** o post que fecha uma história (TCC, lançamento, cargo novo).

**Sem produto clicável** (back-end, código privado): o 1º item passa a ser a melhor prova que abre num clique. Use um destes: estudo de caso de arquitetura (sem dado sensível), palestra, repositório open source com bom README, diagrama ou artigo técnico.

Para cada um: link, título, descrição curta com contagem e um "Por quê" de uma frase.

### 4.12 Perfil no segundo idioma

Só faça se o usuário consegue fazer entrevista nesse idioma. Um perfil em inglês que a pessoa não sustenta na conversa atrapalha.

- **Alvo no exterior: escreva o inglês junto com o português**, item a item, não no fim. No plano, o bloco em inglês fica logo abaixo do português. Os dois saem das mesmas fontes, e o inglês deixado para o fim costuma não sair.
- **Idioma principal:** decida com o usuário na fase 0. Quem abre o perfil vê a versão no idioma da própria interface do LinkedIn, se ela existir; se não, vê a principal. Alvo misto (Brasil e exterior): português como principal e inglês como segundo idioma. Alvo só no exterior: os textos do perfil principal podem ir em inglês; se o perfil já está em inglês, mantenha, e o português vira opcional. Na busca discreta, não troque o idioma principal, porque a troca aparece para quem já conhece o perfil: crie o inglês como segundo idioma.
- **Headline:** uma por idioma, inteira num idioma só (no inglês, a fórmula 3 da seção do título). Não junte português e inglês na mesma headline: fica confuso e estoura os 220. A prova e os números são os mesmos nas duas, e a regra do número sem data vale para as duas.
- Crie pela opção de perfil em outro idioma, na página do perfil (detalhes em `aplicar-no-navegador.md`).
- Datas, empresas e competências são compartilhadas com o perfil principal. Traduza o título, o Sobre e as descrições das experiências principais.
- Adapte, não traduza palavra por palavra. "Bacharelando em ..." vira "B.S. in ... (expected <Mon YYYY>)". Use os nomes de cargo do mercado de fora.
- São os mesmos fatos, com as mesmas fontes. Conte de novo, porque o texto muda de tamanho.

### 4.13 Rede e visibilidade

No `linkedin.md`, faça só um resumo: quem pedir recomendação, Open to work (decisão do usuário; na busca discreta, só para recrutadores), URL personalizada, foto e capa, e os posts com data. O detalhe fica no `rede-linkedin.md` (ver `rede-e-ssi.md` e `textos-modelo.md`).

## 5. Regras de conteúdo

Valem para todo o plano, e o porquê vem junto:
- **Sem fonte, sem número.** Ver `evidencias.md`, seção "Sem fonte, sem número". O número que a pessoa não sabe defender cai na entrevista.
- **Não infle.** Bolsa não é emprego. Contribuição pequena é descrita como pequena. Participar não é liderar. O perfil vai ser confrontado com referências e com o próprio CV.
- **Projeto de terceiros:** diga exatamente a parte do usuário (só o front, pair programming, testes, validação). O dono do projeto pode estar lendo.
- **Projeto que o usuário pediu para tirar:** some de todo canal.
- **Dado sensível:** nada de segredos, IPs, nomes de clientes internos ou detalhes de segurança exploráveis. Fale de padrão e decisão, não de configuração.
- **Empregador atual:** o perfil fala de padrão e decisão ("migrei o monólito para Go"), não do que só alguém de dentro saberia (volume de transações, nome de cliente ou de fornecedor). O que passar disso, e todo post sobre o trabalho atual, pede o OK da chefia antes. Na busca discreta, o pedido já denuncia: ver "Busca discreta".
- **Explique as mudanças.** Cada bloco com mudança relevante tem um "Por que muda" curto. O usuário aprova melhor o que entende.

## 6. Júnior ou primeiro emprego

Com pouca experiência, a prova está nos projetos. Ajuste o plano assim:
- **Projetos e Destaques vêm primeiro.** No `linkedin.md`, eles viram a etapa 3, logo depois do título e do Sobre, e as Experiências passam para a 4, junto com o resto das seções novas. São a prova que a experiência curta ainda não dá.
- **GitHub arrumado antes de ir para o perfil.** Fixe os repositórios que provam algo, até 6, cada um com README que diz o que faz, como rodar e onde está no ar. Exercício de curso e clone de tutorial não entram. O recrutador abre o link e decide em segundos.
- **Estágio e projeto acadêmico com entrega real contam.** Estágio entra como experiência, com o tipo "Estágio". Projeto acadêmico entra em Projetos se alguém usou ou se virou publicação.
- **Formação com previsão de conclusão**, nas datas e no Sobre ("conclusão prevista para dez/2027").
- **Título:** as fórmulas 4 e 5 da seção do título.
- **Open to work:** se a pessoa já está empregada, só para recrutadores (ver "Busca discreta").

## 7. Busca discreta

Vale quando o usuário está empregado e não quer que o empregador saiba da busca (resposta da fase 0). O chefe e os colegas também leem o perfil, e uma mudança brusca vira sinal de saída.

- **Título:** nada de "aberto a", "Aberto(a) a remoto", "Open to remote" nem "Looking for". O título diz o que a pessoa faz; quem procura é o recrutador.
- **Sobre:** a linha "O que busca" vira uma frase neutra de foco ("Hoje meu foco é front-end de produto e performance."). Nada de "aberta a oportunidades".
- **Open to work:** só para recrutadores, sem o selo na foto. O LinkedIn diz que tenta esconder dos recrutadores da empresa atual, mas não garante. A decisão e o clique são do usuário.
- **Compartilhamento:** desligue o "compartilhar com a rede" em toda edição, inclusive num cargo novo, que vira "parabéns" no feed. Em Configurações > Visibilidade, desligue também o compartilhamento de mudanças de emprego e de formação (procure por "compartilhar"; o rótulo muda). Espalhe as edições por alguns dias, em vez de trocar tudo numa tarde. Uma rajada de edições anunciada no feed é o sinal mais visível.
- **Validações e recomendações:** peça só a quem não está na empresa atual: ex-colegas, ex-gestores, turma, professores, clientes de projeto próprio. Colega atual e gestor comentam, e o pedido avisa a empresa (ver `textos-modelo.md`, "Pedidos na busca discreta").
- **Empregador atual:** não peça o OK da chefia, porque o pedido já denuncia. Confira a política escrita da empresa (código de conduta, redes sociais), fique em padrão e decisão (ver "Regras de conteúdo") e não ponha estudo de caso dele nos Destaques.
- **Convites e posts:** posts técnicos sobre temas de fora do empregador; convites sem falar de procura de vaga (ver `textos-modelo.md`, "Busca discreta").

## 8. Exemplo curto (inventado)

Ana Souza (fictícia) é dev front-end em Recife, com React e TypeScript. Está há 2 anos no emprego atual, num e-commerce, e tem com um sócio um produto pessoal no ar: um SaaS de agendamento. Tem 150 conexões, e a busca dela não é discreta (por isso o título diz "Aberta a remoto"). É a mesma persona dos exemplos das outras referências. Pessoa, empresas e números são inventados.

````markdown
## Diagnóstico (13/10/2026)

Lido de: PDF do perfil, enviado pela usuária.

**Errado**
- Experiência atual: o início está "jan/2025", o contrato diz out/2024. <!-- fonte: contrato, conferido pela usuária em 10/10/2026 -->

**Fraco**
- Título: "Desenvolvedora | Apaixonada por tecnologia". Sem cargo buscável, sem stack e sem prova.

**Vazio**
- Projetos: o SaaS de agendamento não aparece. Sai da ficha do repositório e do painel do produto.
- Destaques: nenhum. O 1º passa a ser o link do SaaS.

### 2.1 Título

- [ ] Colar o título (**188/220**):
```text
Desenvolvedora Front-end · React · TypeScript · Next.js · Playwright | Design system e performance em e-commerce + SaaS de agendamento próprio com 30 clínicas | Inglês B2 · Aberta a remoto
```
<!-- fonte: 30 clínicas: painel do SaaS, out/2026 (print enviado pela usuária em 10/10/2026); a data fica no Sobre. Inglês B2: certificado de proficiência enviado pela usuária -->

### 2.2 Sobre (gancho)

O gancho (**180 caracteres**), que aparece antes do "ver mais". O e-commerce já está no título e vem logo depois, no bloco de prova:
```text
Desenvolvedora front-end que transforma fluxo confuso em tela que a pessoa termina sem ajuda.
Com um sócio, criei um SaaS de agendamento que tinha 30 clínicas pagantes em out/2026.
```

### 3.1 Desenvolvedora Front-end · [Empresa]

- [ ] **Cargo:** Desenvolvedora Front-end
- [ ] **Tipo de emprego:** Tempo integral
- [ ] **Local:** Recife, Pernambuco, Brasil · **Tipo de local:** Híbrido
- [ ] **Início/Fim:** out/2024 – atual
- [ ] **Competências (5):** React.js · TypeScript · Next.js · Storybook · Testes de software (use o nome que o LinkedIn sugerir)
- [ ] **Descrição (415/2.000):**
```text
Front-end de uma plataforma de e-commerce, numa equipe de 6 devs. Cuido do checkout e do design system.

• Montei com outra dev o design system, com 40 componentes documentados no Storybook, hoje usado pelas 3 equipes de produto.
• Reduzi o bundle inicial de 480 KB para 210 KB (gzip) com divisão por rota.
• Pus testes de ponta a ponta com Playwright no CI, que bloqueiam o merge quando o fluxo de checkout quebra.
```
<!-- fonte: equipe e "com outra dev": usuária, 10/10/2026; componentes: Storybook interno, contado pela usuária em 10/10/2026; bundle: relatório do build no PR de divisão por rota -->

**Por que muda:** a descrição antiga listava tarefas ("responsável pelo front-end"). A nova mostra entrega e resultado, diz que o design system foi feito a quatro mãos, e a stack sai do texto para o campo Competências.

### 4.1 Projetos

#### SaaS de agendamento
- [ ] **Nome:** [Nome do produto]: agenda on-line para clínicas pequenas
- [ ] **Datas:** jan/2025 – "Estou trabalhando neste projeto"
- [ ] **Associado a:** nenhum · **Link:** [url do produto]
- [ ] **Competências (5):** React.js · TypeScript · Next.js · Tailwind CSS · Testes de usabilidade (use o nome que o LinkedIn sugerir)
- [ ] **Descrição (369/2.000):**
```text
Agenda on-line para clínicas pequenas: o paciente marca pelo link e recebe lembrete. Tinha 30 clínicas pagantes em out/2026.

• Criei o produto com um sócio, que cuida do back-end. O front-end em Next.js e TypeScript é meu.
• Refiz a tela de agenda depois de testes com 5 recepcionistas, e a mediana do tempo para marcar uma consulta caiu de 3 min 10 s para 1 min 20 s.
```
<!-- fonte: clínicas: painel do SaaS, out/2026; tempo de agendamento: métricas do produto, set/2026; testes e divisão com o sócio: usuária, 10/10/2026 -->
````
