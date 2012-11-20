(function () {
	var input = document.getElementById("img"), 
		formdata = false;

	function showUploadedItem (source) {
		$('<img />', { 'src': source}).appendTo('#preview-org');
	}   

	if (window.FormData) {
  		formdata = new FormData();
  		$("#btn-submit").hide();
	}
	
 	$('input').on('change', function(){
 		$('#upload-form').slideUp('slow');
 		$('#loading-gif').show();
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
						$('#image-list').remove();
						$('#response').html('');
						$('<img />', { 'src': data.filtered}).appendTo('#response');
					},
					error: function (res) {
						$('#response').html('Server Error'); 
					}
				});
			}
		}
	});
}());