//5. TV Input Interaction (JavaScript):**
//javascript
// Example JavaScript code to handle TV input and recommend Yoga posture
function handleTVInput(input) {
    // Get the initial letter of the input
    var initialLetter = input.charAt(0).toUpperCase();
    
    // Fetch GREEN Team members from the server based on the initial letter
    // Display the options to the user and recommend a Yoga posture
    // ...

    // Example code to display a pop-up
    var popup = document.createElement("div");
    popup.className = "popup";
    popup.innerHTML = "Recommended Yoga Posture: " + recommendedYogaPosture;
    document.body.appendChild(popup);
}
