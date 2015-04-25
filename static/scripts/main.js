$(document).ready(function() {

  $(".challenge").on('click', function(){
    console.log("project");
    challenge = $(this).text().substring(2, $(this).text().length-1)
    /*$.get("/project", {challenge: challenge}, function(data){
      if (data == "0")*/
        window.location="challenge/" + challenge;
      //$(document).load("challenge/" + challenge);

      /*else if(data == "-1"){
        window.location.href="invalid"
        console.log("Unknown Email");
      }*/
    })

  
  //});   

/*$( "#checkout" ).submit(function( event ) {

  console.log("submitting form");
  // Stop form from submitting normally
  event.preventDefault();

  // Get some values from elements on the page:
  var $form = $( this ),
  term = $form.find( "input[name='s']" ).val(),
  url = $form.attr( "action" );

  console.log(term);
  console.log(url);

  // Send the data using post
  var posting = $.post( url, { s: term } );

  // Put the results in a div
  posting.done(function( data ) {
    console.log(data);
    var content = $( data ).find( "#content" );
    $( "#result" ).empty().append( content );
  });
});*/
});