/* File: popup.js
 * -----------------------
 * This javascript file restores settings when the DOM loads.
 * You shouldn't have to change this file unless you also
 * change the corresponding popup.html file.
 */

const element1 = document.getElementById("script");
element1.addEventListener("click", goPython);

function getValue(url){
   var value= $.ajax({ 
      url: url, 
      async: false
   }).responseJSON;
	console.log(value)
   return value;
}

function goPython(){
	
chrome.tabs.query({active: true, lastFocusedWindow: true, currentWindow: true}, tabs => {
    let url = tabs[0].url;
	console.log(url)
	let newURL = "http://localhost:5000/opensea?url="+url
//	chrome.tabs.create({ url: newURL });
	var result = getValue(newURL)
	console.log(result)
	document.getElementById("duplicates").innerHTML = "Found "+result["duplicates"] +" duplicates";
	document.getElementById("enhance").innerHTML = result["enhance_msg"];
	document.getElementById("verify").innerHTML = result["verify"];
})
}
