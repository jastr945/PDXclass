'use strict';

var alphabet = ['a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
var newIndex;
var newLetter;

//Iterates over a given string; matches each letter with the alphabet array; gets its index and calculates the new index,
//based on the given key; finds a new letter and returns a new string.
function caesarEncrypt(plainStr, key) {
    var result = '';
    for (var i = 0, len = plainStr.length; i < len; i++) {
        var indexInAlphabet = alphabet.indexOf(plainStr[i]); // determining the index of a letter in the alphabet array
        var alphabetRemainder = alphabet.length - (indexInAlphabet + 1); // determining how many letters are left till the end of array

        if (parseInt(key) <= alphabetRemainder) {
            newIndex = indexInAlphabet + parseInt(key); // determining a new index
            newLetter = alphabet[newIndex]; // determining a new letter
            result += newLetter;
        } else {
            //goes though the alphabet array several times until the right index is found
            if ((parseInt(key) + alphabetRemainder) > alphabet.length) {
                if ((parseInt(key) - alphabetRemainder) % alphabet.length === 0) {
                    newLetter = alphabet[alphabet.length - 1];
                    result += newLetter;
                } else {
                    newIndex = ((parseInt(key) - alphabetRemainder) % alphabet.length) - 1;
                    newLetter = alphabet[newIndex];
                    result += newLetter;
                }
            } else if ((parseInt(key) + alphabetRemainder) === alphabet.length) {
                newLetter = alphabet[alphabet.length - 1];
                result += newLetter;
            } else {
                newIndex = (parseInt(key) - alphabetRemainder) - 1;
                newLetter = alphabet[newIndex];
                result += newLetter;
            }
        }
        $('#encryptResult').html(result);
    }
}
// encrypts upon clicking the 'submit' button
$('#encrypt').click(function (e) {
    e.preventDefault();
    caesarEncrypt($('#encryptString').val(), $('#encryptKey').val());
});

//an opposite process with a similar logic as above
function caesarDecrypt(encStr, key) {
    var result = '';
    for (var i = 0, len = encStr.length; i < len; i++) {
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
