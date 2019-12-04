import React from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import axios from 'axios';
import Login from './Login';

class Register extends React.Component {
    // initialize register page with proper values
    constructor(props){
        super(props);
        this.state={
            name:'',
            username:'',
            password:''
        }
    }

    handleClick = e => {
        var apiBaseUrl = "http://35.239.108.248:5000/";
        console.log("values: ",this.state.name, this.state.username,this.state.password);
        //To be done:check for empty values before hitting submit
        var self = this;
        var payload={
            "name": this.state.name,
            "username": this.state.username,
            "password": this.state.password
        }
        axios.post(apiBaseUrl+'/register', payload).then(function (response) {
            console.log(response);
            if(response.data.code === 200){
                var loginscreen=[];
                loginscreen.push(<Login parentContext={this}/>);
                var loginmessage = "Not Registered yet. Go to registration";
                self.props.parentContext.setState({loginscreen: loginscreen,
                    loginmessage:loginmessage,
                    buttonLabel:"Register",
                    isLogin:true
                });
            }
        })
       .catch(function (error) {
         console.log(error);
       });
    }

    render() {
        return (
            <div>
                <MuiThemeProvider>
                <div>
                    <AppBar title="Register"/>
                    <TextField
                        hintText="Enter your Name"
                        floatingLabelText="Name"
                        onChange = {(event, newValue) => this.setState({name:newValue})}/>
                    <br/>
                    <TextField
                        hintText="Provide a Username"
                        floatingLabelText="Username"
                        onChange = {(event, newValue) => this.setState({username:newValue})}
                        />
                    <br/>
                    <TextField
                        type = "password"
                        hintText="Provide your Password"
                        floatingLabelText="Password"
                        onChange = {(event, newValue) => this.setState({password:newValue})}
                        />
                    <br/>
                    <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
                </div>
                </MuiThemeProvider>
            </div>
        );
    }
}
const style = {
  margin: 15,
};
export default Register;