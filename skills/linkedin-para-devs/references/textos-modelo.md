# Textos-modelo

Modelos para a seção "Textos prontos" do `rede-linkedin.md`. Adapte cada um ao usuário, com fatos das fichas de evidência, e preencha os trechos entre [colchetes].

Regras de uso:
- **Você prepara, o usuário envia**, um a um e à mão. São mensagens em nome dele.
- **Conte depois de preencher.** As contagens abaixo usam `len()` do Python (a quebra de linha conta 1) e já incluem os colchetes. A "folga" é o que ainda cabe no preenchimento. Depois de adaptar, rode o script pelo caminho absoluto, `python3 <diretório base desta skill>/scripts/contar.py --limite convite` (ou `--limite mensagem`), e escreva a contagem ao lado do texto. O caminho relativo falha, porque o diretório de trabalho não é a pasta da skill.
- **Nenhum número sem fonte.** Se um texto cita um resultado, ele vem de uma ficha de evidência ou de uma resposta do usuário.
- **Ajuste o gênero** de "obrigado" e afins ao usuário.
- **Peça só o que a pessoa viu.** Validação ou recomendação sobre algo que a pessoa não acompanhou vale pouco e a deixa numa posição chata.

Exemplo usado nos trechos preenchidos (inventado): **Ana Souza (fictícia), dev front-end em Recife, React/TypeScript**, há 2 anos num e-commerce e com um SaaS de agendamento próprio, feito com um sócio que cuida do back-end. É a mesma persona das outras referências.

**Busca discreta:** antes de usar as seções 1 e 2, leia a 2.5. Pedido a colega atual avisa a empresa.

## 1. Pedido de validação de competências

Mande por mensagem direta, só para conexões de 1º grau. Cite 2 ou 3 competências, as que aquela pessoa viu o usuário usar. Antes de pedir, o usuário valida nos colegas as competências que viu na prática: a reciprocidade aumenta a resposta e é honesta.

### 1.1 Colega de trabalho (440 caracteres)

```text
Oi, [Nome], tudo bem?

Estou arrumando meu LinkedIn e as competências do perfil ainda têm poucas validações. Se fizer sentido para você, pode validar as que me viu usar em [projeto ou empresa]: [2 ou 3 competências]? Só as que você acompanhou de perto.

Se quiser, faço o mesmo: me diz quais competências suas você quer destacar e eu valido as que vi você usar.

Link direto: linkedin.com/in/[seu-usuario]/details/skills/

Valeu!
[Seu nome]
```

### 1.2 Colega de estudo ou pesquisa (399 caracteres)

```text
Oi, [Nome], tudo bem?

Estou arrumando meu LinkedIn e queria uma ajuda rápida: validar as competências que você me viu usar em [disciplina, projeto de pesquisa ou TCC]: [2 ou 3 competências]. Só as que você acompanhou.

Faço o mesmo pelas suas: me diz quais você quer destacar e eu valido as que vi você usar no projeto.

Link direto: linkedin.com/in/[seu-usuario]/details/skills/

Valeu!
[Seu nome]
```

### 1.3 Tabela "quem valida o quê"

Monte uma tabela para cada usuário, a partir das fichas de evidência: a stack de cada projeto sai do código (package.json, Dockerfile e afins), e quem estava junto sai dos commits ou da resposta do usuário. A coluna "Não peça" evita pedir o que a pessoa não viu.

Modelo, com o exemplo da Ana:

| Onde trabalharam juntos | Peça | Não peça |
|---|---|---|
| E-commerce, equipe de front-end | React · TypeScript · Storybook | Node.js, que a equipe de front não usa |
| SaaS de agendamento, com o sócio | Next.js · TypeScript | Node.js, porque o back-end é dele |
| Projeto de extensão da faculdade | Python · Pesquisa científica | React e TypeScript, que o projeto não usou |

Abaixo da tabela, diga por onde começar: o contexto em que aparecem mais competências principais é o caminho mais curto para a meta de validações.

## 2. Pedido de recomendação

O usuário escolhe de 2 a 4 pessoas que viram o trabalho dele de perto: gestor, colega sênior, cliente ou orientador. Quem já topou vai primeiro.

### 2.1 Versão genérica (330 caracteres)

```text
Olá, [Nome], tudo bem?

Estou atualizando meu perfil e queria pedir uma recomendação sua sobre [o nosso trabalho em X]. Se ajudar, três pontos que você acompanhou:
- [ponto 1];
- [ponto 2];
- [ponto 3].

Escreva do seu jeito e só sobre o que viu de perto. Se preferir, te mando um rascunho para você ajustar.

Obrigado!
[Seu nome]
```

### 2.2 Pontos que a pessoa pode citar

