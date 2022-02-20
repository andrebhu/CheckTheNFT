/* File: popup.js
 * -----------------------
 * This javascript file restores settings when the DOM loads.
 * You shouldn't have to change this file unless you also
 * change the corresponding popup.html file.
 */

const element = document.getElementById("script");
element.addEventListener("click", goPython);

function goPython(){
chrome.tabs.query({active: true, lastFocusedWindow: true, currentWindow: true}, tabs => {
    let url = tabs[0].url;
	let newURL = "http://localhost:5000/opensea?url="+url
	chrome.tabs.create({ url: newURL });
//	alert(url)
	
    // use `url` here inside the callback because it's asynchronous!
});
}
