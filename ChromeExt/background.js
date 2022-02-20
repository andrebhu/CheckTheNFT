var serverhost = 'http://localhost:5000/';

	chrome.runtime.onMessage.addListener(
		function(request, sender, sendResponse) {
		  
			  
			
			console.log(serverhost);
			
			//var url = "http://127.0.0.1:8000/wiki/get_wiki_summary/?topic=%22COVID19%22"	
			fetch(serverhost)
			.then(response => response.json())
			.then(response => sendResponse({farewell: response}))
			.catch(error => console.log(error))
				
			return true;  // Will respond asynchronously.
		  
	});
