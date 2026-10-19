/*
 * config.js — TUDO que muda de um cliente para outro fica neste arquivo.
 * O index.html não tem nenhum dado de cliente fixo: ele lê este arquivo
 * e monta a página (textos, links, cores, JSON-LD, meta tags) em tempo
 * de execução. Para reaproveitar o site para um novo cliente, edite
 * apenas este arquivo — veja também CADASTRO-CLIENTE.md.
 */

/* Paletas de cor prontas. "principal" é a cor de botões/links/ícones de
   destaque; "destaque" é a cor secundária (selos, marcadores). Os tons
   *Dark/*Darker já são pensados para manter contraste AA com texto branco. */
var PALETTES = {
  verde:   { principal: "#01C1C2", principalDark: "#017F80", principalDarker: "#016061",
             destaque:  "#FF75B0", destaqueDark:  "#AD5078", destaqueDarker:  "#7F3B58" },
  azul:    { principal: "#2563EB", principalDark: "#1D4ED8", principalDarker: "#1E3A8A",
             destaque:  "#F59E0B", destaqueDark:  "#B45309", destaqueDarker:  "#78350F" },
  rosa:    { principal: "#EC4899", principalDark: "#BE185D", principalDarker: "#831843",
             destaque:  "#01C1C2", destaqueDark:  "#017F80", destaqueDarker:  "#016061" },
  roxo:    { principal: "#8B5CF6", principalDark: "#6D28D9", principalDarker: "#4C1D95",
             destaque:  "#FF75B0", destaqueDark:  "#AD5078", destaqueDarker:  "#7F3B58" },
  laranja: { principal: "#F97316", principalDark: "#C2410C", principalDarker: "#7C2D12",
             destaque:  "#01C1C2", destaqueDark:  "#017F80", destaqueDarker:  "#016061" }
};

/* Catálogo de todos os serviços que o modelo sabe exibir. "liga/desliga"
   cada um em CONFIG.servicos. tipo:"icone" vai na faixa "Estrutura";
   tipo:"foto" vai na grade "Petshop e cuidados". */
var CATALOGO_SERVICOS = {
  emergencia24h: { titulo: "Emergência 24h", cor: "principal", icone: "pulso",
    descricao: "Toda hora é hora de levar seu pet se algo não estiver bem. Nossa equipe está de prontidão 24 horas, todos os dias, inclusive feriados." },
  internacao: { titulo: "Internação", cor: "destaque", icone: "internacao",
    descricao: "Estrutura completa para internação e acompanhamento contínuo de pets que precisam de cuidados intensivos." },
  doencasVirais: { titulo: "Doenças virais", cor: "principal", icone: "virus",
    descricao: "Diagnóstico e tratamento de cinomose, parvovirose e outras doenças virais, com estrutura para internação e acompanhamento intensivo." },
  bancoSangue: { titulo: "Banco de sangue", cor: "destaque", icone: "gota",
    descricao: "Bolsas de sangue disponíveis para transfusão na hora da emergência — um diferencial que pode salvar a vida do seu pet." },
  vacinacao: { titulo: "Vacinação", cor: "principal", icone: "seringa",
    descricao: "Protocolo completo de vacinas para cães e gatos, com carteirinha em dia e lembrete da próxima dose." },
  banhoTosa: { titulo: "Banho e tosa", tipo: "foto", imagem: "/assets/banho-tosa.webp",
    alt: "Cão enrolado em toalha macia após o banho",
    descricao: "Seu pet volta para casa cheiroso, escovado e bem cuidado — sem precisar rodar a cidade atrás de um lugar de confiança." },
  racao: { titulo: "Ração", tipo: "foto", imagem: "/assets/racao.webp",
    alt: "Comedouro com ração seca para cães e gatos",
    descricao: "As principais marcas de ração para cães e gatos, com orientação de quem acompanha a saúde do seu pet de perto." },
  brinquedos: { titulo: "Brinquedos", tipo: "foto", imagem: "/assets/brinquedos.webp",
    alt: "Bolinhas, corda e pato de pelúcia entre os brinquedos do petshop",
    descricao: "Linha completa de brinquedos para toda hora de brincadeira, já na hora que você vier buscar ou visitar seu pet." },
  caminhas: { titulo: "Caminhas", tipo: "foto", imagem: "/assets/caminhas.webp",
    alt: "Gato dormindo em caminha felpuda redonda",
    descricao: "Caminhas confortáveis para todos os tamanhos e idades, do filhote ao pet mais idoso." },
  acessorios: { titulo: "Acessórios", tipo: "foto", imagem: "/assets/acessorios.webp",
    alt: "Cachorro sentado usando coleira com identificação",
    descricao: "Coleiras, guias, comedouros e tudo que seu pet precisa no dia a dia, sem sair do bairro." }
};
// marca os itens acima que não têm "tipo: foto" como sendo do tipo "icone"
Object.keys(CATALOGO_SERVICOS).forEach(function (k) {
  if (!CATALOGO_SERVICOS[k].tipo) CATALOGO_SERVICOS[k].tipo = "icone";
});

