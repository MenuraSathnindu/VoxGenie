function startListening() {
  fetch("/listen")
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").innerText = "🗣️ " + data.command;
    });
}