Cada ponto é uma entrega concreta (verbo + o quê + resultado), que a pessoa viu e que tem fonte. Ponto vago ("é muito dedicado") gera recomendação vaga. Monte a tabela por contexto e escolha 2 ou 3 pontos por pedido.

| Contexto | Pontos |
|---|---|
| SaaS de agendamento, pedido ao sócio (exemplo da Ana) | a migração do painel de JavaScript para TypeScript sem parar as entregas; a tela de agenda refeita depois de testes com usuários; [resultado com número e fonte] |
| [contexto] | [ponto 1]; [ponto 2]; [ponto 3] |

Deixe fora o que é sensível, como falhas de segurança e nomes de clientes, mesmo que a pessoa tenha visto.

### 2.3 Lembrete, cerca de 1 semana depois (194 caracteres)

```text
Oi, [Nome]! Passando para lembrar do pedido de recomendação que te mandei pelo LinkedIn semana passada. Se ficar mais fácil, te mando um rascunho curto para você ajustar ou reescrever. Obrigado!
```

Um lembrete só. Depois disso, a pessoa já respondeu com o silêncio.

### 2.4 Agradecimento (180 caracteres)

```text
Recebi sua recomendação, [Nome]. Muito obrigado! [Uma frase sobre um trecho específico do texto.] Se quiser uma recomendação minha sobre [o trabalho que vi você fazer], é só falar.
```

A recomendação só aparece no perfil depois que o usuário a aceita na notificação.

### 2.5 Pedidos na busca discreta

Quando a busca é discreta, colega atual e gestor ficam fora dos pedidos de validação e de recomendação. Eles comentam, e o pedido avisa a empresa. Peça a ex-colegas, ex-gestores, turma, professores e clientes de projeto próprio. Um colega atual só entra se for de confiança e o usuário decidir.

Tire do texto "Estou arrumando meu LinkedIn" (1.1 e 1.2) e "Estou atualizando meu perfil" (2.1), que soam como procura de vaga. Vá direto ao pedido ("Queria te pedir uma ajuda rápida: ...") e conte de novo.

## 3. Convites de conexão (nota de até 200 caracteres)

A conta gratuita permite poucas notas por mês: em out/2026 eram 3, e o LinkedIn mostra a cota restante ao clicar em "Adicionar nota". Trate o número como observado naquela data, não como garantia. Com tão poucas, escolha no início do mês quem recebe nota, de preferência recrutadores e tech leads da prioridade A. Quando acabar, convide sem nota e mande o texto como 1ª mensagem depois do aceite. A caixa da nota tem contador: confira depois de preencher.

O que vale para todos: diga por que aquela pessoa, quem é o usuário em uma linha e não peça vaga. "Gostaria de adicionar você à minha rede" não diz nada.

### 3.1 Recrutador

**A. Recrutador da área (148 caracteres, folga de 52)**
```text
Olá, [Nome]. Vi que você recruta para [área]. Sou dev [especialidade] ([stack principal]) e trabalho com [tipo de produto]. Gostaria de me conectar.
```

Preenchido com o exemplo da Ana (138 caracteres, folga de 62):
```text
Olá, [Nome]. Vi que você recruta para front-end. Sou dev front-end (React, TypeScript) e trabalho com e-commerce. Gostaria de me conectar.
```

**B. Recrutador de uma vaga específica (149 caracteres, folga de 51)**
```text
Olá, [Nome]. Vi a vaga de [cargo] na [empresa]. Trabalho com [stack da vaga] em [tipo de produto]. Gostaria de me conectar e saber mais sobre o time.
```
Em [stack da vaga], ponha só o que o usuário usa de fato.

### 3.2 Tech lead

**A. A partir de um post dele (156 caracteres, folga de 44)**
```text
Olá, [Nome]. Li seu post sobre [tema] e [concordo com X / gostei da parte sobre X]. Sou dev [especialidade] ([stack]) e quero acompanhar o que você publica.
```
O usuário precisa ter lido o post. Elogio genérico a um post que ele não leu aparece logo.

**B. A partir da stack da empresa (153 caracteres, folga de 47)**
```text
Olá, [Nome]. Vi que o time da [empresa] usa [tecnologia]. Também trabalho com [tecnologia] em [tipo de produto] e queria acompanhar o que vocês publicam.
```

### 3.3 Quem reagiu ao seu post (131 caracteres, folga de 69)

```text
Olá, [Nome]. Obrigado por reagir ao meu post sobre [tema]. Sou dev [especialidade] ([stack]) e quero acompanhar o que você publica.
```
Essas pessoas já interagiram com o usuário, então o convite pode ir sem nota. Guarde a nota para quando a cota sobrar.

