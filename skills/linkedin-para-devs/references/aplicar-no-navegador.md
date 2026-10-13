# Aplicar o plano no LinkedIn pelo navegador

Este guia mostra como aplicar o plano do perfil (etapas 1 a 5) no LinkedIn web com uma ferramenta de navegador: o navegador do app, o Claude in Chrome ou outra. A etapa 6 (rede e visibilidade) não entra aqui. Ela é feita de envios: convites, mensagens, posts, pedidos de recomendação e Open to work. Quem envia é o usuário. A única exceção são os convites que ele pedir para você enviar, com a lista e o texto aprovados item a item (ver "Enviar convites (só com lista e texto aprovados)", no fim deste guia).

Aplicar pelo navegador é opcional. Se o usuário preferir colar os textos à mão, o plano já basta.

Na fase 2 (diagnóstico), leia o perfil nesta ordem e pare na primeira fonte que bastar:
1. o PDF do perfil (Mais > Salvar como PDF) ou o texto colado pelo usuário;
2. com navegador, as páginas `/in/<vanity>/details/<secao>/`;
3. a API interna (voyager), só como alternativa e depois de avisar o usuário (ver "Consulte antes de criar").

Ler não muda nada e não precisa de escopo.

> **Verificado em 13/10/2026, no LinkedIn web em PT-BR.** O LinkedIn muda a interface e a API interna sem aviso. Se um seletor, rótulo, URL ou endpoint falhar, leia a página (texto ou árvore de acessibilidade) antes de insistir. Repetir a mesma ação às cegas é o jeito mais rápido de criar duplicatas.

## Pré-requisitos

- **Usuário logado** no navegador que a ferramenta controla. O login é dele. Nunca digite senha nem código de verificação, e nunca resolva captcha. Se o LinkedIn pedir login ou verificação no meio do caminho, pare e peça ao usuário.
- **Escopo aprovado no chat**, por exemplo: "aplique as etapas 1 a 4, menos os destaques". Aplique só o que está no escopo. O que surgir fora dele vira pergunta. O perfil é público e cada edição fica visível para recrutadores, então o usuário decide o que muda.
- **Plano pronto**, com os textos finais e as contagens de caracteres. Se um texto mudar durante a aplicação, reconte com `<diretório base desta skill>/scripts/contar.py` antes de colar. Use o caminho absoluto, porque o diretório de trabalho não é a pasta da skill.
- **Vanity do perfil:** a parte do link depois de `/in/`. Peça ao usuário ou leia na barra de endereço depois que ele abrir o próprio perfil. Nos exemplos abaixo, ela aparece como `<vanity>`.

## Ordem de aplicação

Siga esta ordem, que detalha a do plano. Ela foi pensada para que cada passo encontre pronto o que precisa.

1. **Correções urgentes.** Dados errados prejudicam mais e se corrigem rápido.
2. **Título e Sobre.**
3. **Experiências.**
4. **Formação, projetos, publicações, certificados, prêmios, voluntariado e organizações.**
5. **Competências.** Vêm depois de experiências e projetos porque o formulário liga cada competência a itens que já existem.
6. **Destaques.** Apontam para itens e links que precisam existir.
7. **Informações de contato e idiomas.**
8. **Perfil no segundo idioma.** Por último, porque traduz os textos já finais. **Exceção:** se o alvo é o exterior, o perfil em inglês sobe junto com o português. Crie o perfil em inglês no início, se estiver no escopo, e salve e confira as duas versões de cada item antes de passar ao próximo. Por quê: para quem recruta de fora, o perfil que conta é o em inglês, e deixá-lo para o fim é deixá-lo de fora se a aplicação parar no meio.

Cada item segue o mesmo ciclo:

1. Consulte se o item já existe.
2. Abra o formulário pela URL.
3. Preencha com foco e teclado reais.
4. Leia os valores do formulário e compare com o plano.
5. Desligue a notificação à rede.
6. Salve.
7. Recuse as ofertas que aparecerem.
8. Confira o que foi salvo pela página de detalhes ou, como alternativa, pela API.
9. Marque o item no plano.

Faça um item por vez. Um erro visto cedo custa um item, e não vinte.

## Consulte antes de criar

A tela do perfil não é confiável. Num teste real, a página do perfil não renderizou as seções de baixo no painel do navegador. As publicações pareciam não cadastradas, foram cadastradas de novo e viraram duplicatas. Vazio na tela do perfil não prova que o item não existe.

Consulte nesta ordem:

