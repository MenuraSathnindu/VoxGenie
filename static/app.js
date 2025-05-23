function startListening() {
    fetch("/listen")
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = "🗣️ " + data.command;
        });

    function startListening() {
        const wave = document.getElementById("wave");
        const status = document.getElementById("status");
        const resultText = document.getElementById("response-text");

        // Show wave animation
        wave.classList.add("listening");
        status.innerText = "🎧 Listening...";

        fetch("/listen")
            .then(response => response.json())
            .then(data => {
                wave.classList.remove("listening");
                status.innerText = "✅ Processed!";
                resultText.innerText = `🗣️ You said: ${data.command}`;
            })
            .catch(err => {
                wave.classList.remove("listening");
                status.innerText = "⚠️ Error listening.";
                resultText.innerText = "";
            });
    }
}