### 3.4 Colega de evento ou faculdade

**A. Evento (164 caracteres, folga de 36)**
```text
Olá, [Nome]. Estivemos no [evento]: [assisti à sua palestra sobre X / conversamos sobre X]. Sou dev [especialidade] ([stack]) e quero acompanhar o que você publica.
```

**B. Faculdade (146 caracteres, folga de 54)**
```text
Olá, [Nome]. Estudamos juntos em [curso e instituição]. Hoje sou dev [especialidade] em [tipo de empresa ou produto]. Bom te reencontrar por aqui.
```

### 3.5 Em inglês, para recrutador internacional

Use quando o usuário tem inglês para entrevista e busca vaga remota no exterior. "Based in Brazil" já responde a dúvida do fuso. Os mesmos limites valem.

**A. Recruiter in the area (151 caracteres, folga de 49)**
```text
Hi [Name], I see you recruit for [area]. I'm a [specialty] developer based in Brazil ([main stack]), working on [type of product]. I'd like to connect.
```

**B. Specific opening (142 caracteres, folga de 58)**
```text
Hi [Name], I saw the [role] opening at [company]. I work with [job's stack] on [type of product] and I'm based in Brazil. I'd like to connect.
```

### 3.6 Busca discreta

Use quando o usuário está empregado e não quer que a procura apareça. A nota não fala de vaga, de "aberto a" nem de "novos desafios", porque o recrutador pode atender o empregador atual ou conhecer gente de lá. O convite se apoia no trabalho ou no conteúdo da pessoa.

**Recrutador que publica (158 caracteres, folga de 42)**
```text
Olá, [Nome]. Vi seus posts sobre o mercado de [área]. Sou dev [especialidade] ([stack]) e trabalho com [tipo de produto]. Quero acompanhar o que você publica.
```
Se o recrutador não publica, convide sem nota e guarde a nota para outra pessoa.

**Em inglês, para recrutador de fora (158 caracteres, folga de 42)**
```text
Hi [Name], I've been following your posts on the [area] market. I'm a [specialty] developer in Brazil ([stack]) working on [type of product]. Glad to connect.
```

Os convites de tech lead (3.2) e de colega (3.4) não falam de vaga e servem como estão. Não use os de vaga específica (3.1 B e 3.5 B). Depois do aceite, a mensagem 4.1 também serve, porque pergunta sobre o mercado sem pedir vaga. Se o usuário quiser dizer que está aberto a propostas, ele diz na conversa privada e pede sigilo.

## 4. Mensagem depois do aceite (até 500 caracteres)

Mande no dia do aceite ou no seguinte. Mensagem para conexão de 1º grau não gasta a cota de notas. O teto de 500 caracteres é desta skill, para a mensagem ser lida até o fim; o limite do LinkedIn é bem maior. Conte com `--limite mensagem`, que é esse teto de 500. O mesmo teto vale para os pedidos de validação e de recomendação das seções 1 e 2.

Não peça vaga na 1ª mensagem. Com recrutador, pergunte o que pesa na triagem: a resposta é útil e abre a conversa. Com tech lead, puxe uma conversa técnica sobre algo que o usuário fez de verdade.

### 4.1 Recrutador (371 caracteres)

```text
Obrigado por aceitar, [Nome]. Para contexto: sou dev [especialidade] em [cidade ou "remoto"] ([stack]), trabalho com [o que você faz hoje] e [uma entrega concreta, com número que tenha fonte].

Uma pergunta: nas vagas de [área] que você tem recrutado, o que mais pesa na triagem hoje? [Inglês, cloud, tempo de experiência?] Quero entender o que as empresas estão pedindo.
```
Se a pessoa responder, só então o usuário diz o que procura (área, senioridade, remoto ou presencial) e oferece o CV.

### 4.2 Tech lead (249 caracteres)

```text
Obrigado por aceitar, [Nome]. [Vi que vocês fazem X / Li seu post sobre Y.] Em [projeto], eu [decisão técnica que você tomou e o resultado]. Uma dúvida que sempre volta nesse tipo de solução: [pergunta técnica concreta]. Como vocês resolvem isso aí?
```
O tema sai de algo que já está público no perfil ou nos posts. Nada interno do empregador além do que já foi publicado.

### 4.3 Recruiter, em inglês (411 caracteres)

```text
Thanks for connecting, [Name]. For context: I'm a [specialty] developer in Brazil ([stack]), currently [what you do now], and [one concrete delivery, with a number you can back up].

Quick question: for the [area] roles you've been hiring for, what weighs most when screening candidates from Latin America? [English level, time zone overlap, years of experience?] I'd like to understand what companies look for.
```
