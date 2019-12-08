import React from 'react';
import  MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
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
            password:'',
        }
    }

     handleClick = async(e) =>{
        e.preventDefault();
        // to change in the future for custom routing
        var apiBaseUrl = "http://35.202.227.79:5000/";
        var self = this;
        let userinfo={
            uid : this.state.username,
            password : this.state.password
        }
        // post it to the backends
        axios.post(apiBaseUrl+'login', userinfo).then(function (response) {
            if(response.status === 200){
                // let's parse through the returned data
                let result = JSON.parse(response.request.response);
                // array at index 0 is 0 
                let userInfo = result[0];
                // array at index 1 is array of group dictionaries
                let userGroups = result[1];
                
                // update groups in main App page
                self.props.updateUser(userInfo);
                self.props.updateGroups(userGroups);
                self.props.onLogin();
            }
            else if(response.status === 204){
                alert("Username password do not match");
            }
            else{
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
                            variant="outlined"
                            hintText="Enter your Username"
                            floatingLabelText="Username"
                            onChange = {(e, newValue) => this.setState({username:newValue})}/>
                            <br/>
                            <TextField
                            variant="outlined"
                            type="password"
                            hintText="Enter your Password"
                            floatingLabelText="Password"
                            onChange = {(e, newValue) => this.setState({password:newValue})}/>
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