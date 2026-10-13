# linkedin-para-devs

Uma skill do [Claude Code](https://claude.com/claude-code) para desenvolvedores melhorarem o LinkedIn com base em fatos, não em adjetivos. Ela foi pensada para devs brasileiros e trabalha em português.

A skill junta evidências do seu trabalho (repositórios, documentos e o que só você sabe), diagnostica o seu perfil e escreve o plano campo a campo. Depois, monta o plano de rede até o seu prazo, com textos prontos, ideias de post e uma lista curada de recrutadores. Se você quiser, ela também aplica as edições do perfil pelo navegador, item a item.

Ela **prepara**. Você **envia**.

## Escopo

A skill cuida da sua presença no LinkedIn e do funil básico de vagas: alertas, candidaturas, conversas com recrutador e entrevistas, com meta semanal. Ela não escreve CV nem se candidata por você.

O caminho muda conforme o seu caso:
- **Júnior ou 1º emprego:** projetos e destaques vêm primeiro, e os convites começam por colegas de trabalho, de turma e de comunidades locais.
- **Sênior:** com código privado, a evidência sai do seu relato (escopo, decisões, pessoas lideradas, incidentes), e a rede mira recrutadores e tech leads das empresas-alvo, com menos volume.
- **Exterior:** o perfil em inglês é escrito junto com o português, e a busca de recrutadores mira empresas remote-first, com aceite esperado menor.

## O que você recebe

| Arquivo | O que tem |
|---|---|
| `linkedin.md` | Diagnóstico, status da aplicação e todos os textos do perfil prontos para colar, com a contagem de caracteres: título, Sobre, experiências, projetos, competências, destaques e a versão em inglês. |
| `rede-linkedin.md` | Linha de base, plano semana a semana até o prazo (com as premissas declaradas), rotina diária, funil de vagas (se o objetivo for vaga), limites da conta gratuita, textos de convite, validação e recomendação e ideias de post técnico tiradas dos seus projetos. |
| `recrutadores.md` | Lista curada de recrutadores ou tech leads, com prioridade, motivo e link, mais os excluídos e as próximas buscas. |
| `checklist.md` | O que fazer em cada dia nos próximos 10 a 14 dias. |

## Instalação

### Como plugin (recomendado)

No Claude Code, rode:

```
/plugin marketplace add periclesanfe/linkedin-para-devs
/plugin install linkedin-para-devs@linkedin-para-devs
```

Para atualizar depois:

```
/plugin marketplace update linkedin-para-devs
```

### Copiando a pasta

Se preferir não usar plugins, copie a skill para a sua pasta de skills pessoais:

```bash
git clone https://github.com/periclesanfe/linkedin-para-devs.git
mkdir -p ~/.claude/skills
cp -R linkedin-para-devs/skills/linkedin-para-devs ~/.claude/skills/
```

Para usar só num projeto, copie para `.claude/skills/` dentro dele.

### O que ajuda ter (opcional)

- **`gh` (GitHub CLI) autenticado:** para a skill ler os seus repositórios e tirar daí período, stack e o que você fez.
- **Python 3:** para o script que conta caracteres.
- **Uma ferramenta de navegador ligada ao Claude Code**, com o LinkedIn logado por você: para ler o perfil, aplicar as edições e buscar recrutadores. Sem ela, a skill trabalha com o PDF do perfil ou com o texto que você colar, e você aplica à mão.

## Como usar

A skill dispara sozinha quando você fala de LinkedIn, perfil, recrutadores, networking ou busca de emprego como dev. Alguns pedidos de exemplo:

- "Quero melhorar meu LinkedIn até o fim do mês. Sou dev back-end, Node e Go, e quero vaga remota."
- "Reescreve meu título e o Sobre. Meus repositórios estão no GitHub, no meu usuário e na org da empresa."
- "Estou procurando o primeiro emprego como dev. Por onde começo?"
- "Monta um plano de networking de 6 semanas, com os textos de convite."
- "Tenho um SaaS de agendamento no ar. Me dá ideias de post técnico sobre ele."
- "Me ajuda a achar recrutadores de tecnologia em Recife que contratam front-end."
- "Aplica no meu perfil as etapas 1 a 3 do `linkedin.md`."

O processo tem oito fases: combinar, evidências, diagnóstico, plano do perfil, aplicar (opcional), rede e SSI, recrutadores e checklist. Você pode pedir só uma parte. Antes de escrever, a skill faz todas as perguntas numa mensagem só: o perfil atual (PDF ou texto), a sua situação hoje, se a busca é discreta, o alvo, o prazo, 3 a 5 vagas-alvo, o seu GitHub, o tempo por dia e o que é privado. Se o pedido for vago, ela já devolve um rascunho de título junto com as perguntas.

## O que a skill não faz

- Não escreve CV nem se candidata a vagas.
- Por padrão, não envia convites, mensagens, posts nem pedidos de recomendação, e não liga o "Open to work". Ela deixa tudo pronto; quem envia é você. Se você pedir, ela envia convites pelo navegador, só os da lista e com o texto que você aprovou, um a um.
- Não faz login, não digita senha e não resolve captcha.
- Não edita o perfil sem você aprovar o escopo, e não exclui nada sem pedido explícito, item a item.
- Não faz automação em massa: nada de convites ou mensagens em lote.
- Não inventa números nem infla experiência. Sem fonte, ela pergunta ou deixa fora.
- Não garante vaga nem pontuação de SSI. As metas são estimativas, com as premissas escritas.
- Não monta dossiê de ninguém. A lista de recrutadores guarda só dados profissionais e públicos, sem cruzar com outras fontes.

## Cota de notas nos convites

Na conta gratuita, o LinkedIn limita as notas personalizadas nos convites. A cota aparece ao clicar em "Adicionar nota": em outubro de 2026 eram 3 por mês, e o número pode mudar. Por isso a skill guarda as notas para recrutadores e tech leads e, para o resto, prepara a 1ª mensagem depois do aceite.

## Privacidade

Os arquivos gerados têm os seus dados e, no `recrutadores.md`, dados de terceiros. Guarde tudo num repositório **privado** ou fora de controle de versão.

## Aviso sobre os termos do LinkedIn

Este projeto não tem relação com o LinkedIn.

Os termos de uso do LinkedIn proíbem bots, automação e coleta de dados em massa (scraping). A skill foi desenhada para ficar longe disso:
- as edições do perfil são poucas, pedidas e conferidas por você;
- a leitura de buscas se limita a algumas páginas que você mesmo abriria;
- nenhum convite ou mensagem sai sem você aprovar a lista e o texto.

Ainda assim, quem responde pela conta é você. A leitura do perfil pela API interna do site (não documentada, usada só como alternativa e com aviso) e o extrator da página de busca podem deixar de funcionar ou ser vistos como automação. Se quiser risco zero, use só o planejamento e aplique tudo à mão. A lista de recrutadores também pode ser feita à mão.

As instruções de navegador foram testadas com a interface do LinkedIn em português, em outubro de 2026. A interface muda. Por isso, a skill confere cada item antes e depois de salvar.

## Licença

[MIT](LICENSE).