1. **A página de detalhes da seção**, `/in/<vanity>/details/<secao>/`, lida como texto ou pela árvore de acessibilidade. Ela lista os itens salvos de uma seção só e não depende da página do perfil, que é a que falha. Se vier vazia ou parecer incompleta, recarregue uma vez.
2. **A API interna (voyager), só como alternativa**, quando a página de detalhes não bastar. Antes da primeira chamada, avise o usuário, porque ela roda com a sessão dele. Por exemplo: "Vou conferir pela API interna do LinkedIn, com a sua sessão. É só leitura, e o token não sai da chamada."

Para a API, rode na aba do LinkedIn, já logado:

```js
// O token csrf é o valor do cookie JSESSIONID, sem aspas. Ele é lido só
// dentro do fetch: não vai para variável, console, arquivo nem chat.
const api = (path, accept) =>
  fetch('/voyager/api' + path, {
    headers: {
      'csrf-token': document.cookie.match(/JSESSIONID="?([^";]+)/)[1],
      ...(accept ? { accept } : {}),
    },
  }).then(r => (r.ok ? r.json() : r.status));

const vanity = '<vanity>';
const existe = async (secao, trecho) =>
  JSON.stringify(await api(`/identity/profiles/${vanity}/${secao}?count=50`))
    .toLowerCase()
    .includes(trecho.toLowerCase());

await existe('publications', '<trecho do título>'); // true: já existe, edite em vez de criar
```

Para competências, pegue antes o URN do perfil no topo:

```js
const topo = await api(`/identity/dash/profiles?q=memberIdentity&memberIdentity=${vanity}&decorationId=com.linkedin.voyager.dash.deco.identity.profile.WebTopCardCore-19`);
const urn = JSON.stringify(topo).match(/urn:li:fsd_profile:[\w-]+/)[0];
const sk = await api(
  `/identity/dash/profileSkills?q=viewee&profileUrn=${encodeURIComponent(urn)}&count=100`,
  'application/vnd.linkedin.normalized+json+2.1',
);
const competencias = sk.included.filter(i => i.name).map(i => i.name);
```

| O que ler | Endpoint (depois de `/voyager/api`) | Situação em 13/10/2026 |
|---|---|---|
| Publicações, projetos, prêmios, certificados, voluntariado, organizações e idiomas | `/identity/profiles/<vanity>/<secao>?count=50`, com `<secao>` = `publications`, `projects`, `honors`, `certifications`, `volunteerExperiences`, `organizations` ou `languages` | Funciona |
| Competências | `/identity/dash/profileSkills?q=viewee&profileUrn=<urn>&count=100`, com o header `accept: application/vnd.linkedin.normalized+json+2.1`; nomes em `included[].name` | Funciona, mas não traz as validações |
| Topo do perfil (de onde sai o URN) | `/identity/dash/profiles?q=memberIdentity&memberIdentity=<vanity>&decorationId=com.linkedin.voyager.dash.deco.identity.profile.WebTopCardCore-19` | Funciona |
| Recomendações recebidas | `/identity/profiles/<vanity>/recommendations?q=received&recommendationStatuses=List(VISIBLE)` | Funciona |
| `profileView`, `positions`, `educations`, `skills` e `profileContactInfo` | `/identity/profiles/<vanity>/...` | Dá 410 |

Onde a API dá 410, só a página de detalhes serve: `/in/<vanity>/details/experience/`, `/details/education/` e `/details/skills/` (esta também mostra as validações). Informações de contato se conferem reabrindo o formulário.

Use a API só para ler. Não edite por POST ou PUT: isso pula as validações do formulário e o controle de notificação, e é automação que o usuário não vê.

**O token é a sessão do usuário.** Quem tem o valor do JSESSIONID age como ele, logado. Por isso:
- leia o cookie só dentro do `fetch`, como no `api()` acima, sem guardá-lo em variável;
- nunca o imprima: nada de `console.log`, e não termine a chamada com o token ou com `document.cookie`, porque a ferramenta devolve o valor da última expressão;
- nunca o grave nem o registre: nem em arquivo, nem no plano, nem na memória, nem no chat.

## URLs dos formulários

| O que | URL |
|---|---|
| Lista de uma seção, com os links "Editar" | `/in/<vanity>/details/<secao>/`. O slug aparece no link "Exibir todos" da seção, por exemplo `experience`, `education`, `projects`, `skills`, `featured` e `languages`. |
| Editar um item | `/in/<vanity>/details/<secao>/edit/forms/<id>/`, com o `<id>` tirado do link "Editar" da lista |
| Competência nova | `/in/<vanity>/skills/edit/forms/new/` |
| Idioma novo | `/in/<vanity>/details/languages/edit/forms/new/` |
| Informações de contato | `/in/<vanity>/edit/forms/contact-info/new/` (sem o `new/`, dá 404) |
| Item novo nas outras seções | Botão de adicionar na página `/details/<secao>/` ou "Adicionar seção" no perfil. Leia a página para achar o rótulo. |
| Reordenar destaques | Clique no link de reordenar dentro de `/details/featured/`. A URL direta dá erro (ver Destaques). |

