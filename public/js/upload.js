$(document).ready(function() {
	var formdata = false;

	function showUploadedItem (source) {
		addImg({ 'src': source, 'id': 'img-original', 'class': 'img-instapy'}, false)
	}   

	if (window.FormData) {
  		formdata = new FormData();
  		$("#btn-submit").hide();
	}
	
 	$('input').on('change', function(){
 		$('#upload-form').slideUp('slow');
 		$('#img-container').slideDown('slow');
 		var i = 0, len = this.files.length, img, reader, file;
 		if(len > 0){
			for ( ; i < len; i++ ) {
				file = this.files[i];
		
				if (!!file.type.match(/image.*/)) {
					if ( window.FileReader ) {
						reader = new FileReader();
						reader.onloadend = function (e) { 
							showUploadedItem(e.target.result, file.fileName);
						};
						reader.readAsDataURL(file);
					}
					if (formdata) {
						formdata.append("data", file);
					}
				}	
			}
		
			if (formdata) {
				formdata.append('filter', $('#filter-select').val());
				$.ajax({
					url: "/upload",
					type: "POST",
					data: formdata,
					processData: false,
					contentType: false,
					success: function (data) {
						$('#img-container').html('');
						$('#img-toggle').fadeIn('slow');
						addImg({ 'src': data.filtered, 'id': 'img-filtered', 'class': 'img-instapy'})
					},
					error: function (data) {
						$('#img-container').html('Server Error'); 
					}
				});
			}
		}
	});
	
	// Show original image
	$('#img-toggle').on('click', function(){
		toggleImg();
		
	});
	
	// Adds image to img list and if 'show' == true shows image
	function addImg(props, show)
	{
		show = (typeof show === "undefined") ? true : show;
		$('<img />', props).appendTo('#img-list');
		if (show){
			$('#img-container').html('');
			$('<img />', props).appendTo('#img-container');
		}
	}
	
	function toggleImg()
	{
		var curImg = $('#img-container .img-instapy');
		$('#img-container').html('');
		if (curImg.prop('id') == 'img-filtered'){
			$('#img-list #img-original').clone().appendTo("#img-container");
			$('#img-toggle').text('Show filtered image');
		}else if (curImg.prop('id') == 'img-original'){
			$('#img-list #img-filtered').clone().appendTo("#img-container");
			$('#img-toggle').text('Show original image');
		}else{
			$('#img-container').html('Error when toggle image.');
		}
	}
});