import React from 'react';

import './App.css';
import Start from './Start/Start'
import HomePage from './Home/HomePage';

const START_PAGE = 0;
const USER_HOME_PAGE = 1;


class App extends React.Component {

  constructor(props){
    super(props);
    this.state={
      page: START_PAGE,
      groups: []
    }
  }

  changeScreenState = () => {
    // keep it between 1 and 0
    var currState = this.state.page;
    this.setState({
      page: currState === START_PAGE ? USER_HOME_PAGE : START_PAGE
    })

    console.log("STATE HATH BEEN CHANGETH:" + this.state.page);
  }

  updateGroups = groups => {
    this.setState({
      groups : groups
    })
    console.log("GROUPS AFTER UPDATES:");
    console.log(this.state.groups);
  }

  render() {
    // pass the updateGroups function
    // var {updateGroups} = this
    // pass the actual groups
    // var groups = this.groups
    
    var childpage;

    switch(this.state.page) {
          case START_PAGE:
            childpage = (
              <Start onLogin={this.changeScreenState} updateGroups={this.updateGroups}></Start>
            )
            break;
          case USER_HOME_PAGE:
            childpage = (
              <HomePage onLogout={this.changeScreenState} groups={this.state.groups}></HomePage>
            )
            break;
          default:
            childpage = (
              null
            )
    }
    return (
      
        <div className="App">
          {childpage}
        </div>
      );
  }
}
export default App;
