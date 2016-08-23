$(document).ready(
	function(){
		$('#uploadBtn').click(function(e){
			//e.preventDefault();
			if ($('#inputFile').get(0).files.length === 0) {
				e.preventDefault();
			    console.log("No files selected.");
			}

		});


	}
)