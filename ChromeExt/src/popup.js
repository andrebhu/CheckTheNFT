/* File: popup.js
 * -----------------------
 * This javascript file restores settings when the DOM loads.
 * You shouldn't have to change this file unless you also
 * change the corresponding popup.html file.
 */

const element1 = document.getElementById("script");
element1.addEventListener("click", async () => {    
    await goPython(); 
//	await toggleLoader();
});

function getValue(url){
   var value= $.ajax({ 
      url: url, 
      async: false
   }).responseJSON;
	console.log(value)
   return value;
}

function style(metric, value){
	var orange = "#FFCD89"
	var blue = "#6FC8EE"
	if (metric == "duplicates"){
		if (value > 0) {
	  		return [orange, "https://raw.githubusercontent.com/andrebhu/CheckTheNFT/main/ChromeExt/icons/caution.png"]
		}
		return [blue, "https://raw.githubusercontent.com/andrebhu/CheckTheNFT/main/ChromeExt/icons/check.png"]
	}
	if (metric == "enhance"){
		if (value.includes("manipulations")) {
	  		return [orange, "https://raw.githubusercontent.com/andrebhu/CheckTheNFT/main/ChromeExt/icons/caution.png"]
		}
		return [blue, "https://raw.githubusercontent.com/andrebhu/CheckTheNFT/main/ChromeExt/icons/check.png"]
	}
	if (metric == "verify"){
		if (value.includes("Unverified")) {
	  		return [orange, "https://raw.githubusercontent.com/andrebhu/CheckTheNFT/main/ChromeExt/icons/caution.png"]
		}
		return [blue, "https://raw.githubusercontent.com/andrebhu/CheckTheNFT/main/ChromeExt/icons/check.png"]
	}
	
}

function duplicate_sentence(duplicates){
	// plural of duplicate handling if fuplicate not 1
	if (duplicates != 1){
		return "    "+duplicates +" duplicates found"
	}
	return "    "+duplicates +" duplicate found"
}

async function goPython(){
	chrome.tabs.query({active: true, lastFocusedWindow: true, currentWindow: true}, tabs => {
	    let url = tabs[0].url;
		console.log(url)
		let newURL = "http://localhost:5000/opensea?url="+url
		//	chrome.tabs.create({ url: newURL });
		console.log(newURL)
		var result = getValue(newURL)
		console.log(result)
		
			
		var [color, logo] = style("duplicates",result["duplicates"])
		var image = document.createElement('img');
		image.src = logo
		image.height = 30
		image.style="vertical-align:middle"
		document.getElementById("duplicates").innerHTML = duplicate_sentence(result["duplicates"])
		document.getElementById("duplicates").style = "border:2px solid #696969; border-radius:5px; font-size:16px; padding-left: 10px; padding-right: 10px; padding-bottom: 5px; padding-top: 5px; display:inline height:30px; width:230px; text-align: left; font-weight: bold;"
		document.getElementById("duplicates").style.backgroundColor = color
		document.getElementById("duplicates").prepend(image)	
		
		var [color, logo] = style("enhance",result["enhance"])
		var image = document.createElement('img');
		image.src = logo
		image.height = 30
		image.style="vertical-align:middle"
		document.getElementById("enhance").innerHTML = "    "+result["enhance"];
		document.getElementById("enhance").style = "border:2px solid #696969; border-radius:5px; font-size:16px; padding-left: 10px; padding-right: 10px; padding-bottom: 5px; padding-top: 5px; display:inline height:30px; width:230px; text-align: left; font-weight: bold;"
		document.getElementById("enhance").style.backgroundColor = color
		document.getElementById("enhance").prepend(image)	
			
		var [color, logo] = style("verify",result["verify"])
		var image = document.createElement('img');
		image.src = logo
		image.height = 30
		image.style="vertical-align:middle"
		document.getElementById("verify").innerHTML = "    "+result["verify"];
		document.getElementById("verify").style = "border:2px solid #696969; border-radius:5px; font-size:16px; padding-left: 10px; padding-right: 10px; padding-bottom: 5px; padding-top: 5px; display:inline height:30px; width:230px; text-align: left; font-weight: bold;"
		document.getElementById("verify").style.backgroundColor = color
		document.getElementById("verify").prepend(image)
	
	})
}

async function toggleLoader() {
    var x = document.getElementById("loader");
    if (x.style.display === "none") {
        x.style.display = "inline";
    } else {
        x.style.display = "none";
    }
}