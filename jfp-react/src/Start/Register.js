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
        backgroundColor: "#84c1ff",
        paddingRight: 20,
        paddingLeft: 20,
        paddingTop: 5,
        paddingBottom: 5,
        color: 'white'
    },
    bar: {
        backgroundColor: "#84c1ff",
        alignItems: 'center'
    },
    row: {
        paddingBottom: 20
    },
    fieldsRight: {
        paddingRight: 10
    },
    fieldsLeft: {
        paddingLeft: 10
    },
    multi: {
        width: "87.5%"
    }
  });

class Register extends React.Component {
    // initialize register page with proper values
    constructor(props){
        super(props);
        this.state={
            name:'',
            uid:'',
            password:'',
            bio: '',
            zip_code: ''

        }
    }

    handleClick = e => {
        e.preventDefault();
        var apiBaseUrl = "http://35.202.227.79:5000/";
        //To be done:check for empty values before hitting submit
        var self = this;
        var payload={
            name: this.state.name,
            uid: this.state.uid,
            password: this.state.password,
            bio: this.state.bio,
            zip_code: this.state.zip_code

        }
        var config = {
            headers: {
                'Access-Control-Allow-Origin': '*'
            },
            withCredentials: false
        };
        axios.post(apiBaseUrl+'add-user', payload, config).then(function (response) {
            if(response.data.code === 200){
                var loginscreen=[];
                loginscreen.push(<Login parentContext={this}/>);
                var loginmessage = "Not Registered yet? Go to registration";
                self.props.parentContext.setState({loginscreen: loginscreen,
                    loginmessage:loginmessage,
                    buttonLabel:"Register",
                    isLogin:true
                });
            }
            else if(response.status === 204){
                alert("Username taken. Please enter a different username.");
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
                        <Toolbar><h2>Register</h2></Toolbar>
                    </AppBar>
                    <br/>
                    <div className={classes.row}>
                        <TextField
                            className={classes.fieldsRight}
                            label="Name"
                            variant="outlined"
                            onChange = {(e) => this.setState({name: e.target.value})}
                            />
                        <TextField
                            className={classes.fieldsLeft}
                            label="Username"
                            variant="outlined"
                            onChange = {(e) => this.setState({uid: e.target.value})}
                            />
                    </div>
                    <div className={classes.row}>
                        <TextField
                            className={classes.fieldsRight}
                            label="Password"
                            variant="outlined"
                            type = "password"
                            onChange = {(e) => this.setState({password: e.target.value})}
                            />
                        <TextField
                            className={classes.fieldsLeft}
                            label="Zip code"
                            variant="outlined"
                            onChange = {(e) => this.setState({zip_code: e.target.value})}
                            />
                    </div>
                    <div className={classes.paper}>
                        <TextField
                            className={classes.multi}
                            label="Tell us about yourself!"
                            variant="outlined"
                            multiline
                            rows="3"
                            onChange = {(e) => this.setState({bio: e.target.value})}
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
