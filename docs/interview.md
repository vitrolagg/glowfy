# Formulário de Entrevista e Levantamento de Requisitos

## Bloco 0: Antes de começar

Objetivo: saber quem está respondendo e quem decide.

0. Quem é a pessoa respondendo essas perguntas — é quem decide o escopo, ou
   existe outra pessoa (sócio, diretoria, gestor) que precisa validar depois?

    R: Cláudia, a dona. Quando mencionando Bia é a recepcionista e Patrícia é a coordenadora

## Bloco 1: Contexto e Objetivo do Sistema

Objetivo: entender a dor real e a operação do cliente antes de definir
qualquer solução tecnológica.

1. Qual é o principal objetivo do software que você deseja criar?
    
    R: Um software para gerenciar o salão de beleza. O principal objetivo é ter o salão inteiro em um único lugar.
        - Agenda: Marcar as clientes sem encaixe duplicado e enxergar o dia de cada profissional, já sabendo quanto tempo cada serviço leva.  Também quero diminuir as faltas, porque hoje umas 15% das clientes simplesmente não aparecem.

        - Serviços e comissões: Tudo que foi feito fica registrado no atendimento, e a comissão de cada profissional sai calculada certinha. Hoje o fechamento da quinzena me toma um dia inteiro com calculadora e sempre dá discussão.

        - Dinheiro do salão: Saber o que entrou e o que saiu, por forma de pagamento, e quais contas vão vencer.  No fim do mês eu quero saber se tive lucro de verdade, porque hoje eu sinceramente não sei.

        - Organização da equipe: Criar tarefas e lembretes para mim, para a coordenadora e para as funcionárias. Coisas como "pagar a fornecedora dia 10" , "renovar o alvará" ou "limpar os pincéis", que hoje ficam em post-it e se perdem.

        - Histórico das clientes: Guardar a fórmula da coloração, as alergias, o que ela fez da última vez e com quem. Assim, se a profissional sair, eu não perco a cliente junto.

        Organizar a agenda, acertar o dinheiro e parar de esquecer as coisas. E ver tudo pelo celular, de casa.

2. Como você resolve esse problema hoje? (papel, planilha, mensagens de
   WhatsApp, outro sistema, processo verbal)
    
    R: Notas mentais, post-its, caderno e whatsapp

3. Qual é a maior dor ou gargalo atual no seu processo? (ex: demora pra
   localizar informação, perda de histórico, erros de agendamento/cadastro)
    
    R: Falta de otimização no processo pelo método manual atual, dados de comissão e agendamentos perdidos. Se a dona ou a coordenadora ficam doentes o processo para e vira uma bagunça no salão. Demora no cálculo de comissão das funcionárias.

## Bloco 2: Mapeamento de Usuários e Perfis de Acesso

Objetivo: descobrir quem são os atores que vão interagir com a aplicação e
seus níveis de privilégio.

4. Quem serão as pessoas ou cargos que vão usar o sistema? (ex:
   administrador, atendente, cliente final)
    
    R:  
    
    - A dona: Precisa ver de tudo: agenda, dinheiro, comissões, relatórios, tarefas de todo mundo e as configurações. É quem define o preço de serviço e percentual de comissão.

    - A Coordenadora: Braço direito da dona, cuida da agenda, abre o caixa do dia, faz a escala das meninas, controla o estoque e cria tarefas para a equipe. Vê quase tudo, mas tem coisa que a dona não quer que ela veja. 

    - A Recepcionista: Fica no balcão. Marca, remarca e confirma clientes, faz o check-in quando a cliente chega e recebe o pagamento no caixa. Não precisa mexer em comissão nem relatório.
        
    - As Profissionais (Cabeleireira, manicure, etc.):São parceiras, a maioria é MEI. Cada uma tem que ver a própria agenda, a ficha das clientes que vai atender (alergia, fórmula de cor, etc.) e quanto já tem de comissão na quinzena. Assim ela confere ao longo da quinzena e não briga no fechamento. Também precisam ver as tarefas e lembretes que eu ou a Coordenadora mandarmos para elas.
        
    - As Auxiliares: Não atendem cliente direto e não ganham comissão. O único uso para elas é ver as tarefas delas, tipo checklist de abertura e fechamento e limpeza. Uma coisa bem simples, de preferência no celular.
        
    - As Clientes: Eu adoraria que elas pudessem marcar sozinhas pelo celular, vendo os horários livres, e também cancelar ou remarcar. Isso tira muita mensagem do whatsapp da recepção. Mas acho que isso pode ficar mais para frente, depois a gente vê. 
        

