const Bite = require('./class.js');

class EnterpriseBite extends Bite {
  str(){
    return 'EP ' + super.str();
  }
}

let bite = new EnterpriseBite('hangman', 4);

console.log(bite.title);
console.log(bite.str());
