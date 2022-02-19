/* File: content.js
 * ---------------
 * Hello! You'll be making most of your changes
 * in this file. At a high level, this code replaces
 * the substring "cal" with the string "butt" on web pages.
 *
 * This file contains javascript code that is executed
 * everytime a webpage loads over HTTP or HTTPS.
 */

// Get Contract Information
let url = location.href;

const urlArray = url.split("/");
var contractAddress = urlArray[4];
var tokenID = urlArray[5];

console.log("Contract Address:", contractAddress)
console.log("Token ID:", tokenID)

var nft_MetaData = getJSON(contractAddress, tokenID);
console.log(nft_MetaData);
// var image_url = nft_MetaData['image'];
// console.log("Image URL:", image_url);


function getJSON(contractAddress, tokenID) {
    fetch(`https://api.opensea.io/api/v1/metadata/${contractAddress}/${tokenID}`).then(r => r.text()).then(result => {
        // Result now contains the response text, do what you want...
        return r.text();
    })
}



// var elements = document.getElementsByTagName('*');

// for (var i = 0; i < elements.length; i++) {
//     var element = elements[i];

//     for (var j = 0; j < element.childNodes.length; j++) {
//         var node = element.childNodes[j];

//         if (node.nodeType === 3) {
//             var text = node.nodeValue;
//             var replacedText = text.replace(/cal/gi, "butt"); // replaces "cal," "Cal", etc. with "butt"

//             if (replacedText !== text) {
//                 element.replaceChild(document.createTextNode(replacedText), node);
//               }
//         }
//     }
// }
