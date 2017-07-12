$('.like').on('click', function(event){
  event.preventDefault();
  var element = $(this);
  $.ajax({
    url: '/like_treasure/',
    method: 'GET',
    data: {treasure_id: element.attr('data-id')},
    success: function(response){
      element.html('Likes: ' + response);
    }
  })
})
$( ".date-card" ).on( "click", ".delete-date", function( event ) {
    event.preventDefault();
    $.ajax({
      url: '/delete_treasure/',
      method: 'GET',
      data: {treasure_id: element.attr('data-id')},
      success: function(response){
         $(this).parent().remove();
      }
    })

});
// $('.delete').on('click', "a", function(event){
//   event.preventDefault();
//   var element = $(this);
  // $.ajax({
  //   url: '/delete_treasure/',
  //   method: 'GET',
  //   data: {treasure_id: element.attr('data-id')},
  //   success: function(response){
      // element.parent().remove();
      $(this).parent().remove();
  //   }
  // })
// })
