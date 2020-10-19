# mattermost-command-meet

![screenshot](https://github.com/instruct-br/mattermost-command-meet/blob/main/screenshots/screenshot.jpg)

## Descrição

Essa API faz com que seja possível criar instantaneamente uma sala no **Google Meet** com o comando `/meet`.

O comando aceita o nome de uma sala como primeiro argumento, e uma lista de users para serem marcados como segundo argumento:

```
/meet nome_da_sala @user1 @user2 @user3
```

O comando retorna o link da sala, assim como uma mensagem marcando todos os usuários convidados.

## Adicionando o comando ao Mattermost

Para adicionar o comando, siga [este](https://docs.mattermost.com/developer/slash-commands.html#custom-slash-command) guia.
