(function(){

	$(".flex-slide").each(function(){
		$(this).hover(function(){
			$(this).find('.flex-title').css({
				transform: 'rotate(0deg)',
				top: '10%'
			});
			$(this).find('.flex-about').css({
				opacity: '1'
			});
		}, function(){
			$(this).find('.flex-title').css({
				transform: 'rotate(90deg)',
				top: '15%'
			});
			$(this).find('.flex-about').css({
				opacity: '0'
			});
		})
	});
})();
$(document).ready(function() {
  $('#menu').click(function() {
 
    	$('#mainWrapper').css({"position": "absolute"});
    	$('.flex-container').slideDown(function() {

      $('.flex-container').css({"display": "flex"})
  });
  })
  $('#home').click(function() {
 
    	$('#mainWrapper').css({"position": "reletive"});
    	$('.flex-container').slideUp(function() {

      $('.flex-container').css({"display": "none"})
  });
  })
})