//This is one of the first simple Javascript labs.

var input = prompt('Enter a character');
function myVowel (letter) {
    if (['a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I'].indexOf(letter) === 0) {
        alert('The character you entered is a vowel');
    } else {
        alert('The character you entered is NOT a vowel');
    }
}

myVowel(input);

