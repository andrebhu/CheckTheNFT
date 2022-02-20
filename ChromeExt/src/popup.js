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

function color_duplicates(duplicates){
	if (duplicates > 0) {
  		return "#FFAF42" 
	}
	return "#00aaf2"
}

function goPython(){
	
chrome.tabs.query({active: true, lastFocusedWindow: true, currentWindow: true}, tabs => {
    let url = tabs[0].url;
	console.log(url)
	let newURL = "http://localhost:5000/opensea?url="+url
//	chrome.tabs.create({ url: newURL });
	var result = getValue(newURL)
	console.log(result)
	document.getElementById("duplicates").innerHTML = "Found "+result["duplicates"] +" duplicates online";
	document.getElementById("duplicates").style = "border:2px solid #696969; border-radius:5px; font-size:18px; padding-left: 10px; padding-bottom: 5px; padding-top: 5px"
	document.getElementById("duplicates").style.backgroundColor = color_duplicates(result["duplicates"])

		
		
	document.getElementById("enhance").innerHTML = result["enhance_msg"];
	document.getElementById("verify").innerHTML = result["verify"];
})
}
