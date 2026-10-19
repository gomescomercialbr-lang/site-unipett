# Ficha de cadastro do cliente

Use esta lista ao fechar um novo cliente (clínica veterinária ou petshop)
para coletar tudo o que é necessário antes de configurar e publicar o site.
O site é o modelo "Clínica Pet Vida" — nada precisa ser reescrito no
`index.html`, só preenchido em `config.js`.

## 1. Dados básicos

- [ ] Nome oficial da clínica/petshop
- [ ] Slogan curto (uma linha)
- [ ] Qual versão o cliente é: **hospital** (emergência/internação/banco de
      sangue) ou **petshop** (banho e tosa/produtos/agendamento)?
- [ ] Cor principal desejada (verde-água, azul, rosa, roxo ou laranja — ou
      peça a cor exata do logo em hex, se for diferente das 5 prontas)

## 2. Contato

- [ ] WhatsApp completo, com DDI e DDD, só números (ex.: 5592988887777)
- [ ] Telefone para exibir formatado (ex.: (92) 98888-7777)
- [ ] Instagram (@usuario) e o link completo do perfil
- [ ] E-mail de contato, se for usar em algum lugar futuramente

## 3. Endereço

- [ ] Rua e número
- [ ] Bairro
- [ ] Cidade e estado (UF)
- [ ] CEP
- [ ] Ponto de referência, se ajudar o cliente a chegar
- [ ] Link do Google Maps com a rota até o endereço (ou gere a partir do
      endereço acima — veja o passo a passo mais abaixo)
- [ ] Link da página de avaliações no Google (Google Meu Negócio)

## 4. Horário de funcionamento

- [ ] É 24h todos os dias, ou tem horário específico? Se tiver horário
      específico, anote por dia da semana — o texto do site precisará
      de um pequeno ajuste manual em `config.js` (campo `horario`)

## 5. Responsável técnico (obrigatório para clínicas veterinárias)

- [ ] Nome do médico-veterinário responsável
- [ ] Número do CRMV e estado de registro
- [ ] Esse dado não aparece no site hoje — se o cliente quiser exibir,
      peça onde (rodapé é o lugar mais comum) e inclua manualmente

## 6. Serviços oferecidos (liga/desliga)

Marque o que o cliente realmente oferece — cada um vira `true`/`false`
em `config.js` → `CONFIG.servicos`:

- [ ] Emergência 24h
- [ ] Internação
- [ ] Doenças virais (diagnóstico/tratamento)
- [ ] Banco de sangue
- [ ] Vacinação
- [ ] Banho e tosa
- [ ] Petshop / loja de produtos (chave-mestra da seção "Petshop e cuidados")
- [ ] Ração
- [ ] Brinquedos
- [ ] Caminhas
- [ ] Acessórios

## 7. Identidade visual

- [ ] Logo em alta resolução (.png com fundo transparente ou .svg),
      de preferência com o ícone separado do nome por extenso
- [ ] Cores exatas da marca, em hex, se não for usar uma das 5 paletas
      prontas
- [ ] Fotos reais da clínica/petshop e da equipe, se houver (substituem
      as fotos de banco de imagens usadas no modelo)
- [ ] Vídeo real da clínica/petshop para a abertura, se houver (formato
      próximo de 16:9, pelo menos 1920×1080, 5 a 10 segundos)

## 8. Acessos

- [ ] Acesso de administrador ao Google Meu Negócio (ou convite para o
      e-mail que vai gerenciar)
- [ ] Domínio: o cliente já tem um? Se sim, pedir acesso ao painel de DNS
      (Registro.br, GoDaddy, etc.) ou pedir para o cliente apontar o
      domínio para a Vercel
- [ ] Confirmar quem paga e é dono do domínio e da conta Vercel/GitHub
      no longo prazo

---

## Passo a passo para configurar e publicar

1. **Duplique o projeto** (ou crie um branch/repo novo a partir dele) para
   não misturar configurações de clientes diferentes.
2. **Edite `config.js`** com os dados coletados acima:
   - `tipo`: `"hospital"` ou `"petshop"`
   - `corPaleta`: uma das chaves de `PALETTES` (ou adicione uma nova
     paleta com as cores exatas da marca)
   - `nome`, `slogan`, `whatsapp`, `telefone`, `telefoneLink`, `endereco`,
     `mapsLink`, `avaliacoesLink`, `horario`, `instagram`, `instagramLink`
   - `servicos`: ligue/desligue cada item da lista do item 6
   - Revise os textos de `abertura`, `estrutura`, `petshopSecao` e
     `contatoTitulo` — os tokens `{nome}` e `{cidade}` são trocados
     automaticamente, o resto pode ser reescrito livremente
3. **Troque as imagens**, se houver fotos/vídeo reais:
   - Vídeo da abertura: gere `abertura-desktop.mp4` (1920px), 
     `abertura-mobile.mp4` (960px) e `abertura.webp` (poster) com ffmpeg,
     na pasta `assets/`, e aponte `CONFIG.video` para os novos arquivos
   - Fotos do petshop: substitua `banho-tosa.webp`, `racao.webp`,
     `brinquedos.webp`, `caminhas.webp`, `acessorios.webp` (proporção
     4:3, WebP) e ajuste o campo `imagem`/`alt` de cada item em
     `CATALOGO_SERVICOS` dentro de `config.js`
   - Logo: gere um novo favicon/apple-touch-icon/og-image a partir do
     logo do cliente (veja `scripts/make_petvida_brand.py` como
     referência) e troque o ícone inline (SVG) no `index.html` se o
     cliente não usar uma patinha
4. **Remova a faixa de demonstração e o `noindex`**:
   - Apague o `<meta name="robots" content="noindex, nofollow">` do
     `<head>` do `index.html`
   - Esvazie `CONFIG.faixaDemo` (string vazia `""`) para a faixa não
     aparecer mais
5. **Teste localmente** em 390px e 1440px, nas duas versões
   (`?tipo=hospital` e `?tipo=petshop`) antes de publicar.
6. **Suba o código** para um repositório próprio do cliente no GitHub e
   publique na Vercel em produção (`vercel --prod`).
7. **Aponte o domínio do cliente** nas configurações do projeto na
   Vercel (ou `vercel domains add`) e confirme que o certificado SSL
   foi emitido e o site abre no domínio final.
8. **Entregue ao cliente**: link do site, acesso ao repositório (se ele
   quiser) e explique que qualquer alteração de texto, telefone, cores
   ou serviços se faz editando só o `config.js`.
