import React from 'react';

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Start from './Start/Start'
import HomePage from './Home/HomePage';


const START_PAGE = 0;
const USER_HOME_PAGE = 1;


class App extends React.Component {

  constructor(props){
    super(props);
    this.state={
      page: START_PAGE,
      groups: [],
      user: []
    }
  }

  changeScreenState = () => {
    // keep it between 1 and 0
    var currState = this.state.page;
    this.setState({
      page: currState === START_PAGE ? USER_HOME_PAGE : START_PAGE
    })
    console.log("CURRENT STATE:" + this.state.page);
  }

  updateGroups = (groups) => {
    this.setState({
      groups : groups
    })
    console.log(this.state.groups);
  }

  updateUser = (user) => {
    this.setState({
      user : user
    })
    console.log(this.state.user);
  }

  render() {
    
    var childpage;

    switch(this.state.page) {
          case START_PAGE:
            childpage = (
              <Start onLogin={this.changeScreenState} updateGroups={this.updateGroups} updateUser={this.updateUser}></Start>
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
