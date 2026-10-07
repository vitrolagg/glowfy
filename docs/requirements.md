# Documento de Requisitos

# Nome
    - Glowfy

## 1. Objetivo do Sistema
<!-- Descreva em poucas frases o proposito do sistema: o que ele faz, para quem, e qual problema de negocio ele resolve. -->

    - Sistema web de gestão para salão de beleza que centraliza em um único lugar a
      agenda das clientes, o registro dos atendimentos, o cálculo das comissões das
      profissionais parceiras, o caixa e o financeiro do salão, além de tarefas e
      lembretes da equipe. Atende a dona, a coordenadora, a recepção, as
      profissionais e as auxiliares, e substitui o controle atual em caderno,
      post-its e WhatsApp. O objetivo é reduzir erros de agenda e faltas, acabar com
      o fechamento manual de comissões, dar visibilidade do lucro real e permitir
      acompanhar o salão pelo celular.

## 2. Perfis de Usuarios
<!-- Liste os papeis/perfis de acesso que vao interagir com o sistema (ex: tipos de usuario, nao pessoas especificas nem personas detalhadas). -->

    - Dona (administradora): acesso total, incluindo configurações, preços,
      comissões, financeiro, lucro e relatórios completos.
    - Coordenadora: gestão operacional (agenda de todas, caixa, escala, estoque e
      tarefas da equipe), sem acesso a lucro nem às comissões das profissionais.
    - Recepcionista: agenda (marcar, remarcar, confirmar, check-in), cadastro de
      clientes, comanda e recebimento no caixa.
    - Profissional (parceira): a própria agenda, a ficha técnica das clientes que
      atende, as próprias comissões e extrato, e as próprias tarefas.
    - Auxiliar: apenas as próprias tarefas e checklists.

## 3. Problemas Identificados
<!-- Liste as dores e justificativas atuais que motivam a construcao do sistema (processos manuais, falhas, riscos, lentidao etc.). -->

    - Controle manual em caderno, post-its, notas mentais e WhatsApp, sem um local
      único de informação.
    - Agendamentos duplicados ou perdidos, e cerca de 15% de faltas (no-show) das
      clientes.
    - Fechamento quinzenal de comissões feito à mão, que consome um dia inteiro e
      gera discussões com as profissionais.
    - Dados de comissão e de agendamentos perdidos.
    - Falta de visibilidade do lucro real do salão e das contas a vencer.
    - Tarefas e lembretes (pagamentos, alvará, limpeza) esquecidos ou perdidos.
    - Perda do histórico das clientes (fórmula de coloração, alergias, serviços
      feitos), inclusive quando uma profissional deixa o salão.
    - Dependência da dona e da coordenadora: se uma delas falta, a operação para.
    - Senha compartilhada entre funcionárias, sem saber quem fez cada alteração.

