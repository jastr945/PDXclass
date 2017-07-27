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
                if ((parseInt(key) - alphabetRemainder) % alphabet.length < 0) {
                    newIndex = alphabet.length - (parseInt(key) - alphabetRemainder) - 1;
                    newLetter = alphabet[newIndex];
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
        $('#encryptResult').html(result).css('background-color', '#5b5a5a');
    }
}


//encrypts a string upon clicking the 'submit' button
$(document).ready(function() {
    $('#encryptionTab').validate({
        rules: {
            encryptString: "required",
            encryptKey: "required"
        },
        message: {
            encryptString: 'Enter a word.',
            encryptKey:'Enter a key.'
        },
        errorPlacement: function(error, element) {
            element.attr('placeholder', error.text());
        }
    });
    $('#encrypt').click(function (e) {
        e.preventDefault();
        if ($('#encryptionTab').valid()) {
            caesarEncrypt($('#encryptString').val().toLowerCase(), $('#encryptKey').val());
        }
    });
});

//an opposite process with a similar logic as above
function caesarDecrypt(plainStr, key) {
    var result = '';
    for (var i = 0, len = plainStr.length; i < len; i++) {
        var indexInAlphabet = alphabet.indexOf(plainStr[i]); // determining the index of a letter in the alphabet array
        var alphabetRemainder = indexInAlphabet; // determining how many letters are left till the beginning of array

        if (parseInt(key) <= alphabetRemainder) {
            newIndex = indexInAlphabet - parseInt(key); // determining a new index
            newLetter = alphabet[newIndex]; // determining a new letter
            result += newLetter;
        } else {
            //goes though the alphabet array several times until the right index is found
            if ((parseInt(key) + alphabetRemainder) > alphabet.length) {
                if ((parseInt(key) - (alphabet.length - alphabetRemainder)) === alphabet.length) {
                newLetter = alphabet[alphabet.length - 2];
                result += newLetter;
                } else {
                    newIndex = indexInAlphabet + (indexInAlphabet - ((parseInt(key) + alphabetRemainder) % alphabet.length));
                    console.log(newIndex);
                    if (newIndex < 0) {
                        newLetter = alphabet[newIndex + alphabet.length];
                        result += newLetter;
                    } else {
                        newLetter = alphabet[newIndex];
                        result += newLetter;
                    }
                }
            } else if ((parseInt(key) + alphabetRemainder) === alphabet.length) {
                newLetter = alphabet[alphabet.length - alphabet.length];
                result += newLetter;
            } else {
                newIndex = alphabet.length - parseInt(key) + alphabetRemainder;
                newLetter = alphabet[newIndex];
                result += newLetter;
            }
        }
        $('#decryptResult').html(result).css('background-color', '#5b5a5a');
    }
}
// decrypts a string upon clicking the 'submit' button
$('#decrypt').click(function (e) {
    e.preventDefault();
    caesarDecrypt($('#decryptString').val().toLowerCase(), $('#decryptKey').val());
});

