// extrair_busca.js: extrator da busca de pessoas do LinkedIn. Só lê a página.
//
// ATENÇÃO: o que acumular() guarda em localStorage.__rec são dados de
// terceiros. Termine sempre com lerELimpar(), que apaga a chave.
// Sessão interrompida: se a sessão cair antes do lerELimpar(), na próxima
// sessão, antes de qualquer outra coisa, cole este arquivo numa página do
// linkedin.com e rode lerELimpar(). Sem navegador, peça ao usuário para limpar
// o localStorage do linkedin.com (no console: localStorage.removeItem('__rec')).
//
// Onde rodar: numa página de resultados
//   https://www.linkedin.com/search/results/people/?keywords=...&page=N
// pelo console do navegador ou pela ferramenta de JavaScript do agente.
//
// Uso:
//   1. Espere a página carregar e role até o fim, para todos os cards aparecerem.
//   2. Cole este arquivo inteiro. Trocar de página apaga as funções, então
//      cole de novo em cada página (os dados acumulados não se perdem).
//   3. acumular('tech recruiter p1')
//        extrai os cards da página, soma em localStorage.__rec e devolve
//        o total acumulado (com repetidos). Avisa no console se vier vazio.
//   4. Vá para a próxima página ou busca e repita os passos 1 a 3.
//   5. No fim: lerELimpar()
//        devolve a lista sem repetidos (pela URL decodificada) e apaga a chave.
//        No console do Chrome, copy(JSON.stringify(lerELimpar(), null, 2))
//        já copia o resultado. Para só espiar sem apagar:
//        JSON.parse(localStorage.__rec)
//   extrairBusca('rotulo') extrai a página atual sem guardar nada.
//
// O script não clica, não convida e não abre perfis. Os nomes das conexões em
// comum ficam só no texto do campo emComum; eles não viram resultados.
// Depende do HTML do LinkedIn: cards em [role=listitem] e o grau ("2º" ou
// "2nd") ao lado do nome. Se acumular() avisar que veio vazio numa página
// cheia, o layout mudou e os seletores precisam de ajuste.

(() => {
  const GRAU = /(1º|2º|3º|1st|2nd|3rd)/;
  const SO_GRAU = /^•?\s*(1º|2º|3º|1st|2nd|3rd)\+?$/;
  const CHAVE = '__rec';

  function extrairBusca(rotulo = '') {
    const out = [];
    for (const card of document.querySelectorAll('main [role=listitem]')) {
      const a = card.querySelector('a[href*="/in/"]');
      if (!a) continue;
      const linhas = card.innerText.split('\n').map((s) => s.trim()).filter(Boolean);
      const i = linhas.findIndex((l) => GRAU.test(l));
      if (i < 0) continue;
      const nome = linhas[i].replace(/•?\s*(1º|2º|3º|1st|2nd|3rd).*/, '').trim() || linhas[i - 1] || linhas[0];
      const resto = linhas.slice(i + 1).filter((l) => !SO_GRAU.test(l) && !l.startsWith('·'));
      out.push({
        rotulo,
        nome,
        grau: linhas[i].match(GRAU)[0],
        cargo: resto[0] || '',
        local: resto[1] || '',
        emComum: (linhas.find((l) => /em comum|mutual/i.test(l)) || '').slice(0, 90),
        url: a.href.split('?')[0],
      });
    }
    return out;
  }

  function acumular(rotulo) {
    const novos = extrairBusca(rotulo);
    if (!novos.length) console.warn('Nenhum card nesta página: espere carregar, role até o fim ou confira os seletores.');
    const salvos = JSON.parse(localStorage.getItem(CHAVE) || '[]').concat(novos);
    localStorage.setItem(CHAVE, JSON.stringify(salvos));
    return salvos.length;
  }

  function lerELimpar() {
    const porUrl = new Map();
    for (const p of JSON.parse(localStorage.getItem(CHAVE) || '[]')) {
      const id = decodeURIComponent(p.url).replace(/\/+$/, '').toLowerCase();
      const visto = porUrl.get(id);
      if (!visto) porUrl.set(id, p);
      else if (!visto.rotulo.split(' | ').includes(p.rotulo)) visto.rotulo += ' | ' + p.rotulo; // achado em mais de uma busca
    }
    localStorage.removeItem(CHAVE);
    return [...porUrl.values()];
  }

  Object.assign(globalThis, { extrairBusca, acumular, lerELimpar });
})();