5. Cada perfil terá permissões diferentes?
    
    R:

    - Quem pode cadastrar e alterar:
        
        - Clientes: A dona a coordenadora e a recepcionista podem cadastrar e editar. As profissionais não cadastram cliente nova, mas podem anotar na ficha da cliente que atenderam: A fórmula da cor, uma observação ou uma reação alérgica que perceberam.

        - Serviços: preços e percentuais de comissão: Apenas a dona. Já aconteceu de mudarem o preço "Só para aquela cliente" sem me avisar. 

        - Profissionais e usuários do sistema: Só a dona cadastra e define o que cada uma acessa. A coordenadora pode editar a escala e os horários das parceiras, mas não pode mexer em percentual de comissão. 

        - Despesas e contas a pagar: A dona e a coordenadora. A recepcionista só lança o que entra no caixa.

        - Tarefas e lembretes: A dona cria para qualquer pessoa. A coordenadora cria para ela mesma e para a equipe, mas não para a dona. As profissionais e auxiliares criam lembretes só para elas mesmas e marcam como feitas as tarefas que receberam.

    - Descontos: 
        
        - A Recepcionista só pode dar até 5% de desconto.

        - A coordenadora pode dar até 15% de desconto.

        - Acima desses valores apenas a dona. Se a cliente estiver lá na hora, a profissional pede pelo sistema e a dona aprova pelo celular.

        - Todo desconto tem que ficar registrado: quem deu e por quê.

    - Quem vê informações sensíveis: 
        
        - Lucro, relatório completo e comissão de todas: só a dona.

        - A coordenadora: vê o caixa, a agenda de todas e o estoque. Não vê o lucro nem a comissão das outras.

        - Cada profissional: Vê a própria comissão e a própria agenda.

        - Informações das clientes: as profissionais não podem ver telefone nem endereço das clientes. Elas veem apenas o nome, a ficha técnica e o histórico de serviços. O contato da cliente fica apenas com a recepção, a coordenadora e a dona.

    - Quem pode excluir: 
        
        - Ninguém apaga nada de dinheiro. Nem pagamento, nem atendimento finalizado, nem lançamento do caixa. Se errou, cancela ou estorna com uma justificativa, e o registro original continua lá. Isso vale para a dona também, porque a contadora precisa disso certinho.

        - Caixa fechado não reabre, apenas com liberação da dona.

        - Cliente e profissional não se apagam, se desativam. Se a profissional saiu do salão, o histórico de atendimentos e comissões dela tem que continuar existindo. 

        - Agendamento pode ser cancelado pela recepcionista, pela coordenadora ou pela dona. Mas deve registrar quem cancelou e quando, porque às vezes some horário e ninguém sabe o que aconteceu.

    No geral: Tudo que mexe com dinheiro ou com cliente fica registrado com o nome de quem fez. Se der problema, a dona pode ver o histórico.


## Bloco 3: Requisitos Funcionais (RF)

Objetivo: mapear o que o sistema precisa fazer na prática.