Para tirar os ids de edição de uma lista:

```js
[...document.querySelectorAll('a[href*="/edit/forms/"]')]
  .map(a => [a.closest('li')?.innerText.split('\n')[0], a.href]);
```

## Autocompletar

Competência, empresa, instituição e cargo usam autocompletar. A primeira sugestão nem sempre é a certa. Num teste real, digitar "Prisma" (o ORM) e confirmar às cegas cadastrou "Prisma Photo Editor".

Depois de digitar, espere as sugestões e liste todas antes de confirmar:

```js
[...document.querySelectorAll('[role=option]')].map(o => o.innerText.trim());
```

Escolha a opção que bate exatamente com o plano. Se nenhuma bater, não aperte Enter: use uma equivalência da tabela abaixo ou pergunte ao usuário.

| Pretendido | O que o LinkedIn sugere | Use |
|---|---|---|
| Prisma (ORM) | "Prisma Photo Editor" em 1º lugar | "Prisma", a opção exata |
| LGPD | Só "RGPD" (GDPR) | "Privacidade dos dados" |
| Single Sign-On | "Okta Single Sign-On" | "Logon único (SSO)" |

Registre no plano cada equivalência usada. Assim o usuário sabe por que o nome ficou diferente.

Em empresa e instituição, a opção escolhida define o logo e a página ligada ao item. Confira o nome completo. Se houver mais de uma página parecida, pergunte qual é a certa.

## Cargos normalizados

O campo de cargo troca o texto digitado por um cargo padronizado da lista. Por exemplo, "Desenvolvedora de Software Pleno" pode virar "Desenvolvedor de software".

1. Digite o cargo.
2. Feche as sugestões com Escape.
3. Leia o valor do campo (`input.value`) e compare com o plano.
4. Se mudou, limpe e digite de novo, sem aceitar sugestão.
5. Depois de salvar, confira o cargo em `/details/experience/`.

## Foco e digitação

- **Não atribua `.value` por JS.** Os campos são React controlados ou `contenteditable`. Mudar o valor direto no DOM pode não atualizar o estado do formulário, e o texto salvo pode ser o antigo.
- **Dê foco por JS e digite com o teclado real.** Use `el.focus()` no campo e depois a ação de digitar da ferramenta.
- **Confira o foco depois de um Escape.** Ele pode ir para a busca global. Antes de digitar, leia `document.activeElement`. Se o foco estiver na busca, você digita lá e dispara uma pesquisa.
- **Para limpar um campo,** use `el.select()` e depois Backspace. O atalho cmd+a não funcionou.
- **Leia de volta o que digitou** (`el.value` ou `el.innerText`) e compare com o texto do plano, inclusive o tamanho.

## Salvar e conferir

1. Leia todos os campos do formulário e compare com o plano.
2. Desligue a notificação à rede (ver a próxima seção).
3. Salve. Clicar no botão por JS funciona, porque o clique dispara o handler do React:

   ```js
   [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'Salvar')?.click();
   ```

4. Se o formulário não fechar, leia a mensagem de erro dele antes de tentar de novo.
5. Recuse as ofertas que aparecerem (ver Recusar ofertas).
6. Confira o que foi salvo pela página de detalhes (ou, como alternativa, pela API), e nunca só pela tela do perfil.
7. Marque o item no plano.

## Desligar a notificação à rede

Alguns formulários, como o de experiência, têm um controle para compartilhar a mudança com a rede. Deixe desligado em todas as edições, a menos que o usuário peça o contrário.

Por quê: dezenas de edições seguidas viram dezenas de avisos de "atualizou o perfil" no feed das conexões. Isso queima a primeira impressão. O anúncio do perfil novo deve ser um post planejado pelo usuário.

Leia o formulário para achar o controle: é um switch ou checkbox com texto sobre rede ou compartilhar. Antes de salvar, confirme que ele está com `aria-checked="false"` ou desmarcado.

## Recusar ofertas

Depois de salvar, o LinkedIn pode oferecer:

- compartilhar a atualização num post;
- pedir uma recomendação;
- testar o Premium;
- adicionar mais itens sugeridos.

