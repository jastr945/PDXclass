var alphabet = ['a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

function caesarEncrypt(plainStr, key) {
    for(var i = 0, len = plainStr.length; i < len; i++) {
        var indexInAlphabet = alphabet.indexOf(i);
        var newIndex = indexInAlphabet + key;
        var newLetter = alphabet[newIndex];
        console.log(newLetter);
    }
}