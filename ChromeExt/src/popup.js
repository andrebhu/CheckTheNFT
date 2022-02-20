/* File: popup.js
 * -----------------------
 * This javascript file restores settings when the DOM loads.
 * You shouldn't have to change this file unless you also
 * change the corresponding popup.html file.
 */

chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var currentTab = tabs[0]; // there will be only one in this array
    console.log(currentTab); // also has properties like currentTab.id
    var tabUrl = currentTab.url;

    var flaskUrl = `http://localhost:5000/opensea?url=${tabUrl}`;

    document.addEventListener('DOMContentLoaded', () => {
        var y = document.getElementById("script");
        y.addEventListener("click", openIndex);
        
    });
    
    function openIndex() {
    chrome.tabs.create({active: true, url: flaskUrl});
    }
});