6. Quais são os cadastros fundamentais que o sistema precisa ter? (ex:
   pessoas, produtos, serviços, pedidos)
    
    R:

    - Clientes: nome, telefone celular, data de nascimento, email e cpf opcionais, Muita cliente não gosta de dar cpf. Como conheceu o salão: Instagram, indicação (de quem) passou na frente. Alergias e restrições em destaque Profissional preferida e observações ("Gosta de café sem açúcar", "não gosta de conversar", etc). Autorização para receber mensagens de whatsapp, por causa daquela lei de dados a LGPD.

    - Ficha técnica da cliente (dentro do cadastro dela): Fórmula de coloração: marca, tom, volume do oxidante e tempo de pausa, com data e quem fez. Ficha de estética (anamnese) para limpeza de pele e depilação: tipo de pele, medicamentos, gravidez; A esteticista preenche, e a cliente tem que concordar. Hoje isso é em papel e a cliente assina.

    - Profissionais e equipe: nome, função, contato, tipo de vínculo(MEI ou CLT), CNPJ do MEI e dados bancários ou chaves pix para o repasse. Quais serviços ela faz. A manicure não pode aparecer como opção para escova por exemplo. Escala: Dias, horários e almoço. Percentual de comissão em cada serviço, quando for diferente do padrão.

    - Serviços: Nome, categoria (cabelo, unhas, estética, etc.): preço e duração estimada. Tempo de pausa? na coloração por exemplo a cliente fica uns 40 minutos com a tinta. Nesse tempo a cabeleireira consegue fazer uma escova em outra cliente. Hoje a gente perde muito horário por não aproveitar isso. Comissão padrão e se é química (para descontar o custo do produto antes da comissão, isso pode ser opcional). Preço "a partir de". Progressiva em cabelo longo é mais cara por exemplo, então a dona configura uma tabela de valores padrão para os tamanhos de cabelo de cliente: curto, médio, longo, extra longo/muito volume, etc. Relação tamanho x preço x duração média. Ao cadastrar o serviço a dona escolhe se o cálculo do preço vai usar essa tabela, por exemplo na hidratação, coloração e etc. Quando marca: se a recepção conhece a cliente, já escolhe o tamanho. Se é cliente nova, marca o tamanho "provável", e para ela aparece "a partir de R$ 50". Na hora do atendimento: a profissional confirma o tamanho real. Se marcaram "médio" e o cabelo é longo, ela troca para "longo". Ela pode fazer isso, porque está vendo o cabelo. Mas ela só escolhe entre as variações cadastradas. No caixa: a recepcionista ou a coordenadora veem que mudou e de quanto para quanto. Fica registrado quem mudou. Às vezes tem um extra: a cliente pediu uma ampola a mais, ou o cabelo estava muito embaraçado. Para isso: A profissional não coloca acréscimo sozinha. Ela pede para a recepção ou para a coordenadora. A recepção ou a coordenadora podem lançar acréscimo, sempre com motivo. Se for um produto, o ideal é lançar como produto (a ampola), e não como "valor a mais", para baixar no estoque. A coordenadora pode acrescentar até 20% sobre o preço da variação. Mais que isso, só comigo. Valor menor que o da tabela é desconto, e segue aquela regra que te passei: recepção até 5%, coordenadora até 15% e acima disso só eu, sempre com motivo. desconto que eu dou por conta própria (cortesia, parceria com influenciadora) não pode reduzir a comissão da profissional. Ela trabalhou igual. Nesse caso a comissão é sobre o preço de tabela, e o salão absorve o desconto.

    - Produtos e estoque: separar produto de revenda (shampoo, máscara para a cliente levar e etc) de produto de uso interno (tinta, oxidante, esmalte e etc). Quantidade, custo, preço de venda (no caso da revenda) e estoque mínimo para avisar quando estiver acabando.

    - Fornecedores: Nome, contato e o que fornece. Serve para lançar as compras e as contas a pagar.

    - Pacotes: Por exemplo, "4 escovas por R$160,00", com validade (60 dias, por exemplo). O sistema vai abatendo cada sessão usada.

    - Financeiro (as configurações): Formas de pagamento com a taxa de cada uma: Débito, crédito à vista, crédito parcelado, Pix e dinheiro. Isso é para descontar a taxa da maquininha certinho na comissão. Categorias de despesa: Aluguel, luz, água, produtos, salários, impostos, manutenção, marketing. 

    - Salas e equipamentos: Tenho uma sala de estética só e dois lavatórios. Não adianta marcar duas limpezas de pele no mesmo horário, mesmo tendo duas profissionais livres. O sistema tem que entender isso.

    - Funcionamento do salão. Horário de funcionamento, feriados e dias fechados (fechamos uma semana no começo do ano).

    - Modelos de tarefa: Os checklists que se repetem: Abertura e fechamento do salão, limpeza semanal, pagar aluguel todo dia 5, Cadastro uma vez e o sistema cria sozinho na data certa.

