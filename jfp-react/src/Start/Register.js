import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';


import axios from 'axios';
import Login from './Login';

import { withStyles } from '@material-ui/styles';
import Toolbar from '@material-ui/core/Toolbar';

const styles = theme => ({
    colors: {
        backgroundColor: "#84c1ff"
    },
    fields: {
        paddingBottom: 30
    },
    bar: {
        backgroundColor: "#84c1ff",
    }
  });

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
position="static"
    render() {
        const {classes} = this.props;
        return (
            <div>
                <form>
                <div>
                    <AppBar className={classes.bar} position="static">
                        <Toolbar>Register</Toolbar>
                    </AppBar>
                    <br/> 
                    <div className={classes.fields}>
                        <TextField
                            label="Name"
                            variant="outlined"
                            hintText="Enter your Username"
                            onChange = {(e) => this.setState({name: e.target.value})}/>
                    <br/>
                    </div>
                    <div className={classes.fields}>
                        <TextField
                            label="Username"
                            variant="outlined"
                            hintText="Provide a Username"
                            onChange = {(e) => this.setState({username: e.target.value})}
                            />
                    </div>
                    <div className={classes.fields}>
                        <TextField
                            type = "password"
                            label="Password"
                            variant="outlined"
                            hintText="Provide your Password"
                            onChange = {(e) => this.setState({password: e.target.value})}
                            />
                    </div>
                    <Button className={classes.colors} primary={true} style={style} onClick={(event) => this.handleClick(event)}>Submit</Button>
                </div>
                </form>
            </div>
        );
    }
}
const style = {
  margin: 15,
};
export default withStyles(styles)(Register);