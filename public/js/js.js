$(document).ready(function(){
	$('.fileinput-button').on('change', function() {
    	$.ajax({
    		type: 'POST',
    		url: '/upload',
			cache: false,
			datatype: 'json',
			data: {test: 'kingen'}
			success: function(msg){
				console.log(msg)
				
			},
			error: function(){
				alert('Nu blev det fel!');
			}
		});
		//showPreview(this);
		
    });
    
	function showPreview(input) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();
			
			reader.onload = function (e) {
			$('.active-img')
			.attr('src', e.target.result)
			.width(150)
			.height(200);
			};
			reader.readAsDataURL(input.files[0]);
		}
	}
});