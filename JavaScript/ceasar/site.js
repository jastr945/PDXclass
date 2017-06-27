'use strict';

var alphabet = ['a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

//Iterates over a given string; matches each letter with the alphabet array; gets its index and calculates the new index,
//based on the given key; finds a new letter and returns a new string.
function caesarEncrypt(plainStr, key) {
    var result = '';
    for(var i = 0, len = plainStr.length; i < len; i++) {
        var indexInAlphabet = alphabet.indexOf(plainStr[i]);
        var newIndex = indexInAlphabet + parseInt(key);
        var newLetter = alphabet[newIndex];
        result += newLetter;
    }
    document.getElementById('encryptResult').innerHTML = result;
}

// If  key > (alphabet.length - indexInAlphabet):
// newIndex = key - (alphabet.length - indexInAlphabet) - 1

// Connects the encrypting function to the text window and submit button
document.getElementById('encrypt').addEventListener('click', function (e) {
    e.preventDefault();
    var EncryptStr = document.getElementById('encryptString').value;
    var EncryptKey = document.getElementById('encryptKey').value;
    caesarEncrypt(EncryptStr, EncryptKey);
});

function caesarDecrypt(encStr, key) {
    var result = '';
    for(var i = 0, len = encStr.length; i < len; i++) {
        var indexInAlphabet = alphabet.indexOf(encStr[i]);
        var newIndex = indexInAlphabet - parseInt(key);
        var newLetter = alphabet[newIndex];
        result += newLetter;
    }
    document.getElementById('decryptResult').innerHTML = result;
}

document.getElementById('decrypt').addEventListener('click', function (e) {
    e.preventDefault();
    var DecryptStr = document.getElementById('decryptString').value;
    var DecryptKey = document.getElementById('decryptKey').value;
    caesarDecrypt(DecryptStr, DecryptKey);
});