Feche todas pela opção de dispensar ("Agora não", "Fechar" ou o X; leia o modal para achar o rótulo). Compartilhar é publicar em nome do usuário. Pedir recomendação é enviar mensagem. Premium é assinatura paga. As três decisões são do usuário.

## Competências

1. **Compare com a lista atual** (em `/details/skills/` ou, como alternativa, pela API; ver "Consulte antes de criar") antes de adicionar. Ignore maiúsculas e procure variantes com erro de digitação, como "Kubernets" para "Kubernetes". Assim você não cria quase-iguais.
2. **Abra** `/in/<vanity>/skills/edit/forms/new/`, digite o nome e escolha a opção exata do autocompletar.
3. **Marque os vínculos.** O formulário mostra as experiências, a formação e os projetos onde a competência foi usada, como `[role=checkbox]` com `aria-label`. Marque só os itens que o plano aponta como evidência:

   ```js
   [...document.querySelectorAll('[role=checkbox]')]
     .map(c => [c.getAttribute('aria-label'), c.getAttribute('aria-checked')]);
   ```

4. **Desmarque "Siga esta competência".** Ela assina conteúdos do tema no feed do usuário, e ninguém pediu isso.
5. **Respeite o limite de 100 competências.** Se o plano passar disso, pergunte quais saem.
6. **As 5 principais** aparecem no Sobre. Escolha-as no formulário do Sobre, alinhadas ao título, depois que todas existirem. Leia o formulário para achar o campo.
7. **Validações** não vêm na API. Confira em `/details/skills/`.

## Excluir

Exclua só com pedido explícito do usuário, item a item. Isso vale também para as duplicatas que você mesmo criou: registre o erro no plano e pergunte. Por quê: excluir não tem volta, e entre duas versões o usuário pode preferir a que você descartaria. Numa sessão real, o classificador de segurança bloqueou uma exclusão que não tinha sido pedida, e isso estava certo.

Com o pedido em mãos:

1. Se houver duplicatas, compare os detalhes (coautores, páginas, datas, links) nos formulários de edição ou pela API e diga ao usuário qual fica.
2. Abra o formulário de edição do item que sai.
3. Clique em "Excluir ..." no fim do formulário.
4. A confirmação abre com atraso. Espere cerca de 1 s antes de ler a tela ou tirar screenshot.
5. Clique em "Excluir" no diálogo.
6. Confira na página de detalhes (ou pela API) que só o item certo saiu.

## Destaques

- Use 3 ou 4 destaques. O 1º é o produto que se pode clicar.
- Para adicionar, use o botão de adicionar em `/details/featured/` e leia a página para achar o rótulo.
- Para reordenar, abra a tela de reordenar clicando no link dentro de `/details/featured/`. A URL direta `/details/featured/reorder/` dá erro.
- O teclado não move os itens. Arraste com o mouse, pela alça do item até a posição nova. A ordem salva sozinha.
- Recarregue `/details/featured/` e leia a ordem para conferir.

## Informações de contato

- Abra `/in/<vanity>/edit/forms/contact-info/new/`.
- Cabem até 3 sites. Cada um tem um tipo (Portfólio, Empresa, Pessoal etc.). Use "Adicionar site" para abrir o próximo campo.
- Escolha o tipo que descreve o site, por exemplo Portfólio para o GitHub ou o portfólio, e Empresa para o produto.
- Telefone, endereço e aniversário são dados pessoais. Preencha só se o usuário pedir.
- A API de contato dá 410. Confira reabrindo o formulário.

## Idiomas

- Consulte os idiomas atuais em `/in/<vanity>/details/languages/` (pela API, `/identity/profiles/<vanity>/languages`).
- Para um idioma novo, abra `/in/<vanity>/details/languages/edit/forms/new/`.
- Use o nível que o usuário declarou, sem inflar, entre as opções da lista (por exemplo, "Fluente ou nativo" e "Nível avançado"). Se houver certificado, o nível segue o certificado.
- Não mude um idioma que já existe sem perguntar. O usuário pode querer manter como está.

## Perfil em segundo idioma

- Se o perfil em inglês ainda não existir, crie-o pela opção de perfil em outro idioma da página do perfil, desde que isso esteja no escopo aprovado.
- Para editar, use as URLs dos formulários com `?language=en&country=US&locale=en_US` no fim, por exemplo `/in/<vanity>/details/experience/edit/forms/<id>/?language=en&country=US&locale=en_US`.
- No formulário, clique na aba "English" antes de digitar. Sem isso, o texto pode cair na versão em português.
- Aplique o que o plano traz para o segundo idioma: em geral, headline, About e as experiências principais. Se o alvo é o exterior, faça isso item a item, junto com o português (ver "Ordem de aplicação").
- Confira lendo a página do perfil com os mesmos parâmetros, e confira também que o texto em português continua igual.

