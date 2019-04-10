const ninjas = [
  { name: 'martin', points: 225 },
  { name: 'mike', points: 200 },
  { name: 'dirk', points: 175 },
];

console.log(
  ninjas
  .filter(ninja => ninja.points >= 200)
  .map(ninja => `<li>${ninja.name}</li>`)
)