## 4. Requisitos Funcionais
<!-- Liste as acoes e funcionalidades que o sistema deve executar, numeradas como RF01, RF02, RF03... Cada item descreve algo que o sistema FAZ. -->

    Acesso
    - RF01 - Permitir login individual com e-mail e senha para cada membro da equipe.
    - RF02 - Permitir recuperação de senha por e-mail.
    - RF03 - Permitir à dona cadastrar usuários e definir o perfil de acesso de cada um.

    Cadastros
    - RF04 - Cadastrar clientes com nome, celular (WhatsApp), data de nascimento, e-mail e CPF opcionais, origem (Instagram, indicação e de quem, passagem), profissional preferida, observações, alergias/restrições e consentimento LGPD para receber mensagens.
    - RF05 - Cadastrar cliente dependente (ex: criança) vinculada a uma cliente responsável, usando o contato da responsável e com histórico próprio.
    - RF06 - Buscar clientes exibindo celular e data de nascimento junto ao nome, e avisar quando o celular digitado já pertence a uma cliente cadastrada.
    - RF07 - Manter a ficha técnica da cliente com fórmulas de coloração (marca, tom, volume do oxidante, tempo de pausa, data e profissional) e observações, exibindo alergias em destaque no agendamento e no atendimento.
    - RF08 - Cadastrar profissionais e equipe com nome, função, contato, CPF, vínculo (parceira MEI ou CLT), CNPJ do MEI, dados bancários/chave Pix e os serviços que realiza.
    - RF09 - Configurar a escala de cada profissional: dias, horários, intervalo de almoço e folga padrão.
    - RF10 - Cadastrar serviços com nome, categoria, preço, duração, comissão padrão, indicação de serviço químico com custo de produto a descontar (opcional) e recursos físicos necessários.
    - RF11 - Manter a tabela de variações por tamanho de cabelo (curto, médio, longo, extra longo/muito volume…) com preço e duração próprios, e indicar por serviço se ele usa essa tabela.
    - RF12 - Definir percentual de comissão específico por profissional e serviço.
    - RF13 - Cadastrar produtos de revenda com preço de venda, custo, quantidade e código de barras, com baixa automática da quantidade na venda.
    - RF14 - Cadastrar fornecedores com nome, CNPJ, contato e o que fornecem.
    - RF15 - Cadastrar pacotes (serviço, quantidade de sessões, preço e validade) e controlar o saldo de sessões de cada cliente.
    - RF16 - Cadastrar formas de pagamento (débito, crédito à vista, crédito parcelado, Pix, dinheiro) com a taxa de cada uma, e as condições de parcelamento.
    - RF17 - Cadastrar categorias de despesa.
    - RF18 - Cadastrar salas e equipamentos (ex: sala de estética, lavatórios) com a quantidade disponível.
    - RF19 - Configurar o funcionamento do salão (dias e horários, feriados e períodos fechados) e os horários operacionais usados pelo sistema.

    Agenda
    - RF20 - Exibir a agenda do dia de todas as profissionais em uma única tela e a agenda individual, com a situação de cada horário (agendado, confirmado, em atendimento, concluído, cancelado, falta).
    - RF21 - Agendar serviço escolhendo variação, profissional e horário, ou sugerindo o primeiro horário livre de quem realiza o serviço.
    - RF22 - Agendar vários serviços para a mesma cliente, com profissionais diferentes, no mesmo horário ou em sequência.
    - RF23 - Remarcar, cancelar e registrar falta de agendamentos, com motivo obrigatório.
    - RF24 - Detectar conflitos de horário da profissional e de recursos físicos, e permitir encaixe mediante confirmação de quem tem permissão.
    - RF25 - Permitir à profissional solicitar bloqueio de horário com motivo, exibido como "bloqueio pendente" na agenda até ser aprovado ou recusado pela coordenadora ou pela dona.
    - RF26 - Permitir à coordenadora e à dona bloquear diretamente o horário de qualquer profissional.
    - RF27 - Ao aprovar um bloqueio sobre horários com clientes marcadas, listar as clientes afetadas, sugerir profissionais e horários disponíveis para remarcação e gerar tarefa para a recepcionista avisá-las.
    - RF28 - Contabilizar mensalmente os bloqueios e as faltas de cada profissional.
    - RF29 - Gerar a lista de confirmação dos agendamentos do próximo dia de funcionamento, com botão que abre o WhatsApp com a mensagem pré-preenchida, e permitir registrar a resposta da cliente.
    - RF30 - Registrar sinal recebido (lançamento manual) vinculado ao agendamento.

    Atendimento
    - RF31 - Registrar o check-in da cliente e notificar a profissional.
    - RF32 - Abrir comanda numerada por atendimento, com serviços (inclusive de profissionais diferentes e extras incluídos na hora) e produtos vendidos.
    - RF33 - Permitir à profissional confirmar ou trocar a variação de tamanho do serviço, registrando quem alterou e o valor anterior e o novo.
    - RF34 - Lançar acréscimo na comanda com motivo obrigatório.
    - RF35 - Lançar desconto com motivo e tipo (comercial ou cortesia), e enviar à dona uma solicitação de aprovação quando exceder o limite do usuário.
    - RF36 - Permitir à profissional registrar anotações na ficha técnica da cliente atendida.

    Pagamento
    - RF37 - Fechar a comanda recebendo em uma ou mais formas de pagamento, incluindo crédito parcelado.
    - RF38 - Consumir sessão de pacote na comanda e exibir o saldo restante.
    - RF39 - Abater o sinal já pago no fechamento da comanda.
    - RF40 - Registrar valor pendente da cliente ("ficou devendo") com motivo, controlar a quitação e listar as clientes com pendência.
    - RF41 - Cancelar ou estornar pagamentos com justificativa obrigatória.

    Caixa
    - RF42 - Abrir o caixa registrando o fundo de troco.
    - RF43 - Registrar sangrias, pequenas despesas pagas com dinheiro do caixa e vales (adiantamentos) às profissionais.
    - RF44 - Fechar o caixa mostrando o valor esperado por forma de pagamento, registrando o valor contado e justificando as diferenças.
    - RF45 - Permitir a reabertura de caixa fechado mediante liberação da dona.

    Comissões
    - RF46 - Calcular automaticamente a comissão de cada atendimento e de cada venda de produto.
    - RF47 - Gerar o fechamento quinzenal por profissional, com aprovação da dona e registro do pagamento (repasse).
    - RF48 - Disponibilizar à profissional o extrato atualizado da quinzena e o histórico de fechamentos.

    Financeiro
    - RF49 - Registrar contas a pagar e a receber com vencimento e baixa, alertando antes do vencimento.
    - RF50 - Registrar compras de fornecedor, gerando a conta a pagar e a entrada dos produtos de revenda no estoque.

    Tarefas e lembretes
    - RF51 - Criar tarefas e lembretes com responsável e prazo, marcar como concluídos e listar os atrasados.
    - RF52 - Cadastrar modelos de tarefas e checklists recorrentes (abertura, fechamento, limpeza, pagamentos fixos), gerados automaticamente na data configurada.

    Relatórios
    - RF53 - Exibir painel inicial com faturamento do dia, da semana e do mês, contas a vencer e tarefas atrasadas, conforme o perfil.
    - RF54 - Gerar relatório de faturamento por período e por forma de pagamento, incluindo o total de taxas pagas.
    - RF55 - Gerar relatório de resultado do mês (entradas menos repasses às parceiras menos despesas).
    - RF56 - Gerar relatório de comissões e atendimentos por profissional.
    - RF57 - Gerar relatório de contas a vencer.
    - RF58 - Gerar relatório de taxa de faltas (no-show) geral e por cliente.
    - RF59 - Gerar relatório mensal para a contadora com entradas por forma de pagamento, despesas por categoria e a separação entre a parte do salão e a parte de cada parceira.
    - RF60 - Filtrar relatórios por período e profissional, e exportá-los em Excel e PDF.
    - RF61 - Permitir à dona consultar o histórico de alterações (quem fez, o quê e quando).