7. Quais operações do dia a dia o sistema deve executar? (ex: registrar um
   pagamento, emitir um documento, marcar um agendamento)
    
    R:

    Abertura (8h30)

    - Abrir o caixa com o fundo de troco (R$ 200). A coordenadora conta o dinheiro e registra.
    - Checklist de abertura das auxiliares: ligar os equipamentos, conferir a esterilização e repor toalhas. Elas vão marcando no celular.
    - Ver a agenda do dia de todo mundo numa tela só, com quem já confirmou e quem não.

    Agenda (o dia inteiro)

    - Marcar a cliente: escolher o serviço (com a variação de tamanho), a profissional e o horário. Ou deixar o sistema sugerir o primeiro horário livre de quem faz aquele serviço.
    - Marcar vários serviços juntos. Ex: escova com a Carla e mão e pé com a Fernanda no mesmo horário, para a cliente ficar 1h em vez de 2h.
    - Remarcar, cancelar e marcar falta, sempre com o motivo.
    - Encaixe: a Patrícia pode encaixar mesmo com conflito, mas o sistema tem que avisar e ela confirma que sabe.
    - Lista de espera: cliente que queria sábado e não tinha vaga. Se alguém cancelar, o sistema me mostra quem está esperando.
    - Confirmação do dia seguinte: hoje a Bia manda mensagem uma por uma. Quero que isso seja automático. É o "lembrete" que a gente manda um dia antes, para a cliente não esquecer e para eu saber se ela vem mesmo. É a minha maior arma contra falta! 

    1. O sistema manda sozinho, no dia anterior, uma mensagem para cada cliente com horário marcado: o serviço, o horário e a profissional.
    2. A cliente responde "1" para confirmar ou "2" para remarcar ou cancelar.
    3. Na agenda, cada horário mostra a situação:
    - 🟡 Agendado: mensagem enviada, mas ainda sem resposta;
    - 🟢 Confirmado;
    - 🔴 Cancelou ou pediu para remarcar: a Bia entra em contato e vê o novo horário.
    4. Quem não respondeu até as 18h aparece numa lista para a Bia ligar.
    5. Se a cliente cancelou, o horário fica livre e o sistema me mostra quem está na lista de espera para aquele dia.

    Um detalhe

    Como a gente fecha domingo e segunda, as clientes de terça têm que receber a mensagem no sábado. Senão vão receber na segunda, com o salão fechado e ninguém para responder.

    Atendimento

    - Check-in: a cliente chegou, e a profissional fica sabendo.
    - Comanda: cada atendimento abre uma comanda, onde vão entrando:
    - os serviços (podem ser de profissionais diferentes);
    - o produto usado (na química: quantos gramas de tinta, para baixar do estoque e calcular o custo da comissão);
    - o produto vendido (shampoo que a cliente levou), com os 10% para quem vendeu.
    - A profissional anota na ficha da cliente (a fórmula, uma observação).
    - Serviço extra na hora: a cliente veio para escova e resolveu fazer sobrancelha. Adiciona na comanda, se tiver gente livre.

    Pagamento

    - Fechar a comanda e receber. Pode ser dividido: parte no Pix, parte no cartão.
    - Crédito parcelado em até 3x sem juros, para serviço acima de R$ 300, por exemplo, isso é configurável.
    - Usar sessão de pacote e mostrar quantas sessões ainda restam.
    - Usar o sinal já pago. Na progressiva peço 30% de sinal por Pix na hora de marcar, também é opcional meu para cada cliente.
    - Gorjeta: vai 100% para a profissional, separada da comissão e sem taxa descontada… bom, isso eu preciso ver com a contadora se pode.
    - Fiado não. Já tomei muito calote. Mas quero poder registrar quando a cliente "ficou devendo" por algum motivo, para cobrar depois.

    Caixa durante o dia

    - Sangria: tirar dinheiro do caixa para o cofre ou para pagar um motoboy.
    - Vale para a profissional: a menina pede um adiantamento de "R$ 100", que é descontado no fechamento dela.
    - Pequenas despesas: café, material de limpeza, etc. Comprado com o dinheiro do caixa.

    Fechamento (20h)

    - Fechar o caixa: o sistema mostra quanto deveria ter em cada forma de pagamento, a Patrícia conta o que tem, e se tiver diferença, registra com justificativa.
    - Checklist de fechamento.

    Fora do dia a dia, mas sempre

    - Fechamento de comissão quinzenal (dias 15 e último dia do mês): o sistema calcula tudo e eu confiro e aprovo. Cada menina vê o extrato dela e o repasse é feito por Pix. Marco como pago.
    - Contas a pagar e a receber: lançar aluguel, fornecedor e luz, com vencimento, e me avisar antes de vencer.
    - Entrada de mercadoria: chegou o pedido do fornecedor, dá entrada no estoque e lança a conta.
    - Tarefas e lembretes: criar, atribuir, ver o que está atrasado.
    - Aniversariantes da semana, para mandar uma mensagem.
    - Clientes sumidas: quem não volta há mais de 60 dias. Quero chamar de volta.

    Esses horários também precisam ser configuráveis. Os mencionados são os que usamos hoje mas no futuro pode mudar.

8. O sistema precisa gerar relatórios ou indicadores? Se sim, quais
   informações devem constar?
    
    R:

    Precisa muito! É a parte que eu mais quero, porque hoje eu tomo decisão "no achismo". Vou separar por assunto e já dizer quem vê cada coisa.

    Painel inicial (o que eu abro todo dia no celular)

    - O faturamento de hoje, da semana e do mês, comparado com o mesmo período do mês passado.
    - Quantos atendimentos teve no dia, quantas faltas e quantos cancelamentos.
    - As contas que vencem nos próximos 7 dias.
    - As tarefas atrasadas.
    - Os produtos abaixo do estoque mínimo.

    A Patrícia teria um painel parecido, mas sem os valores de faturamento total e lucro.

    Financeiro (só eu)

    - Entradas por forma de pagamento e quanto paguei de taxa de maquininha no mês. Quero saber quanto o cartão me custa.
    - Despesas por categoria.
    - Resultado do mês: quanto entrou, menos os repasses das parceiras, menos as despesas, igual ao lucro. É o que a contadora chama de DRE, mas para mim basta "quanto sobrou".
    - Previsão: quanto tenho a pagar e a receber nos próximos 30 dias, para saber se vai faltar dinheiro.
    - Ticket médio: quanto cada cliente gasta, em média, por visita.
    - Evolução mês a mês, para ver se estou crescendo. Um gráfico de 12 meses.

    Profissionais

    - Para mim: o faturamento e a comissão de cada uma, o número de atendimentos, o ticket médio, a venda de produtos, a taxa de ocupação (quanto da agenda dela ficou cheia), quantas clientes dela voltaram e aqueles bloqueios e faltas que te falei.
    - Para cada profissional: só os números dela: a comissão da quinzena, os atendimentos e o histórico de fechamentos.
    - Para a Patrícia: a ocupação e os atendimentos de cada uma, sem os valores de comissão.

    Serviços

    - Os serviços mais vendidos.
    - Os serviços que mais dão lucro, e não só os que mais faturam. A progressiva fatura muito, mas gasta muito produto e tem comissão alta. Quero ver o preço menos o custo do produto menos a comissão.

    Clientes

    - Clientes novas no mês e de onde vieram (Instagram, indicação…), para saber se vale pagar anúncio.
    - Clientes sumidas há mais de 60 dias, com o telefone para chamar de volta.
    - As melhores clientes: quem mais gasta e quem vem com mais frequência.
    - Taxa de falta (no-show) geral e por cliente, para eu saber se os 15% estão caindo.
    - Aniversariantes do mês.

    Agenda

    - Ocupação por dia da semana e horário. Desconfio que terça de manhã é morta, e quero ver isso para fazer promoção.
    - Cancelamentos e remarcações, com os motivos.

    Estoque

    - Os produtos abaixo do mínimo e o consumo do mês.
    - Diferença entre o que deveria ter e o que tem. Se o sistema sabe quanto de tinta foi usado nos atendimentos e quanto entrou, ele sabe quanto deveria ter. Quando a Patrícia contar e não bater, eu quero ver. Produto some aqui, e eu nunca consigo provar.

    Controle (só eu)

    - Descontos e cortesias: quem deu, para quem, quanto e por quê.
    - Diferenças de caixa nos fechamentos.
    - Cancelamentos e estornos de pagamento.

    Em todos os relatórios

    - Filtrar por período (dia, semana, mês ou datas que eu escolher) e por profissional.
    - Exportar em Excel e PDF, como te falei para a contadora.

