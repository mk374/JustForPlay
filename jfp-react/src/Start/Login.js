import React, {Component, useContext} from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';

import axios from 'axios';
import AppContext from '../AppContext.js';

// basic styling
const style = {margin: 15};

// login in component
class Login extends React.Component {
    static contextType = AppContext;

    // initialize login page with proper values
    constructor(props){
        super(props);
        this.state={
            username:'',
            password:''
        }
    }

     handleClick = (e) =>{
        e.preventDefault();
        // to change in the future for custom routing
        var apiBaseUrl = "http://35.239.108.248:5000/";
        var self = this;
        let userinfo={
            uid : this.state.username,
            password : this.state.password
        }
        // post it to the backend
        axios.post(apiBaseUrl+'login', userinfo).then(function (response) {
            
            // status & data check
            // console.log(response.status);
            // console.log(response.data);


            if(response.status === 200){
                // let's parse through the returned data
                let result = JSON.parse(response.request.response);
                // array at index 0 is 0 
                let userInfo = result[0];
                // array at index 1 is array of group dictionaries
                let userGroups = result[1];
                console.log(userGroups);
                self.setState({userInfo : userInfo, groups: userGroups})

                // update groups in main App page
                // self.props.updateGroups(userGroups);

                // self.props.onLogin();
            }
            else if(response.status === 204){
                console.log("Username password do not match");
                alert("Username password do not match");
            }
            else{
                console.log("Username does not exists");
                alert("Username does not exist");
            }
        })
        .catch(function (error) {
            console.log(error);
        });
    }
    // rendering of the login page
    render() {
        return (
                <div>
                    <MuiThemeProvider>
                        <div>
                        <AppBar title="Login"/>
                            <TextField
                            hintText="Enter your Username"
                            floatingLabelText="Username"
                            onChange = {(event, newValue) => this.setState({username:newValue})}/>
                            <br/>
                            <TextField
                            type="password"
                            hintText="Enter your Password"
                            floatingLabelText="Password"
                            onChange = {(event, newValue) => this.setState({password:newValue})}/>
                            <br/>
                            <RaisedButton label="Submit" primary={true} style={style} onClick={this.handleClick}/>
                        </div>
                    </MuiThemeProvider>
                </div>
             );
        }
    }

// export
export default Login;