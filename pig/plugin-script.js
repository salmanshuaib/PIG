(function($) {
    // Initialize variables to store team members' data
    var blueTeamMembers = [];
    var greenTeamMembers = [];

    // Function to prompt the user for BLUE Team members' data
    function setupBlueTeam() {
        var name = prompt("Enter BLUE Team-member NAME:");
        var comment = prompt("Enter COMMENT about an activity:");
        var time = prompt("Select Hour and Minutes from a digital clock (e.g., HH:MM AM/PM):");

        if (name && comment && time) {
            blueTeamMembers.push({ name: name, comment: comment, time: time });
            setupBlueTeam(); // Repeat for the next member
        } else {
            // User completed entering BLUE Team members
            setupGreenTeam();
        }
    }

    // Function to prompt the user for GREEN Team members' data
    function setupGreenTeam() {
        var name = prompt("Enter GREEN Team-member NAME:");
        var posture = prompt("Enter Yoga Posture:");

        if (name && posture) {
            greenTeamMembers.push({ name: name, posture: posture });
            setupGreenTeam(); // Repeat for the next member
        } else {
            // User completed entering GREEN Team members
            startNotifications();
        }
    }

    // Function to start notifications when time matches BLUE Team members' time
    function startNotifications() {
        setInterval(function() {
            var currentTime = new Date();
            var currentHour = currentTime.getHours();
            var currentMinutes = currentTime.getMinutes();
            var ampm = currentHour >= 12 ? "PM" : "AM";

            // Format the current time in HH:MM AM/PM
            var formattedTime =
                (currentHour % 12 || 12) + ":" + (currentMinutes < 10 ? "0" : "") + currentMinutes + " " + ampm;

            // Check if any BLUE Team members' time matches the current time
            blueTeamMembers.forEach(function(member) {
                if (member.time === formattedTime) {
                    // Notify the user about the BLUE Team member
                    alert("Time to check BLUE Team-member: " + member.name + "\n" + member.comment);
                }
            });
        }, 60000); // Check every minute
    }

    // Initialize user setup when the plugin is activated
    $(document).ready(function() {
        setupBlueTeam();
    });
})(jQuery);
