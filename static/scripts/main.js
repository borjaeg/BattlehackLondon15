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

   var iconFeature = new ol.Feature({
    geometry: new ol.geom.Point(ol.proj.transform([-0.90725, 41.659699], 'EPSG:4326', 'EPSG:3857'))
  });
  var iconStyle = new ol.style.Style({
    image: new ol.style.Icon( /** @type {olx.style.IconOptions} */ ({
      anchor: [0.5, 46],
      anchorXUnits: 'fraction',
      anchorYUnits: 'pixels',
      opacity: 0.9,
      src: 'static/images/map_logo_v2.png'
    }))
  });

    iconFeature.setStyle(iconStyle);

  var vectorSource = new ol.source.Vector({
    features: [iconFeature]
  });
  var vectorLayer = new ol.layer.Vector({
    source: vectorSource
  });

  var map = new ol.Map({
    target: 'map',
    interactions: ol.interaction.defaults({mouseWheelZoom:false}),
    layers: [
    new ol.layer.Tile({ source: new ol.source.OSM() }),
    vectorLayer
    ],
    view: new ol.View({
      center: ol.proj.transform([-0.907045, 41.659445], 'EPSG:4326', 'EPSG:3857'),
      zoom: 17
    })
  });
  var element = document.getElementById('popup');

  var popup = new ol.Overlay({
    element: element,
    positioning: 'bottom-center',
    stopEvent: false
  });
  map.addOverlay(popup);


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