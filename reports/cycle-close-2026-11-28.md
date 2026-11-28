# Encerramento do ciclo · 28 de novembro de 2026

A exploração contínua foi encerrada e o timer horário do Community Explorer foi desabilitado no host. A fila permanece no GitHub.

## Entregas

- A fila encerrou o ciclo com 800 issues, 747 abertas e 53 fechadas. Entre as fechadas, 41 têm o rótulo `published`. A contagem de rótulos não equivale a uma auditoria do catálogo público. [Fila do Community Explorer](https://github.com/UFFeScience/akoflow-community-explorer/issues?q=is%3Aissue).
- As últimas candidatas, #791 a #800, estão registradas como propostas com referências, atividades paralelas e critérios de aceitação. As prévias de cálculo foram produzidas localmente. [Última proposta, BraSNAM](https://github.com/UFFeScience/akoflow-community-explorer/issues/800).
- As evidências concluídas de DTW, convolução gaussiana, cinemática inversa e caminhada de partículas já estão em `akoflow-examples/main`, nos commits `22d2fa5`, `1ea8462`, `a6aa54c` e `6298b8b`. As issues #662 e #672 estão fechadas. [Relatório com execuções e links](2026-11-28.md).

## Próximo ciclo

1. [#780](https://github.com/UFFeScience/akoflow-community-explorer/issues/780) · Retomar do estado confirmado da referência gaussiana. Conferir se já existe publicação pública, verificar os perfis registrados e reproduzir a importação em ambiente limpo antes de fechar.
2. [#395](https://github.com/UFFeScience/akoflow-community-explorer/issues/395) · Repetir a importação e execução completa com uma versão oficial que contenha a correção de preflight de receitas compartilhadas. O resultado com daemon corrigido já está registrado.
3. Escolher a próxima proposta brasileira pelo valor da figura e dos dados baixáveis, pela independência entre as atividades e pela viabilidade da validação. Há 32 issues abertas com rótulo `blocked` ou `needs-*`, contando cada issue uma única vez. [Fila aberta](https://github.com/UFFeScience/akoflow-community-explorer/issues?q=is%3Aissue+is%3Aopen).
4. Revisar o material local antes de reiniciar a automação. O checkout principal de `akoflow-examples` tem alterações não comitadas nos exemplos Buffon e Shannon BSC, e os worktrees de DTW e cinemática têm YAMLs não rastreados. Os cinco arquivos do commit local de WeatherBench `0432298` já têm conteúdo idêntico no remoto. As prévias geradas para o chat permanecem no diretório local de artefatos do ciclo.
