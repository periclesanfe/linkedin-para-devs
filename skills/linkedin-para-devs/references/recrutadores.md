# Busca de recrutadores

Esta referência guia a fase 6: montar uma lista curta e curada de recrutadores (ou tech leads) para o usuário convidar com critério. A entrega é o arquivo `recrutadores.md`.

## 1. Objetivo

Trocar convites aleatórios por uma lista de pessoas que recrutam para a área, a região e os setores do usuário, com o motivo de cada escolha. A lista alimenta o bloco "Convites" da rotina diária (ver `rede-e-ssi.md`) e diz quem recebe nota. A cota de notas é pequena: em out/2026, a conta gratuita tinha 3 por mês, e o LinkedIn mostra o saldo ao clicar em "Adicionar nota". Trate o número como observado naquela data, não como garantia.

O trabalho é **só de leitura**. Você busca, lê e organiza. Não convida, não segue, não manda mensagem e não abre perfis em sequência. Por padrão, o usuário faz os convites à mão, porque convite em lote arrisca a restrição da conta e os termos do LinkedIn proíbem bots. Se ele pedir que você envie, siga a seção "Enviar convites (só com lista e texto aprovados)" do `aplicar-no-navegador.md`.

Sem ferramenta de navegador, passe ao usuário as URLs dos recortes e peça para ele colar o texto dos resultados.

## 2. URL de busca

```text
https://www.linkedin.com/search/results/people/?keywords=<termos>&geoUrn=%5B%22106057199%22%5D&network=%5B%22S%22%5D&page=N
```

| Parâmetro | Valor | O que faz |
|---|---|---|
| `keywords` | termos com `%20` no lugar dos espaços | o texto da busca |
| `geoUrn` | `%5B%22106057199%22%5D`, que é `["106057199"]` | Brasil. Para outro país, escolha o filtro Localidades na própria busca e copie o `geoUrn` que aparece na URL; nunca escreva um de memória. Tire o parâmetro para buscar no mundo todo. |
| `network` | `%5B%22S%22%5D`, que é `["S"]` | só 2º grau, que aceita mais. Use `%5B%22S%22%2C%22O%22%5D` (`["S","O"]`) para incluir o 3º grau quando o 2º render pouco. |
| `page` | 1, 2... | a página de resultados |

Comece pelo 2º grau. A pessoa tem uma conexão em comum com o usuário, e isso pesa no aceite.

## 3. Recortes de busca

Adapte os termos à área, à região e aos setores do usuário. Um rótulo curto para cada recorte ajuda na curadoria (o extrator guarda o rótulo).

**Alvo no Brasil:**
1. `tech recruiter`, Brasil, 2º grau, 2 páginas;
2. `recrutador tecnologia <cidade do usuário>`;
3. `tech recruiter remoto desenvolvedor`;
4. `tech recruiter <setor>`, um por setor do usuário (por exemplo healthtech, fintech, edtech, govtech);
5. `tech recruiter <polo regional>`, a capital ou o polo de tecnologia mais perto.

**Alvo no exterior**, só se o usuário tem inglês para entrevista. Tire da URL o `geoUrn` do Brasil: ele filtra onde a pessoa recrutadora mora, e muita gente que recruta para empresas de fora mora fora.
1. `<senioridade> <especialidade> recruiter remote LATAM`, por exemplo `senior backend recruiter remote LATAM`;
2. `talent partner engineering remote Brazil`;
3. `recruiter <empresa>`, para 2 ou 3 empresas remote-first que contratam no Brasil. Escolha as empresas com o usuário, a partir das vagas e dos alertas dele, e não de memória;
4. um país-alvo por vez: aplique o filtro Localidades na própria busca e copie o `geoUrn` que aparecer na URL. Não invente o `geoUrn` de outro país, porque um código errado filtra outro lugar e gasta uma busca.

No exterior, o 2º grau costuma render pouco. Se for o caso, inclua o 3º grau e conte com aceite menor. Se o alvo é só o exterior, troque os recortes do Brasil por estes; se é misto, divida as buscas entre os dois. Em qualquer caso, elas cabem nas cerca de 8 da seção "Limite de buscas". Os convites em inglês estão no `textos-modelo.md`, seção "Em inglês, para recrutador internacional".

