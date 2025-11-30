# Guia de Implantação no GitHub Pages

Este guia descreve os passos para colocar o site "Estatística Aplicada" no ar usando o GitHub Pages.

## 1. Enviar as alterações para o GitHub

Como eu (o assistente) não tenho permissão direta para fazer o "push" no seu repositório, você precisará executar o seguinte comando no seu terminal:

```bash
git push upstream main
```

*Nota: Se o comando acima falhar, verifique se o remote correto é `upstream` ou `origin` com `git remote -v`.*

## 2. Configurar o GitHub Pages

1.  Acesse o repositório no GitHub: [https://github.com/alexsantossp71-lgtm/workspace_estatistica_prova](https://github.com/alexsantossp71-lgtm/workspace_estatistica_prova)
2.  Clique na aba **Settings** (Configurações) no topo da página.
3.  Na barra lateral esquerda, clique em **Pages**.
4.  Na seção **Build and deployment**:
    *   Em **Source**, selecione **Deploy from a branch**.
    *   Em **Branch**, selecione `main` e a pasta `/ (root)`.
    *   Clique em **Save**.

## 3. Acessar o Site

Após alguns minutos, o GitHub irá processar o site e ele estará disponível em um link fornecido na mesma página de configurações (geralmente algo como `https://alexsantossp71-lgtm.github.io/workspace_estatistica_prova/`).

## Solução de Problemas

*   **Imagens não carregam**: Verifique se os caminhos das imagens no código são relativos (ex: `./images/foto.jpg` em vez de `/images/foto.jpg`).
*   **CSS/JS não carrega**: O mesmo vale para arquivos CSS e JS. O GitHub Pages pode servir o site em um subdiretório, então caminhos absolutos (começando com `/`) podem quebrar.

---
**Status Atual**:
*   Arquivos locais commitados: Sim
*   Push para remoto: Pendente (Aguardando ação do usuário)