9. O usuário final vai precisar de um portal ou aplicativo próprio pra
   consultar algo? (ex: ver status, consultar histórico/fatura)
    
    R:

    Aplicativo de baixar na loja, não. Ninguém quer baixar mais um aplicativo só para marcar unha. Mas um link que a cliente abre pelo celular, eu quero muito! Eu colocaria na bio do Instagram e na mensagem automática do WhatsApp.

    Como te falei antes, isso pode ficar para depois da primeira versão. Primeiro eu preciso arrumar a casa por dentro. Mas quando for fazer, eu imagino assim:

    O que a cliente pode fazer

    - Ver os serviços e preços. Nos que têm tamanho, mostra "a partir de R$ 50".
    - Agendar sozinha: escolhe o serviço, a profissional (ou "tanto faz"), o dia e um horário livre.
    - Ver os horários marcados e cancelar ou remarcar até 24 horas antes. Com menos de 24h, só falando com o salão.
    - Ver o histórico dela: o que fez, quando e com quem.
    - Ver o saldo do pacote: quantas escovas ainda restam e até quando vale.
    - Pagar o sinal pelo Pix, nos serviços que pedem sinal.

    Como ela entra

    - Sem senha! As minhas clientes vão esquecer a senha na hora. Melhor ela digitar o celular e receber um código pelo WhatsApp ou SMS, igual a banco.
    - Na primeira vez ela faz um cadastro rápido: nome, celular, data de nascimento e aceite da LGPD. Se o celular já existe aqui no salão, o sistema reconhece e não duplica.

    Os cuidados que eu quero

    - Nem todo serviço pode ser marcado online. Coloração em cliente nova, por exemplo, precisa de avaliação antes. Eu quero escolher, serviço por serviço, se aparece ou não no agendamento online.
    - Serviço acima de R$ 300 (progressiva, mechas): o horário só fica garantido depois que o sinal de 30% for pago. Se não pagar em 2 horas, o horário é liberado.
    - Cliente com muitas faltas não pode marcar sozinha. Ela vê uma mensagem para falar com o salão. Depois te conto melhor essa regra.
    - Ela não vê a agenda da profissional, só os horários livres. Não precisa ver quem está atendendo quem.
    - Quando ela marcar, a recepção e a profissional são avisadas no sistema.
    - Eu quero poder segurar horários para não aparecerem online, por exemplo os encaixes que a Patrícia reserva no sábado para as clientes fiéis.

    Mais para frente ainda

    - Programa de fidelidade com pontos ("a cada 10 escovas, ganha uma").
    - Avaliar o atendimento depois do serviço, de 1 a 5 estrelas.
    - Comprar produto pelo link e retirar no salão.