## 4. Limite de buscas

A conta gratuita tem um limite mensal de busca de pessoas, chamado de limite de uso comercial. O LinkedIn não divulga o número. Quando ele é atingido, a busca fica restrita até o mês seguinte, e o usuário perde a ferramenta no meio do plano.

Por isso, **pare em cerca de 8 buscas**. Foi o que bastou para uma lista de dezenas de nomes na sessão que deu origem a esta skill, sem esbarrar no limite. Se aparecer o aviso de limite, pare na hora e trabalhe com o que já tem.

## 5. Como usar o extrator

O `scripts/extrair_busca.js` (leia pelo caminho absoluto, `<diretório base desta skill>/scripts/extrair_busca.js`, porque o diretório de trabalho não é a pasta da skill) lê os cards da página de resultados e acumula os dados entre as páginas em `localStorage.__rec`. Abrir outra página apaga as funções do script, mas não o `localStorage` do domínio.

1. Abra a URL do recorte e espere carregar. Role até o fim, para todos os cards aparecerem.
2. Rode o conteúdo do arquivo inteiro na página e, na mesma chamada, `acumular('<rótulo>')`, por exemplo `acumular('tech recruiter p1')`. A função devolve o total acumulado, com repetidos.
3. Se o console avisar que veio vazio numa página com resultados, espere e repita. Se continuar vazio, o layout mudou: leia o HTML de um card e ajuste os seletores.
4. Vá para a próxima página ou o próximo recorte e repita os passos 1 e 2.
5. No fim, rode o arquivo de novo e chame `lerELimpar()`. Ela devolve a lista sem repetidos e apaga a chave. Guarde o resultado num arquivo da sessão antes de seguir, porque a chave já foi apagada. Para só espiar sem apagar, use `JSON.parse(localStorage.__rec)`.

Cada item traz `rotulo`, `nome`, `grau`, `cargo` (o título do perfil no dia), `local`, `emComum` e `url`.

`extrairBusca('<rótulo>')` extrai só a página atual, sem guardar. Serve para testar os seletores.

Apague a chave no fim, sempre. Dados de terceiros não devem ficar no navegador além do necessário.

**Sessão interrompida.** Se a sessão cair antes do `lerELimpar()`, a chave fica no navegador com dados de terceiros.
- Na próxima sessão, antes de qualquer outra coisa, abra uma página do linkedin.com, rode o arquivo e chame `lerELimpar()`. Guarde o resultado num arquivo, se a coleta ainda servir.
- Sem ferramenta de navegador, peça ao usuário para limpar o localStorage do linkedin.com: no console da aba do LinkedIn, `localStorage.removeItem('__rec')`, ou nas ferramentas do desenvolvedor, em Application > Local storage.
- Para a próxima sessão saber que a coleta ficou pela metade, anote "coleta em andamento: rodar lerELimpar()" no `recrutadores.md` ou no `checklist.md` ao começar. Tire a nota depois do `lerELimpar()`. Numa página do LinkedIn, `localStorage.getItem('__rec')` diferente de `null` diz o mesmo.

## 6. Deduplicação

- O `lerELimpar()` deduplica pela URL decodificada, em minúsculas e sem a barra final. URLs com acento chegam codificadas (`%C3%A9`), e a mesma pessoa aparece em mais de uma busca. Quando isso acontece, os rótulos são juntados com " | ".
- Os nomes das conexões em comum não são resultados. O extrator pega só o primeiro link de perfil de cada card; os nomes em comum ficam no texto do campo `emComum`.
- Tire também quem já é conexão de 1º grau e quem já está num `recrutadores.md` anterior (compare as URLs).

## 7. Curadoria

**Tire da lista:**
- quem não é recrutador: CS, desenvolvedores, compras, marketing, produto, DHO, mentoria e similares. A busca por palavra-chave traz muita gente que só cita o termo;
- recrutadores com foco distante do usuário, como ERP, Salesforce, RH generalista ou varejo, quando o usuário não é dessas áreas;
- conexões de 1º grau;
- no alvo no exterior, quem recruta só para residentes de outro país (por exemplo, "US only"), se o usuário não pode se mudar.

