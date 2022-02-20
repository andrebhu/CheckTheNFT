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
let contractAddress = urlArray[4];
let tokenID = urlArray[5];

console.log("Contract Address:", contractAddress)
console.log("Token ID:", tokenID)

// function loadJSON() {
//     var url = `https://api.opensea.io/api/v1/metadata/${contractAddress}/${tokenID}?format=json`;

//     var settings = {
//         type: "GET",
//         dataType: "json",
//         url: url,
//         data: "{}",
//         success: function (result) {
//             console.log("Success!");
//         },
//         error: function(err) {
//             alert('ERROR');
//         }
//     };

//     $.ajax(settings);
// }

// function getJSON(contractAddress, tokenID) {
//     fetch(`https://api.opensea.io/api/v1/metadata/${contractAddress}/${tokenID}`,
//     {
//         method: "GET",
//     }).then(r => r.text()).then(result => {
//         // Result now contains the response text, do what you want...
//         // console.log(result);
//         return result;
//     })
//     .catch(error => console.warn(error));
// }

// async function getJSON(contractAddress, tokenID) {
//     const response = await fetch(`https://api.opensea.io/api/v1/metadata/${contractAddress}/${tokenID}?format=json`);

//     return response.json();
// }

// Fetch JSON Metadata
// var metaURL= `https://api.opensea.io/api/v1/metadata/${contractAddress}/${tokenID}?format=json`;
// function showJSON(response) {
//     let xhr = new XMLHttpRequest();

//     xhr.open('GET', metaURL, true);

//     xhr.onload() = function() {
//         if (xhr.status == 200) {
//             console.log("Success!");
//             let image_url = JSON.parse(this.response)
//             console.log(image_url);
//         }
//     }
//     xhr.send();
// }


// $.ajax({
//     type: "POST",
//     url: "~/pythoncode.py",
//     data: { param: text}
//   }).done(function( o ) {
//      // do something
//   });

// console.log("meta", { nft_MetaData });

// var json = JSON.parse(nft_MetaData);



// var image_url = json['image'];
// console.log("Image URL:", image_url);