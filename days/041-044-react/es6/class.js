class Bite {

  constructor(title, points){
    this.title = title;
    this.points = points;
  }

  str(){
    return 'Bite: ' + this.title + ' (' + this.points + ' pt.)';
  }
}

if (require.main === module) {
  bite1 = new Bite('sum of numbers', 2)
  console.log(bite1.str())

  bite2 = new Bite('parse list of names', 3)
  console.log(bite2.str())
}

module.exports = Bite;