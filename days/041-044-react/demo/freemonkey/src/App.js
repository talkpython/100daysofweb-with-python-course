import React, { Component } from 'react';
import './App.css';
import './index.css';
import {getRandomMovie} from './data.js';

const GAME_TITLE = 'Free Monkey React';
const WON_MSG = 'Congrats, you freed the monkey!';
const LOST_MSG = 'Ouch, monkey is locked away :(';
const ALPHABET = 'abcdefghijklmnopqrstuvwxyz'.split('');
const PLACEHOLDER = '_';
const ALLOWED_GUESSES = 5;
const MONKEY_IMG = (num) => `http://projects.bobbelderbos.com/hangman/monkey${num}.png`
const WIN_STATE = '_wins';


class App extends Component {
  
  constructor(props){
    super(props);
    this.state = {}
  }

  componentDidMount(){
    this.resetGame();
  }

  resetGame = () => {
    const movie = getRandomMovie();
    console.log(movie);

    this.setState({
      header: GAME_TITLE,
      movie: movie.split(''),
      mask: movie.replace(/[A-Za-z]/g, PLACEHOLDER).split(''),
      buttonWidget: this.createButtons(),
      badGuesses: 0,
    })
  }
  
  createButtons = () => {
    let buttons = [];
    for(const [index, letter] of ALPHABET.entries()){
      buttons.push(
        <button className="letter" key={index} onClick={this.matchChar}>{letter.toUpperCase()}</button>
      )
    }
    return buttons;
  }

  matchChar = (e) => {
    const guessed = e.target.innerHTML;
    const guessedLcase = guessed.toLowerCase();
    let assertedLetter = false;
    let newMask = [];

    for(let i = 0; i < this.state.movie.length; i++){
      if(this.state.movie[i].toLowerCase() === guessedLcase){
        newMask.push(this.state.movie[i]);
        assertedLetter = true;
      } else {
        newMask.push(this.state.mask[i]);
      }
    }

    this.setState({
      mask: newMask,
      badGuesses: assertedLetter? this.state.badGuesses: this.state.badGuesses + 1
    }, this.checkWinOrLoss)

    e.target.disabled = true;
    e.target.style.backgroundColor = assertedLetter? 'green' : 'red';
    e.target.style.color = 'white';
  }

  gameWon = () => !this.state.mask.includes(PLACEHOLDER);

  gameOver = () => this.state.badGuesses >= ALLOWED_GUESSES;

  newGameButton = (btnText) => {
    return <button onClick={this.resetGame}>{btnText}</button>
  }

  checkWinOrLoss = () => {
    if(this.gameWon()){
      this.setState({
        header: WON_MSG,
        badGuesses: WIN_STATE, // show winning image
        buttonWidget: this.newGameButton('Play again')
      })
      return;
    }

    if(this.gameOver()){
      this.setState({
        header: LOST_MSG,
        mask: this.state.movie, // show what the movie was
        buttonWidget: this.newGameButton('Try again')
      })
      return;
    }
  }

  // TODO 6. win / loss helpers = check state
  //
  render() {
    return (
      <div id="game">
        <h1>{this.state.header}</h1>

        <img id="state"
          src={MONKEY_IMG(this.state.badGuesses)}
          alt="monkey state" />

        <div id="mask">
          {this.state.mask}
        </div>

        <div id="keyboard">
          {this.state.buttonWidget}
        </div>

      </div>
    );
  }
}

export default App;