## 5. Requisitos Nao Funcionais
<!-- Liste os criterios de qualidade, desempenho, seguranca e restricoes operacionais do sistema, numerados como RNF01, RNF02... Cada item descreve COMO o sistema deve se comportar. -->

    - RNF01 - O sistema deve ser uma aplicação web responsiva, priorizando o celular nas telas de profissionais e auxiliares (agenda do dia, ficha da cliente, comissão, tarefas).
    - RNF02 - O sistema deve ser instalável como PWA, com ícone na tela inicial, sem publicação em lojas de aplicativo.
    - RNF03 - O sistema deve enviar notificações push no Android e no iOS (16.4+ com o PWA instalado).
    - RNF04 - O acesso deve exigir login individual com e-mail e senha, com senhas armazenadas de forma criptografada (hash) e sem contas compartilhadas.
    - RNF05 - As permissões de cada perfil devem ser validadas no servidor, e não apenas ocultadas na interface.
    - RNF06 - Operações que envolvem dinheiro, agenda ou dados de clientes devem gerar registro de auditoria com usuário, data/hora e valores anterior e novo.
    - RNF07 - Registros de clientes, profissionais e lançamentos financeiros não devem ser excluídos fisicamente (exclusão lógica ou estorno).
    - RNF08 - Deve haver backup automático diário do banco de dados em nuvem.
    - RNF09 - O sistema deve suportar de 15 a 20 usuários simultâneos.
    - RNF10 - A arquitetura deve suportar múltiplas unidades (dados vinculados a uma unidade), mesmo operando com uma única unidade na primeira versão.
    - RNF11 - O tratamento de dados pessoais deve seguir a LGPD, com registro do consentimento da cliente e acesso aos dados de contato restrito aos perfis autorizados.
    - RNF12 - A interface deve seguir a identidade visual do Glowfy: #D4A373, #212529 e #F8F9FA.