10. O que é essencial já na primeira versão, e o que pode ficar pra uma
    versão futura?
    
    R:

    Ai, essa é difícil, eu queria tudo para ontem! 😅 Mas eu entendo que não dá. Vou pensar no que dói mais hoje.

    Primeira versão: sem isso não adianta trocar o caderno

    1. Acesso e segurança
    - Os perfis e permissões que te passei (dona, coordenadora, recepção, profissional e auxiliar).
    - O registro de quem fez o quê em dinheiro, agenda e cliente.

    2. Cadastros
    - Clientes, com alergias em destaque e a ficha técnica (fórmula de cor e observações).
    - Profissionais, com a escala, os serviços que fazem e os percentuais de comissão.
    - Serviços com as variações de tamanho (preço e duração).
    - Produtos de revenda (só o básico: preço, custo e quantidade).
    - Formas de pagamento com as taxas, categorias de despesa, fornecedores e pacotes. Os pacotes eu já vendo hoje e controlo no caderno, então não posso ficar sem.

    3. Agenda
    - Marcar, remarcar, cancelar e marcar falta.
    - Vários serviços e profissionais no mesmo horário.
    - Aviso de conflito e encaixe com confirmação.
    - Bloqueios com aprovação, escala, almoço, feriados.
    - A sala de estética e os lavatórios. É uma regra simples, mas sem ela vai dar conflito todo dia.
    - A confirmação do dia seguinte no modo simples: a lista com o botão que abre o WhatsApp com a mensagem pronta.

    4. Comanda e pagamento
    - Os serviços, a venda de produto, os descontos dentro dos limites e o acréscimo com motivo.
    - Pagamento dividido, sessão de pacote e o sinal, registrado à mão quando a cliente manda o Pix.
    - O "ficou devendo".

    5. Caixa
    - Abertura, sangria, vale da profissional, pequenas despesas e o fechamento com conferência.

    6. Comissões
    - O cálculo com todas as regras: o percentual por serviço e por profissional, o custo do produto na química, a taxa da maquininha, os vales e a cortesia que não reduz a comissão.
    - O fechamento quinzenal com a minha aprovação, e o extrato que cada profissional vê.
    - Isso é a coisa mais importante de todas para mim.

    7. Financeiro
    - Contas a pagar e a receber, com aviso antes de vencer.

    8. Tarefas e lembretes
    - Criar, atribuir e marcar como feita.
    - As tarefas que se repetem (checklist de abertura e fechamento, aluguel todo dia 5).

    9. Relatórios: só os 5 que eu não vivo sem
    1. Faturamento (dia, semana e mês), por forma de pagamento.
    2. Lucro do mês.
    3. Comissão e atendimentos por profissional.
    4. Contas a vencer.
    5. Taxa de falta das clientes.

    Todos com exportação em Excel e PDF para a contadora. E tudo isso funcionando no celular (site responsivo capaz de ser instalado no celular e enviar notificações, sem app na loja).

    Segunda versão: logo em seguida

    - O estoque completo: produto de uso interno, baixa por grama na química e a tal da diferença de estoque. Dói, mas consigo segurar mais uns meses na planilha.
    - O tempo de pausa da química para encaixar outra cliente.
    - A confirmação automática pelo WhatsApp, com resposta "1" ou "2".
    - A lista de espera, as clientes sumidas e os aniversariantes.
    - O resto dos relatórios: serviços mais lucrativos, ocupação por horário, origem das clientes, descontos e diferenças de caixa.
    - Aprovar desconto pelo celular com notificação. Na primeira versão, a Patrícia me chama e eu aprovo entrando no sistema.
    - A ficha de estética (anamnese) digital com o aceite da cliente.

    Terceira versão: o sonho

    - O link de agendamento das clientes, com login por código e o sinal pago por Pix ali mesmo.
    - Fidelidade, avaliação do atendimento, fotos de antes e depois, venda de produtos pelo link.
    - A segunda unidade. Mas eu já te peço: faz a primeira versão pensando nisso, para não ter que refazer tudo daqui a um ano e meio.

## Bloco 4: Regras de Negócio (RN)

Objetivo: definir as diretrizes lógicas, restrições e limites operacionais
do negócio do cliente.

11. Quais identificadores devem ser únicos no sistema? (o que hoje já
    funciona como "identidade" de um registro pro cliente — documento,
    código, e-mail)
    
    R:

    Aqui no salão a gente reconhece as pessoas assim:

    Clientes: o celular

    - Hoje a cliente é "a Ana do celular tal". O número de WhatsApp é a identidade dela aqui. Não pode ter dois cadastros com o mesmo celular. Quando a Bia digitar um número que já existe, o sistema tem que mostrar a cliente que já está cadastrada.
    - CPF é opcional. Mas se a cliente informar, também não pode repetir.
    - E-mail é opcional e quase ninguém dá. Não precisa ser único.
    - Exceções que acontecem de verdade:
    - Mãe e filha pequena: a menina de 8 anos que vem cortar o cabelo não tem celular. Ela tem que ser cadastrada ligada à mãe, usando o celular da mãe para contato, mas com ficha própria (o histórico dela não pode misturar com o da mãe).
    - Cliente que troca de número: a gente atualiza o cadastro, e o histórico continua o mesmo.
    - Duas pessoas com o mesmo nome: é comum ter três "Ana Paula". O nome não identifica ninguém, então na hora de buscar tem que aparecer junto o celular ou a data de nascimento para não confundir.

    Profissionais e equipe

    - CPF é único.
    - CNPJ do MEI é único, para quem é parceira. A contadora usa isso.
    - O login de cada pessoa no sistema é único. Pode ser o e-mail ou o celular, o que for mais fácil. Cada uma tem o seu acesso, nada de senha compartilhada. Hoje a Bia e a Patrícia usam a mesma senha da planilha, e aí eu nunca sei quem fez o quê.

    Serviços e produtos

    - Nome do serviço não pode repetir. Não quero duas "Escova" com preços diferentes.
    - Produtos: o código de barras, quando tiver, é único. Ajuda a dar entrada e a vender rápido.

    Números que a gente usa para conferir

    - Número da comanda: sequencial e que nunca repete. Quando a cliente reclama ("paguei e não lançaram!"), eu procuro pelo número.
    - Fornecedor: o CNPJ é único.

    Coisas que só podem existir "uma de cada vez"

    - Um caixa aberto por vez. Não pode abrir o caixa de hoje com o de ontem ainda aberto.
    - Um fechamento de comissão por profissional por quinzena. Não pode pagar duas vezes a mesma quinzena.

