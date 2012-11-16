$(document).ready(function(){
	/*$('#fileupload').fileupload({
        dataType: 'json',
        done: function (e, data) {
            alert(data);
        }
    });*/
	
	$('fileupload').on('change', function() {
    	$('#img-form').ajax({
    		type: 'POST',
    		url: '/upload',
			cache: false,
			datatype: 'json',
			data: {test: 'kingen'},
			success: function(msg){
				console.log(msg)
			},
			error: function(){
				alert('Nu blev det fel!');
			}
		});
		//console.log('hej');
		//showPreview(this);
		
    });
    
	/*function showPreview(input) {
		console.log('test');
		if (input.files[0]) {
			var reader = new FileReader();
			console.log(reader);
			reader.onload = function (e) {
			$('#active-img')
			.attr('src', e.target.result)
			.width(150)
			.height(200);
			};
			reader.readAsDataURL(input.files[0]);
		}
	}*/
});