## Outras armadilhas

- **Anexos:** a ferramenta pode não conseguir enviar arquivo, como o PDF de um certificado. Se não conseguir, isso vira pendência do usuário.
- **Captcha, verificação ou termos para aceitar:** pare e peça ao usuário. Nunca tente resolver nem aceite por ele.
- **Ritmo:** poucas edições, uma por vez e conferidas. Nada de laço que cria itens em série. Volume de máquina arrisca restrição da conta, e os termos do LinkedIn proíbem bots.

## Registrar no plano

Atualize a seção "Status da aplicação" no topo do plano durante a aplicação e de novo no fim. O usuário precisa saber o que mudou no perfil dele, o que deu errado e o que falta. Registre seus próprios erros com a mesma clareza do resto.

```markdown
## Status da aplicação (<data>, pelo navegador)

**Aplicado e conferido:** título; Sobre; 5 principais competências; 4 experiências (cargos, datas, descrições, competências); 3 projetos com links e competências; 2 certificados; destaques (SaaS de agendamento, artigo, post do TCC). Conferido pelas páginas de detalhes e, onde precisou, pela API. Notificação à rede desligada em todas as edições; nenhuma oferta de compartilhar, de recomendação ou de Premium foi aceita.

**Decisões do usuário durante a aplicação:** <ex.: manter o nível de inglês como estava>.

**Equivalências do autocompletar:** "LGPD" entrou como "Privacidade dos dados" (o LinkedIn só oferece RGPD).

**Meus erros, para você decidir (não excluo sem seu pedido):**
- [ ] Publicação "<título>" ficou duplicada: recadastrei sem consultar antes de criar. Sugiro manter a que tem <detalhe>.
- [ ] A competência "<nome errado>" entrou no lugar de "<nome certo>" pelo autocompletar.

**Para você fazer:**
- [ ] Anexar o PDF do certificado <nome> (a ferramenta não envia arquivo).
- [ ] Colar a URL da credencial <nome> (preciso do link).
- [ ] Etapa 6: pedidos de recomendação, Open to work, convites e posts dependem de envio seu.
```

Se houver memória entre sessões disponível, salve nela as armadilhas novas que surgiram, como seletores ou endpoints que mudaram, para a próxima aplicação não tropeçar nelas.

## Enviar convites (só com lista e texto aprovados)

O padrão é você preparar e o usuário enviar. Envie pelo navegador só se ele pedir e aprovar no chat, item a item, a lista de pessoas (do `recrutadores.md`) e o texto exato de cada nota. Por quê: o convite sai com o nome dele, e convite enviado não se desfaz sem deixar rastro.

Antes de começar, conte cada nota com `<diretório base desta skill>/scripts/contar.py --limite convite`.

Para cada pessoa da lista aprovada, uma de cada vez (convite aprovado sem nota pula os passos 3 a 5):

1. Abra o perfil pela URL da lista e confira se o nome bate.
2. Ache o botão "Conectar". Às vezes ele fica no topo do perfil e às vezes no menu "Mais", então leia a página antes de clicar. Não clique em "Seguir" no lugar dele. Se aparecer "Pendente", ou se a pessoa já for conexão de 1º grau, pule e anote.
3. Clique em "Adicionar nota". O LinkedIn mostra ali a cota restante: em out/2026, a conta gratuita tinha 3 notas por mês. Trate o número como observado naquela data, não como garantia. Se a cota acabou, pare e pergunte se o convite vai sem nota.
4. Clique no campo da nota e digite com o teclado real. O campo não é um `<textarea>`, então não procure um nem atribua o valor por JS.
5. Leia de volta o texto e o contador da caixa e compare com o texto aprovado.
6. Clique em "Enviar".
7. Confirme pelo aviso "Convite enviado a X.", com X igual ao nome da lista. Sem o aviso, não reenvie: recarregue o perfil e veja se o botão virou "Pendente".
8. Marque `[x]` e a data no `recrutadores.md`.

**Ritmo humano.** Um convite por vez, com pausa entre eles, e nunca mais do que a rotina do dia prevê. Nada de laço, script ou lote: convite em lote arrisca a restrição da conta, e os termos do LinkedIn proíbem bots.

**Pare na hora** se aparecer aviso de limite de convites, pedido do e-mail da pessoa, captcha ou verificação. Avise o usuário e anote no `recrutadores.md` até onde chegou.
