'use strict';
var vocabulary;

function Completer() {
    vocabulary = [];

    //adds elements to the array
    this.addCompletion = function (str) {
        vocabulary.push(str.toString());
    };

    //removes elements from the array
    this.removeCompletion = function (str) {
        delete vocabulary[vocabulary.indexOf(str)];
    };

    //iterates over the array and finds words with first letter matching the given prefix; returns the word.
    this.complete = function (prefix) {
        for (var i = 0; i < vocabulary.length; i++) {
            if (vocabulary[i][0] === prefix) {
                console.log(vocabulary[i]);
            }
        }
    }
}

var fruitCompleter = new Completer();
fruitCompleter.addCompletion('apple');
fruitCompleter.addCompletion('avocado');
fruitCompleter.addCompletion('anise');
fruitCompleter.addCompletion('banana');
fruitCompleter.addCompletion('watermelon');
fruitCompleter.complete('w');
fruitCompleter.removeCompletion('apple');
console.log(vocabulary);