12. Existe alguma restrição de quantidade ou duplicidade num registro? (ex:
    não pode ter dois cadastros ativos ao mesmo tempo pra mesma pessoa)
    
    R: Já registrado na pergunta acima.

13. Existe alguma situação de pendência/atraso que bloqueia algo
    automaticamente? (se fizer sentido pro negócio do cliente)
    
    R: 

14. Existem exceções operacionais? (ex: cancelamento, estorno, casos
    especiais que fogem da regra padrão — e se há alguma cobrança/taxa
    associada)
    
    R: Já registrado nas perguntas acima

## Bloco 5: Requisitos Não Funcionais (RNF)

Objetivo: estabelecer os critérios de qualidade, desempenho, usabilidade e
segurança do sistema.

15. O sistema precisa rodar em celular/dispositivos móveis? (layout
    responsivo)
    
    R: Site responsivo instalável

16. Como deve ser o controle de segurança? (login com e-mail/senha,
    autenticação em dois fatores, controle de sessão por perfil)
    
    R: login com email e senha para as trabalhadoras do salão

17. Qual o volume de acesso ou tempo de resposta esperado?
    
    R: Aproximadamente 15 a 20 pessoas no salão, futuramente a definir quando as clientes tiverem acesso.

18. Qual é a política necessária de backup das informações? (diário,
    semanal, cópia automática em nuvem)
    
    R: Diário. Cópia automática.

## Bloco 6: Dúvidas Pendentes e Integrações

Objetivo: mapear pontos em aberto e integrações externas, pra evitar
retrabalho durante o desenvolvimento.

19. O sistema precisará se integrar com alguma ferramenta externa? (ex:
    meio de pagamento, emissor de nota fiscal, envio de SMS/WhatsApp, outro
    sistema que o cliente já usa)
    
    R: 

    Nota fiscal

    - Hoje é bem confuso. Pela lei do salão-parceiro, o salão emite nota da parte dele e cada parceira MEI emite da parte dela. Na prática, quase nenhuma cliente pede nota. Quando pede, a Dra. Regina emite pelo site da prefeitura.
    - Na primeira versão eu não preciso que o sistema emita nota. Preciso que o relatório separe direitinho a parte do salão e a parte de cada parceira, como te falei, para a contadora fazer a parte dela.
    - Para o futuro eu quero. Mas antes eu preciso conversar com a Dra. Regina para entender como tem que ser: se o sistema emite a do salão e também a das meninas, se é por atendimento ou no fim do mês. Isso fica comigo, eu te trago a resposta.

    Maquininha (Stone)

    - A maquininha continua separada. A Bia passa o cartão e lança no sistema que foi "crédito" ou "débito". Para mim, isso está bom na primeira versão.
    - O que seria ótimo no futuro: o sistema conferir sozinho o que a Stone me pagou com o que foi lançado. Às vezes a Stone desconta taxa errada e eu nunca percebo. Mas é coisa para depois.

    Pix

    - Primeira versão: o Pix cai na conta do salão, e a Bia confere no aplicativo do banco e lança no sistema "recebido via Pix". É manual, como é hoje.
    - Quando tiver o link das clientes: aí eu quero o Pix automático para o sinal. O sistema gera o QR code, a cliente paga e o horário é confirmado sozinho, sem ninguém ter que conferir. Senão não adianta nada a cliente marcar sozinha às 23h.

    Banco

    - Futuro, se der: puxar o extrato do banco para conferir com o caixa. Não é prioridade.

    Instagram

    - Só o link do agendamento na bio, quando existir. Integração com o Instagram mesmo, não preciso.

    E-mail

    - Seria bom o sistema conseguir mandar o relatório da contadora por e-mail, direto para ela, mas não é essencial. Eu baixo e mando, tranquilo.
    - E, claro, aquele "esqueci minha senha" das meninas precisa funcionar. Vai acontecer toda semana!

    Não preciso

    - Google Agenda, outros sistemas, programa de contabilidade da Dra. Regina: nada disso. A planilha resolve para ela.

20. Existe mais de uma unidade, filial ou equipe que vai usar o mesmo
    sistema?

    R: No momento apenas uma unidade porém a cliente disse que quer abrir uma segunda daqui um ano e meio, a primeira versão já deve ser feita pensando na escalabilidade e na adição de uma segunda unidade

21. Existe prazo ou marco importante pra essa versão?

    R: Não definido pois o projeto é para portfólio.