## 6. Regras de Negocio
<!-- Liste as diretrizes logicas e restricoes da operacao que o sistema deve respeitar, numeradas como RN01, RN02... Sao regras do negocio, nao funcionalidades. -->

    - RN01 - Clientes podem ser cadastradas e editadas pela dona, pela coordenadora e pela recepcionista. Profissionais não cadastram clientes, apenas registram anotações na ficha técnica das clientes que atenderam.
    - RN02 - Somente a dona pode alterar serviços, preços, variações, percentuais de comissão, usuários e perfis de acesso.
    - RN03 - A coordenadora pode editar a escala e os horários das profissionais, mas não os percentuais de comissão.
    - RN04 - Despesas e contas a pagar são lançadas pela dona e pela coordenadora. A recepcionista lança apenas as entradas do caixa.
    - RN05 - A dona cria tarefas para qualquer pessoa. A coordenadora cria tarefas para si e para a equipe, exceto para a dona. Profissionais e auxiliares criam lembretes apenas para si e concluem as tarefas recebidas.
    - RN06 - Limites de desconto: recepcionista até 5%, coordenadora até 15%. Acima disso, apenas com aprovação da dona. Todo desconto exige motivo e registra quem o concedeu.
    - RN07 - Somente a dona concede cortesia. Na cortesia, a comissão da profissional é calculada sobre o preço de tabela, e o salão absorve o desconto.
    - RN08 - A profissional não lança acréscimo. Recepcionista e coordenadora lançam acréscimo com motivo, sendo a coordenadora limitada a 20% sobre o preço da variação. Acima disso, apenas a dona. Itens extras que são produto devem ser lançados como produto.
    - RN09 - A profissional só pode alterar a variação de tamanho entre as variações cadastradas, nunca digitar um valor livre.
    - RN10 - Lucro, relatório completo e comissões de todas as profissionais são visíveis apenas à dona. A coordenadora vê caixa, agenda de todas e estoque. Cada profissional vê apenas a própria agenda e a própria comissão.
    - RN11 - Profissionais não visualizam telefone nem endereço das clientes, apenas nome, ficha técnica e histórico de serviços.
    - RN12 - Somente a dona exporta o relatório completo. A coordenadora exporta apenas o movimento do caixa.
    - RN13 - Pagamentos, atendimentos finalizados e lançamentos de caixa não podem ser excluídos por ninguém. Correções são feitas por cancelamento ou estorno com justificativa, preservando o registro original.
    - RN14 - Caixa fechado só pode ser reaberto com liberação da dona.
    - RN15 - Clientes e profissionais são desativados, nunca excluídos, mantendo o histórico de atendimentos e comissões.
    - RN16 - Agendamentos podem ser cancelados pela recepcionista, pela coordenadora ou pela dona, registrando quem cancelou, quando e o motivo.
    - RN17 - O celular é único entre as clientes titulares. O CPF, quando informado, é único. O e-mail não precisa ser único.
    - RN18 - A cliente dependente usa o celular da responsável para contato, mas possui ficha e histórico próprios.
    - RN19 - CPF, CNPJ do MEI e login são únicos para cada membro da equipe.
    - RN20 - O nome do serviço, o código de barras do produto (quando houver) e o CNPJ do fornecedor são únicos.
    - RN21 - A numeração das comandas é sequencial e nunca se repete.
    - RN22 - Só pode haver um caixa aberto por vez em cada unidade.
    - RN23 - As quinzenas de comissão vão do dia 1 ao 15 e do dia 16 ao último dia do mês. Cada profissional tem apenas um fechamento por quinzena.
    - RN24 - O percentual de comissão específico da profissional no serviço prevalece sobre o percentual padrão do serviço.
    - RN25 - A comissão é calculada sobre o valor final cobrado (com variação, acréscimo e desconto comercial), deduzidos o custo de produto dos serviços químicos (quando configurado) e a taxa da forma de pagamento, de forma proporcional. Os vales são abatidos no fechamento da quinzena.
    - RN26 - A venda de produto de revenda gera 10% de comissão para quem vendeu.
    - RN27 - Apenas profissionais parceiras recebem comissão. Auxiliares e funcionárias CLT não recebem.
    - RN28 - A profissional só pode ser agendada para os serviços que realiza.
    - RN29 - Um horário não pode exceder a disponibilidade da profissional nem dos recursos físicos (ex: uma sala de estética, dois lavatórios). Encaixes em conflito exigem confirmação da coordenadora ou da dona.
    - RN30 - Bloqueios de folga ou dia inteiro devem ser solicitados com pelo menos 7 dias de antecedência, e bloqueios de algumas horas com pelo menos 48 horas. Solicitações fora do prazo são aceitas com alerta, e a decisão fica com a coordenadora ou a dona.
    - RN31 - Folgas em dias de maior fluxo só podem ser aprovadas pela dona.
    - RN32 - Um bloqueio pendente impede novos agendamentos no horário. Um bloqueio não pode ser aprovado sobre clientes já marcadas sem a remarcação delas.
    - RN33 - A confirmação de agendamentos é feita no dia de funcionamento anterior (ex: atendimentos de terça são confirmados no sábado, pois o salão fecha domingo e segunda).
    - RN34 - O parcelamento no crédito (ex: até 3x sem juros acima de R$ 300) segue as condições configuradas pela dona.
    - RN35 - A cobrança de sinal é opcional por cliente (ex: 30% na progressiva), e o valor é abatido no pagamento final.
    - RN36 - As sessões de pacote só podem ser utilizadas dentro da validade do pacote.
    - RN37 - O salão não vende fiado. Valores pendentes são registrados apenas como exceção, com motivo, para cobrança posterior.

