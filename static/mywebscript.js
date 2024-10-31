let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4) {
            if (this.status === 200) {
                const response = JSON.parse(this.responseText);
                // Show each emotion and its score
                let displayText = "Emotion Scores:\n";
                for (let emotion in response) {
                    displayText += `${emotion}: ${response[emotion]}\n`;
                }
                document.getElementById("system_response").innerText = displayText;
            } else {
                const error = JSON.parse(this.responseText).error || "An error occurred";
                document.getElementById("system_response").innerText = `Error: ${error}`;
            }
        }
    };
    xhttp.open("GET", `/analyze_emotion?textToAnalyze=${encodeURIComponent(textToAnalyze)}`, true);
    xhttp.send();
};
