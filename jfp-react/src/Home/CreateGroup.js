import React from 'react';
import TextField from '@material-ui/core/TextField';
import GroupAddIcon from '@material-ui/icons/GroupAdd';
import Button from '@material-ui/core/Button';
import { withStyles } from '@material-ui/styles';

import axios from 'axios';

const styles = theme => ({
    divbyAndy: {
        padding: '10px 20px 40px 20px'
    },

    paper: {
        padding: 10,
        margin: 10,
        maxWidth: 700
    },
    textField: {
        paddingRight: 5,
    }
  });

class CreateGroup extends React.Component {
    constructor(props){
        super(props);
        this.state={
            uid : this.props.uid,
            g_name: "",
            g_community: "",
            g_zip: "",
            g_description: "",
        }
    }

    createGroup = (e) =>{
        e.preventDefault();

        var apiBaseUrl = "http://35.202.227.79:5000/";
        var self = this;
        
        /* POPULATE */
        let userinfo = {
            uid: this.state.uid,
            g_name: this.state.g_name,
            g_community: this.state.g_community,
            g_zip: this.state.g_zip,
            g_description: this.state.g_description,
        };

        console.log(userinfo);

        var config = {
            headers: {
                'Access-Control-Allow-Origin': '*'
            },
            withCredentials: false
        };
        // post it to the backends
        axios.post(apiBaseUrl + 'add-group', userinfo, config).then(function (response) {
                if (response.status === 200) {
                    let result = JSON.parse(response.request.response);
                    // reset the form
                    self.setState({
                        g_name: "",
                        g_community: "",
                        g_zip: "",
                        g_description: "",
                    })

                    // reset the parent page
                    
                    
                }
            })
            .catch(function (error) {
                console.log(error);
        });
    }
    
    render(){
        const { classes } = this.props;

        return(
        <div>
            <h2>Create Group</h2>
            <form onSubmit={this.createGroup}>
                <div  className={classes.paper}>
                    <TextField 
                        className={classes.textField}
                        label="Name"
                        variant="outlined"
                        onChange = {(e) => this.setState({g_name: e.target.value})}
                    />
                </div>
                <div  className={classes.paper}>
                    <TextField
                        className={classes.textField}
                        label="Community"
                        variant="outlined"
                        onChange = {(e) => this.setState({g_community: e.target.value})}
                    />
                    <TextField
                        className={classes.textField}
                        label="Zip Code"
                        type="text"
                        pattern="[0-9]{5}"
                        variant="outlined"
                        onChange = {(e) => this.setState({g_zip: e.target.value})}
                    />
                </div>
                <div className={classes.paper}>
                    <TextField
                        id="outlined-multiline-static"
                        label="Description"
                        multiline
                        rows="3"
                        variant="outlined"
                        onChange = {(e) => this.setState({g_description: e.target.value})}
                    />
                    
                </div>
                <div className={classes.paper}>
                    <Button
                        variant="contained"
                        color="primary"
                        type="submit"
                        className={classes.button}
                        startIcon={<GroupAddIcon/>}
                    >
                        Create Group
                    </Button>
                 </div>
            </form>
        </div>
        );
    }

}
export default withStyles(styles)(CreateGroup);