**Prioridade A**, convite com nota enquanto houver cota. Com 3 notas por mês (out/2026), a nota vai para os 3 da lista A com mais chance de virar conversa. O resto da A recebe convite sem nota e o texto como 1ª mensagem depois do aceite. Entram na A os recrutadores:
- na cidade ou na região do usuário;
- com vagas remotas ou internacionais, se o usuário busca isso;
- especializados nos setores do usuário;
- que estão contratando agora: título com "hiring", "contratando" ou vaga aberta citada.

Antes do convite de prioridade A, o usuário visita o perfil e, se houver post recente, comenta.

**Prioridade B:** recrutadores de tecnologia em geral. Convite sem nota, ou primeiro seguir e interagir num post.

**Conexões em comum fortes** (um colega próximo, um ex-chefe) podem ser citadas na nota, se o usuário confirmar que conhece a pessoa.

## 8. Formato do `recrutadores.md`

```markdown
# Recrutadores-alvo no LinkedIn

Lista montada em **[data]** a partir de [n] buscas:
- [recorte 1];
- [recorte 2];
- ...

Quase todos são **2º grau**. O cargo é o título do perfil no dia da busca. Os modelos de convite e a ordem de envio estão no [rede-linkedin.md](rede-linkedin.md).

**Como usar**
- **Prioridade A:** convite com nota enquanto houver cota (o LinkedIn mostra o saldo ao clicar em "Adicionar nota"; eram 3 por mês em out/2026). Sem cota, convite sem nota e o texto como 1ª mensagem depois do aceite. Antes, visite o perfil e, se houver post recente, comente.
- **Prioridade B:** convite sem nota, ou primeiro siga a pessoa e interaja num post.
- **Controle:** marque `[x]` quando enviar e anote a data do aceite. Não envie mais de 20 convites por dia.

## Prioridade A

### [Grupo, por exemplo: região do usuário / remoto e internacional / setores]
| | Nome | Cargo (resumo) | Local | Por quê | Perfil |
|---|---|---|---|---|---|
| [ ] | Fulana de Tal | Tech Recruiter, vagas remotas de front-end | São Paulo | Recruta para vagas remotas de front-end; 3 conexões em comum | [link](https://www.linkedin.com/in/[usuario]/) |

## Prioridade B
| | Nome | Cargo (resumo) | Local | Perfil |
|---|---|---|---|---|

**Ficaram de fora [n] dos [n] perfis únicos:**
- [n] que não são de recrutamento: [categorias];
- [n] recrutadores com foco distante do perfil: [categorias].

## Próximas buscas
[ver o item 9]
```

Os excluídos entram só como contagem e categoria, sem nomes. O nome de quem ficou de fora não tem uso e é dado de terceiro a menos no arquivo.

## 9. Próximas buscas

Uma por semana, para não gastar o limite de uma vez:
- **Tech leads e gestores de engenharia:** `"engineering manager" OR "tech lead" <stack> remoto`, 2º grau; `"head de engenharia" <setor>`; `CTO <setor>`. Se o campo não aceitar OR, faça uma busca por termo. O convite de tech lead usa os modelos da seção "Tech lead" do `textos-modelo.md`.
- **Empresas para seguir:** as empresas dos recrutadores da prioridade A e as que aparecerem nas buscas de vaga.
- **Alertas de vaga:** em Vagas, busque as palavras-chave da stack (por exemplo `React TypeScript`) com os filtros Remoto ou Híbrido na cidade do usuário e ative o alerta.

## 10. Privacidade

- Guarde só dados profissionais e públicos: nome, título, local, motivo e link do perfil. Nada de e-mail, telefone ou dado pessoal, mesmo que apareça.
- Não cruze com outras fontes (outras redes, buscadores, vazamentos). É uma lista de contatos, não um dossiê.
- Salve num repositório ou pasta privados. Se o repositório for público, deixe o `recrutadores.md` fora dele (por exemplo, no `.gitignore`).
- Não compartilhe a lista nem a reaproveite para outra finalidade.
- Apague o `localStorage.__rec` no fim da coleta (ou no começo da sessão seguinte, se a anterior caiu antes; ver "Sessão interrompida") e o arquivo quando a campanha acabar, se o usuário não precisar mais dele.
