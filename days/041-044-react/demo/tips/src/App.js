import React, { Component } from 'react';
import './App.css';
import Highlighter from "react-highlight-words";

const axios = require('axios');

const PAGE_TITLE = 'PyBites Python Tips API';
const TWITTER_ICON = 'https://codechalleng.es/static/img/icon-twitter.png'
const TIPS_ENDPOINT = 'http://127.0.0.1:8000/api/'


function Tip(props) {
  return (
    <div className="tip">
      <p>
        <Highlighter
         highlightClassName="highlight"
         searchWords={[props.filterStr]}
         autoEscape={true}
         textToHighlight={props.tip || ''}
        />
      { props.link && 
        <span> (<a href={props.link} target="_blank">source</a>)</span>
      }
      </p>
      <pre>
        <Highlighter
         highlightClassName="highlight"
         searchWords={[props.filterStr]}
         autoEscape={true}
         textToHighlight={props.code || ''}
        />
      </pre>
      { props.share_link &&
        <p>
          <a href={props.share_link} target="_blank">
            <img src={TWITTER_ICON} alt="share"/>
          </a>
        </p>
      }
    </div>
  )
}


class App extends Component {
  
  constructor(props){
    super(props);
    this.state = {
      orgTips: [],
      showTips: [],
      filterStr: '',
    }
    this.onFilterChange = this.onFilterChange.bind(this);
    this.filterTips = this.filterTips.bind(this);
  }

  componentDidMount(){
    axios.get(TIPS_ENDPOINT)
    .then(response => {
      this.setState({
        orgTips: response.data,
        showTips: response.data
      })
    })
    .catch(function(error){
      console.log(error);
    })
  }

  onFilterChange(event){
    // filter orgTips into showTips
    const filterStr = event.target.value? event.target.value.toLowerCase(): '';
    this.setState({
      filterStr: filterStr,
      showTips: this.filterTips(filterStr)
    })
  }

  filterTips(filterStr){
    let tips = []
    for(const tip of this.state.orgTips){
      if(tip.tip && tip.tip.toLowerCase().includes(filterStr) ||
         tip.code && tip.code.toLowerCase().includes(filterStr)){
        tips.push(tip);
      }
    }
    return tips;
  }

  render() {
    return (
      <div className="App">
        <h2>{PAGE_TITLE}</h2>

        <form id="searchTips">
          <input type="text"
            placeholder="filter tips"
            value={this.state.filterStr}
            onChange={this.onFilterChange} />
        </form>
        
        <div id="tips">
          {this.state.showTips.map((tip, index) =>
            <Tip {...tip} key={index} filterStr={this.state.filterStr} />
          )}
        </div>

      </div>
    );
  }
}

export default App;
