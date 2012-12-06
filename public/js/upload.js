String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}
$(document).ready(function() {
	hideLoading();
	var formdata = false, imgName;

	function showUploadedItem (source) {
		addImg({ 'src': source, 'id': imgName, 'class': 'img-instapy img-active', 'data-filter-name': 'Original'}, true)
	}   

	if (window.FormData) {
  		formdata = new FormData();
  		$("#btn-submit").hide();
	}
	
 	$('input').on('change', function(){
 		$('#upload-form').slideUp('slow');
 		showLoading();
 		var i = 0, len = this.files.length, img, reader, file;
 		if(len > 0){
			for ( ; i < len; i++ ) {
				file = this.files[i];
				imgName = file.name;
				if (!!file.type.match(/image.*/)) {
					if ( window.FileReader ) {
						reader = new FileReader();
						reader.onloadend = function (e) {
							showUploadedItem(e.target.result);
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
						//addImg({ 'src': data.filtered, 'id': data.filtered.substring(26), 'class': 'img-instapy'});
						addFilters(data.available_filters, data.org);
						hideLoading();
					},
					error: function (data) {
						$('#img-container').html('Server Error');
						hideLoading();
					}
				});
			}
		}
	});
	
	// Upload new image
	$('#img-new').on('click', function(){
		newImg();
		hideLoading();
	});
	
	// Change image
	$('#img-list').on('click', 'div', function(){
		var img = $(this).children('.img-instapy');
		changeImg(img);
	});
	
	// Change image on key
	$(document).keydown(function(e){
		if(!$('#img-container').is(':empty')){
		    if (e.keyCode == 37){
		    	getPrevImg();
		    }
		    if (e.keyCode == 39){
		    	getNextImg();
		    }
		}
	});
	
	// Adds image to img list and if 'show' == true shows image
	function addImg(props, show)
	{
		show = (typeof show === "undefined") ? false : show;
		
		$('#img-new').removeClass('hide');
		$('#img-new').prop('disabled', false);
		
		var labelText = props['data-filter-name'];
		
		var div = $('<div />', {'class': 'img-thumbnail'});
		var img = $('<img />', props);
		var label = $('<p />', {'class': 'img-label'}).text(labelText.capitalize());
		
		img.appendTo(div);
		label.appendTo(div);
		div.appendTo('#img-list');
		
		if (show){
			$('#img-container').empty();
			delete props['id'];
			delete props['class'];
			props['class'] = 'img-instapy';
			$('<img />', props).appendTo('#img-container');
		}
		$('#img-list').fadeIn();
		$('#img-container').fadeIn();
	}
	
	function addFilters(filterList, path)
	{
		var imgOrg = path.split("/");
		imgOrg = imgOrg[imgOrg.length - 1];
		
		for(var i = 0; i < filterList.length; i++){
			filter = filterList[i];
			$.ajax({
				url: '/filter/' + imgOrg + '/' + filter,
				type: 'GET',
				success: function (data) {
					addImg({ 'src': data.src, 'id': imgOrg, 'class': 'img-instapy', 'data-filter-name': data.filter});
					checkLoading(filterList.length);
				},
				error: function (data) {
					$('#img-container').html('Server Error');
				}
			});
		}
	}
	
	function newImg()
	{
		$('#img-new').prop('disabled', true);
		$('#img-list').empty();
		$('#img-list').fadeOut();
		$('#img-container').fadeOut();
		$('#upload-form').slideDown('slow');
		$('<img />', {'src': 'img/loading.gif', 'class': 'loading'}).appendTo('#img-list');
	}
	function getNextImg()
	{
		var newImg = $('.img-active').parent().next().children('.img-instapy');
		if (newImg.length == 1){
			changeImg(newImg);
		}
	}
	function getPrevImg()
	{
		var newImg = $('.img-active').parent().prev().children('.img-instapy');
		if (newImg.length == 1){
			changeImg(newImg);
		}
	}
	function changeImg(img)
	{
		$('#img-container').empty();
		$('.img-instapy').removeClass('img-active')
		img.addClass('img-active');
		var new_img = img.clone().removeProp('id').removeClass('img-active').appendTo("#img-container");
	}
	function showLoading()
	{
		$('#loading-gif').show();
	}
	function hideLoading()
	{
		$('#loading-gif').hide();
	}
	function checkLoading(filtersLength)
	{
		if($('#img-list div').length == filtersLength){
			$('#img-list .loading').fadeOut();
		}
	}
});