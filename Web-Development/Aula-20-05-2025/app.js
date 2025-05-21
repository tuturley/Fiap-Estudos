const form = document.getElementById('form');
const inputNome = document.getElementById('nome');
const inputEmail = document.getElementById('email');
const inputAssunto = document.getElementById('assunto');
const inputMensagem = document.getElementById('mensagem');
const btnEnviar = document.getElementById('btnEnviar');
const paragrafo = document.getElementById('paragrafo');
const cadastro = document.getElementById('cadastroUsuario');

btnEnviar.addEventListener('click', function (event) {
    event.preventDefault();

    let nome = inputNome.value;
    let email = inputEmail.value;
    let mensagem = inputMensagem.value;
    if (nome === "" || email === ""){
        paragrafo.textContent = "Preencha os campos corretamente POR FAVOR!!!."
        paragrafo.style.color = "#ff0000"
        // paragrafo.classList.add('mensagem-alerta') acionar o css diretamente
        // paragrafo.src = ""  trocar a imagem
        return
    };
    
    let card = document.createElement('div')
    card.classList.add('card')
    card.innerHTML = `
    <h3> Nome: ${nome}</h3>
    <h3> Email: ${email}</h3>
    <p> Mensagem: ${mensagem}</p>
    `
    cadastro.append(card)

    form.reset()
})
