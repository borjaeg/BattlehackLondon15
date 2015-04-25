$(document).ready(function() {
  $(".challenge").on('click', function(){
    console.log("project");
    challenge = $(this).text().substring(2, $(this).text().length-1)
    /*$.get("/project", {challenge: challenge}, function(data){
      if (data == "0")*/
        window.location.href="challenge/" + challenge;
      /*else if(data == "-1"){
        window.location.href="invalid"
        console.log("Unknown Email");
      }*/
    })
  //});

 /* $('#usr').keypress(function (e) {
    if (e.which == 13) {
      var email = $(this).val();
      $.get("/authenticate", {email: email}, function(data){
        if (data == "0")
          window.location.href="projects"
        else if(data == "-1")
          window.location.href="invalid"
        else if(data == "-2")
          window.location.href="repeat"
      })
    }
  });*/

  setTimeout(function(){$(".winner").fadeIn('slow');}, 3000);
});