$(document).ready(function() {
    $("#UploadInfo").click(function() {
        var gmailToReceive = $("#gmailToReceive").val();
        var textToReceive = $("#textToReceive").val();
        var serverName = $("#serverName").val();
        var trigger = $("#trigger").val();

        $.ajax({
            type: "POST",
            url: "PHP/mysql_update.php",
            data: {
                gmailToReceive: gmailToReceive,
                textToReceive: textToReceive,
                serverName: serverName,
                trigger: trigger
            },
            success: function(response) {
                console.log(response);
                alert("Information submitted successfully!");
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
                alert("An error occurred while submitting the information.");
            }
        });
    });
});
/* Next update content:
function colorchange(){
document.getElementById('changeColorButton').addEventListener('click', function() {
    var selectedColor = document.getElementById('backgroundColorOptions').value;
    document.body.style.backgroundColor = selectedColor;
});}
 */