## 7. Duvidas Pendentes
<!-- Liste questoes tecnicas ou operacionais ainda sem resposta, que precisam ser validadas com o cliente antes ou durante o desenvolvimento. -->

    - Gorjeta: pode ir 100% para a profissional, fora da comissão e sem desconto de taxa? Deve constar no relatório da contadora? (validar com a contadora)
    - Nota fiscal no regime salão-parceiro: quem emite o quê, se por atendimento ou por mês, e se o sistema precisará emitir no futuro. (validar com a contadora)
    - Legalidade e conformidade contratual do desconto da taxa da maquininha e do custo de produto na comissão. (validar com a contadora)
    - Colunas e formato exatos do relatório mensal da contadora.
    - Prazos de bloqueio (7 dias e 48 horas) e limites da coordenadora (15% de desconto, 20% de acréscimo). (validar com a coordenadora)
    - Conteúdo dos checklists de abertura e fechamento. (validar com a coordenadora)
    - Durações reais de cada serviço e de cada variação de tamanho. (validar com a coordenadora)
    - Conferir se os percentuais de comissão a cadastrar batem com os contratos de parceria de cada profissional.
    - Cortesia: definido provisoriamente como exclusiva da dona. Avaliar se a coordenadora também poderá conceder.
    - Custo de produto nos serviços químicos na primeira versão: custo fixo por serviço ou valor informado na comanda.
    - Limite de acréscimo da recepcionista (não definido; só o da coordenadora foi definido).
    - Quais são os "dias de maior fluxo" para a regra de aprovação de folga (fixos ou configuráveis).
    - Regra de restrição para clientes com faltas recorrentes (quantidade de faltas, período e consequência).
    - Importação dos contatos existentes (~1.500) e das fichas de coloração, ou digitação manual.
    - Validar o funcionamento das notificações push no iPhone da dona. Se não atender, reavaliar o aplicativo nativo.
    - Tempo de resposta esperado não definido.

