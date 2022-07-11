![137392417-f320ce54-6198-475a-9e15-ec0f3d4b162d](https://user-images.githubusercontent.com/86201991/178254895-12003ad6-b49b-4e5d-9b0f-6fb21948a7ac.jpg)
<h2>1. Problema de Negócio</h2>
<h4>1.1 Contextualização</h4>
<p>A Rossmann é uma rede de drogarias de origem alemã, presente na Europa. Possui ao todo mais de 4000 lojas e o faturamento anual da rede é estimado em €10 bilhões. A gama de produtos oferecidos incluem mais de 21 mil itens que podem variar de acordo com o tamanho da loja, os principais produtos são itens destinados saúde em geral, saúde da pele, cabelos, cuidado com o corpo e infantis.</p>

<h4>1.2 Objetivos</h4>
<p>O projeto foi desenvolvido a partir da necessidade de organizar o cronograma de reforma para as drogarias da Rossmann. Com esse intuito, a Direção da Rossmann solicitou um algorítmo que pudesse prever qual seria o faturamento de cada uma das lojas cadastradas nas proximas seis semanas, tornando possível um planejamento de reforma mais assertivo, baseado na lucratividade da unidade.</p>

<h2>2. Premissas de Negócio</h2>
<p>a) Os dias em que as lojas estão fechadas foram removidos da análise.</p>
<p>b) Para lojas sem concorrente próximo, será considerado uma distância máxima para melhor funcionamento do algorítmo.</p>

<h2>3. Estratégia de Solução</h2>
<p>A estratégia de solução levou em consideração a metodologia CRISP-DS (Crisp-DM adaptado para Data Science), que busca o entendimento do negócio e entrega de resultados de forma cíclica.
<h4>3.1 Carregar dados do Kaggle (https://www.kaggle.com/c/rossmann-store-sales);</h4>
<h4>3.2 Descrição dos dados, criação e filtragem de variáveis;</h4>
<h4>3.3 Análise Exploratória de Dados (EDA);</h4>
<h4>3.4 Validação de Hipóteses;</h4>
<h4>3.5 Preparação dos dados para modelação;</h4>
<h4>3.6 Criação do modelo para produção e automação do BOT no Telegram.</h4>

<h2>4. Top 3 Insights de Negócios</h2>
<h4>4.1 Lojas com concorrentes mais próximos vendem menos;</h4>
<img align="center" alt="4_1" src="https://user-images.githubusercontent.com/86201991/177865941-b64f93d1-b1b5-40ff-84a5-475d768e2f6e.png" />
<p>Essa é uma hipótese falsa, os dados evidenciam que lojas com concorrentes mais próximos tendem a vender mais. O comportamento provavelmente acontece porque centros comerciais tendem a ficar mais cheios e consequentemente ter mais movimentação que pontos isolados de comércio.</p>
<p>A validação dessa hipótese nos mostra que é válido priorizar a expansão de lojas em centros comerciais. </p><p>Aumentar a gama de produtos oferecidos e o estoque de produtos de saída frequente também podem ser saídas dessa validação de hipótese.</p>

<h4>4.2 Lojas devem vender mais depois do dia 10 de cada mês;</h4>
<img align="center" alt="4_1" src="https://user-images.githubusercontent.com/86201991/177865973-bd6d75ce-6d39-474e-b3ba-9bbf632cdc80.png" />
<p>Essa é uma hipótese falsa, os dados evidenciam que as lojas tendem a vender mais antes do dia 10 de cada mês.
A validação dessa hipótese nos permite um melhor planejamento de ciclos de promoções de produtos para as lojas.</p>

<h4>4.3 Lojas abertas durante o feriado de natal vendem mais;</h4>
<img align="center" alt="4_1" src="https://user-images.githubusercontent.com/86201991/177865979-f7da41aa-573c-4823-b975-82d529251080.png" />
<p>Essa também é uma hipótese falsa, os dados evidenciam que as lojas tendem a vender mais no feriado de páscoa do que no feriado de natal.</p>
<p>A validação dessa hipótese nos permite um melhor planejamento de promoções, controle de estoque, dentre outras ações.</p>

<h2>5. Resultados</h4>

<p>Após preparação dos dados, foi utilizado o algorítmo XGBoost aplicado em Cross-Validation para obtenção de resultados mais fiéis de predição. Os valores encontrados foram satisfatórios e possibilitam tomadas de decisões de mercado e de reforma mais assertivas.</p>

<h4>5.1 Melhores desempenhos de predição</h4>

| ranking | store  |  predictions  | MAE | MAPE |
| ---- | ---- | ---- | ---- | ---- |
| 1 | 733 | 637571,81 | 703,24 | 0,047406 |
| 2 | 494 | 321822,28 | 368,68 | 0,050324 |
| 3 | 259 | 546546,68 | 666,37 | 0,052024 |
| 4 | 562 | 739290,37 | 923,59 | 0,052863 |
| 5 | 1097 | 453025,90 | 587,81 | 0,057227 |

<h4>5.2 Piores desempenhos de predição</h4>

| ranking | store | predictions | MAE | MAPE |
| --- | --- | --- | --- | --- |
| 1115 | 909 | 248363,57 | 7460,87 | 0,800148 |
| 1114 | 876 | 203856,59 | 4085,20 | 0,591192 |
| 1113 | 292 | 105301,39 | 3369,14 | 0,493255 |
| 1112 | 183 | 211484,68 | 1731,66 | 0,270650 |
| 1111 | 274 | 205869,96 | 1160,93 | 0,265488 |

<h4>5.3 Dinâmica do recebimento de dados no Telegram</h4>
![rossmann](https://user-images.githubusercontent.com/86201991/178255265-7c1df4d6-e0a1-41dd-921d-b0d79319072a.png)

<h4>6. Lições aprendidas e agradecimentos</h4>
<p>A partir desse projeto foi possível aprender que o planejamento é uma etapa essencial para o desenvolvimento do projeto, mesmo que, na maioria das vezes, não será possível cumprir o plano traçado devido as inconsistências no processo que irão aparecer. Nessas ocasiões, é imprescindível se desdobrar, montar novas estratégias e repensar os passos.</p>
![1_hilp0xizP_43qVQ7wofz-w](https://user-images.githubusercontent.com/86201991/178257200-f94a1af2-c0c5-4705-ac3d-3bdc2ac68052.jpeg)
<p>Uma outra e importante lição aprendida foi o desenvolvimentos de projetos através do método CRISP, que visa entregar resultados de forma cíclica, sempre repensando os passos dados e agregando melhorias. Dessa forma, é possível revisitar o projeto depois dos primeiros resultados serem entregues, analisar a satisfatoriedade e, caso necessario, refinar os resultados.</p>
Agradeço a Comunidade DS pelo apoio no decorrer do trabalho e a você, por ter chegado até aqui!