var CONFIG = {
  // "hospital" ou "petshop" — veja CONFIG_OVERRIDES_POR_TIPO mais abaixo
  tipo: "hospital",
  corPaleta: "verde", // uma das chaves de PALETTES

  nome: "Clínica Pet Vida",
  slogan: "Cuidado completo para o seu pet",

  // dados fictícios — troque pelos dados reais do cliente
  whatsapp: "5500000000000", // só dígitos, com DDI, usado no link wa.me
  telefone: "(00) 00000-0000",
  telefoneLink: "tel:+5500000000000",

  endereco: {
    rua: "Rua Exemplo, 123",
    bairro: "Centro",
    cidade: "Sua Cidade",
    estado: "UF",
    cep: ""
  },

  mapsLink: "https://www.google.com/maps/dir/?api=1&destination=Rua+Exemplo%2C+123%2C+Centro%2C+Sua+Cidade",
  avaliacoesLink: "https://www.google.com/maps/search/?api=1&query=Pet+Vida+Rua+Exemplo+123+Centro+Sua+Cidade",

  horario: "Aberto 24 horas, todos os dias",

  instagram: "@clinicapetvida",
  instagramLink: "https://instagram.com/clinicapetvida",

  // deixe vazias até ter números reais — nunca invente uma nota
  notaGoogle: "",
  totalAvaliacoes: "",

  faixaDemo: "Site de demonstração – personalize com a marca da sua clínica",

  video: {
    desktop: "/assets/abertura-desktop.mp4",
    mobile: "/assets/abertura-mobile.mp4",
    poster: "/assets/abertura.webp",
    alt: "Criança abraçando um filhote de cachorro ao lado de um gato"
  },
  imagemFechamento: {
    src: "/assets/fechamento.webp",
    alt: "Mão acariciando um filhote de cachorro deitado ao lado de um gatinho"
  },

  // textos por versão — {nome} e {cidade} são trocados automaticamente
  abertura: {
    hospital: {
      titulo: "Seu pet cuidado a qualquer hora. Dia e noite, 24h.",
      subtitulo: "Atendimento veterinário 24 horas em {cidade}. Emergência, internação, banco de sangue, vacinas e petshop completo no mesmo endereço.",
      botaoPrincipal: "Chamar no WhatsApp",
      mensagemWhatsapp: "Olá! Vim pelo site da {nome} e gostaria de atendimento."
    },
    petshop: {
      titulo: "Seu pet sempre limpo, feliz e bem cuidado",
      subtitulo: "Banho, tosa, produtos e tudo que seu pet precisa, perto de você em {cidade}.",
      botaoPrincipal: "Agendar banho e tosa",
      mensagemWhatsapp: "Olá! Vim pelo site da {nome} e gostaria de agendar banho e tosa."
    }
  },

  selos: {
    hospital: ["Hospital veterinário", "Aberto 24h", "Banco de sangue", "Petshop"],
    petshop: ["Banho e tosa", "Agende já", "Produtos", "Pet friendly"]
  },

  estrutura: {
    hospital: {
      titulo: "Hospital, emergência e petshop no mesmo endereço",
      subtitulo: "24 horas por dia, todos os dias, inclusive feriados."
    },
    petshop: {
      titulo: "Banho, tosa e tudo para o seu pet no mesmo lugar",
      subtitulo: "Agende pelo WhatsApp e garanta o horário do seu pet."
    }
  },

  petshopSecao: {
    hospital: { titulo: "Petshop e cuidados", subtitulo: "Tudo para o dia a dia do seu pet, no mesmo endereço do hospital." },
    petshop: { titulo: "Produtos e cuidados para o seu pet", subtitulo: "Tudo que você precisa, em um só lugar." }
  },

  balaoFlutuante: {
    hospital: "Emergência? Fale agora",
    petshop: "Dúvidas? Fale agora"
  },

  contatoTitulo: "Venha até a {nome} ou fale com a gente agora",

  // liga (true) / desliga (false) cada serviço do catálogo acima
  servicos: {
    emergencia24h: true,
    internacao: true,
    doencasVirais: true,
    bancoSangue: true,
    vacinacao: true,
    banhoTosa: true,
    petshop: true, // chave-mestra: mostra/esconde a seção "Petshop e cuidados" inteira
    racao: true,
    brinquedos: true,
    caminhas: true,
    acessorios: true
  }
};

/* O que muda automaticamente quando CONFIG.tipo = "petshop".
   Mescla por cima do CONFIG acima (merge raso em "servicos"). */
var CONFIG_OVERRIDES_POR_TIPO = {
  petshop: {
    servicos: { emergencia24h: false, internacao: false, bancoSangue: false }
  }
};
