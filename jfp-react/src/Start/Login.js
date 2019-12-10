import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { withStyles } from '@material-ui/styles';
import Toolbar from '@material-ui/core/Toolbar';



import axios from 'axios';
import AppContext from '../AppContext.js';

// basic styling
const style = {margin: 15};

const styles = theme => ({
    button: {
        backgroundColor: "#84c1ff",
        paddingRight: 30,
        paddingLeft: 30,
        paddingTop: 5,
        paddingBottom: 5,
        color: 'white'
    },
    fields: {
        paddingBottom: 30
    },
    bar: {
        backgroundColor: "#4998e6",
        alignItems: 'center'
    }
});

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
        const { classes } = this.props;
        return (
            <div>
                <form onSubmit={this.handleClick}>
                    <div>
                        <AppBar className={classes.bar} position="static">
                            <Toolbar><h2>JustForPlay</h2></Toolbar>
                        </AppBar>  
                        <br/>
                        <div className={classes.fields}>
                            <TextField
                            label="Username"
                            variant="outlined"
                            onChange = {(e) => this.setState({username:e.target.value})}/>
                        </div>
                        <div>
                            <TextField
                            label="Password"
                            variant="outlined"
                            type="password"
                            onChange = {(e, newValue) => this.setState({password: e.target.value})}/>
                        </div>
                            <Button className={classes.button} label="Submit" primary={true} style={style} type="submit"> Login </Button>
                    </div>
                </form>
            </div>
        );
    }
}

// export
export default withStyles(styles)(Login);