22. O que definitivamente NÃO faz parte do escopo dessa versão?

    R: Já definido

23. Ficou algum ponto em aberto que precisa de validação com outra pessoa
    antes de começar o desenvolvimento?

    R:

    Ficou sim, e não foi pouca coisa. Anotei tudo aqui no meu caderninho (o último uso dele! 😄):

    Com a Dra. Regina (contadora)

    1. Gorjeta: pode ir 100% para a profissional, sem passar pela comissão e sem descontar taxa? Precisa entrar no relatório dela?
    2. Nota fiscal no salão-parceiro: quem emite o quê, se é por atendimento ou por mês, e se o sistema vai precisar emitir no futuro.
    3. Desconto da taxa da maquininha e do custo do produto na comissão: eu faço isso há anos, mas quero ter certeza de que está certo pela lei e pelo contrato das parceiras, antes de colocar no sistema. Depois que estiver no sistema, vira regra.
    4. Formato do relatório mensal: ela vai me dizer quais colunas precisa, para você não ter que refazer.

    Com a Patrícia (coordenadora)

    5. Os prazos de bloqueio (7 dias para folga, 48h para horas): eu chutei. Quero que ela confirme se funciona na prática.
    6. Os limites de desconto e acréscimo dela (15% e 20%): se são suficientes para o dia a dia ou se ela vai ter que me chamar toda hora.
    7. Os checklists de abertura e fechamento: ela sabe melhor do que eu o que tem que ter.
    8. As variações de tamanho e as durações de cada serviço: eu sei os preços, mas o tempo real quem acompanha é ela.

    Com as meninas (parceiras)

    9. Vou avisar que as comissões vão passar a ser calculadas pelo sistema e que elas vão ter o extrato no celular. Não é para pedir permissão, mas os contratos de parceria têm os percentuais escritos. Preciso conferir se o que vou cadastrar bate com o contrato de cada uma. Duas delas eu acho que estão desatualizadas.

    Comigo mesma

    10. Cortesia: só eu posso dar, ou a Patrícia também? Ainda não decidi. Por enquanto, só eu.
    11. Custo do produto na química, na primeira versão: já que o estoque completo fica para a segunda, eu preciso decidir se uso um custo fixo por serviço (ex: progressiva = R$ 60 de produto) ou se a profissional informa na comanda. Acho que o valor fixo é mais simples e evita briga, mas quero ver com a Patrícia quanto realmente gasta cada um.
    12. Os 1.500 contatos e as fichas de cor: se dá para importar, ou quantas horas a Patrícia vai precisar para digitar.

    Com você

    13. O aviso no meu iPhone: testar se funciona, porque daí depende se vamos precisar de aplicativo ou não.
    14. Prazo: me dizer, com sinceridade, se dá para a primeira versão inteira até 12 de janeiro, ou se vamos pelo plano B (comissão só em fevereiro).

    Eu te dou um retorno das conversas com a Dra. Regina e com a Patrícia até o fim de outubro. Pode ser?

## Bloco 7: Anotações

    - Cores: 1 - #D4A373 2 - #212529 3 - #F8F9FA

    -  Exportação de relatório financeiro para a contadora. via planilha baixada no computador ou enviada no email. escolher o período, formato do arquivo. Ela precisa das informações de entradas, separadas por forma de pagamento; Apenas a dona pode ver e exporta o relatório completo. A coordenadora exporta somente o caixa.
    
    -   As parceiras tem o direito de organizar o próprio horário, portanto: Elas podem pedir um bloqueio de horário pelo sistema, e a coordenadora aprova. A profissional escolhe dia e horário e coloca o motivo, médico, folga, curso, pessoal ou etc. A coordenadora ou a dona recebem o aviso e podem aprovar ou recusar. Enquanto não aprovar o horário aparece como bloqueio pendente na agenda geral então a recepcionista sabe que não deve marcar nada naquele horário; Folga ou dia todo devem pedir com pelo menos 7 dias de antecedência. Folga nos dias de maior fluxo só podem ser aprovados diretamente pela dona. Médico, ou banco e etc. Devem ser solicitados com pelo menos 48 horas de antecedência, Qualquer solicitação abaixo dos prazos até é efetuada mas exibe um alerta para o usuário e a coordenadora ou a dona decidem liberar ou não. Se já houver cliente marcada no horário solicitado o sistema não bloqueia por cima, mostra para a coordenadora ou a dona quais clientes serão afetadas para remarcar com outra profissional ou outro horário (mostra profissionais e horarios disponíveis). E a cliente tem que ser avisada então cria tarefa para a recepcionista. A coordenadora e a dona podem bloquear o horário de qualquer uma na hora então as emergências são tratadas por fora do sistema, a profissional liga para a coordenadora diretamente (whatsapp ou ligação normal). A coordenadora/dona também podem configurar intervalos fixos, horários de almoço e o dia de folga padrão de cada profissional. No fim do mês o sistema calcula bloqueios e faltas de cada profissional

