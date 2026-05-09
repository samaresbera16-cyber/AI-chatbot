function sendMessage(){

    let input = document.getElementById("userInput");
    let chatBody = document.getElementById("chatBody");

    let message = input.value.trim();

    if(message === ""){
        return;
    }


    // USER MESSAGE
    let userDiv = document.createElement("div");

    userDiv.classList.add("user-msg");

    userDiv.innerText = message;

    chatBody.appendChild(userDiv);

    chatBody.scrollTop = chatBody.scrollHeight;

    input.value = "";


    // SEND TO FLASK
    fetch("/chat", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    })

    .then(response => response.json())

    .then(data => {

        let botDiv = document.createElement("div");

        botDiv.classList.add("bot-msg");

        botDiv.innerText = data.reply;

        chatBody.appendChild(botDiv);

        chatBody.scrollTop = chatBody.scrollHeight;

    });

}



// ENTER KEY SUPPORT
let inputField = document.getElementById("userInput");

inputField.addEventListener("keypress", function(event){

    if(event.key === "Enter"){

        sendMessage();

    }

});



// OPEN / CLOSE CHATBOT
function toggleChat(){

    let chatbot = document.getElementById("chatbot");

    chatbot.classList.toggle("active");

}
