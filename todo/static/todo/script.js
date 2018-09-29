			//TASK TYPE script 
			$(".dropdown-menu li a").click(function(){
	  			$(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
	  			$(this).parents(".dropdown").find('.btn').val($(this).data('value'));
			});

			//DATE_ADD script
			$("#date_add").val($.datepicker.formatDate('D, d M yy', new Date()));
			$(function(){
				$('#date_add').datepicker({
					'format': 'D, d M yy',
					'autoclose' : true
				})
			});
			$("#date_add").change(function() {
    			$('#date_selected').val($(this).data('value'));
			});

			//DATE_SEARCH
			$("#date_search").val($.datepicker.formatDate('DD, d M yy', new Date()));
			$(function(){
				$('#date_search').datepicker({
					'format': 'DD, d M yy',
					'autoclose' : true
				})
			});
			$("#date").change(function() {
    			$('#date_selected').val($(this).data('value'))	
			});	
		