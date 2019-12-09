import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import Login from './Login';
import Register from './Register';

import { withStyles } from '@material-ui/styles';

const styles = theme => ({
  colors: {
      backgroundColor: "#84c1ff"
  },
  fields: {
      marginBottom: 10
  }
});

class Start extends Component {
  constructor(props){
    super(props);
    this.state={
      username:'',
      password:'',
      loginscreen:[],
      loginmessage:'',
      buttonLabel:'Register',
      isLogin:true
    }
  }
  componentWillMount(){
    var loginscreen=[];
    loginscreen.push(<Login parentContext={this} appContext={this.props.parentContext} onLogin={this.props.onLogin} updateGroups={this.props.updateGroups} updateUser={this.props.updateUser}/>);
    var loginmessage = "Not registered yet? Register now";
    this.setState({
        loginscreen:loginscreen,
        loginmessage:loginmessage
    })
  }
  handleClick(event){
    var loginmessage;
    var loginscreen=[];
    if(this.state.isLogin){
        loginscreen.push(<Register parentContext={this}/>);
        loginmessage = "Already registered? Go to login";
        this.setState({
            loginscreen:loginscreen,
            loginmessage:loginmessage,
            buttonLabel:"Login",
            isLogin:false
        })
    }else{
        loginscreen.push(<Login parentContext={this} appContext={this.props.parentContext} onLogin={this.props.onLogin} updateGroups={this.props.updateGroups} updateUser={this.props.updateUser}/>);
        loginmessage = "Not Registered yet. Go to registration";
        this.setState({
            loginscreen:loginscreen,
            loginmessage:loginmessage,
            buttonLabel:"Register",
            isLogin:true
        })
    }
  }

  render() {
    const { classes } = this.props;
    
    return (
      <div>
        {this.state.loginscreen}
        <div>
          {this.state.loginmessage}
            <div>
               <Button className={classes.colors} primary={true} style={style} onClick={(event) => this.handleClick(event)}>{this.state.buttonLabel}</Button>
           </div>
        </div>
      </div>
    );
  }
}
const style = {
  margin: 15,
};
export default withStyles(styles)(Start);