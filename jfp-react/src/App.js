import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom'

import './App.css';
import Start from './Start/Start'
import AppProvider from './AppProvider';
import HomePage from './Home/HomePage';

const START_PAGE = 0;
const USER_HOME_PAGE = 1;


class App extends React.Component {
  constructor(props){
    super(props);
    this.state={
      page: START_PAGE,
      groups: []
      // loginPage:[],
      // uploadScreen:[]
    }
  }
  // componentWillMount(){
  //   var loginPage =[];
  //   loginPage.push(<Start key={this} parentContext={this}/>);
  //   this.setState({
  //       loginPage: loginPage
  //   })
  // }

  changeScreenState = () => {
    // keep it between 1 and 0
    var p = USER_HOME_PAGE
    this.setState({
      page: p
    })
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
      
      // <AppProvider values={{groups, updateGroups}}>
        <div className="App">
          {childpage}
        </div>
      // </AppProvider>
      );
  }
}
export default App;
